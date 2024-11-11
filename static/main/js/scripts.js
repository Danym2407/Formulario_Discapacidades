function cambiarDescripcion(tipo, element) {
    let descripcionTexto = "";
    let imagenUrl = "";
    let titulo = "";
    
    // Información sobre cada discapacidad
    switch (tipo) {
      case 'motriz':
        descripcionTexto = "Las discapacidades motrices afectan la capacidad de moverse o controlar el cuerpo. Esto puede incluir parálisis, amputaciones o condiciones que limitan el movimiento.";
        imagenUrl = "https://via.placeholder.com/500x300?text=Discapacidad+Motriz";
        titulo = "Discapacidad Motriz";
        break;
      case 'auditiva':
        descripcionTexto = "Las discapacidades auditivas afectan la capacidad de oír, lo que puede implicar desde pérdida parcial hasta completa de la audición.";
        imagenUrl = "https://via.placeholder.com/500x300?text=Discapacidad+Auditiva";
        titulo = "Discapacidad Auditiva";
        break;
      case 'visual':
        descripcionTexto = "Las discapacidades visuales afectan la capacidad de ver, lo que puede incluir ceguera o visión parcial.";
        imagenUrl = "https://via.placeholder.com/500x300?text=Discapacidad+Visual";
        titulo = "Discapacidad Visual";
        break;
      case 'cognitiva':
        descripcionTexto = "Las discapacidades cognitivas afectan las funciones mentales como el razonamiento, el aprendizaje y la memoria, y pueden incluir condiciones como el autismo o la demencia.";
        imagenUrl = "https://via.placeholder.com/500x300?text=Discapacidad+Cognitiva";
        titulo = "Discapacidad Cognitiva";
        break;
      default:
        descripcionTexto = "Las discapacidades son condiciones que afectan las capacidades físicas, mentales o sensoriales de las personas.";
        imagenUrl = "https://via.placeholder.com/500x300";
        titulo = "Tipos de discapacidades";
        break;
    }
  
    // Actualizar la sección de descripción
    document.getElementById('descripcion-texto').textContent = descripcionTexto;
    document.getElementById('descripcion-imagen').src = imagenUrl;
    document.getElementById('descripcion-titulo').textContent = titulo;
  
    // Cambiar el color de la tarjeta seleccionada
    let tarjetas = document.querySelectorAll('.tipo-discapacidad');
    tarjetas.forEach(function(card) {
      card.classList.remove('bg-dark', 'text-white'); // Eliminar las clases de hover
    });
    element.classList.add('bg-dark', 'text-white'); // Aplicar las clases al elemento seleccionado
  }
  