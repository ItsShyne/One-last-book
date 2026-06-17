init python:
    import renpy.exports as rempy
    #movimiento de las dianas
    def diana1_desaparecer():
        store.diana1 = False
        store.puntos += 1
    def diana2_desaparecer():
        store.diana2 = False
        store.puntos += 1
    def diana3_desaparecer():
        store.diana3 = False
        store.puntos += 1
    def diana4_desaparecer():
        store.diana4 = False
        store.puntos += 1
        
#VELOCIDAD NIVEL 1
transform movimiento_lento1:
    zoom 0.5
    xpos 0.8
    linear 2.0 xpos 0.1
    repeat        
transform movimiento_lento2:
    zoom 0.5
    xpos 0.1  
    linear 2.0 xpos 0.8
    repeat
#VELOCIDAD NIVEL 2
transform movimiento_normal1:
    zoom 0.5
    xpos 0.8
    linear 1.5 xpos 0.1
    repeat        
transform movimiento_normal2:
    zoom 0.5
    xpos 0.1  
    linear 1.5 xpos 0.8
    repeat
#VELOCIDAD NIVEL 3
transform movimiento_dificil1:
    zoom 0.5
    xpos 0.8
    linear 1.0 xpos 0.1
    repeat        
transform movimiento_dificil2:
    zoom 0.5
    xpos 0.1  
    linear 1.0 xpos 0.8
    repeat
#VELOCIDAD NIVEL 4
transform movimiento_extremo1:
    zoom 0.5
    xpos 0.8
    linear 0.5 xpos 0.1
    repeat        
transform movimiento_extremo2:
    zoom 0.5
    xpos 0.1  
    linear 0.5 xpos 0.8
    repeat
#VARIABLES
default puntos = 0
default tiempo = 15
default nivel = 1
default diana1 = True
default diana2 = True
default diana3 = True
default diana4 = True
#esto no tiene importancia
screen scene_1:
    add ""
#IMAGENES Y PUNTOS
screen galeria_tiro:

    #fondos/anotodor

    add "images/bg/fondo_fiesta.png" xysize (config.screen_width, config.screen_height)
    add "images/bg/anotador.webp" xpos 10 ypos 0 zoom 1.0

    #los puntos y su ubicacion tambien del tiempo y nivel
    text "puntos: [puntos]" xpos 25 ypos 60 size 35
    text "tiempo: [tiempo]" xpos 25 ypos 110 size 35
    text "nivel: [nivel]" xpos 25 ypos 160 size 35

    #esto es para que la diana vuelva a aparecer
    if not diana1:
        timer 0.5 action SetVariable("diana1", True) 
    if not diana2:
        timer 0.5 action SetVariable("diana2", True)
    if not diana3:
        timer 0.5 action SetVariable("diana3", True)
    if not diana4:
        timer 0.5 action SetVariable("diana4", True)

    #DIANAS NIVEL 1
    if diana1:
        if nivel == 1:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_lento1

                ypos 0.3
                action  Function(diana1_desaparecer)
    if diana2:
        if nivel == 1:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_lento2

                ypos 0.5
                action  Function(diana2_desaparecer)
    if diana3:
        if nivel == 1:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_lento1

                ypos 0.5
                action  Function(diana3_desaparecer)
    if diana4:
        if nivel == 1:

            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_lento2

                ypos 0.3
                action  Function(diana4_desaparecer)
    #DIANAS NIVEL 2
    if diana1:
        if nivel == 2:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_normal1

                ypos 0.3
                action  Function(diana1_desaparecer)
    if diana2:
        if nivel == 2:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_normal2

                ypos 0.5
                action  Function(diana2_desaparecer)
    if diana3:
        if nivel == 2:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_normal1

                ypos 0.5
                action  Function(diana3_desaparecer)
    if diana4:
        if nivel == 2:

            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_normal2

                ypos 0.3
                action  Function(diana4_desaparecer)
    #DIANAS NIVEL 3
    if diana1:
        if nivel == 3:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_dificil1

                ypos 0.3
                action  Function(diana1_desaparecer)
    if diana2:
        if nivel == 3:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_dificil2

                ypos 0.5
                action  Function(diana2_desaparecer)
    if diana3:
        if nivel == 3:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_dificil1

                ypos 0.5
                action  Function(diana3_desaparecer)
    if diana4:
        if nivel == 3:

            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_dificil2

                ypos 0.3
                action  Function(diana4_desaparecer)
    
        #tiempo
    #DIANA NIVEL 4
    if diana1:
        if nivel == 4:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_extremo1

                ypos 0.3
                action  Function(diana1_desaparecer)
    if diana2:
        if nivel == 4:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_extremo2

                ypos 0.5
                action  Function(diana2_desaparecer)
    if diana3:
        if nivel == 4:
            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_extremo1

                ypos 0.5
                action  Function(diana3_desaparecer)
    if diana4:
        if nivel == 4:

            imagebutton:
                idle "images/bg/diana.webp"
                hover "images/bg/diana.webp"
        
                at movimiento_extremo2

                ypos 0.3
                action  Function(diana4_desaparecer)
    timer 1.0 repeat True action If(tiempo > 0, SetVariable("tiempo", tiempo - 1), Return())

image bg fondo_fiesta = im.Scale("images/bg/fondo_fiesta.png", config.screen_width, config.screen_height)

label festival:
    scene bg fondo_fiesta 
    "para pasar de nivel tienes que conseguir 20 puntos, al no conseguirlo lo puedes volver a intentar"
    "para conseguir puntos centrare el darle al centro de la diana"
    "buena suerte"

    $puntos = 0
    $tiempo = 20

    call screen galeria_tiro
    "tiempo se acabo, tus puntos fueron [puntos]"
    if puntos >= 20:
        if nivel <= 3:
            "felicidades, has pasado al siguiente nivel"
            menu:
                "quieres continuar al siguiente nivel?"

                "si":
                    $nivel += 1
                    jump festival 
                "no":
                    return

        elif nivel > 3:
            "por las barbas de odin, has pasado el nivel mas dificil"
            "vaya, nunca espere que alguien ganara esto"
            "bueno, te dare una recompensa por tu esfuerzo"

    else:
        if nivel <=3:

            "lo siento, no has alcanzado el puntaje necesario para pasar al siguiente nivel"

            menu:

                "quieres intentarlo de nuevo?"

                "si":
                    jump festival
                "no":
                    "pendejo no dura nada"
                    return
            
        elif nivel > 3:
            "oye, es muy dificl, mejor rendite"
        menu:
            "te vas a rendir?"
            "si":
                "bueno, no es para todos"
                return
            "no":
                "pero cuanta, DETERMINACION"   
                jump festival
    return