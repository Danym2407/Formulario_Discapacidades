from django import forms
from .models import Usuario, Pregunta 

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'edad']


class PreguntaForm(forms.Form):
    # Primer grupo de preguntas
    PREGUNTA_CHOICES = [
        ('a', 'Una condición física o mental que afecta la vida diaria'),
        ('b', 'Una diferencia de habilidades'),
        ('c', 'Algo temporal que se puede superar'),
        ('d', 'Otro (especifica): ________'),
    ]

    pregunta_1 = forms.ChoiceField(
        choices=PREGUNTA_CHOICES, widget=forms.RadioSelect, label="1. ¿Cómo defines la discapacidad?"
    )

    pregunta_2 = forms.ChoiceField(
        choices=[
            ('a', 'Sí, completamente'),
            ('b', 'Sí, pero hay mucho por mejorar'),
            ('c', 'No, los apoyos son insuficientes'),
            ('d', 'No tengo información suficiente'),
        ],
        widget=forms.RadioSelect,
        label="2. ¿Consideras que México cuenta con suficientes apoyos para personas con discapacidad?"
    )

    pregunta_3 = forms.IntegerField(
        min_value=0, max_value=10, label="3. ¿Qué tanto conoces las leyes en México que protegen los derechos de las personas con discapacidad?"
    )

    pregunta_4 = forms.ChoiceField(
        choices=[
            ('a', 'Discapacidad visual'),
            ('b', 'Discapacidad auditiva'),
            ('c', 'Discapacidad motriz'),
            ('d', 'Discapacidad intelectual'),
            ('e', 'Discapacidad psicosocial'),
        ],
        widget=forms.RadioSelect,
        label="4. ¿Cuál crees que es la discapacidad más común en México?"
    )

    pregunta_5 = forms.ChoiceField(
        choices=[
            ('a', 'Visual'),
            ('b', 'Auditiva'),
            ('c', 'Motriz'),
            ('d', 'Intelectual'),
            ('e', 'Psicosocial'),
            ('f', 'No tengo preferencia'),
        ],
        widget=forms.RadioSelect,
        label="5. ¿Con cuál de las siguientes discapacidades sientes más empatía?"
    )

    # Segundo grupo de preguntas
    pregunta_6 = forms.IntegerField(
        min_value=0, max_value=10, label="6. ¿Qué tan dispuesto estarías a ofrecer ayuda a una persona con discapacidad en un lugar público?"
    )

    pregunta_7 = forms.IntegerField(
        min_value=0, max_value=10, label="7. ¿Sientes incomodidad al interactuar con personas con discapacidad?"
    )

    pregunta_8 = forms.IntegerField(
        min_value=0, max_value=10, label="8. ¿Qué tan importante consideras que es incluir a las personas con discapacidad en la vida laboral?"
    )

    pregunta_9 = forms.ChoiceField(
        choices=[
            ('a', 'Infraestructura y accesibilidad'),
            ('b', 'Prejuicios y estigmas'),
            ('c', 'Falta de educación inclusiva'),
            ('d', 'Falta de políticas públicas adecuadas'),
        ],
        widget=forms.RadioSelect,
        label="9. ¿Cuál crees que es la principal barrera para la inclusión de personas con discapacidad en México?"
    )

    pregunta_10 = forms.ChoiceField(
        choices=[
            ('a', 'Sí, en mi familia'),
            ('b', 'Sí, en mi círculo de amigos o trabajo'),
            ('c', 'Sí, en mi comunidad o entorno'),
            ('d', 'No, no conozco a nadie personalmente'),
        ],
        widget=forms.RadioSelect,
        label="10. ¿Conoces a alguna persona con discapacidad en tu vida cotidiana?"
    )

    # Tercer grupo de preguntas
    pregunta_11 = forms.IntegerField(
        min_value=0, max_value=10, label="11. ¿Consideras que los espacios públicos en México son accesibles para personas con discapacidad?"
    )

    pregunta_12 = forms.IntegerField(
        min_value=0, max_value=10, label="12. ¿Qué tanto crees que el sistema educativo en México está adaptado para personas con discapacidad?"
    )

    pregunta_13 = forms.IntegerField(
        min_value=0, max_value=10, label="13. ¿Qué tan importante crees que es enseñar empatía y respeto hacia personas con discapacidad en las escuelas?"
    )

    pregunta_14 = forms.ChoiceField(
        choices=[
            ('a', 'Sí, conozco varias'),
            ('b', 'Sí, conozco una'),
            ('c', 'No, no conozco ninguna'),
        ],
        widget=forms.RadioSelect,
        label="14. ¿Conoces alguna organización en México que apoye a personas con discapacidad?"
    )

    pregunta_15 = forms.IntegerField(
        min_value=0, max_value=10, label="15. ¿Consideras que las políticas de salud en México brindan una atención adecuada a personas con discapacidad?"
    )

    pregunta_16 = forms.IntegerField(
        min_value=0, max_value=10, label="16. ¿Qué tan importante crees que es implementar tecnologías de apoyo para personas con discapacidad en el trabajo?"
    )

    pregunta_17 = forms.ChoiceField(
        choices=[
            ('a', 'Sí, ha mejorado mucho'),
            ('b', 'Sí, ha mejorado un poco'),
            ('c', 'No ha habido cambio'),
            ('d', 'Ha empeorado'),
        ],
        widget=forms.RadioSelect,
        label="17. ¿Crees que la inclusión de personas con discapacidad en medios de comunicación (TV, películas) ha mejorado en México en los últimos años?"
    )

    pregunta_18 = forms.IntegerField(
        min_value=0, max_value=10, label="18. ¿Qué tan común crees que es la discriminación hacia personas con discapacidad en México?"
    )

    pregunta_19 = forms.IntegerField(
        min_value=0, max_value=10, label="19. ¿Consideras que el entorno social en México es consciente y empático hacia las personas con discapacidad?"
    )

    pregunta_20 = forms.ChoiceField(
        choices=[
            ('a', 'Sí, sería muy beneficioso'),
            ('b', 'Sí, sería beneficioso, pero no prioritario'),
            ('c', 'No, no es necesario'),
            ('d', 'Otro (especifica): ________'),
        ],
        widget=forms.RadioSelect,
        label="20. ¿Crees que sería beneficioso implementar más campañas de concientización sobre discapacidades en México?"
    )
