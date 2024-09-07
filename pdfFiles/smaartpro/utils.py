import locale
from datetime import datetime
import pytz
import qrcode
import base64
from io import BytesIO
from django.template import Template, Context
from django.utils.safestring import mark_safe


AGENT_PREFIX = "AG"
TEACHER_PREFIX = "ES"
STUDENT_PREFIX = "LV"
RECEIPT_FEES_PREFIX = "REC"
RECEIPT_TRANSACTION_PREFIX = "TRN"


week_days = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"    
]

def get_current_datetime():
    tz = pytz.timezone('Africa/Kinshasa')  # Par exemple, Kinshasa est dans le fuseau horaire de l'Afrique centrale

    # Définir la locale en français
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

    # Obtenir la date et l'heure actuelles
    now = datetime.now(tz)

    # Formater la date et l'heure de manière lisible par les humains en français
    return now.strftime("%A %d %B %Y %H:%M:%S %Z")

def traitement_html(content, dataContext):
    templates = Template(content)
    context = Context(dataContext)
    rendered_html = templates.render(context)
    return mark_safe(rendered_html)


def generate_qr_code(data: str):
    # Générer le code QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Créer une image PNG du code QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Sauvegarder l'image dans un buffer en mémoire
    buffered = BytesIO()
    img.save(buffered, format="PNG")

    # Encoder l'image en base64
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return img_base64


