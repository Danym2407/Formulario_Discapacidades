from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UsuarioForm, PreguntaForm
from .models import Usuario, Pregunta, Respuesta, OpcionPregunta

def home(request):
    return render(request, "main/home.html")

def cuestionario_view(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        pregunta_form = PreguntaForm(request.POST)

        if usuario_form.is_valid() and pregunta_form.is_valid():
            usuario = usuario_form.save()

            # Iterar sobre los campos dinámicamente generados en el formulario
            for field_name, field_value in pregunta_form.cleaned_data.items():
                if field_name.startswith('pregunta_'):
                    pregunta_id = field_name.split('_')[1]  # Extraer el ID de la pregunta del nombre del campo
                    pregunta = Pregunta.objects.get(id=pregunta_id)

                    # Procesar diferentes tipos de respuesta según el tipo de pregunta
                    if pregunta.tipo_pregunta == 'opcion_multiple':
                        opcion = OpcionPregunta.objects.get(id=field_value)
                        Respuesta.objects.create(
                            usuario=usuario,
                            pregunta=pregunta,
                            respuesta_opcion=opcion
                        )
                    elif pregunta.tipo_pregunta == 'escala':
                        Respuesta.objects.create(
                            usuario=usuario,
                            pregunta=pregunta,
                            respuesta_escala=field_value
                        )

            return redirect('gracias')  # Asegúrate de usar el nombre correcto de la URL
    else:
        usuario_form = UsuarioForm()
        pregunta_form = PreguntaForm()

    return render(request, 'main/cuestionario.html', {
        'usuario_form': usuario_form,
        'pregunta_form': pregunta_form,
    })

def gracias_view(request):
    return render(request, 'main/gracias.html', {'mensaje': "Gracias por contestar, tus respuestas han sido enviadas"})
