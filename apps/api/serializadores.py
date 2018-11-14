from rest_framework import serializers

#from SRC.apps.muro.models import post
from ..muro.models import post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = "__all__"