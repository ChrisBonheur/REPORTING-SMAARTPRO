from rest_framework.serializers import Serializer
from rest_framework import serializers


class GroupSerializer(Serializer):
    groupeLogo = serializers.CharField(allow_null=True, allow_blank=True)
    groupeName = serializers.CharField(allow_null=True, allow_blank=True)
    groupDevise = serializers.CharField(allow_null=True, allow_blank=True)
    siteName = serializers.CharField(allow_null=True, allow_blank=True)
    siteContact = serializers.CharField(allow_null=True, allow_blank=True)
    siteAddress = serializers.CharField(allow_null=True, allow_blank=True)
    schoolYear = serializers.CharField(allow_null=True, allow_blank=True)
    
    
class AgentSerializer(Serializer):
    photo = serializers.CharField(allow_null=True, allow_blank=True)
    id = serializers.CharField(allow_null=True, allow_blank=True, default=0)
    civility = serializers.IntegerField()
    nom = serializers.CharField(allow_null=True, allow_blank=True)
    prenom = serializers.CharField(allow_null=True, allow_blank=True)
    email = serializers.CharField(allow_null=True, allow_blank=True) 
    address = serializers.CharField(allow_null=True, allow_blank=True) 
    cityName = serializers.CharField(allow_null=True, allow_blank=True) 
    cityArea = serializers.CharField(allow_null=True, allow_blank=True) 
    street = serializers.CharField(allow_null=True, allow_blank=True) 
    nationalityName = serializers.CharField(allow_null=True, allow_blank=True) 
    phone1 = serializers.CharField(allow_null=True, allow_blank=True) 
    phone2 = serializers.CharField(allow_null=True, allow_blank=True) 
    roleName = serializers.CharField(allow_null=True, allow_blank=True)
    qrCode = serializers.CharField(allow_null=True, allow_blank=True, default='')
    birthCity = serializers.CharField(allow_null=True, allow_blank=True)   
    dateOfBirth = serializers.CharField(allow_null=True, allow_blank=True)


class StudentSerializer(Serializer):
    matricule = serializers.CharField(allow_null=True, allow_blank=True)
    id = serializers.CharField(allow_null=True, allow_blank=True, default=0)
    firstName = serializers.CharField(allow_null=True, allow_blank=True)
    lastName = serializers.CharField(allow_null=True, allow_blank=True)
    dateOfBirth = serializers.CharField(allow_null=True, allow_blank=True)
    civility = serializers.CharField(allow_null=True, allow_blank=True)
    address = serializers.CharField(allow_null=True, allow_blank=True)
    photo = serializers.CharField(allow_null=True, allow_blank=True)
    email = serializers.CharField(allow_null=True, allow_blank=True)
    phone1 = serializers.CharField(allow_null=True, allow_blank=True)
    phone2 = serializers.CharField(allow_null=True, allow_blank=True)
    bloodGroup = serializers.CharField(allow_null=True, allow_blank=True)
    inscriptionStatus = serializers.CharField(allow_null=True, allow_blank=True)
    siteClassTitle = serializers.CharField(allow_null=True, allow_blank=True)
    birthCity = serializers.CharField(allow_null=True, allow_blank=True)
    nationalityTitle = serializers.CharField(allow_null=True, allow_blank=True)
    # cityArea = serializers.CharField(allow_null=True, allow_blank=True)
    qrCode = serializers.CharField(allow_null=True, allow_blank=True, default="")


class TeacherSerializer(Serializer):
    photo = serializers.CharField(allow_null=True, allow_blank=True)
    id = serializers.CharField(allow_null=True, allow_blank=True, default=0)
    civility = serializers.IntegerField()
    nom = serializers.CharField(allow_null=True, allow_blank=True)
    prenom = serializers.CharField(allow_null=True, allow_blank=True)
    email = serializers.CharField(allow_null=True, allow_blank=True) 
    address = serializers.CharField(allow_null=True, allow_blank=True) 
    cityName = serializers.CharField(allow_null=True, allow_blank=True) 
    cityArea = serializers.CharField(allow_null=True, allow_blank=True) 
    address = serializers.CharField(allow_null=True, allow_blank=True) 
    nationalityName = serializers.CharField(allow_null=True, allow_blank=True) 
    phone1 = serializers.CharField(allow_null=True, allow_blank=True) 
    phone2 = serializers.CharField(allow_null=True, allow_blank=True) 
    qrCode = serializers.CharField(allow_null=True, allow_blank=True, default='')
    birthCity = serializers.CharField(allow_null=True, allow_blank=True)   
    birthDate = serializers.CharField(allow_null=True, allow_blank=True)



