from io import BytesIO
import pandas as pd
from django.http import JsonResponse, HttpResponse
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pdfkit
import base64
from django.http import HttpResponse
from .contentPrincipal import get_profile
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import FicheAgentSerializer, DefaultDataListSerializer, RecuCaisseSerializer, JournalCaisseSerializer, RecuFraisScolaireSerializer, StudentCardSerializer, TimeTableSerializer, ClosedCashSerializer, FicheEleveSerializer, FicheTeacherSerializer, BulletinPaieSerializer, AvisPaiementSerializer, AgentCardSerializer, CreateCertifcatSerializer, GetCertifcatSerializer, ReleveNoteSerializer, ReceiptTransfertSerializer, BulletinSerializer
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
from .templatepdf.quillsnow import quillsnow
from smaartpro.models import FeesReceipt, DataList, FicheAgent, FicheEleve, FicheTeacher, RecuCaisse, CloseCash, StudentCard, TimeTable, TypeReceiptEnum, Bulletin, AgentCard, AvisPaiement, Certificat, ReleveNote, RecuTransfert
from smaartpro.utils import traitement_html, generate_qr_code, AGENT_PREFIX, TEACHER_PREFIX,STUDENT_PREFIX, RECEIPT_FEES_PREFIX, RECEIPT_TRANSACTION_PREFIX, RECEIPT_TRANSFERT_INTERCASH
import pickle
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from django.template.loader import render_to_string

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
            data['agent']['qrCode'] = generate_qr_code(AGENT_PREFIX + data['agent']['id'])
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
            if len(data['transactions']) > 0:
                data['qrcode'] = generate_qr_code(RECEIPT_TRANSACTION_PREFIX + str(data['transactions'][0]['id']))
                
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            double_dataHTML = f"{dataHTML}{dataHTML}"
            pdf_data = pdfkit.from_string(double_dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
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
                templates = FeesReceipt.objects.filter(groupid=serializer.data['groupid'], receipt_type=TypeReceiptEnum.CAISSE.value, type=3)
            else:
                templates = FeesReceipt.objects.filter(groupid=serializer.data['groupid'], receipt_type=TypeReceiptEnum.ORDINAIRE.value)
           
            if(templates.exists()):
                templates = templates[0].content
                
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            data['qrcode'] = generate_qr_code(RECEIPT_FEES_PREFIX + data['recuNumber'])
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            if type_recu == TypeReceiptEnum.ORDINAIRE.value:
                sup = "<div style='page-break-after: always'></div>" if len(data['transactions']) > 4 else '<div></div>' 
                dataHTML = dataHTML + sup + dataHTML
            #set two receipt if ordinaire
            options = {
                'encoding': 'UTF-8',
                'enable-local-file-access': True,
                'no-outline': None,
            }
            pdf_data = pdfkit.from_string(dataHTML , False, options=options)
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
            data['student']['qrCode'] = generate_qr_code(STUDENT_PREFIX + data['student']['id'])
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
            data['teacher']['qrCode'] = generate_qr_code(TEACHER_PREFIX + data['teacher']['id'])
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
    
    
class StudentCardView(APIView):
    @swagger_auto_schema(
        request_body=StudentCardSerializer
    )
    def post(self, request, format=None):
        serializer = StudentCardSerializer(data=request.data)
        if serializer.is_valid():
            templates = StudentCard.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = StudentCard.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            for student in data['students']:
                student['qrCode'] = 'data:application/pdf;base64,' + generate_qr_code(STUDENT_PREFIX + student['id'])
           
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AvisPaiementView(APIView):
    @swagger_auto_schema(
        request_body=AvisPaiementSerializer
    )
    def post(self, request, format=None):
        serializer = AvisPaiementSerializer(data=request.data)
        if serializer.is_valid():
            templates = AvisPaiement.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = AvisPaiement.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
           
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AgentCardView(APIView):
    @swagger_auto_schema(
        request_body=AgentCardSerializer
    )
    def post(self, request, format=None):
        serializer = AgentCardSerializer(data=request.data)
        if serializer.is_valid():
            templates = AgentCard.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = AgentCard.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            for agent in data['agents']:
                prefix = AGENT_PREFIX if data['type_agent'] == 'agent' else TEACHER_PREFIX
                agent['qrCode'] = 'data:application/pdf;base64,' + generate_qr_code(prefix + agent['id'])
            dataHTML = traitement_html(templates, data)
             #set booth for agent and beneficiare
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CertifcatView(ModelViewSet):
    serializer_class = CreateCertifcatSerializer
    queryset = Certificat.objects.all()
    
    @swagger_auto_schema(
        request_body=CreateCertifcatSerializer
    )
    def post(self, request, format=None):
        serializer = CreateCertifcatSerializer(data=request.data)
        if serializer.is_valid():
            data_ser = serializer.data
            data_ser['title'] = "Certificat de frequentation" if data_ser['type'] == 1 else "Certificat de scolarite"
            templates, is_created = Certificat.objects.get_or_create(groupid=data_ser['groupid'], type=data_ser['type'], defaults=data_ser)
            templates.content = data_ser['content']
            templates.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    

    @swagger_auto_schema(
        request_body=GetCertifcatSerializer
    )
    def get_certificat(self, request, format=None):
        serializer = GetCertifcatSerializer(data=request.data)
        if serializer.is_valid():
            templates = get_object_or_404(Certificat, groupid=serializer.data['groupid'], type=serializer.data['type'])
            dataHTML = templates.content.replace('\n', '')
            dataHTML = templates.content.replace('None', '')
            pdf_pages = []

            for student in serializer.data['students']:
                certificat = dataHTML.replace('NOM_ELEVE', student['firstName'] if student.get('firstName') else '')\
                    .replace('PRENOM_ELEVE', student['lastName'] if student.get('lastName') else '')\
                    .replace('DATE_NAISSANCE_ELEVE', student['dateOfBirth'] if student.get('') else '')\
                    .replace('GENRE_ELEVE', student['civility'] if student.get('civility') else '')\
                    .replace('ADRESSE_ELEVE', student['address'] if student.get('address') else '')\
                    .replace('CLASSE_ELEVE', student['siteClassTitle'] if student.get('siteClassTitle') else '')\
                    .replace('LIEU_NAISSANCE_ELEVE', student['birthCity'] if student.get('birthCity') else '')\
                    .replace('NATIONNALITE_ELEVE', student['nationalityTitle'] if student.get('nationalityTitle') else '')
                # Ajoutez un style pour forcer un saut de page après chaque certificat
                certificat = f'<div class="ql-editor" style="page-break-after: always;">{certificat}</div>'
                pdf_pages.append(certificat)

            # Joindre toutes les pages dans une seule chaîne
            finaldata = ''.join(pdf_pages)
            finaldata = f"<style>{quillsnow}</style> {finaldata}"
            print(finaldata)
            pdf_data = pdfkit.from_string(finaldata, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_type_certificat(self, request, pk):
        certificat = Certificat.objects.filter(groupid=pk)
        serializer = CreateCertifcatSerializer(certificat, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class GenerateNoteReportView(APIView):
    @swagger_auto_schema(
        request_body=ReleveNoteSerializer
    )
    def post(self, request):
        serializer = ReleveNoteSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Générer le contenu HTML pour le PDF
                templates = ReleveNote.objects.last()
                if templates:
                    templates = templates.content
                else:
                    templates = ''
                    
                    
                data = serializer.data
                data['eleves'] = request.data.get('eleves', [])
                data['note'] = request.data.get('note', [])
                dataHTML = traitement_html(templates, data)
                #set booth for agent and beneficiare
                dataHTML = dataHTML.replace('\n', '')
                dataHTML = dataHTML.replace('None', '')
                
                pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True, 'orientation': 'Landscape'})
                encoded_data = base64.b64encode(pdf_data).decode()
                return Response({"base64_data": encoded_data})           
            
            except Exception as e:
                return Response({
                    'status': 'error',
                    'message': str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecuTransfertView(APIView):
    @swagger_auto_schema(
        request_body=ReceiptTransfertSerializer
    )
    def post(self, request, format=None):
        serializer = ReceiptTransfertSerializer(data=request.data)
        if serializer.is_valid():
            templates = RecuTransfert.objects.filter(groupid=serializer.data['groupid'])
            if(templates.exists()):
                templates = templates[0].content
            else:
                templates = RecuTransfert.objects.get(groupid=0).content
            #add bootstrap
            data = serializer.data
            data['bootstrap'] = bootstrap
            data['qrcode'] = generate_qr_code(RECEIPT_TRANSFERT_INTERCASH + str(data['idTransaction']))
                
            dataHTML = traitement_html(templates, data)
            
             #set booth for agent and beneficiare
            dataHTML = dataHTML.replace('\n', '')
            dataHTML = dataHTML.replace('None', '')
            dataHTML = dataHTML + "<div style='margin-bottom: 3em'></div>" + dataHTML
            pdf_data = pdfkit.from_string(dataHTML, False, options={'encoding': 'UTF-8', 'enable-local-file-access': True})
            encoded_data = base64.b64encode(pdf_data).decode()
            return Response({"base64_data": encoded_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenerateBulletinAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BulletinSerializer(data=request.data)
        if serializer.is_valid():
            bulletin_data = serializer.validated_data
            
            # Render the HTML template
            html_content = render_to_string('bulletin_template.html', {'bulletin': bulletin_data})
            
            # Return the rendered HTML as response
            return HttpResponse(html_content, content_type='text/html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    data = {
  "group": {
    "groupeLogo": "string",
    "groupeName": "string",
    "groupDevise": "string",
    "siteName": "string",
    "siteContact": "string",
    "siteAddress": "string",
    "schoolYear": "string"
  },
  "groupid": 0,
  "students": [
    {
      "matricule": "string",
      "id": "0",
      "firstName": "string",
      "lastName": "string",
      "dateOfBirth": "string",
      "civility": "string",
      "address": "string",
      "photo": "string",
      "email": "string",
      "phone1": "string",
      "phone2": "string",
      "bloodGroup": "string",
      "inscriptionStatus": "string",
      "siteClassTitle": "string",
      "siteClassCode": "string",
      "birthCity": "string",
      "nationalityTitle": "string",
      "qrCode": ""
    },
        {
      "matricule": "string",
      "id": "0",
      "firstName": "string",
      "lastName": "string",
      "dateOfBirth": "string",
      "civility": "string",
      "address": "string",
      "photo": "string",
      "email": "string",
      "phone1": "string",
      "phone2": "string",
      "bloodGroup": "string",
      "inscriptionStatus": "string",
      "siteClassTitle": "string",
      "siteClassCode": "string",
      "birthCity": "string",
      "nationalityTitle": "string",
      "qrCode": ""
    }
  ]
}
    
    data['bootstrap'] = bootstrap
    return render(request, 'work.html', data)



@csrf_exempt
def export_to_excel(request):
    #if request.method == 'POST':
        try:
            # Lire les données JSON du corps de la requête
            body = json.loads(request.body)
            data_list = body.get('dataList', [])
            title = body.get('title') if  body.get('title')  else 'data'

            # Convertir la liste en DataFrame
            df = pd.DataFrame(data_list)

            # Créer un fichier Excel en mémoire
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={title}.xlsx'

            # Écrire le DataFrame dans le fichier Excel
            with pd.ExcelWriter(response, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')

            return response
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    #else:
        #return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
