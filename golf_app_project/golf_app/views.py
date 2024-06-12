from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from .models import *
from .serializers import *

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
def get_hole(request):
    user = request.user
    rounds = Round.objects.filter(user=user)
    rounds_serialized = RoundSerializer(rounds, many=True)
    
    print('User Rounds', rounds_serialized.data)
    holes = []
    for round in rounds_serialized.data:
        if round['holes']:
            print('ROUND HAS HOLES!', round['holes'])
            round_holes = round['holes']
            for h in round_holes:
                the_golf_hole = Hole.objects.get(id=h['id'])
                holes.append(the_golf_hole)
            # holes.extend(round_holes.all())
    holes_serialized = HoleSerializer(holes, many=True)
    return Response(holes_serialized.data)