class SiteSerializer(Serializer):
    name = serializers.CharField(allow_null=True, allow_blank=True)
    description = serializers.CharField(allow_null=True, allow_blank=True)
    siteCode = serializers.CharField(allow_null=True, allow_blank=True)
    address = serializers.CharField(allow_null=True, allow_blank=True)

class FicheAgentSerializer(Serializer):
    group = GroupSerializer()
    agent = AgentSerializer()
    site = SiteSerializer()
    groupid = serializers.IntegerField(allow_null=True, default=0)


class FicheEleveSerializer(Serializer):
    group = GroupSerializer()
    student = StudentSerializer()
    groupid = serializers.IntegerField(allow_null=True, default=0)


class MatiereNiveaux(Serializer):
   matiere = serializers.CharField(allow_null=True, allow_blank=True) 
   levels = serializers.CharField(allow_null=True, allow_blank=True) 


class FicheTeacherSerializer(Serializer):
    group = GroupSerializer()
    teacher = TeacherSerializer()
    matieres = MatiereNiveaux(many=True)
    groupid = serializers.IntegerField(allow_null=True, default=0)
    
# ########DEFAULT LIST DATA##################


class DataTotalListSerializer(Serializer):
    key = serializers.CharField(allow_null=True, allow_blank=True)
    value = serializers.CharField(allow_null=True, allow_blank=True)    


class DefaultDataListSerializer(Serializer):
    title = serializers.CharField()
    group = GroupSerializer()
    heads = serializers.ListField(child=serializers.CharField())
    dataList = serializers.ListField(child=serializers.ListField(child=serializers.CharField()))
    portrait = serializers.BooleanField(allow_null=True)
    totalData = serializers.ListField(child=DataTotalListSerializer())
    groupid = serializers.IntegerField(allow_null=True, default=0)


#############RECU CAISSE##############################


class CaisseTransactionSerializer(Serializer):
    label = serializers.CharField(allow_null=True, allow_blank=True)
    numerate = serializers.CharField(allow_null=True, allow_blank=True)
    typeRecipient = serializers.CharField(allow_null=True, allow_blank=True)
    payMode = serializers.CharField(allow_null=True, allow_blank=True)
    amount = serializers.CharField(allow_null=True, allow_blank=True)


class RecuCaisseSerializer(Serializer):
    groupid = serializers.IntegerField(allow_null=True, default=0)
    modePay = serializers.CharField(allow_null=True, allow_blank=True)
    groupeLogo = serializers.CharField(allow_null=True, allow_blank=True)
    groupeName = serializers.CharField(allow_null=True, allow_blank=True)
    groupeDevise = serializers.CharField(allow_null=True, allow_blank=True)
    siteName = serializers.CharField(allow_null=True, allow_blank=True)
    siteAdress = serializers.CharField(allow_null=True, allow_blank=True)
    siteContact = serializers.CharField(allow_null=True, allow_blank=True)
    caisse = serializers.CharField(allow_null=True, allow_blank=True)
    scholarYear = serializers.CharField(allow_null=True, allow_blank=True)
    dateRecu = serializers.CharField(allow_null=True, allow_blank=True)
    recuNumber = serializers.CharField(allow_null=True, allow_blank=True)
    printerAgent = serializers.CharField(allow_null=True, allow_blank=True)
    transactions = CaisseTransactionSerializer(many=True)
    totalAmountTransaction = serializers.CharField(allow_null=True, allow_blank=True)
    isDebit = serializers.BooleanField(allow_null=True)
    
    
class TransactionSerializer(Serializer):
    transactionDate = serializers.CharField(allow_null=True, allow_blank=True)
    valueDate = serializers.CharField(allow_null=True, allow_blank=True)
    description = serializers.CharField(allow_null=True, allow_blank=True)
    recipientTypeCodeLabel = serializers.CharField(allow_null=True, allow_blank=True)
    compte = serializers.CharField(allow_null=True, allow_blank=True)
    debitAmount = serializers.CharField(allow_null=True, allow_blank=True)
    creditAmount = serializers.CharField(allow_null=True, allow_blank=True)
    paymentMethod = serializers.CharField(allow_null=True, allow_blank=True)
    """
    responsibleAgentName = serializers.CharField(allow_null=True, allow_blank=True)
    groupeTransactionTypeTitle = serializers.CharField(allow_null=True, allow_blank=True)
    cashAccountTitle = serializers.CharField(allow_null=True, allow_blank=True)
    creatorAgentName = serializers.CharField(allow_null=True, allow_blank=True)
    """


