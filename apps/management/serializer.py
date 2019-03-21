from rest_framework import serializers

from .models import Card,BlogSettings

class CardSer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ["id","img","title","content"]