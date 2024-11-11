from django.contrib import admin
from .models import Usuario, Pregunta, OpcionPregunta, Respuesta

admin.site.register(Usuario)
admin.site.register(Pregunta)
admin.site.register(OpcionPregunta)
admin.site.register(Respuesta)