class JournalCaisseSerializer(Serializer):
    title = serializers.CharField(allow_null=True, allow_blank=True)
    scholarYear = serializers.CharField(allow_null=True, allow_blank=True)
    groupeLogo = serializers.CharField(allow_null=True, allow_blank=True)
    groupeName = serializers.CharField(allow_null=True, allow_blank=True)
    groupeDevise = serializers.CharField(allow_null=True, allow_blank=True)
    siteName = serializers.CharField(allow_null=True, allow_blank=True)
    caisse = serializers.CharField(allow_null=True, allow_blank=True)
    compte = serializers.CharField(allow_null=True, allow_blank=True)
    printerAgent = serializers.CharField(allow_null=True, allow_blank=True)
    periode = serializers.CharField(allow_null=True, allow_blank=True)
    transactions = TransactionSerializer(many=True)
    totalAmountTransaction = serializers.CharField(allow_null=True, allow_blank=True)
    totalCredit = serializers.BooleanField(allow_null=True)
    totalDebit = serializers.BooleanField(allow_null=True)
    openSold = serializers.BooleanField(allow_null=True)
    closeSold = serializers.BooleanField(allow_null=True)


class FeesCashTransactionSerializer(Serializer):
    label = serializers.CharField(allow_null=True, allow_blank=True)
    receipt_type = serializers.CharField(allow_null=True, allow_blank=True, default=0)
    typeRecipient = serializers.CharField(allow_null=True, allow_blank=True)
    amount = serializers.CharField(allow_null=True, allow_blank=True)
    restPaied = serializers.CharField(allow_null=True, allow_blank=True)
    paied = serializers.CharField(allow_null=True, allow_blank=True)


class EleveFeesSerializer(Serializer):
    standardAmount = serializers.CharField(allow_null=True, allow_blank=True)
    discountAmount = serializers.CharField(allow_null=True, allow_blank=True)
    increaseAmount = serializers.CharField(allow_null=True, allow_blank=True)
    totalAmountPaid = serializers.CharField(allow_null=True, allow_blank=True)
    transactionTypeTitle = serializers.CharField(allow_null=True, allow_blank=True)
    amountNet = serializers.CharField(allow_null=True, allow_blank=True)
    restToPay = serializers.CharField(allow_null=True, allow_blank=True)


class RecuFraisScolaireSerializer(Serializer):
    groupid = serializers.IntegerField(allow_null=True, default=0)
    receipt_type = serializers.IntegerField(allow_null=True, default=0)
    groupeLogo = serializers.CharField(allow_null=True, allow_blank=True)
    groupeName = serializers.CharField(allow_null=True, allow_blank=True)
    groupeDevise = serializers.CharField(allow_null=True, allow_blank=True)
    siteName = serializers.CharField(allow_null=True, allow_blank=True)
    siteAdress = serializers.CharField(allow_null=True, allow_blank=True)
    siteContact = serializers.CharField(allow_null=True, allow_blank=True)
    caisse = serializers.CharField(allow_null=True, allow_blank=True)
    scholarYear = serializers.CharField(allow_null=True, allow_blank=True)
    dateRecu = serializers.CharField(allow_null=True, allow_blank=True)
    recuNumber = serializers.CharField(allow_null=True, allow_blank=True)
    printerAgent = serializers.CharField(allow_null=True, allow_blank=True)
    eleveName = serializers.CharField(allow_null=True, allow_blank=True)
    elevePrenom = serializers.CharField(allow_null=True, allow_blank=True)
    niveau = serializers.CharField(allow_null=True, allow_blank=True)
    matricule = serializers.CharField(allow_null=True, allow_blank=True)
    transactions = FeesCashTransactionSerializer(many=True)
    totalAmountTransaction = serializers.CharField(allow_null=True, allow_blank=True)
    totalAmountPaied = serializers.CharField(allow_null=True, allow_blank=True)
    totalAmountRest = serializers.CharField(allow_null=True, allow_blank=True)
    modePay = serializers.CharField(allow_null=True, allow_blank=True)
    isDebit = serializers.BooleanField(allow_null=True)
    eleveFees = EleveFeesSerializer(many=True)
    ##total eleveFees
    totalstandardAmount = serializers.CharField(allow_null=True, allow_blank=True)
    totaltotalAmountPaid = serializers.CharField(allow_null=True, allow_blank=True)
    totalrestToPay = serializers.CharField(allow_null=True, allow_blank=True)

