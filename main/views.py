from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UsuarioForm, PreguntaForm

def home(request):
    return render(request, "main/home.html")

def cuestionario_view(request):
    pagina = int(request.GET.get('pagina', 1))  # Default a la página 1 si no está en GET

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        pregunta_form = PreguntaForm(request.POST)
        if usuario_form.is_valid() and pregunta_form.is_valid():
            # Aquí puedes guardar la información del formulario si es necesario
            return redirect('gracias')
    else:
        usuario_form = UsuarioForm()
        pregunta_form = PreguntaForm()

    if pagina == 1:
        return render(request, 'main/cuestionario.html', {
            'usuario_form': usuario_form,
            'pregunta_form': pregunta_form,
            'pagina': 1,
        })
    elif pagina == 2:
        return render(request, 'main/cuestionario.html', {
            'usuario_form': usuario_form,
            'pregunta_form': pregunta_form,
            'pagina': 2,
        })
    elif pagina == 3:
        return render(request, 'main/cuestionario.html', {
            'usuario_form': usuario_form,
            'pregunta_form': pregunta_form,
            'pagina': 3,
        })
    else:
        return render(request, 'main/cuestionario.html', {})
