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
from .serializers import FicheAgentSerializer, DefaultDataListSerializer, RecuCaisseSerializer, JournalCaisseSerializer, RecuFraisScolaireSerializer, TimeTableSerializer, ClosedCashSerializer, FicheEleveSerializer, FicheTeacherSerializer, BulletinPaieSerializer
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
from smaartpro.models import FeesReceipt, DataList, FicheAgent, FicheEleve, FicheTeacher, RecuCaisse, CloseCash, TimeTable, TypeReceiptEnum, Bulletin
from smaartpro.utils import traitement_html, generate_qr_code
import pickle


class FicheAgentView(APIView):
    @swagger_auto_schema(
        request_body=FicheAgentSerializer
    )
    def post(self, request, format=None):
        serializer = FicheAgentSerializer(data=request.data)
        if serializer.is_valid():
            templates = FicheAgent.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = FicheAgent.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
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
            templates = DataList.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = DataList.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            data['colspan'] = len(data['heads']) - len(data['totalData'])
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
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
            templates = RecuCaisse.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = RecuCaisse.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
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
            type_recu = TypeReceiptEnum.ORDINAIRE.value
            if(serializer.data.get('receipt_type') and serializer.data['receipt_type'] == TypeReceiptEnum.CAISSE.value):
                type_recu = TypeReceiptEnum.CAISSE.value
                templates = FeesReceipt.objects.filter(groupid=serializer.data['groupid'], receipt_type=TypeReceiptEnum.CAISSE.value)
            else:
                templates = FeesReceipt.objects.filter(groupid=serializer.data['groupid'], receipt_type=TypeReceiptEnum.ORDINAIRE.value)
           
            if(templates.exists()):
                templates = templates[0].content
                
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            data['qrcode'] = generate_qr_code("REC" + data['recuNumber'])
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            #set two receipt if ordinaire
            pdf_data = pdfkit.from_string(dataHTML , False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
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
            templates = TimeTable.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = TimeTable.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            data['days'] = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
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
            templates = CloseCash.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = CloseCash.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
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
            templates = FicheEleve.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = FicheEleve.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
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
            templates = FicheTeacher.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = FicheTeacher.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class BulletinView(APIView):
    @swagger_auto_schema(
        request_body=BulletinPaieSerializer
    )
    def post(self, request, format=None):
        serializer = BulletinPaieSerializer(data=request.data)
        if serializer.is_valid():
            templates = Bulletin.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = Bulletin.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    
class AirtelMomo(APIView):
    def post(self, request, format=None):
        with open('data.pkl', 'wb') as file_to_write:
            pickle.dump(request.data, file_to_write)
        return Response({}) 


def home(request):
    import pickle
    import pprint
    chemin_pickle = 'pdfFiles/data.pkl'
    
    # Charger le contenu du fichier pickle
    with open(chemin_pickle, 'rb') as fichier:
        contenu = pickle.load(fichier)
    
    # Utiliser pprint pour formater l'affichage
    contenu_formate = pprint.pformat(contenu, indent=4)
    
    # Retourner le contenu formatté dans la réponse HTTP
    return HttpResponse(f"<pre>{contenu_formate}</pre>")


