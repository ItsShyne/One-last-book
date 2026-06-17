# TRANSFORMS
image  bg recuerdos = "images/bg/borde_blanco.png.avif"
image bg residensial_noche = "images/bg/residential-night.png"

transform heartbeat_weak:
    zoom 1.00
    linear 0.15 zoom 1.02
    linear 0.15 zoom 1.00

transform heartbeat_medium:
    zoom 1.00
    linear 0.12 zoom 1.04
    linear 0.12 zoom 1.00

transform heartbeat_strong:
    zoom 1.00
    linear 0.10 zoom 1.06
    linear 0.10 zoom 1.00

# Imagen de viñeta (PNG con centro transparente)
image vignette = "vignette.png"

label panic_scene:

    stop music fadeout 2.0

    scene bg class_day

    "Algo no estaba bien."

    play sound audio.heart

    show bg class_day at heartbeat_weak
    pause 0.3

    "Mi pecho se sentía extraño..."

    play sound audio.heart

    show bg class_day at heartbeat_weak
    pause 0.3

    show vignette:
        alpha 0.0
        linear 1.0 alpha 0.3

    "Podía escuchar mis propios latidos."

    play sound audio.heart

    show bg class_day at heartbeat_medium
    pause 0.25

    play sound audio.heart

    show bg class_day at heartbeat_medium
    pause 0.25

    show vignette:
        alpha 0.3
        linear 1.0 alpha 0.6

    "Cada vez más fuertes..."

    play sound audio.heart

    show bg class_day at heartbeat_strong
    pause 0.2

    play sound audio.heart

    show bg class_day at heartbeat_strong
    pause 0.2

    play sound audio.heart

    show bg class_day at heartbeat_strong
    pause 0.15

    show vignette:
        alpha 0.6
        linear 0.5 alpha 0.8

    "No podía concentrarme."

    scene black with Dissolve(1.0)

    stop sound

    "..."



    return
      
screen recuerdo_border():

    $ grosor = 60

    # Arriba
    add Solid("#857777b0") xysize (1280, grosor) xpos 0 ypos 0

    # Abajo
    add Solid("#857777b0") xysize (1280, grosor) xpos 0 ypos (720 - grosor)

    # Izquierda
    add Solid("#857777b0") xysize (grosor, 720 - grosor * 2) xpos 0 ypos grosor

    # Derecha
    add Solid("#857777b0") xysize (grosor, 720 - grosor * 2) xpos (1280 - grosor) ypos grosor

transform memory_zoom:
    zoom 1.05
    ease 10.0 zoom 1.08

label recordar:

    scene bg residential_day at memory_zoom

    show screen recuerdo_border

    with Dissolve(0.5)

    "Nunca me he puesto a pensar en la primera vez que conocí a Sayori."

    hide screen recuerdo_border

    return



image lluvia_tile:

    contains:
        "images/bg/lluviarecta.png"
        ypos 0

    contains:
        "images/bg/lluviarecta.png"
        ypos -1080

    contains:
        "images/bg/lluviarecta.png"
        ypos -2160

    subpixel True

    yoffset 0
    linear 1.0 yoffset 1080
    repeat

transform noche:
    matrixcolor BrightnessMatrix(-0.25)


label lluvia:

    stop music fadeout 2.0
    

    
    show bg residensial_noche

    play music audio.lluvia fadein 3.0 loop 

    show lluvia_tile onlayer front at noche

    with dissolve

    show sayori 4r at noche

    "La lluvia caía sin descanso."

    "Las gotas golpeaban el suelo con una monotonía casi hipnótica."

    "El cielo gris parecía extenderse hasta el infinito."

    mc "..."

    mc "No esperaba que terminara así."

    "El viento frío recorrió la calle vacía."

    "Por un momento pensé en regresar a casa."

    "Pero mis pies se negaban a moverse."

    mc "Supongo que ya no importa."

    "Las gotas continuaron descendiendo mientras observaba el horizonte."

    # Relámpago opcional
    show expression Solid("#FFF") as relampago
    with Dissolve(0.05)

    play sound audio.trueno

    pause 0.05

    hide relampago
    with Dissolve(0.15)
    
    hide s
    show sayori 2m at noche
    s "..."
    hide s
    show sayori 2l at noche
    s "¿es-eso fue un trueno?" 

    pause 2.0

    "\"vaya...\""
     
    hide lluvia_tile 
    stop music fadeout 3.0

    return

init:

    image top_lid = Solid("#000")
    image bottom_lid = Solid("#000")

transform top_closed:
    xpos 0
    ypos 0
    xsize 1280
    ysize 360

transform bottom_closed:
    xpos 0
    ypos 360
    xsize 1280
    ysize 360

transform top_open:
    ease 0.8 ypos -360

transform bottom_open:
    ease 0.8 ypos 720

transform top_close:
    ease 0.8 ypos 0

transform bottom_close:
    ease 0.8 ypos 360

label despertar_realista:

    scene bg bedroom at noche

    # Ojos cerrados
    show top_lid at top_closed
    show bottom_lid at bottom_closed

    pause 0.8

    "\"Toc Toc\""

    # Primer parpadeo
    show top_lid at top_open
    show bottom_lid at bottom_open

    pause 0.9

    show top_lid at top_close
    show bottom_lid at bottom_close

    pause 0.9

    "\"Toc Toc\""

    # Segundo parpadeo
    show top_lid at top_open
    show bottom_lid at bottom_open

    pause 0.9

    show top_lid at top_close
    show bottom_lid at bottom_close

    pause 0.9

    "\"Toc Toc\""

    # Apertura final
    show top_lid at top_open
    show bottom_lid at bottom_open

    pause 1.0

    hide top_lid
    hide bottom_lid

    pause 1.2

    scene bg bedroom with Dissolve(0.3)

    player "¿Quién es...?"

    return


transform camera_idle:
    subpixel True
    xoffset 0
    yoffset 0

    linear 2.0 xoffset -10 yoffset -5
    linear 2.0 xoffset 10 yoffset 5
    repeat

transform sleepy_camera:

    subpixel True

    zoom 1.05
    xalign 0.5
    yalign 0.5

    linear 4.0 xoffset -15 yoffset -8
    linear 4.0 xoffset 15 yoffset 8
    repeat