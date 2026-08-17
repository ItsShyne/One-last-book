label test_yuri_afm:

    scene bg club_day
    with dissolve

    # Mostramos a Yuri inicialmente con boca cerrada (cm)
    show yuri turned cm neut uniform at t11

    mc "Hola Yuri, ¿qué tal tu día?"

    # Usamos 'ya' para que abra la boca mientras escribe la frase 
    # y la cierre en cuanto el jugador pueda hacer clic:
    ya "A-Ah... Hola. Ha sido un día bastante tranquilo, la verdad."

    mc "¿Estabas leyendo?"

    # Cambias la postura/expresión normalmente en el show...
    show yuri turned flus blus

    # ...y al usar 'ya', la boca vuelve a abrirse y cerrarse sola:
    ya "Sí... Un libro de misterio. Es sumamente fascinante."

    ya "Si te interesa, puedo contarte un poco de la trama."

    # Cambio a pose 'shy'
    show yuri shy neut uniform at t11

    ya "A no ser que prefieras empezar tu propia lectura en silencio, claro..."

    return