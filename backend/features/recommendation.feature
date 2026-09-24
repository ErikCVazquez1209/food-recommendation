# language: es

Característica: Recomendación de recetas
  Como usuario del sistema de recomendación
  Quiero indicar mis preferencias y límites
  Para recibir una receta que cumpla mis necesidades

  Escenario: Recomendar una receta dentro de los límites
    Dado que el usuario selecciona la categoría "Veg"
    Y establece un máximo de 30 minutos
    Y establece un máximo de 10 pasos
    Y establece un máximo de 8 ingredientes
    Cuando solicita una recomendación
    Entonces la receta debe pertenecer a la categoría "Veg"
    Y su duración debe ser menor o igual a 30 minutos
    Y no debe superar los límites indicados

  Escenario: Rechazar una solicitud incompleta
    Dado que una solicitud no contiene "step" ni "ingr"
    Cuando se envía la solicitud al endpoint de recomendación
    Entonces la API debe responder con el código 400
    Y debe indicar cuáles campos están ausentes

  Escenario: Rechazar una categoría inexistente
    Dado que el usuario proporciona la categoría "Unknown"
    Cuando solicita una recomendación
    Entonces la API debe responder con el código 400
    Y debe devolver el mensaje "Invalid food type"

  Escenario: Rechazar un límite no numérico
    Dado que el usuario proporciona "fast" como límite de minutos
    Cuando solicita una recomendación
    Entonces la API debe responder con el código 400
    Y debe indicar que los límites deben ser numéricos