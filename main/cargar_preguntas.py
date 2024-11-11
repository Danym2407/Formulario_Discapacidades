# cargar_preguntas.py

from .models import Usuario, Pregunta, Respuesta, OpcionPregunta
from django.db import IntegrityError

# Función para cargar las preguntas
def cargar_preguntas():
    # Lista de preguntas con sus opciones
    preguntas_data = [
        {
            "texto_pregunta": "1. ¿Cómo defines la discapacidad?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Una condición física o mental que afecta la vida diaria'),
                ('b', 'Una diferencia de habilidades'),
                ('c', 'Algo temporal que se puede superar'),
                ('d', 'Otro (especifica): ________')
            ]
        },
        {
            "texto_pregunta": "2. ¿Consideras que México cuenta con suficientes apoyos para personas con discapacidad?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Sí, completamente'),
                ('b', 'Sí, pero hay mucho por mejorar'),
                ('c', 'No, los apoyos son insuficientes'),
                ('d', 'No tengo información suficiente')
            ]
        },
        {
            "texto_pregunta": "3. ¿Qué tanto conoces las leyes en México que protegen los derechos de las personas con discapacidad?",
            "tipo_pregunta": "escala",
            "opciones": []  # No hay opciones ya que es una escala
        },
        {
            "texto_pregunta": "4. ¿Cuál crees que es la discapacidad más común en México?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Discapacidad visual'),
                ('b', 'Discapacidad auditiva'),
                ('c', 'Discapacidad motriz'),
                ('d', 'Discapacidad intelectual'),
                ('e', 'Discapacidad psicosocial')
            ]
        },
        {
            "texto_pregunta": "5. ¿Con cuál de las siguientes discapacidades sientes más empatía?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Visual'),
                ('b', 'Auditiva'),
                ('c', 'Motriz'),
                ('d', 'Intelectual'),
                ('e', 'Psicosocial'),
                ('f', 'No tengo preferencia')
            ]
        },
        {
            "texto_pregunta": "6. ¿Qué tan dispuesto estarías a ofrecer ayuda a una persona con discapacidad en un lugar público?",
            "tipo_pregunta": "escala",
            "opciones": []  # No hay opciones ya que es una escala
        },
        {
            "texto_pregunta": "7. ¿Sientes incomodidad al interactuar con personas con discapacidad?",
            "tipo_pregunta": "escala",
            "opciones": []  # No hay opciones ya que es una escala
        },
        {
            "texto_pregunta": "8. ¿Qué tan importante consideras que es incluir a las personas con discapacidad en la vida laboral?",
            "tipo_pregunta": "escala",
            "opciones": []  # No hay opciones ya que es una escala
        },
        {
            "texto_pregunta": "9. ¿Cuál crees que es la principal barrera para la inclusión de personas con discapacidad en México?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Infraestructura y accesibilidad'),
                ('b', 'Prejuicios y estigmas'),
                ('c', 'Falta de educación inclusiva'),
                ('d', 'Falta de políticas públicas adecuadas')
            ]
        },
        {
            "texto_pregunta": "10. ¿Conoces a alguna persona con discapacidad en tu vida cotidiana?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Sí, en mi familia'),
                ('b', 'Sí, en mi círculo de amigos o trabajo'),
                ('c', 'Sí, en mi comunidad o entorno'),
                ('d', 'No, no conozco a nadie personalmente')
            ]
        },
        {
            "texto_pregunta": "11. ¿Crees que las personas con discapacidad deberían tener las mismas oportunidades que las personas sin discapacidad?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Sí, sin lugar a dudas'),
                ('b', 'Sí, pero con algunas adaptaciones'),
                ('c', 'No, porque las capacidades son diferentes'),
                ('d', 'No tengo una opinión clara sobre esto')
            ]
        },
        {
            "texto_pregunta": "12. ¿Qué tan informado(a) te sientes sobre la accesibilidad en tu comunidad para personas con discapacidad?",
            "tipo_pregunta": "escala",
            "opciones": []  # No hay opciones ya que es una escala
        },
        {
            "texto_pregunta": "13. ¿Consideras que la tecnología ha mejorado la calidad de vida de las personas con discapacidad?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Sí, de manera significativa'),
                ('b', 'Sí, pero hay mucho por mejorar'),
                ('c', 'No, las barreras tecnológicas siguen siendo grandes'),
                ('d', 'No tengo información suficiente')
            ]
        },
        {
            "texto_pregunta": "14. ¿En tu opinión, qué aspectos de la vida diaria de una persona con discapacidad deberían recibir más atención?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Accesibilidad en el transporte público'),
                ('b', 'Acceso a la educación inclusiva'),
                ('c', 'Adaptación de espacios públicos'),
                ('d', 'Políticas laborales inclusivas')
            ]
        },
        {
            "texto_pregunta": "15. ¿Cómo definirías la inclusión social de las personas con discapacidad en la actualidad?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Es una prioridad en la sociedad'),
                ('b', 'Está mejorando pero aún falta mucho'),
                ('c', 'Es mínima y no se valora lo suficiente'),
                ('d', 'No tengo una opinión sobre esto')
            ]
        },
        {
            "texto_pregunta": "16. ¿Qué opinas sobre la representación de personas con discapacidad en los medios de comunicación?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Es adecuada y diversa'),
                ('b', 'Está mejorando, pero sigue siendo insuficiente'),
                ('c', 'Es estigmatizada y poco realista'),
                ('d', 'No tengo una opinión sobre esto')
            ]
        },
        {
            "texto_pregunta": "17. ¿Qué tan accesible consideras el transporte público para personas con discapacidad?",
            "tipo_pregunta": "escala",
            "opciones": []  # No hay opciones ya que es una escala
        },
        {
            "texto_pregunta": "18. ¿Qué piensas sobre la actitud de las personas hacia las personas con discapacidad en tu entorno?",
            "tipo_pregunta": "escala",
            "opciones": []  # No hay opciones ya que es una escala
        },
        {
            "texto_pregunta": "19. ¿Cómo consideras que debería mejorar la educación para personas con discapacidad?",
            "tipo_pregunta": "opcion_multiple",
            "opciones": [
                ('a', 'Implementar más programas educativos inclusivos'),
                ('b', 'Mejorar la formación de los docentes en temas de discapacidad'),
                ('c', 'Crear más recursos adaptados para estudiantes con discapacidad'),
                ('d', 'Aumentar la sensibilización en la comunidad escolar')
            ]
        },
        {
            "texto_pregunta": "20. ¿Qué tanto te comprometes a apoyar a personas con discapacidad en tu entorno?",
            "tipo_pregunta": "escala",
            "opciones": []  # No hay opciones ya que es una escala
        }
    ]

    # Verificar si ya se cargaron las preguntas
    if Pregunta.objects.count() == 0:
        # Iterar sobre las preguntas y agregar las opciones
        for pregunta_data in preguntas_data:
            try:
                # Crear la pregunta
                pregunta = Pregunta.objects.create(
                    texto_pregunta=pregunta_data["texto_pregunta"],
                    tipo_pregunta=pregunta_data["tipo_pregunta"]
                )

                # Si la pregunta tiene opciones, agregarlas
                for opcion in pregunta_data["opciones"]:
                    OpcionPregunta.objects.create(
                        pregunta=pregunta,
                        texto_opcion=opcion[1]
                    )

                print(f"Pregunta '{pregunta.texto_pregunta}' cargada exitosamente.")

            except IntegrityError as e:
                print(f"Error al cargar la pregunta '{pregunta_data['texto_pregunta']}': {e}")
    else:
        print("Las preguntas ya han sido cargadas anteriormente.")

# Ejecutar la función para cargar las preguntas solo si no existen
if __name__ == '__main__':
    cargar_preguntas()
