from rest_framework import serializers

from .models import *

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = ('name',)

class WeaknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weakness
        fields = ('name',)

class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ('intelligence', 'strength', 'speed', 'durability', 'power', 'combat',)

class HeroSerializer(serializers.ModelSerializer):
    attributes = AttributesSerializer()
    powers = serializers.CharField(source='power_list')
    weaknesses = serializers.CharField(source='weakness_list')

    class Meta:
        model = Heroes
        fields = ('hero_name', 'real_name', 'gender', 'attributes', 'powers', 'weaknesses',)

