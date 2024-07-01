from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pdfkit
import base64
from django.http import HttpResponse
from .contentPrincipal import get_profile
from rest_framework.views import APIView
from .serializers import FicheAgentSerializer, DefaultDataListSerializer, RecuCaisseSerializer, JournalCaisseSerializer, RecuFraisScolaireSerializer, TimeTableSerializer, ClosedCashSerializer, FicheEleveSerializer, FicheTeacherSerializer
from rest_framework.response import Response
from rest_framework import status
from .templatepdf.agent_default_profil import default_profile
from .templatepdf.data_list_default import default_list
from .templatepdf.recu_caisse import recu_caisse
from .templatepdf.journal_caisse import journal_caisse
from .templatepdf.recu_frais import recu_frais
from .templatepdf.timeslot import timeslot
from .templatepdf.closed_cash import closed_Cash
from.templatepdf.student_default_profil import default_profile_student
from .templatepdf.enseignant_fiche import default_profile_teacher
from drf_yasg.utils import swagger_auto_schema
import base64
from .templatepdf.bootstrap import bootstrap
from smaartpro.models import FeesReceipt, TypeReceiptEnum
from smaartpro.utils import traitement_html


class FicheAgentView(APIView):
    @swagger_auto_schema(
        request_body=FicheAgentSerializer
    )
    def post(self, request, format=None):
        serializer = FicheAgentSerializer(data=request.data)
        if serializer.is_valid():
            base64Data = default_profile(serializer.data)
            pdf_data = pdfkit.from_string(base64Data, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DefaultDataListView(APIView):
    @swagger_auto_schema(
        request_body=DefaultDataListSerializer
    )
    def post(self, request, format=None):
        serializer = DefaultDataListSerializer(data=request.data)
        if serializer.is_valid():
            dataHTML = default_list(serializer.data)
            orientation = 'Portrait' if serializer.data['portrait'] == True else 'Landscape'
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True, 'orientation': orientation})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RecuCaisseView(APIView):
    @swagger_auto_schema(
        request_body=RecuCaisseSerializer
    )
    def post(self, request, format=None):
        serializer = RecuCaisseSerializer(data=request.data)
        if serializer.is_valid():
            dataHTML = recu_caisse(serializer.data)
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class JournalCaisseView(APIView):
    @swagger_auto_schema(
        request_body=JournalCaisseSerializer
    )
    def post(self, request, format=None):
        serializer = JournalCaisseSerializer(data=request.data)
        if serializer.is_valid():
            dataHTML = journal_caisse(serializer.data)
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
class RecuFraisView(APIView):
    @swagger_auto_schema(
        request_body=RecuFraisScolaireSerializer
    )
    def post(self, request, format=None):
        serializer = RecuFraisScolaireSerializer(data=request.data)
        
        if serializer.is_valid():
            templates = FeesReceipt.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = FeesReceipt.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML + '<div class="my-3"></div>' + dataHTML
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class TimeSlotView(APIView):
    @swagger_auto_schema(
        request_body=TimeTableSerializer
    )
    def post(self, request, format=None):
        serializer = TimeTableSerializer(data=request.data)
        if serializer.is_valid():
            dataHTML = timeslot(serializer.data)
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True, 'orientation': 'Landscape'})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ClosedCashView(APIView):
    @swagger_auto_schema(
        request_body=ClosedCashSerializer
    )
    def post(self, request, format=None):
        serializer = ClosedCashSerializer(data=request.data)
        if serializer.is_valid():
            dataHTML = closed_Cash(serializer.data)
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FicheEleveView(APIView):
    @swagger_auto_schema(
        request_body=FicheEleveSerializer
    )
    def post(self, request, format=None):
        serializer = FicheEleveSerializer(data=request.data)
        if serializer.is_valid():
            
            dataHTML = default_profile_student(serializer.data)
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class FicheTeacherView(APIView):
    @swagger_auto_schema(
        request_body=FicheTeacherSerializer
    )
    def post(self, request, format=None):
        serializer = FicheTeacherSerializer(data=request.data)
        if serializer.is_valid():
            dataHTML = default_profile_teacher(serializer.data)
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



def home(request):
    templates = FeesReceipt.objects.filter(groupid=1)
    if(templates.exists()):
        templates = templates[0].content
    else:
        templates = FeesReceipt.objects.get(groupid=0).content
    data = {
        "groupeLogo": "string",
        "groupeName": "string",
        "groupeDevise": "string",
        "siteName": "string",
        "siteAdress": "string",
        "siteContact": "string",
        "caisse": "string",
        "scholarYear": "string",
        "dateRecu": "string",
        "recuNumber": "string",
        "printerAgent": "string",
        "eleveName": "string",
        "elevePrenom": "string",
        "niveau": "string",
        "matricule": "string",
        "transactions": [
            {
                "label": "string",
                "type": "string",
                "typeRecipient": "string",
                "payMode": "string",
                "amount": "string"
            }
        ],
        "totalAmountTransaction": "string",
        "isDebit": True
    }
    return render(request, 'index.html', data)

