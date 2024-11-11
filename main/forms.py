from django import forms
from .models import Usuario, Pregunta, OpcionPregunta

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'edad']

class PreguntaForm(forms.Form):
    # Inicializar un diccionario para almacenar las preguntas
    preguntas = Pregunta.objects.all()

    # Iterar sobre las preguntas y agregar campos dinámicamente
    for pregunta in preguntas:
        tipo_pregunta = pregunta.tipo_pregunta
        
        # Si la pregunta es de opción múltiple
        if tipo_pregunta == 'opcion_multiple':
            opciones = OpcionPregunta.objects.filter(pregunta=pregunta)
            opciones_choices = [(opcion.id, opcion.texto_opcion) for opcion in opciones]
            campo = forms.ChoiceField(
                choices=opciones_choices,
                widget=forms.RadioSelect,
                label=pregunta.texto_pregunta
            )
            # Agregar dinámicamente al formulario
            locals()[f'pregunta_{pregunta.id}'] = campo
        
        # Si la pregunta es de escala (por ejemplo, de 1 a 10)
        elif tipo_pregunta == 'escala':
            campo = forms.IntegerField(
                min_value=0, max_value=10,
                label=pregunta.texto_pregunta
            )
            # Agregar dinámicamente al formulario
            locals()[f'pregunta_{pregunta.id}'] = campo
