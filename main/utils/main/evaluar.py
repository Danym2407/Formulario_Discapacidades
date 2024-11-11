def evaluar_respuestas(respuestas):
    """
    Evaluar las respuestas de un usuario para calcular el puntaje en diferentes dimensiones
    relacionadas con la inclusión y discapacidad.

    Args:
    respuestas (dict): Diccionario con las respuestas del usuario. Ejemplo:
                        {
                            'pregunta_1': 'b',
                            'pregunta_2': 'a',
                            'pregunta_3': 4,  # en caso de ser una escala
                            ...
                        }

    Returns:
    dict: Puntajes por dimensión. Ejemplo:
          {
              'empatía': 80,
              'respeto': 60,
              'conciencia_social': 70,
              'disposicion_accion': 85,
              'inclusion_social': 90,
              'prejuicios': 40,
              'realidad': 65,
              'sensibilidad_derechos': 75
          }
    """
    # Definir el puntaje de cada opción
    puntajes = {
        'pregunta_1': {
            'a': 20,  # Empatía: "Una condición física o mental que afecta la vida diaria"
            'b': 40,  # Conciencia social: "Una diferencia de habilidades"
            'c': 10,  # Prejuicios: "Algo temporal que se puede superar"
            'd': 30   # Sensibilidad: "Otro"
        },
        'pregunta_2': {
            'a': 30,  # Inclusión social: "Sí, completamente"
            'b': 50,  # Inclusión social: "Sí, pero hay mucho por mejorar"
            'c': 10,  # Prejuicios: "No, los apoyos son insuficientes"
            'd': 0    # Conciencia social: "No tengo información suficiente"
        },
        'pregunta_3': {
            1: 10,  # Prejuicios: "Muy poco"
            2: 20,  # Prejuicios: "Poco"
            3: 50,  # Conciencia social: "Bastante"
            4: 80   # Conciencia social: "Mucho"
        },
        'pregunta_4': {
            'a': 10,  # Inclusión social: "Discapacidad visual"
            'b': 20,  # Inclusión social: "Discapacidad auditiva"
            'c': 30,  # Inclusión social: "Discapacidad motriz"
            'd': 40,  # Inclusión social: "Discapacidad intelectual"
            'e': 50   # Inclusión social: "Discapacidad psicosocial"
        },
        'pregunta_5': {
            'a': 40,  # Empatía: "Visual"
            'b': 30,  # Empatía: "Auditiva"
            'c': 20,  # Empatía: "Motriz"
            'd': 10,  # Empatía: "Intelectual"
            'e': 50   # Empatía: "Psicosocial"
        },
        # Otras preguntas se pueden agregar con un esquema similar...
    }

    # Inicializar el puntaje por dimensión
    puntuaciones_dimensiones = {
        'empatía': 0,
        'respeto': 0,
        'conciencia_social': 0,
        'disposicion_accion': 0,
        'inclusion_social': 0,
        'prejuicios': 0,
        'realidad': 0,
        'sensibilidad_derechos': 0
    }

    # Evaluar las respuestas y asignar puntajes a las dimensiones
    for pregunta, respuesta in respuestas.items():
        if pregunta in puntajes:
            if isinstance(respuesta, str):
                # Si la respuesta es una opción de texto
                for dimension, opciones in puntajes[pregunta].items():
                    if respuesta in opciones:
                        puntuaciones_dimensiones[dimension] += opciones[respuesta]
            elif isinstance(respuesta, int):
                # Si la respuesta es una escala numérica
                puntuaciones_dimensiones['conciencia_social'] += puntajes[pregunta][respuesta]

    # Calcular los puntajes finales, por ejemplo, normalizados entre 0 y 100
    for dimension, puntuacion in puntuaciones_dimensiones.items():
        puntuaciones_dimensiones[dimension] = round((puntuacion / max(puntajes[dimension])) * 100, 2)

    return puntuaciones_dimensiones

# Ejemplo de uso de la función
respuestas = {
    'pregunta_1': 'b',
    'pregunta_2': 'a',
    'pregunta_3': 3,
    'pregunta_4': 'c',
    'pregunta_5': 'd',
}

# Evaluar las respuestas
puntajes = evaluar_respuestas(respuestas)
print(puntajes)
