from api.models import *
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
  songs = serializers.StringRelatedField(many=True, read_only=True)
  #songs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail') # show the hyperlink of the related songs
  #songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # show the primary key of the related songs
  class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songs']