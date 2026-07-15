

label mostrar_poema_nat:
    
    "Natsuki no esta compartiendo poema con nadie supongo que lo compartire con ella primero"
    show natsuki 1c zorder 2 at t11
    n "A ver qué traes ahí..."
    
    pause 1
    
    show natsuki 4m zorder 2 at t11
    n "Ugh... ¿en serio escribiste esto?"
    mc "¿Tan malo es?"
    
    show natsuki 4w zorder 2 at t11
    n "¡No es malo estructuralmente! Es que... ¡es tan aburrido!"
    n "Estás intentando usar palabras súper largas y metáforas raras solo para sonar inteligente. Pareces una copia barata de Yuri."
    show natsuki 2e zorder 2 at t11
    n "La escritura debería ser honesta, no un truco para impresionar a la gente con un diccionario."
    mc "Bueno, cada quien tiene su propio estilo..."
    
    show natsuki 2h zorder 2 at t11
    n "Supongo... Toma tu poema de vuelta."
    
    n 2c "A ver si aprendes algo leyendo el mío. Te servirá para ver a qué me refiero con ir directo al grano."
    n "Toma, léelo. Y más te vale no reírte."
    
    
    $ poem_db.show_poem("natsuki_poem1")
    
    show natsuki 1p zorder 2 at t11
    n "...Y bien? ¿Qué cara es esa? ¿Vas a decir algo?"
    mc "Es... bastante diferente a lo que suelo leer. Es muy directo, casi parece una rima infantil al principio."
    
    show natsuki 1r zorder 2 at t11
    n "¡Ugh! ¡Sabía que dirías algo así! ¡Completamente perdiste el punto!"
    n 4w "No es una 'rima infantil'. ¡Es sobre el sentimiento de rendirse y la frustración con la gente!"
    mc "Lo sé, lo sé... la última estrofa lo deja claro. Solo digo que la estructura es simple."
    
    show natsuki 1g zorder 2 at t11
    n "Simple no significa fácil o tonto. Significa que no necesito esconderme detrás de palabras pretenciosas."
    n 1h "Mañana espero ver algo con más honestidad de tu parte, [player]."
    mc "vale vale"
    show natsuki 1g zorder 2 at thide
    hide natsuki
    "Yuri deberia estar libre, iré a mostrale mi poema"

    jump mostrar_poema_yuri




    
