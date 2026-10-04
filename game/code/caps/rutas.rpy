#aqui iran todas las elecciones de todas las rutas
#buena, neutra, mala y en el futuro secreta 
#se guiara por dias
########## DIA 1 ##########
#esto involucra el cap1 y el inicio del cap2
#Elecciones de la ruta
label rutas:
#Decision ir con Sayori
    label ir_sayori:
        show sayori turned happ cm oe zorder 2 at t11
        mc "Por supuesto, Sayori."
        show sayori turned lup rup happ om ce zorder 2 at h11
        s "¡Yaaay~!"
        mc "Dame un momento y tomo mis cosas."
        show sayori turned lup rup happ om ce zorder 2 at thide
        hide sayori
        "Rápidamente guardo mis cosas y alcanzo a Sayori en la puerta del aula. Me espera con una sonrisa enorme, balanceándose sobre los talones."
        mc "Listo, Sayori. Podemos irnos."
        s "¡¡¡Nos vemos mañana, chicas!!!"
        show bg residential_aft
        with wipeleft_scene
        "Durante todo el camino a casa no dejo de pensar en qué voy a escribir."
        "Con la cabeza fría, no sé por qué acepté tan rápido. Natsuki tenía razón."
        "Lastimosamente ya no puedo echarme atrás. Tendré que idear un plan."
        show sayori turned happ cm ce zorder 2 at t11
        mc "Oye, Sayori... ¿de qué escribirás tu poema?"
        show sayori turned lsur om oe zorder 2 at f11
        s "Hmmm..."
        "Se lleva un dedo al mentón y mira al cielo."
        show sayori turned happ om oe zorder 2 at f11
        s "Quizás sea acerca del sol. Es muy lindo, sobre todo cuando voy a la escuela."
        show sayori turned happ cm oe zorder 2 at t11
        mc "Nunca he escrito un poema. Honestamente, no tengo idea de qué podría escribir."
        mc "Aunque me sorprende que tú escribas poemas. Nunca me imaginé que podrías hacerlo."
        show sayori tap nerv om oe zorder 2 at f11
        s "S-sí... ehehe..."
        "Desvía la mirada y se rasca la mejilla, como si no supiera qué responder."
        show sayori tap pout cm oe zorder 2 at t11
        mc "Adivinaré... estamos en las mismas, ¿cierto?"
        show sayori turned lup rup pani om oe zorder 2 at f11
        s "¡¡¡Oye!!!"
        "Infla las mejillas y me da la espalda a medias, fingiendo ofensa."
        show sayori tap pout zorder 2 at t11
        s "Claro que sé lo que voy a escribir."
        s "¡¡Voy a escribir el mejor poema del mundo!! Ya verás."
        "Ver los aires de grandeza de Sayori no puedo evitar reírme."
        show sayori turned mu e1a b1d zorder 2 at t11
        s "Hmmpf... ¿Por qué te ríes tan fuerte?"
        mc "Jajaja, nada, nada."
        show sayori turned me e2g b2a zorder 2 at t11
        mc "Es que extrañaba esto: salir de la escuela, hablar y bromear con mi mejor amiga de la infancia."
        show sayori zorder 2 at thide
        hide sayori
        "Al oír mis palabras, Sayori se adelanta unos pasos."
        mc "Sayori, espérame."
        "Acelero el paso hasta quedar a su lado."
        show sayori turned mg e2i b1c zorder 2 at t11
        mc "Oye, ¿por qué me dejas atrás?"
        show sayori turned me e1a b1d zorder 2 at t11
        s "Qué tonto eres, [player]..."
        "Un golpecito suave llega a mi hombro."
        mc "Sayori..."
        show sayori ma e1a b1a zorder 2 at t11
        s "Si tienes problemas para escribir un poema, puedes buscar ideas en todo lo que te rodea: tus amigos, los colores, el sonido que no te deja dormir, hasta tu propio reflejo."
        s "Leer libros siempre me ayuda a recuperar la inspiración. Intenta leer algo que te guste."
        mc "Oh... no se me habría ocurrido. Muchas gracias, Sayori."
        "No entiendo por qué reaccionó así, y tampoco parece querer hablar de ello."
        show sayori mb e4b b3c zorder 2 at t11
        "Seguimos charlando el resto del camino, hasta separarnos rumbo a nuestras casas."
        show sayori turned lup rup pani om ce zorder 2 at thide
        hide sayori
        stop music fadeout 2.0
        jump biblioteca
    #RUTA NEUTRA ELECCIÓN 1
    label sayori_insiste:
        show sayori 2m zorder 2 at f11
        s "¿¡Qué!? ¿En serio?"
        show sayori tap zorder 2 at f11
        s "Vamos, [player], hace tiempo que no salimos juntos."
        show sayori tap zorder 2 at t11
        window show
        menu:
            #CONTINUACIÓN DE LA RUTA NEUTRA
            "Irse con sayori":
                $ puntos_ruta += 1
                $ decision_sayori = "insistir"
                mc "Está bien, está bien..."
                show sayori turned lup rup happ om ce zorder 2 at h11
                s "¡Yaaay~!"
                show sayori turned happ om oe zorder 2 at t11
                mc "Dame un momento y tomo mis cosas."
                show sayori turned lup rup happ om ce zorder 2 at thide
                hide sayori
                "Rápidamente guardo mis cosas y alcanzo a Sayori en la puerta del aula. Me espera con una sonrisa enorme, balanceándose sobre los talones."
                mc "Listo, Sayori. Podemos irnos."
                s "¡¡¡Nos vemos mañana, chicas!!!"
                show bg residential_aft
                with wipeleft_scene
                "Durante todo el camino a casa no dejo de pensar en qué voy a escribir."
                "Con la cabeza fría, no sé por qué acepté. Natsuki tenía razón."
                "Lastimosamente ya no puedo echarme atrás. Tendré que idear un plan."
                show sayori turned happ cm ce zorder 2 at t11
                mc "Oye, Sayori... ¿de qué escribirás tu poema?"
                show sayori turned lsur om oe zorder 2 at f11
                s "Hmmm..."
                "Se lleva un dedo al mentón y mira al cielo, pensativa."
                show sayori turned happ om oe zorder 2 at f11
                s "Quizás sea acerca del sol. Es muy lindo, sobre todo cuando voy a la escuela."
                show sayori turned happ cm oe zorder 2 at t11
                mc "Nunca he escrito un poema. Honestamente, no tengo idea de qué podría escribir."
                mc "Aunque me sorprende que tú escribas poemas. Nunca me imaginé que podrías hacerlo."
                show sayori tap nerv om oe zorder 2 at f11
                s "S-sí... ehehe..."
                "Desvía la mirada y se rasca la mejilla, como si no supiera qué responder."
                show sayori tap pout cm oe zorder 2 at t11
                mc "Adivinaré... estamos en las mismas, ¿cierto?"
                show sayori turned lup rup pani om oe zorder 2 at f11
                s "¡¡¡Oye!!!"
                "Infla las mejillas y me da la espalda a medias, fingiendo ofensa."
                show sayori tap pout zorder 2 at t11
                s "Claro que sé lo que voy a escribir."
                s "¡¡Voy a escribir el mejor poema del mundo!! Ya verás."
                "Ver los aires de grandeza de Sayori no puedo evitar reírme."
                show sayori turned mu e1a b1d zorder 2 at t11
                s "Hmmpf... ¿Por qué te ríes tan fuerte?"
                mc "Jajaja, nada, nada."
                show sayori turned me e2g b2a zorder 2 at t11
                mc "Es que extrañaba esto: salir de la escuela, hablar y bromear con mi mejor amiga de la infancia."
                show sayori zorder 2 at thide
                hide sayori
                "Al oír mis palabras, Sayori se adelanta unos pasos. Por un instante, su sonrisa parece vacilar."
                mc "Sayori, espérame."
                "Acelero el paso hasta quedar a su lado."
                show sayori turned mg e2i b1c zorder 2 at t11
                mc "Oye, ¿por qué me dejas atrás?"
                show sayori turned me e1a b1d zorder 2 at t11
                s "Qué tonto eres, [player]..."
                "Un golpecito suave llega a mi hombro."
                mc "Sayori..."
                show sayori ma e1a b1a zorder 2 at t11
                s "Si tienes problemas para escribir un poema, puedes buscar ideas en todo lo que te rodea: tus amigos, los colores, el sonido que no te deja dormir, hasta tu propio reflejo."
                s "Leer libros siempre me ayuda a recuperar la inspiración. Intenta leer algo que te guste."
                mc "Oh... no se me habría ocurrido. Muchas gracias, Sayori."
                "No entiendo por qué reaccionó así, y tampoco parece querer hablar de ello."
                show sayori mb e4b b3c zorder 2 at t11
                "Seguimos charlando el resto del camino, hasta separarnos rumbo a nuestras casas."
                show sayori turned lup rup pani om ce zorder 2 at thide
                hide sayori
                jump biblioteca
            #RUTA MALA    
            "Prefiero irme solo":
                $ decision_sayori = "no ir"
                $ puntos_ruta -= 1
                mc "Lo siento, Sayori, pero prefiero irme solo."
                show sayori turned curi cm oe zorder 2 at t11
                s "..."
                "Me retiré del salón."
                show sayori turned curi cm oe zorder 2 at thide
                hide sayori
                jump biblioteca 
