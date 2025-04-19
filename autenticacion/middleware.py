from django.contrib.auth import logout
from django.contrib import messages
from .models import SesionUsuario
from django.shortcuts import redirect

class SingleSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                session = SesionUsuario.objects.get(usuario=request.user)
                if session.session_key != request.session.session_key:
                    logout(request)
                    messages.warning(request, 
                        "Tu sesión se ha iniciado en otro dispositivo")
                    return redirect('Logear')
            except SesionUsuario.DoesNotExist:
                pass

        response = self.get_response(request)
        return response