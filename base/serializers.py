#we created this file because , the model's data cant be passed through api , the data should be first converted to json format to be passed through api

from rest_framework import serializers
from .models import MyUser

class MyUserProfileSerializer(serializers.ModelSerializer):

    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ['username','bio','profile_image','follower_count','following_count']

    def get_follower_count(self,obj):
        return obj.followers.count()
    def get_following_count(self,obj):
        return obj.following.count()