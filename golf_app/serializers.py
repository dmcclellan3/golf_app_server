from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class HoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hole
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Score
        fields = '__all__'

class RoundSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    user = UserSerializer()
    # holes = HoleSerializer(many=True)
    scores = ScoreSerializer(many=True)
    class Meta:
        model = Round
        fields = '__all__'