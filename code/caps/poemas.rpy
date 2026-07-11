
#acá se mostaran los poemas de las dokis en dado caso se eliga no mostar el poema a Yuri
#dia 1 Natsuki

label mostrar_poema_natsukis:
    
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

#dia 2 Sayori
label mostrar_poema_Sayori:
    stop music fadeout 1.5
    play music audio.t5
    "Me acerque a Sayori, ayer me mencionó que haría \"el mejor poema del mundo\" seguramente lo hizo"
    show sayori turned lup rup happ om oe zorder 2 at f11
    s "¡hola [player]!"
    show sayori turned lup rup happ cm oe zorder 2 at t11
    mc "hola Sayori ¿lograste hacer el mejor poema del mundo?"
    show sayori tap nerv om oe zorder 2 at f11
    s "ya lo verás~"
    show sayori tap nerv cm oe zorder 2 at t11
    "le entregué mi poema a Sayori"
    show sayori turned rup happ om oe zorder 2 at f11
    s "este poema, es muy bueno"
    s "me encanta [player]"
    s "me sorprendió relamente parece como un poema que haría Yuri jeje..."
    show sayori turned rup happ om oe zorder 2 at t11
    mc "espera Sayori creo que te estas confundiendo-"
    show sayori turned rup happ om ce zorder 2 at f11
    s "jeje, te conozco desde que somos niños es imposible no notar cosas obvias"
    show sayori turned lsur om ce zorder 2 at t11
    mc "lo que digas..."
    "Sayori me ofreció su poema"
    $ poem_db.show_poem("Sayori_poem1")
    show sayori turned happ cm oe zorder 2 at t11
    mc "¿Sayori tu escribiste esto?"
    show sayori tap nerv om oe zorder 2 at f11
    s "si, quería probar un estilo mas diferente al de ayer"
    s "te dije que haria el mejor poema del mundo"
    show sayori tap nerv om ce zorder 2 at f11
    s "y seguramente lo es, tu cara me lo dice"
    show sayori tap neut cm oe zorder 2 at t11
    mc "¿si?"
    show sayori tap neut om oe zorder 2 at f11
    s "sip"
    show sayori tap neut cm oe zorder 2 at t11
    mc "diría que es mas por sorpresa, no pensaba en que podrías expreasrte asi"
    show sayori tap nerv om ce zorder 2 at f11
    s "hay muchas cosas que no sabes de mi [player]"
    show sayori tap pout om oe zorder 2 at t11
    mc "¿de qué hablas? nos conocemos desde la infancia sé todo de ti"
    show sayori turned lup rup laug om oe zorder 2 at f11
    s "¿cuándo es mi cumpleaños?"
    show sayori turned lup rup laug cm oe zorder 2 at t11
    mc "eh... eh.. ¿25 de enero?"
    show sayori turned lup rup happ om ce zorder 2 at f11
    s "muuuy cerca, el 10 de mayo"
    show sayori turned lup rup happ om ce zorder 2 at thide
    hide sayori

    with wipeleft_scene 
    jump mostrar_poema_yuri2

    






label mostrar_poema_Yuri:
    
