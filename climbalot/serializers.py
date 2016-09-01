from rest_framework import serializers
from climbalot.models import Monkey, Session, C_Routes, V_Routes, Y_Routes, Gym, Quest
from django.contrib.auth.models import User

class GymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = ('id', 'gym')

class QuestSerializer(serializers.ModelSerializer):
    monkey = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Quest
        fields = ('id', 'start_date', 'monkey', 'name', 'short_description', 'c_value',
                'v_value', 'y_value', 'attempts_total', 'days_open', 'status')

class C_RoutesSerializer(serializers.ModelSerializer):

    class Meta:
        model = C_Routes
        fields = ('id', 'yellow', 'green', 'red', 'blue', 'orange', 'purple', 'black')

class V_RoutesSerializer(serializers.ModelSerializer):

    class Meta:
        model = V_Routes
        fields = ('v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10')

class Y_RoutesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Y_Routes
        fields = ('c5_7', 'c5_8_neg', 'c5_8_pos', 'c5_9_neg', 'c5_9_pos', 'c5_10_a',
                  'c5_10_b', 'c5_10_c', 'c5_10_d', 'c5_11_a', 'c5_11_b', 'c5_11_c',
                  'c5_11_d', 'c5_12_a', 'c5_12_b', 'c5_12_c', 'c5_12_d')

class SessionSerializer(serializers.ModelSerializer):
    monkey = serializers.StringRelatedField(read_only=True)
    gym = serializers.StringRelatedField(many=False)
    c_routes = C_RoutesSerializer(many=False, allow_null=True)
    v_routes = V_RoutesSerializer(many=False, allow_null=True)
    y_routes = Y_RoutesSerializer(many=False, allow_null=True)

    class Meta:
        model = Session
        fields = ( 'id', 'session_date', 'monkey', 'gym', 'extra_points', 'workout',
                  'quest_one_id', 'quest_one_attempts', 'quest_two_id', 'quest_two_attempts',
                  'quest_three_id', 'quest_three_attempts', 'session_exp', 'c_routes',
                  'v_routes', 'y_routes')

class MonkeySerializer(serializers.ModelSerializer):
    player = serializers.ReadOnlyField(source='player.username')
    #crest = serializers.URLField()
    experience = serializers.IntegerField(read_only = True)
    level = serializers.IntegerField(read_only=True)
    home_gym = serializers.StringRelatedField(many=False)
    sessions = SessionSerializer(many=True, read_only=True)
    quests = QuestSerializer(many=True, read_only=True)

    class Meta:
        model = Monkey
        depth = 3
        fields = ('id', 'player', 'name', 'date_created', 'home_gym',
                'experience', 'level', 'main_color_grade', 'main_v_grade', 'main_y_grade', 'sessions', 'quests')

class UserSerializer(serializers.ModelSerializer):
    monkey = MonkeySerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'monkey')
