
from rest_framework import serializers
from users.models import Citizen,Officer,Message,Agency
from reports.models import Report,Incident,ThreatLevel,Status
from django.contrib.auth.models import User
from django.shortcuts import render


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','is_staff']

class CitizenSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Citizen
        fields=['user','profile_picture','phone']

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Officer
        fields=['user','profile_picture','location']

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model=Agency
        fields=['name']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=['status_name']
    

class ThreatLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ThreatLevel
        fields=['threat_level_name','color']

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Incident
        fields=['incident_name','threat_level']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields=['incident','citizen','officer','status','media','location']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields='__all__'