from django.db import models
from enum import Enum


class TypeReceiptEnum(Enum):
    ORDINAIRE = 1
    CAISSE = 2
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    
class ReportingBase(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    groupid = models.IntegerField(default=0)
    
    class Meta:
        abstract = True

class FeesReceipt(ReportingBase):
    receipt_type = models.IntegerField(choices=TypeReceiptEnum.choices, default=TypeReceiptEnum.ORDINAIRE.value)
    is_family = models.BooleanField(default=False)
    
    
class DataList(ReportingBase):
    list_type = models.IntegerField(default=0)