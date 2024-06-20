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
    qrCode = serializers.CharField(allow_null=True, allow_blank=True)   
    birthCity = serializers.CharField(allow_null=True, allow_blank=True)   
    dateOfBirth = serializers.CharField(allow_null=True, allow_blank=True)   
    
class SiteSerializer(Serializer):
    name = serializers.CharField(allow_null=True, allow_blank=True) 
    description = serializers.CharField(allow_null=True, allow_blank=True) 
    siteCode = serializers.CharField(allow_null=True, allow_blank=True) 
    address = serializers.CharField(allow_null=True, allow_blank=True) 
    phoneNumbers = serializers.CharField(allow_null=True, allow_blank=True) 

class FicheAgentSerializer(Serializer):
    group = GroupSerializer()
    agent = AgentSerializer()
    site = SiteSerializer()
    
    
#########DEFAULT LIST DATA##################
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


#############RECU CAISSE##############################
class CaisseTransactionSerializer(Serializer):
    label = serializers.CharField(allow_null=True, allow_blank=True)
    type = serializers.CharField(allow_null=True, allow_blank=True)
    typeRecipient = serializers.CharField(allow_null=True, allow_blank=True)
    payMode = serializers.CharField(allow_null=True, allow_blank=True)
    amount = serializers.CharField(allow_null=True, allow_blank=True)
    
class RecuCaisseSerializer(Serializer):
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
    """
    paymentMethod = serializers.CharField(allow_null=True, allow_blank=True)
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
    

class RecuFraisScolaireSerializer(Serializer):
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
    transactions = CaisseTransactionSerializer(many=True)
    totalAmountTransaction = serializers.CharField(allow_null=True, allow_blank=True)
    isDebit = serializers.BooleanField(allow_null=True)
  


###########EMPLOI DU TEMPS######################3
class DaysDataSerializer(Serializer):
    matiere = serializers.CharField(allow_null=True, allow_blank=True)
    salle = serializers.CharField(allow_null=True, allow_blank=True)
    teacher = serializers.CharField(allow_null=True, allow_blank=True)

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

    
class SoldCashSerializer(Serializer):
    closureDateTime = serializers.CharField(allow_null=True, allow_blank=True)
    openingBalance = serializers.CharField(allow_null=True, allow_blank=True)
    totalCashIn = serializers.CharField(allow_null=True, allow_blank=True)
    totalCashOut = serializers.CharField(allow_null=True, allow_blank=True)
    closingBalance = serializers.CharField(allow_null=True, allow_blank=True)
    currentSold = serializers.CharField(allow_null=True, allow_blank=True)
    compte_caisse = serializers.CharField(allow_null=True, allow_blank=True)
    caisse_name = serializers.CharField(allow_null=True, allow_blank=True)
    
class ClosedCashSerializer(Serializer):
    group = GroupSerializer()
    transactions = TransactionSerializer(many=True)
    sold = SoldCashSerializer()
    #totalDebit = serializers.CharField(allow_null=True, allow_blank=True)
    #totalCredit = serializers.CharField(allow_null=True, allow_blank=True)
    printerName = serializers.CharField(allow_null=True, allow_blank=True)
    #losedSold = serializers.CharField(allow_null=True, allow_blank=True)