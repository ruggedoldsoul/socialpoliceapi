from django.shortcuts import render
from .serializers import( UserSerializer,
AgencySerializer,
CitizenSerializer,
OfficerSerializer,
ReportSerializer,
IncidentSerializer,
StatusSerializer,
ThreatLevelSerializer,MessageSerializer
)
from users.models import Citizen,Officer,Message,Agency
from reports.models import Report,Incident,ThreatLevel,Status
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CitizenViewSet(viewsets.ModelViewSet):
    queryset=Citizen.objects.all()
    serializer_class=CitizenSerializer

class OfficerViewSet(viewsets.ModelViewSet):
    queryset=Officer.objects.all()
    serializer_class=OfficerSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset=Incident.objects.all()
    serializer_class=IncidentSerializer

class ThreatLevelViewSet(viewsets.ModelViewSet):
    queryset=ThreatLevel.objects.all()
    serializer_class=ThreatLevelSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer


class AgencyViewSet(viewsets.ModelViewSet):
    queryset=Agency.objects.all()
    serializer_class=AgencySerializer
