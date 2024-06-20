from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
import logging

logger = logging.getLogger(__name__)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = ProfileSerializer(profile, many=False)
    return Response(serialized_profile.data)

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data['username'],
    )   
    user.set_password(request.data['password'])
    user.save()
    profile = Profile.objects.create(
        user = user,
        first_name = request.data['first_name'],
        last_name = request.data['last_name']
    )

    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

class HoleViewSet(viewsets.ModelViewSet):
    queryset = Hole.objects.all()
    serializer_class = HoleSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_round(request):
    user = request.user
    rounds = user.rounds
    serializer = RoundSerializer(rounds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_hole(request, pk):
    print ('GET HOLE!  PK: ', pk)
    try: # we have a round
        round = Round.objects.get(pk=pk)
        print('existing Round', round)
    except: # we need to create a round
        round = Round.objects.create(
            course = Course.objects.get(pk=1), # hard coded to Lakeside
            user = request.user
        )
        print('new round: ', round)
        
    course = Course.objects.get(id = round.course.id)

    holes = Hole.objects.filter(course = course)

    
    scores = []
    for hole in holes:
        score = Score.objects.filter(round=round, hole=hole).first()
        if score:
            scores.append(score)
        print('Hole: ', hole)
        print('Score: ', score)

    holes_serialized = HoleSerializer(holes, many=True)
    scores_serialized = ScoreSerializer(scores, many=True)
    data = {
        'holes': holes_serialized.data,
        'strokes' : scores_serialized.data
    }
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_round(request):
    user = request.user
    course_id = request.data.get('course_id')
    course = Course.objects.get(id=course_id)
    new_round = Round.objects.create(user=user, course=course)
    
    serializer = RoundSerializer(new_round)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_score(request):
    user = request.user
    data = request.data
    print('data: ', data)
    print(data['content'])
    content = data["content"]
    print('CONTENT: ', content)
    hole = content['hole']
    round = content['round']
    strokes = content['strokes']

    score = Score.objects.filter(
        hole=hole,
        round=round,        
    ).first()
    print('SCORE: ', score)

    # score.strokes = content['strokes']

    data = {
        'round':round,
        'hole':hole,
        'strokes':strokes
    }

    serializer = ScoreSerializer(score, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_rounds_history(request):
    user = request.user
    rounds = Round.objects.filter(user=user).order_by('-date')
    score = Score.objects.filter()
    serializer = RoundSerializer(rounds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_round_details(request, round_id):
    try:
        round = Round.objects.get(id=round_id, user=request.user)
        serializer = RoundSerializer(round)
        return Response(serializer.data)
    except Round.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   




