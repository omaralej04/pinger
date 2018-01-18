from pushbullet.pushbullet import PushBullet
import time
from datetime import datetime

#insert pushbullet API key
apiKey = ""

p = PushBullet(apiKey)
# Get a list of devices
devices = p.getDevices()

# Get a list of contacts
contacts = p.getContacts()

# My Iphone Addr
phone = devices[0]["iden"]

def send_message(status):
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Checkin' status"
    if status:
        print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Enviando mensaje Positivo"
        p.pushNote(phone, 'La Pagina Funciona!', 'Se reporta que la pagina no ha enviado el mensaje negativo')
    else:
        print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Enviando mensaje Negativo (Console Only Mode)"
        # p.pushNote(phone, 'No es posible la operacion', 'Se reporta que la pagina ha enviado el mensaje negativo')