# Decision biblioteca
    label hablar_yuri_biblioteca:
        play music t6 fadein 1.0
        "Sin pensarlo dos veces, camino hacia Yuri."
        "Espero no interrumpir nada importante."
        show yuri turned lup dist om oe zorder 2 at t11
        "Parece leer un libro de terror."
        "La portada es un tanto espeluznante."
        show yuri turned shoc om oe zorder 2 at h11
        mc "Hola, Yuri. Qué oportuno verte también por aquí."
        pause 0.5
        show yuri turned flus cm ce zorder 2 at s11
        pause 0.9
        show yuri turned n2 flus om oe zorder 2 at f11
        y "O-Oh, hola, [player]."
        y "No esperaba verte por aquí."
        "Yuri esconde el rostro tras el libro, sus ojos son apenas visibles."
        y "{size=-6}{alpha=*0.8}{i}¿S-Sueles venir a buscar libros a la biblioteca?{/i}{/alpha}{/size}"
        "Apenas logro escucharla detrás del libro."
        show yuri turned n2 sedu om oe zorder 2 at t11
        mc "No exactamente. Como acabo de ingresar al club, quería sumergirme al menos un poco en esto de la literatura."
        mc "Para no sentirme fuera de lugar y poder discutir con ustedes sobre el tema."
        mc "Ah, y Sayori me aconsejó leer libros para encontrar ideas para el poema."
        "No es del todo mentira, pero sigue siendo una mentira."
        show yuri turned happ om oe zorder 2 at f11
        "Al oír la palabra «libros», Yuri baja el libro de golpe y su expresión se ilumina."
        y turned n1 mb estar1a b1a "Maravilloso."
        show yuri turned shoc om oe zorder 2 at h11
        "Parece darse cuenta de lo rápido que reaccionó y desvía la mirada un segundo."
        show yuri turned shoc cm ce zorder 2 at s11
        pause 0.9
        y turned n2 mg e1c b1b "A-Agradezco tu compromiso por ser parte del club de literatura."
        y turned rup happ cm ce "Si necesitas ayuda con alguna recomendación, n-no dudes en decírmelo."
        y "Tengo muchos libros que son una excelente introducción para lectores principiantes."
        show yuri turned happ om oe zorder 2 at t11
        mc "¿En serio? Me serviría de mucha ayuda."
        show yuri turned ldown rdown sedu om oe zorder 2 at t11
        "Yuri se percata de los libros que llevo en los brazos."
        show yuri turned ldown rdown sedu om oe zorder 2 at f11
        y "¿[player]... te gusta el terror?"
        show yuri turned ldown rdown sedu om oe zorder 2 at t11
        mc "¿Mmh? ¿Por qué lo dices?"
        "Rápidamente recuerdo por qué estoy aquí en la biblioteca."
        mc "Ah, sí. Me fascinan las historias que pueden hacerme temblar de miedo mientras las leo."
        show yuri turned n1 happ om ce zorder 2 at f11
        y turned happ om ce "¿En serio? El terror psicológico está siendo uno de mis géneros favoritos últimamente."
        y turned happ cm oe "Si es así, me gustaría darte unas cuantas recomendaciones sobre algunos libros que estoy segura de que te darán una grata sorpresa."
        show yuri turned happ cm oe zorder 2 at t11
        mc "Si no es mucha molestia, por favor."
        show yuri turned happ cm ce zorder 2 at t11
        "Yuri cierra su libro, se toma unos segundos y empieza a hablar"
        show yuri turned lup rup dist om ce zorder 2 at t11
        "Parece muy feliz de poder hablar con alguien sobre sus gustos."
        "Es lindo escucharla hablar sobre libros mientras sonríe."
        "Yuri describe múltiples obras que leyó recientemente."
        "Escuchar a alguien hablar con tanta pasión te transmite un entusiasmo difícil de ignorar."
        "Eso sí, cada título que menciona suena más perturbador y oscuro que el anterior."
        "Todo suena inofensivo cuando lo dice Yuri, pero en realidad describe tramas repletas de asesinatos, trastornos y torturas de lo más siniestras."
        show yuri turned lup rup dist om ce zorder 2 at f11
        y "Se titula «El susurro de la caja», es de un autor poco conocido, pero es una joya."
        y "La protagonista encuentra una pequeña caja de madera en su apartamento. Desde ese día, algo comienza a perseguirla."
        y "Susurros extraños y lamentos de una niña pequeña atormentan sus noches."
        y "Pero la maldición no busca matarla. Lo que quiere es despojarla, poco a poco, de aquello que le da sentido a su vida."
        y "Cada noche, antes de quitarle algo nuevo, la figura de la niña aparece en la oscuridad de su habitación y le susurra:"
        y "{size=-4}{i}¿Quién eres?{/i}{/size}"
        y "Primero fue su empleo, luego sus amigos, su familia y, al final... su propia identidad."
        y "Ella lucha desesperadamente por romper la maldición antes de perderse por completo en el olvido."
        y "Lo que más me estremece es ese pavor constante de no saber qué será lo próximo que perderá. La va carcomiendo, hasta hacerle perder la cordura."
        y "Y lo mejor es que el autor nunca explica de dónde sale la niña, aunque hay una pista que..."
        y "Sin olvidar que la niña no—{nw}"
        show yuri turned pani om oe zorder 2 at h11
        play sound alarm
        $ renpy.pause(2.0)
        stop sound fadeout 0.3
        "Una fuerte alarma interrumpe a Yuri y la devuelve bruscamente a la realidad."
        show yuri turned pani om oe zorder 2 at f11
        y "A-Ah..."
        y turned ldown rdown lsur om oe "L-Lamento haberte retenido aquí tanto tiempo escuchándome..."
        show yuri turned ldown rdown lsur om oe zorder 2 at t11
        mc "No, no te preocupes."
        mc "Te agradezco mucho las recomendaciones. Lograste capturar toda mi atención al contarme de qué trataban."
        show yuri turned happ cm oe zorder 2 at f11
        y turned happ cm oe "E-Está bien... Debo irme, se ha hecho un poco tarde."
        show yuri turned happ cm oe zorder 2 at t11
        mc "Sí, no sé en qué momento el tiempo pasó tan rápido."
        mc "De nuevo, muchas gracias por las recomendaciones. Te aseguro que intentaré leerlos todos."
        show yuri turned happ cm ce zorder 2 at f11
        y turned happ cm ce "Fue un placer. Nos vemos mañana, [player]."
        y "No olvides escribir tu poema."
        show yuri turned happ cm ce zorder 2 at t11
        mc "Tienes razón."
        mc "Adiós, Yuri."
        show yuri turned happ cm ce zorder 2 at thide 
        hide yuri
        "Yuri se levanta y se lleva consigo una pequeña pila de libros."
        "Despertando de aquel letargo, recuerdo que yo también debo llevarme algunos libros para escribir mi poema."
        "La biblioteca está a punto de cerrar."
        "Rápidamente me levanto de la mesa y tomo los libros que traía conmigo."
        jump noche_poem1
    label no_hablar_yuri_biblioteca:
        mc "¿Monika?"
        "Monika inmediatamente vuelve a la realidad."
        stop music fadeout 2.0
        show monika forward dist om oe zorder 2 at f11
        m "[player]... ¿hay algún problema si te hago una pregunta?"
        show monika forward dist cm oe zorder 2 at t11
        mc "No tendría problema, adelante."
        play music t10 fadein 1.0
        show monika forward dist om oe zorder 2 at f11
        m "¿Qué opinas de las chicas del club?"
        show monika forward dist cm oe zorder 2 at t11
        "¿Qué tipo de pregunta es esa?"
        "Por alguna razón, Monika me lo pregunta seriamente."
        mc "Bueno... eh, las chicas..."
        mc "Sayori... sí, Sayori y yo nos conocemos desde pequeños. Somos amigos de la infancia y se podría decir que es mi mejor amiga."
        mc "Tú, pues... me agradas. Ya te conocía desde hace un tiemp-{nw}"
        show monika forward pout om oe zorder 2 at f11
        m "¿Y Yuri?"
        show monika forward pout cm oe zorder 2 at t11
        mc "¿Yuri?"
        show monika forward nerv om oe zorder 2 at f11
        m "Bueno, noté que la mirabas mucho."
        show monika forward nerv cm oe zorder 2 at t11
        mc "No creo que haya pasado eso."
        show monika forward rhip pout om oe zorder 2 at f11
        m "Pero pasó..."
        m "Yuri es un poco tímida con los demás, sobre todo con las personas nuevas."
        show monika forward lpoint neut om oe zorder 2 at f11
        m "Y sería una pena si se fuera porque alguien la hace sentir incómoda en el club..."
        show monika forward lpoint neut cm oe zorder 2 at t11
        mc "Monika, entiendo eso, pero yo nunca incomodaría a alguien, y mucho menos a Yuri."
        m "..."
        show monika forward lpoint pout om oe zorder 2 at f11
        m "Está bien... pero mantente alejado de ella. Créeme, ella siempre está mejor sola."
        show monika forward pout cm oe zorder 2 at t11
        mc "..."
        "Realmente no sé qué decir, ¿cómo podría alejarme o evitar a Yuri?"
        "No puedo hacer eso."
        show monika forward neut om oe zorder 2 at f11
        m "Bueno, me tengo que retirar. Hasta mañana, [player], cuídate."
        show monika forward neut cm oe zorder 2 at t11
        mc "Hasta pronto, Monika."
        show monika forward neut om oe zorder 2 at thide 
        hide monika
        "Veo cómo Monika camina hacia la salida."
        "No logro ver a Yuri en el mismo lugar que la vi antes."
        "Supongo que Yuri se ha ido."
        "No creo que realmente esté incomodando a Yuri... o que podría hacerlo."
        "Quizás esté sobrepensando. Es la presidenta del club, obviamente querrá lo mejor para... para el club."
        "N-no debería darle tantas vueltas ahora."
        stop music fadeout 2.0
        "Reviso las estanterías y llevo conmigo unos cuantos libros para continuar con la tarea que me espera en casa."
        "El mismo silencio que me recibió antes me despide mientras salgo de la biblioteca rumbo a casa."
        jump noche_poem1
    # Decision discusion yuri natsuki
    label apoyar_yuripoem:
        "Me levanto de mi asiento con determinación."
        mc "N-Natsuki... Creo que Yuri tiene un punto en lo que dice..."
        "Intento modular mi voz para sonar lo más seguro posible."
        mc "Además..."
        show natsuki cross angr om ce zorder 2 at f22
        n "¡¿Ah, sí?! ¡¿Ahora vienes tú a defenderla?!"
        n "Claro, cómo no..."
        show natsuki cross angr om ce zorder 2 at t22
        show yuri shy happ cm oe zorder 2 at t21 
        y "..."
        "Yuri juega con su cabello tímidamente mientras me observa en silencio."
        mc "Natsuki, cálmate."
        mc "No hay necesi—{nw}"
        show natsuki turned vang cm ce zorder 2 at f22
        n "¡Solo pedía UN POCO de comprensión por parte de Yuri!"
        n "¡¿Cómo puede decir que mi poema es simplemente 'lindo'?! ¡¿Por qué todos tienen que encasillarme en eso?!"
        n turned angr om ce "¡¿Acaso no son capaces de ver que hay algo más en mí?!"
        n "¡Ush!"
        n turned pani cm oe "¡¡JÓDANSE TODOS!!"
        show natsuki turned cry cm oe zorder 2 at correr_izquierda
        pause 0.8
        hide natsuki
        play audio closet_close
        "Con pisotones violentos que retumban en el aula, Natsuki sale corriendo del salón del club, dejándonos a Yuri y a mí en un silencio sepulcral."
        show yuri shy neut om oe zorder 2 at f11
        y "Y-Yo..."
        "Yuri desvía la mirada por completo, rehuyendo de mí como si le lastimara verme."
        show yuri shy neut om oe zorder 2 at t11
        mc "Yuri... Tranquila..."
        "Doy un paso cauteloso hacia ella."
        show yuri shy angr cm ce zorder 2 at f11
        "Yuri se aleja bruscamente, apretando los puños con tanta fuerza que sus nudillos se tornan blancos."
        "Me quedo inmóvil, contemplando su silenciosa agitación."
        y "P-Por favor... D-Déjame sola un momento..."
        show yuri shy angr cm ce zorder 2 at thide
        hide yuri
        play audio closet_close
        "Yuri huye de mi presencia y se encierra de un portazo en el armario."
        mc "..."
        "Me quedo clavado en el sitio, completamente mudo ante la hostilidad del ambiente."
        "La atmósfera en el aula se siente extrañamente pesada, como si el aire se hubiera vuelto denso y frío."
        "Será mejor que les dé su espacio a ambas."
        with dissolve_scene_full
        jump final_discusion
    label ruta_bad_1:
        "Me levanté de mi asiento con un poco de miedo."
        mc "¿Chicas por qué tanto alboro-{nw=1}"
        show natsuki cross n1 angr om ce zorder 2 at f22
        n cross n1 angr om ce "Si vas a hacerte el tonto, cállate y siéntate."
        show natsuki cross n1 angr om ce zorder 2 at t22
        "Me senté rápidamente en mi asiento."
        show yuri turned n1 angr om oe zorder 2 at f21
        y turned n1 angr om oe "Natsuki, no deberías hablarle así a [player]. Es una total falta de respeto."
        show natsuki turned angr om oe zorder 2 at f22
        show yuri turned angr om oe zorder 2 at t21
        n "¿Falta de respeto? Mira quién habla."
        n "Llevas toda la reunión mirándome como si lo que escribo no valiera nada."
        show yuri turned doub om oe zorder 2 at f21
        y "Yo no dije eso en ningún momento."
        show natsuki turned angr cm oe zorder 2 at t22
        n "No hace falta que lo digas, Yuri. Se te nota en la cara."
        stop music fadeout 2.0
        n "¿Sabes qué? Te voy a decir lo que realmente pienso de ti."
        n turned angr om ce "Al principio pensaba que iba a ser increíble tener una amiga con mis mismos gustos..."
        "Natsuki se detuvo unos segundos."
        "Está a punto de estallar la bomba."
        n turned vang om oe "¡Pero ahora pienso que eres una perra engreída que se cree superior a todos!"
        show natsuki turned vang om oe zorder 2 at h22
        with vpunch
        n "No me sorprende que no tengas amigos, con esa actitud de que todo lo que a los demás nos gusta es 'poco profundo'."
        show yuri turned me e1g b1b zorder 2 at s21
        y "..."
        show natsuki sad om oe zorder 2 at s22
        pause 2
        show yuri turned cry cm ce zorder 2 at s21
        "El silencio que sigue es peor que cualquier grito."
        n "..."
        window hide
        show yuri shy sad om oe zorder 2 at t21
        pause 2
        show yuri shy sad om oe zorder 2 at correr_izquierda
        pause 0.4
        hide yuri
        play audio closet_open
        window show
        "Yuri salió del club cubriendo sus ojos con una de sus mangas."
        "El club se queda en silencio por un par de segundos."
        show natsuki turned fs cry om oe zorder 2 at t11
        "Miro a Natsuki; parece arrepentida."
        n "Yo... no quería decir eso..."
        n "Ya regreso..."
        show natsuki turned fs cry cm ce zorder 2 at correr_izquierda
        pause 0.8
        hide natsuki 
        play audio closet_close
        "Natsuki caminó hacia la puerta del salón y la cerró de un portazo." 
        "Miré a Sayori. Parecía igual de impactada que yo"
        show sayori turned sad om oe zorder 2 at t11
        s "Oh... Seguramente todo se arreglará, [player]."
        show monika forward sad om oe zorder 2 at t21
        show sayori turned sad om oe zorder 2 at t22
        m "Sí, yo también pienso que todo estará bien. Solo denles espacio."
        show monika forward sad om oe zorder 2 at thide
        show sayori turned sad om oe zorder 2 at thide
        hide sayori 
        hide monika 
        "Tal vez pueda ayudar un poco en la situación."
        "Caminé hacia la puerta del club, pero sentí cómo alguien me agarró del brazo."
        show monika forward anno om oe zorder 2 at f11
        m "[player], quédate aquí. Soy la presidenta y conozco a mis miembros, así que..."
        m "Confía en mí."
        show monika forward anno cm oe zorder 2 at t11
        mc "¿De qué hablas? Deberíamos intentar ayudarlas. No las conozco lo suficiente a ambas, pero..."
        mc "Esa pelea fue muy estúpida. ¿Pelear por el tema de un poema?"
        mc "Solo les ganó el calor del momento."
        show monika lean anno om ce zorder 2 at f11
        m "Como mencionas, a ellas no las conoces. Pero a mí sí."
        show monika lean anno om oe zorder 2 at f11
        m "Así que, confía en mí."
        hide monika 
        with dissolve_scene_full
    jump final_discusion
    label mostrar_poema_monika2:
        play music audio.t5 fadein 0.5
        show monika 1a at f11
        m "¡Hola de nuevo, [player]!"
        m "Veo que te estás tomando esto de la escritura muy en serio."
        m 1b "Déjame ver qué preparaste para hoy."
        "Le entrego mi poema a Monika."
        show monika 1d at f11
        m "..."
        show monika 2g at f11
        "Monika entrecierra los ojos mientras lee el papel. Por un segundo, su sonrisa desaparece por completo."
        show monika 4b at f11
        m "Oh... ya veo."
        m "Vaya, [player]... parece que te esforzaste bastante en impresionar a alguien en específico hoy, ¿verdad?"
        show monika 4b at t11
        mc "¿Eh? ¿A qué te refieres?"
        show monika 2h at f11
        m "Je, no te hagas el tonto."
        m "La elección de palabras en este poema... es demasiado profunda, metafórica y oscura."
        show monika 1r at f11
        "Monika desvía la mirada un momento, cruzándose de brazos con un ligero suspiro de fastidio."
        m 1g "Definitivamente tiene la vibra de Yuri escrita por todos lados."
        m "A ella le fascinan este tipo de cosas pretenciosas... ya sabes, misterios pesados y un vocabulario innecesariamente complejo."
        show monika 1g zorder 2 at t11
        mc "Bueno, yo... solo intenté escribir algo diferente."
        show monika 2f at f11
        m "No tienes que justificarte conmigo, [player]. Aunque..."
        m 2g "Me sorprende un poco que te hayas decantado por su estilo tan rápido."
        show monika 3b at f11
        m "Solo ten cuidado de no perder tu propia voz en el proceso, ¿de acuerdo? No querrás cambiar solo para complacerla."
        m 3h "A veces, intentar encajar en el mundo de alguien tan... inestable y reservado como Yuri, puede hacer que te olvides de ti mismo."
        show monika 2e at f11
        m "Y, honestamente, sería una lástima que desperdiciaras tu potencial limitándote a lo que a ella le gusta."
        show monika 5a at f11
        "Monika recupera rápidamente su sonrisa perfecta, aunque sus ojos aún muestran un toque de recelo."
        m "¡Pero bueno, es solo un consejo de tu presidenta! En general, hiciste un buen esfuerzo..."
        # Monika se prepara para mostrar su poema
        show monika 1b at f11
        m "Ahora, es mi turno. Déjame mostrarte lo que escribí hoy."
        m "Es un poema que habla sobre decisiones reales, algo que de verdad importa. No metáforas vacías."
        m 1a "¡Espero que te guste!"
        $ poem_db.show_poem("poem_m2")
        show monika 1a at f11
        m "¿Y bien? ¿Qué te pareció?"
        m 1b "Sé que es mucho más directo que lo que acabas de escribir, pero a mí me gusta ser clara con lo que quiero transmitir."
        show monika 1a at t11
        mc "Es... bastante único, Monika. Me hace pensar en cómo a veces nos sentimos atrapados."
        show monika 5a at f11
        m "¡Exactamente! Me alegra tanto que lo entiendas de esa manera, [player]."
        m 1j "Significa muchísimo para mí que prestes atención a mis palabras."
        show monika 2a at f11
        m "En fin... será mejor que sigas compartiendo tu poema con las demás."
        m 2g "Estoy segura de que Yuri se morirá de ganas por leer lo que escribiste 'especialmente' para ella."
        show monika 2a at thide
        hide monika
        with wipeleft_scene
        jump pelea 
    label mostrar_poema_yuri2:
        if decision_biblioteca == "Monika":
            play music audio.t5
            "Me acerqué a Yuri."
            show yuri turned happ cm oe zorder 2 at t11
            mc "¿Lista?"
            show yuri turned happ om oe zorder 2 at f11
            y "Por supuesto, quiero ver cómo seguiste mis consejos."
            show yuri turned happ cm oe zorder 2 at f11
            "Espero no me destruya..."
            "Alcé mi mano para darle el poema a Yuri."
            #añadir poema 
            show yuri turned neut om oe zorder 2 at f11
            y "[player]..."
            show yuri turned neut cm oe zorder 2 at t11
            mc "¿S-sí?"
            "Siento que va a notar que lo escribí en la noche... Supongo que no vale la pena sobrepensar, eso no soluciona nada."
            #añadir escena de interrumpir dependiendo de la reescritura 
            show yuri turned happ om ce zorder 2 at f11
            y "Me gustó mucho más que el de ayer."
            show yuri turned happ cm ce zorder 2 at t11
            "¿Qué?"
            show yuri mb e1d zorder 2 at f11
            y "Añadiste muy bien el simbolismo y esta vez intentaste algo nuevo, experimentaste y realmente te salió bien."
            show yuri turned laug om oe zorder 2 at f11
            y "Si sigues mejorando, incluso podrías ser el mejor escritor del club, yo lo creo."
            show yuri turned laug cm oe zorder 2 at f11
            mc "No creo que sea tan bueno como mencionas, Yuri, pero sí seguí tus consejos y además leí algunos libros."
            show yuri turned nerv om oe zorder 2 at f11
            y "Tu poema es tan impresionante... ¿T-te importaría si me lo quedo?"
            show yuri turned lsur cm oe zorder 2 at t11
            mc "Pero aún tengo que compartirlo, Yuri..."
            show yuri turned worr cm oe zorder 2 at t11
            mc "Pero no tengo problemas."
            show yuri turned laug om oe zorder 2 at t11
            "Yuri me sonrió ligeramente. Espero no se lo tome a mal."
            show yuri turned flus om oe zorder 2 at f11
            y "Con más práctica, podrías incluso expresar tus sentimientos o cómo te sientes. Yo... a veces lo hago."
            show yuri turned rup laug cm oe zorder 2 at t11
            mc "Sería muy difícil escribir mis pensamientos."
            show yuri turned curi om oe zorder 2 at f11
            y "¿A qué te refieres?"
            show yuri turned curi cm oe zorder 2 at t11
            mc "No me sentiría tan cómodo describiéndome a los demás."
            mc "E incluso creo que incomodaría a los demás miembros haciéndolo."
            show yuri turned happ om oe zorder 2 at f11
            y "Bueno, no tiene que ser a todos, puede ser con alguien especial."
            show yuri turned happ om oe zorder 2 at s11
            y "Como yo..."
            show yuri turned nerv cm ce zorder 2 at t11
            "Se quedó en silencio un segundo, como si recién hubiera escuchado lo que acababa de decir."
            show yuri turned nerv om oe zorder 2 at f11
            y "Q-quiero decir... alguien en quien confíes. No tiene que ser yo, necesariamente."
            show yuri turned flus cm oe zorder 2 at t11
            mc "No sé, Yuri. Contigo se siente bastante fácil hablar de estas cosas."
            show yuri turned happ om ce zorder 2 at f11
            y "..."
            show yuri turned laug cm oe zorder 2 at t11
            mc "Suena a una buena idea para mi próximo poema."
            "Yuri me pasó su poema. Era una hoja suelta."
            $ poem_db.show_poem("Yuri_poem2")
            show yuri turned nerv om oe zorder 2 at f11
            y "¿Y bien...?"
            show yuri turned nerv cm oe zorder 2 at t11
            mc "Es realmente hermoso, Yuri... El \"Señor tic tac\". ¿En quién pensabas cuando lo escribiste?"
            show yuri turned flus om ce zorder 2 at f11
            y "E-eso no es algo que pueda responder tan fácilmente."
            show yuri shy m4 e1 b1 zorder 2 at f11
            y "Solo... hay alguien que ha estado ahí, aunque no se lo haya pedido. Alguien paciente, que no se rindió conmigo aunque tuviera motivos de sobra."
            show yuri shy m4 e1 b1 zorder 2 at t11
            y "No sabía cómo agradecer eso con palabras normales, así que... lo escribí de la única forma que sé hacerlo."
            show yuri shy m1 e2 b1 zorder 2 at t11
            mc "Oh... conque es eso."
            mc "Entonces vale mucho más ahora que sé lo que hay detrás de esas palabras."
            show yuri shy m3 e1 b1 zorder 2 at f11
            y "..."
            show yuri shy m3 e1 b1 zorder 2 at t11
            y "Me alegra que lo veas de esa forma."
            show yuri shy m3 e1 b1 zorder 2 at thide
            hide yuri
            with wipeleft_scene
            jump pelea
        elif decision_biblioteca == "Yuri":
            $ decision_poema_my = "yuriyuri"
            play music audio.t5
            "Yuri se acerca lentamente a mí."
            show yuri turned happ cm oe zorder 2 at f11
            y "[player], ¿quieres compartir poemas?"
            show yuri turned happ cm oe zorder 2 at t11
            mc "Por supuesto"
            mc "¿Lista?"
            show yuri turned happ om oe zorder 2 at f11
            y "Por supuesto, quiero ver cómo seguiste mis consejos."
            show yuri turned happ cm oe zorder 2 at f11
            "Espero no me destruya..."
            "Alcé mi mano para darle el poema a Yuri."
            #añadir poema 
            show yuri turned neut om oe zorder 2 at f11
            y "[player]..."
            show yuri turned neut cm oe zorder 2 at t11
            mc "¿S-sí?"
            "Siento que va a notar que lo escribí en la noche... Supongo que no vale la pena sobrepensar, eso no soluciona nada."
            #añadir escena de interrumpir dependiendo de la reescritura 
            show yuri turned happ om ce zorder 2 at f11
            y "Me gustó mucho más que el de ayer."
            show yuri turned happ cm ce zorder 2 at t11
            "¿Qué?"
            show yuri mb e1d zorder 2 at f11
            y "Añadiste muy bien el simbolismo y esta vez intentaste algo nuevo, experimentaste y realmente te salió bien."
            show yuri turned laug om oe zorder 2 at f11
            y "Si sigues mejorando, incluso podrías ser el mejor escritor del club, yo lo creo."
            show yuri turned laug cm oe zorder 2 at t11
            mc "No creo que sea tan bueno como mencionas, Yuri, pero sí seguí tus consejos y además leí algunos libros."
            show yuri turned nerv om oe zorder 2 at f11
            y "Tu poema es tan impresionante... ¿T-te importaría si me lo quedo?"
            show yuri turned lsur cm oe zorder 2 at t11
            mc "Pero aún tengo que compartirlo, Yuri..."
            show yuri turned worr cm oe zorder 2 at t11
            mc "Pero no tengo problemas luego de compartirlo con las chicas."
            show yuri turned laug om oe zorder 2 at t11
            "Yuri me sonrió ligeramente. Espero no se lo tome a mal."
            show yuri turned flus om oe zorder 2 at f11
            y "Con más práctica, podrías incluso expresar tus sentimientos o cómo te sientes. Yo... a veces lo hago."
            show yuri turned rup laug cm oe zorder 2 at t11
            mc "Sería muy difícil escribir mis pensamientos."
            show yuri turned curi om oe zorder 2 at f11
            y "¿A qué te refieres?"
            show yuri turned curi cm oe zorder 2 at t11
            mc "No me sentiría tan cómodo describiéndome a los demás."
            mc "E incluso creo que incomodaría a los demás miembros haciéndolo."
            show yuri turned happ om oe zorder 2 at f11
            y "Bueno, no tiene que ser a todos, puede ser con alguien especial."
            show yuri turned happ om oe zorder 2 at s11
            y "Como yo..."
            show yuri turned nerv cm ce zorder 2 at t11
            "Se quedó en silencio un segundo, como si recién hubiera escuchado lo que acababa de decir."
            show yuri turned nerv om oe zorder 2 at f11
            y "Q-quiero decir... alguien en quien confíes. No tiene que ser yo, necesariamente."
            show yuri turned flus cm oe zorder 2 at t11
            mc "No sé, Yuri. Contigo se siente bastante fácil hablar de estas cosas."
            show yuri turned happ om ce zorder 2 at f11
            y "..."
            show yuri turned laug cm oe zorder 2 at t11
            mc "Suena a una buena idea para mi próximo poema."
            "Yuri me pasó su poema. Era una hoja suelta."
            $ poem_db.show_poem("Yuri_poem2")
            show yuri turned nerv om oe zorder 2 at f11
            y "¿Y bien...?"
            show yuri turned nerv cm oe zorder 2 at t11
            mc "Es realmente hermoso, Yuri... El \"Señor tic tac\". ¿En quién pensabas cuando lo escribiste?"
            show yuri turned flus om ce zorder 2 at f11
            y "E-eso no es algo que pueda responder tan fácilmente."
            show yuri turned worr om oe zorder 2 at f11
            y "Solo... hay alguien que ha estado ahí, aunque no se lo haya pedido. Alguien paciente, que no se rindió conmigo aunque tuviera motivos de sobra."
            show yuri turned worr cm oe zorder 2 at t11
            y "No sabía cómo agradecer eso con palabras normales, así que... lo escribí de la única forma que sé hacerlo."
            show yuri turned flus cm oe zorder 2 at t11
            mc "Oh... conque es eso."
            mc "Entonces vale mucho más ahora que sé lo que hay detrás de esas palabras."
            show yuri turned happ om ce zorder 2 at f11
            y "..."
            show yuri turned flus cm oe zorder 2 at t11
            y "Me alegra que lo veas de esa forma."
            show yuri turned laug cm oe zorder 2 at t11
            show yuri turned laug cm oe zorder 2 at thide
            hide yuri
            with wipeleft_scene
            jump pelea
