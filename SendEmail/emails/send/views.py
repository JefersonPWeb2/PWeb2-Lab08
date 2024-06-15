from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    
    send_mail('HOLA PARA MI AMIGO',
    'Hola. Este es un mesaje automatico.',
    'jbasurco@unsa.edu.pe',
    ['padeb44113@kernuo.com'],
    fail_silently=False)
    
    return render(request, 'send/index.html')