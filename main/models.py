from django.db import models

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=255)
    edad = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo

class Pregunta(models.Model):
    TEXTO = 'texto'
    OPCION_MULTIPLE = 'opcion_multiple'
    ESCALA = 'escala'

    TIPO_PREGUNTA_CHOICES = [
        (TEXTO, 'Texto'),
        (OPCION_MULTIPLE, 'Opción múltiple'),
        (ESCALA, 'Escala'),
    ]

    texto_pregunta = models.TextField()
    tipo_pregunta = models.CharField(max_length=20, choices=TIPO_PREGUNTA_CHOICES)

    def __str__(self):
        return self.texto_pregunta

class OpcionPregunta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    texto_opcion = models.CharField(max_length=255)

    def __str__(self):
        return self.texto_opcion

class Respuesta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_texto = models.TextField(blank=True, null=True)  # Para respuestas de texto
    respuesta_opcion = models.ForeignKey(OpcionPregunta, blank=True, null=True, on_delete=models.CASCADE)  # Para opción múltiple
    respuesta_escala = models.IntegerField(blank=True, null=True)  # Para la escala (0-10)

    def __str__(self):
        return f"Respuesta de {self.usuario} a la pregunta {self.pregunta.id}"
