#aqui iran todas las elecciones de todas las rutas
#buena, neutra, mala y en el futuro secreta 
#se guiara por dias

########## DIA 1 ##########
#esto involucra el cap1 y el inicio del cap2

#Elecciones de la ruta

#RUTA BUENA ELECCIÓN 1
label rutas:
    if rutabuena == "Se eligió ir con Sayori":
        show sayori turned happ cm oe zorder 2 at t11

        mc "por supuesto Sayori"

        show sayori turned lup rup happ om ce zorder 2 at h11 
        s "yaaay~"
        mc "Dame un momento y tomo mis cosas"
        show sayori turned lup rup happ om ce zorder 2 at thide
        hide sayori 
        "Rapidamente guarde mis cosas y alcancé a Sayori en la puerta del aula"
        mc "Listo Sayori, podemos irnos"
        s "¡¡¡Nos vemos mañana chicas!!!"

        show bg residential_day
        with wipeleft_scene

        "Durante todo el camino a casa he pensado en ella"

        show yuri 3b zorder 2 at t11

        "En Yuri.{w} Quizas no esté pensando bien pero siento como si tuvieramos algo en común"

        "estoy seguro que me la pasaré muy bien todos los días con ella"
        "Y por supuesto con las demas chicas tambien"
   
        "Quiero conocerla un poco más, espero que no me mire como un rarito..."

        show yuri zorder 2 at thide
        hide yuri

        "¡perfecto! solo necesito hacerlo bien y lo lograré"

        "asi que escribir un poema...{w} si hago un poema que a ella le guste será más facil acercarme"

        show sayori turned happ cm ce zorder 2 at t11

        mc "oye Sayori ¿de qué escribirás tu poema?"

        show sayori turned lsur om oe zorder 2 at f11

        s "hmmm..."

        show sayori turned happ om oe zorder 2 at f11

        s "quizás sea acerca del sol, es muy lindo, sobretodo cuando voy a la escuela"

        show sayori turned happ cm oe zorder 2 at t11

        mc "nunca he escrito un poema. no tengo idea de que hacerlo"

        mc "aunque me sorprende que escribas poemas, nunca me imagine que podrias hacerlo"

        show sayori tap nerv om oe zorder 2 at f11

        s "s-si..."

        show sayori tap pout cm oe zorder 2 at t11

        mc "adivino... estamos en las mismas ¿cierto?"

        show sayori turned lup rup pani om oe zorder 2 at f11

        s "¡¡¡Oye!!!"

        show sayori turned lup rup pani om ce zorder 2 at thide
        hide sayori

        return
    #RUTA NEUTRA ELECCIÓN 1
    elif rutaneutra == "Se rechazó ir con Sayori":
        show sayori 2m zorder 2 at f11
        s "¿¡qué!? ¿enserio?"
        show sayori 2p zorder 2 at t11
        menu:
            #CONTINUACIÓN DE LA RUTA NEUTRA
            "Irse con sayori":
                mc "Pensandolo bien quizás si sea buena idea"
                show sayori turned happ cm oe zorder 2 at t11

                mc "por supuesto Sayori"

                show sayori turned lup rup happ om ce zorder 2 at h11 
                s "yaaay~"
                mc "Dame un momento y tomo mis cosas"
                show sayori turned lup rup happ om ce zorder 2 at thide
                hide sayori 
                "guardé mis cosas y alcancé a Sayori en la puerta del aula"
                stop music fadeout 2.0

                show bg residential_day
                with wipeleft_scene

                "Durante todo el camino a casa he pensado en ella"

                show yuri 3b zorder 2 at t11

                "En Yuri.{w} Quizas no esté pensando bien pero siento como si tuvieramos algo en común"

                "estoy seguro que me la pasaré muy bien todos los días con ella"
                "Y por supuesto con las demas chicas tambien"
        
                "Quiero conocerla un poco más, espero que no me mire como un rarito..."

                show yuri zorder 2 at thide
                hide yuri

                "¡perfecto! solo necesito hacerlo bien y lo lograré"

                "asi que escribir un poema...{w} si hago un poema que a ella le guste será más facil acercarme"

                show sayori turned dist cm oe zorder 2 at t11

                s "..."
                show sayori turned dist cm ce zorder 2 at thide
                hide sayori
                with wipeleft_scene
                call biblioteca
            #RUTA MALA    
            "Prefiero irme solo":
                mc "lo siento Sayori pero prefiero irme solo"
                show sayori turned curi cm oe zorder 2 at t11
                s "..."
                "me retiré del salón"
                show sayori turned curi cm oe zorder 2 at thide
                hide sayori
                call biblioteca 
        return




