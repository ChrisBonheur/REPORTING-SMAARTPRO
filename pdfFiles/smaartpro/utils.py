import locale
from datetime import datetime
import pytz

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