###########EMPLOI DU TEMPS######################3
class DaysDataSerializer(Serializer):
    matiere = serializers.CharField(allow_null=True, allow_blank=True, default="")
    salle = serializers.CharField(allow_null=True, allow_blank=True, default="")
    teacher = serializers.CharField(allow_null=True, allow_blank=True, default="")
    otherValue = serializers.CharField(allow_null=True, allow_blank=True, default="")

class SlotLineSerializer(Serializer):
    hour = serializers.CharField(allow_null=True, allow_blank=True)
    monday = DaysDataSerializer()
    tuesday = DaysDataSerializer()
    wednesday = DaysDataSerializer()
    thursday = DaysDataSerializer()
    friday = DaysDataSerializer()
    saturday = DaysDataSerializer()
    sunday = DaysDataSerializer()
    
class TimeTableSerializer(Serializer):
    title = serializers.CharField(allow_null=True, allow_blank=True)
    data = SlotLineSerializer(many=True)
    group = GroupSerializer()
    groupid = serializers.IntegerField(allow_null=True, default=0)

    
class SoldCashSerializer(Serializer):
    closureDateTime = serializers.CharField(allow_null=True, allow_blank=True)
    openingBalance = serializers.CharField(allow_null=True, allow_blank=True)
    totalCashIn = serializers.CharField(allow_null=True, allow_blank=True)
    totalCashOut = serializers.CharField(allow_null=True, allow_blank=True)
    closingBalance = serializers.CharField(allow_null=True, allow_blank=True)
    currentSold = serializers.CharField(allow_null=True, allow_blank=True)
    compte_caisse = serializers.CharField(allow_null=True, allow_blank=True)
    caisse_name = serializers.CharField(allow_null=True, allow_blank=True)

class TotalByMethod(Serializer):
    title = serializers.CharField(allow_null=True, allow_blank=True)
    totalCredit = serializers.CharField(allow_null=True, allow_blank=True)
    totalDebit = serializers.CharField(allow_null=True, allow_blank=True)
    
class ClosedCashSerializer(Serializer):
    groupid = serializers.IntegerField(allow_null=True, default=0)
    group = GroupSerializer()
    transactions = TransactionSerializer(many=True)
    sold = SoldCashSerializer()
    #totalDebit = serializers.CharField(allow_null=True, allow_blank=True)
    #totalCredit = serializers.CharField(allow_null=True, allow_blank=True)
    printerName = serializers.CharField(allow_null=True, allow_blank=True)
    totalByMode = TotalByMethod(many=True)
    #losedSold = serializers.CharField(allow_null=True, allow_blank=True)
    
    
    
###############################BULLETIN
class BulletinCalculSerializer(Serializer):
    base_salary = serializers.CharField(allow_null=True, allow_blank=True)
    base_salary_horaire = serializers.CharField(allow_null=True, allow_blank=True)
    volume_horaire_mensuel = serializers.CharField(allow_null=True, allow_blank=True)
    day_work_number = serializers.CharField(allow_null=True, allow_blank=True)
    late_justify = serializers.CharField(allow_null=True, allow_blank=True)
    holiday = serializers.CharField(allow_null=True, allow_blank=True)
    

class BulletinRecipientAgentOrEnsignantSerializer(Serializer):
    fullname = serializers.CharField(allow_null=True, allow_blank=True)
    fonction = serializers.CharField(allow_null=True, allow_blank=True)
    matricule = serializers.CharField(allow_null=True, allow_blank=True)
    
class BulletinDetailsSerializer(Serializer):
    label = serializers.CharField(allow_null=True, allow_blank=True)
    amount = serializers.CharField(allow_null=True, allow_blank=True)
    
class BulletinPaieSerializer(Serializer):
    group = GroupSerializer()
    groupid = serializers.IntegerField(allow_null=True, default=0)
    recipient = serializers.CharField(allow_null=True, default=0)
    month = serializers.CharField(allow_null=True, allow_blank=True)
    date = serializers.CharField(allow_null=True, allow_blank=True)
    agent = serializers.CharField(allow_null=True, allow_blank=True)
    recipient = BulletinRecipientAgentOrEnsignantSerializer()
    remunerations = BulletinDetailsSerializer(many=True)
    deductions = BulletinDetailsSerializer(many=True)
    base_calcul = BulletinDetailsSerializer(many=True)
    total_remuneration = serializers.CharField(allow_null=True, allow_blank=True)
    total_deduction = serializers.CharField(allow_null=True, allow_blank=True)
    brut_salary = serializers.CharField(allow_null=True, allow_blank=True)
    net_to_pay = serializers.CharField(allow_null=True, allow_blank=True)
    
    
