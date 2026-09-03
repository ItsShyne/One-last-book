## creditos.rpy
##
## Estructura (según el storyboard):
## 1. Los 3 ganadores del concurso de fan art, mostrados grandes y destacados.
## 2. El resto de los dibujos van pasando de a pocos, y mientras se muestran
##    aparece una categoría del equipo (Artistas, Programadores, etc.) con
##    sus nombres -- igual que los créditos originales de DDLC muestran un
##    CG del juego mientras listan cada categoría, pero acá con fan art de
##    la comunidad en vez de CGs.
##
## Ganadores confirmados:
## - 1er lugar: dibujo2.png, por s4ant
## - 2do lugar: dibujo10.png, por robinlolyin11
## - 3er lugar: dibujo11.png, por parraga_jc
##
## Los 11 dibujos restantes están agrupados por proporción parecida entre
## sí (ver comentarios en "label creditos" más abajo), para que la caja de
## cada categoría se ajuste a esa forma y no queden franjas vacías:
## - Artistas: dibujo3, 4, 9 (retratos muy angostos, ratio ~0.56)
## - Programadores: dibujo6, 7 (panorámicas anchas, ratio 1.78)
## - Escritores: dibujo1, 12 (retratos, ratio ~0.86)
## - Compositores: dibujo5, 14 (cuadradas, ratio ~1.0)
## - Promocionadores: dibujo8, 13 (levemente panorámicas, ratio ~1.2-1.3)
##
## Artistas de cada dibujo confirmados hasta ahora:
## dibujo1 = ajoloteMC | dibujo3 = b1_b0ss | dibujo4 = Mr Bachi |
## dibujo7 = Sin Cereal | dibujo8 = Comandante Acuarion |
## dibujo13 = Ledezx_aa | dibujo14 = gersonmr_
## Sin confirmar todavía (quedaron con "Arte de la comunidad"):
## dibujo5, dibujo6, dibujo9, dibujo12
##
## Colores por categoría ajustados a la estética otoñal del mod (naranja
## calabaza, ámbar, rojo arce, dorado oliva, terracota) en vez del
## arcoíris saturado que tenía antes.


# Fondo ambiental de los créditos: 3 lugares con peso emocional en la
# historia (el club, la biblioteca, el cuarto de Yuri), ya oscurecidos y
# desenfocados (ver mod_assets/bg/creditos/).
#
# Se reparten TODA la duración de los créditos (~53.2s, desde que arrancan
# los ganadores hasta justo antes de "Gracias por jugar" -- incluye
# "Dirigido por/Creado por" y la categoría de Poemas) en 3 tramos iguales
# de ~17.7s cada uno (3s apareciendo + 11.7s sostenido + 3s
# desapareciendo), sin repetirse -- cada uno se muestra una sola vez y le
# pasa la posta al siguiente con un crossfade de 3s.
image credits_ambient_1:
    "mod_assets/bg/creditos/creditos_bg_club.png"
    xysize (1280, 720)
    fit "cover"
    alpha 0.0
    linear 3.0 alpha 1.0
    11.7
    linear 3.0 alpha 0.0

image credits_ambient_2:
    "mod_assets/bg/creditos/creditos_bg_library.png"
    xysize (1280, 720)
    fit "cover"
    alpha 0.0
    17.7
    linear 3.0 alpha 1.0
    11.7
    linear 3.0 alpha 0.0

image credits_ambient_3:
    "mod_assets/bg/creditos/creditos_bg_yuri.png"
    xysize (1280, 720)
    fit "cover"
    alpha 0.0
    35.4
    linear 3.0 alpha 1.0
    11.7
    linear 3.0 alpha 0.0

# Fondo del reconocimiento inicial: el fondo de lunares del menú de Fallen
# Angel, oscurecido y desenfocado igual que los otros 3.
image credits_ambient_fallen:
    "mod_assets/bg/creditos/creditos_bg_fallen.png"
    xysize (1280, 720)
    fit "cover"


# Pantalla de los 3 ganadores del concurso, destacados.
screen creditos_ganadores(primero, segundo, tercero, artista_1="Saucefy10", artista_2="Arte de la comunidad", artista_3="Arte de la comunidad"):
    add Solid("#00000060")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        text "GANADORES DEL CONCURSO DE FAN ART":
            xalign 0.5
            size 40
            color "#ffcc66"
            bold True

        hbox:
            xalign 0.5
            spacing 50

            # 2do lugar
            vbox:
                xalign 0.5
                yalign 1.0
                spacing 10
                add segundo:
                    xsize 300
                    ysize 380
                    fit "contain"
                    xalign 0.5
                text "2° lugar":
                    xalign 0.5
                    size 28
                    color "#cccccc"
                    bold True
                text artista_2:
                    xalign 0.5
                    size 22
                    color "#aaaaaa"

            # 1er lugar (mas grande, al centro)
            vbox:
                xalign 0.5
                yalign 1.0
                spacing 12
                add primero:
                    xsize 380
                    ysize 470
                    fit "contain"
                    xalign 0.5
                text "1er lugar":
                    xalign 0.5
                    size 36
                    color "#ffcc66"
                    bold True
                text artista_1:
                    xalign 0.5
                    size 26
                    color "#ffffff"

            # 3er lugar
            vbox:
                xalign 0.5
                yalign 1.0
                spacing 10
                add tercero:
                    xsize 300
                    ysize 380
                    fit "contain"
                    xalign 0.5
                text "3° lugar":
                    xalign 0.5
                    size 28
                    color "#cccccc"
                    bold True
                text artista_3:
                    xalign 0.5
                    size 22
                    color "#aaaaaa"


# Pantalla especial: "Dirigido por" y "Creado por", uno a cada lado de la
# misma toma (en vez de una categoría más con lista de nombres).
screen creditos_director_creador():
    add Solid("#00000060")

    hbox:
        xfill True
        yalign 0.5

        vbox:
            xsize 640
            xalign 0.5
            spacing 14
            text "DIRIGIDO POR":
                xalign 0.5
                size 44
                color "#ffcc66"
                bold True
            text "Shyne":
                xalign 0.5
                text_align 0.5
                size 40
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]

        vbox:
            xsize 640
            xalign 0.5
            spacing 14
            text "CREADO POR":
                xalign 0.5
                size 44
                color "#ffcc66"
                bold True
            text "Leni":
                xalign 0.5
                text_align 0.5
                size 40
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]


# Pantalla reutilizable: mientras se muestran algunos dibujos (no ganadores)
# de fondo, aparece una categoría del equipo con sus nombres.
# imagenes: lista de tuplas (ruta, artista) -- cada dibujo lleva el nombre
# de quien lo hizo debajo, en chico.
# imgw/imgh: tamaño del cuadro de cada dibujo. Cada categoría junta dibujos
# de proporción (ancho/alto) parecida entre sí, así que el cuadro se ajusta
# por categoría en vez de forzar un único tamaño fijo para todos -- si no,
# los dibujos panorámicos quedaban con enormes franjas vacías al costado
# y los muy verticales se veían diminutos dentro de una caja cuadrada.
# apilar: True pone los dibujos uno encima del otro en vez de lado a lado
# -- para panorámicas (anchas y bajas), apiladas se aprovecha mejor el
# espacio vertical en vez de alargar todo horizontalmente.
screen creditos_categoria(imagenes, titulo, texto, color_titulo="#ffcc66", imgw=280, imgh=320, apilar=False):
    add Solid("#00000060")

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 70

        if apilar:
            vbox:
                spacing 24
                xalign 0.5
                for imagen, artista in imagenes:
                    vbox:
                        xalign 0.5
                        spacing 4
                        add imagen:
                            xsize imgw
                            ysize imgh
                            fit "contain"
                            xalign 0.5
                        text artista:
                            xalign 0.5
                            size 18
                            color "#888888"
        else:
            hbox:
                spacing 20
                xalign 0.5
                for imagen, artista in imagenes:
                    vbox:
                        xalign 0.5
                        spacing 4
                        add imagen:
                            xsize imgw
                            ysize imgh
                            fit "contain"
                            xalign 0.5
                        text artista:
                            xalign 0.5
                            size 18
                            color "#888888"

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14

            text titulo:
                xalign 0.5
                size 44
                color color_titulo
                bold True

            text texto:
                xalign 0.5
                text_align 0.5
                size 30
                color "#ffffff"


# Pantalla de reconocimiento al mod original, antes de los ganadores.
screen creditos_intro():
    add Solid("#00000060")
    add "mod_assets/logos/Yuri Fallen Angel.png":
        xsize 480
        ysize 470
        fit "contain"
        xalign 0.0
        yalign 1.0
    text "Basado en el reconocido mod\nFallen Angel, creado por Noa_AT":
        xalign 0.78
        yalign 0.5
        text_align 0.5
        size 40
        color "#ffffff"
        bold True


# Pantalla de cierre.
screen creditos_final():
    add Solid("#000000")
    text "Gracias por jugar":
        xalign 0.5
        yalign 0.5
        size 60
        color "#ffffff"
        bold True


label creditos:
    # Oculta a la fuerza la caja de diálogo que haya quedado de la última
    # línea del capítulo anterior -- sin esto, a veces queda visible por
    # encima de los créditos si el capítulo no la cerró explícitamente
    # antes del jump.
    window hide

    scene black
    with Dissolve(1.0)
    stop music fadeout 2.0
    play music audio.creditos fadein 2.0

    # Que no se pueda saltar clickeando -- mismo método que usa la
    # secuencia original de créditos de DDLC (ver label credits2 en
    # code/poem_responses/core/credits.rpy).
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False

    show credits_ambient_fallen
    show screen creditos_intro
    with Dissolve(1.0)
    $ renpy.pause(4.0, hard=True)
    hide screen creditos_intro
    hide credits_ambient_fallen
    with Dissolve(0.8)

    show credits_ambient_1
    show credits_ambient_2
    show credits_ambient_3

    show screen creditos_ganadores(
        "mod_assets/bg/dibujo2.png",
        "mod_assets/bg/dibujo10.png",
        "mod_assets/bg/dibujo11.png",
        "s4ant",
        "robinlolyin11",
        "parraga_jc"
    )
    $ renpy.pause(6.0, hard=True)
    hide screen creditos_ganadores
    with Dissolve(1.0)

    show screen creditos_director_creador
    with Dissolve(0.8)
    $ renpy.pause(5.0, hard=True)
    hide screen creditos_director_creador
    with Dissolve(0.8)

    # dibujo3/4/9: retratos muy angostos y altos, casi la misma proporción
    # entre sí (0.56 aprox) -- caja angosta y alta para que no sobre espacio.
    show screen creditos_categoria(
        [
            ("mod_assets/bg/dibujo3.png", "b1_b0ss"),
            ("mod_assets/bg/dibujo4.jpg", "Mr Bachi"),
            ("mod_assets/bg/dibujo9.png", "Arte de la comunidad"),
        ],
        "ARTISTAS",
        "Ajolote\nArtful\nCalvo\nGerson\nLedezx\nMr Bachi\nParraga\nSaorin\nSetfet\nSin Cereal",
        "#e08a3c",
        imgw=200, imgh=355
    )
    with Dissolve(0.8)
    $ renpy.pause(5.0, hard=True)
    hide screen creditos_categoria
    with Dissolve(0.8)

    # dibujo6/7: panorámicas anchas, misma proporción exacta (1.78) --
    # apiladas una encima de otra, aprovechando mejor el espacio vertical
    # en vez de alargarlas lado a lado.
    show screen creditos_categoria(
        [
            ("mod_assets/bg/dibujo6.png", "Setfet"),
            ("mod_assets/bg/dibujo7.png", "Sin Cereal"),
        ],
        "PROGRAMADORES",
        "Falkner\nLeni\nShyne\nSkert\nSlytharbez(Port a Android)",
        "#c9932e",
        imgw=420, imgh=236, apilar=True
    )
    with Dissolve(0.8)
    $ renpy.pause(5.0, hard=True)
    hide screen creditos_categoria
    with Dissolve(0.8)

    # dibujo1/12: retratos de proporción parecida (0.86 aprox).
    show screen creditos_categoria(
        [
            ("mod_assets/bg/dibujo1.png", "ajoloteMC"),
            ("mod_assets/bg/dibujo12.jpg", "Arte de la comunidad"),
        ],
        "ESCRITORES",
        "EduCrock\nJeshu Rusky Dave\nLeni\nLuytenx\nShyne",
        "#a83e2c",
        imgw=280, imgh=320
    )
    with Dissolve(0.8)
    $ renpy.pause(5.0, hard=True)
    hide screen creditos_categoria
    with Dissolve(0.8)

    # dibujo5/14: prácticamente cuadradas.
    show screen creditos_categoria(
        [
            ("mod_assets/bg/dibujo5.png", "Arte de la comunidad"),
            ("mod_assets/bg/dibujo14.jpg", "gersonmr_"),
        ],
        "COMPOSITORES",
        "EMI.chr\nJona\nRadkarvk",
        "#8a6d1f",
        imgw=300, imgh=300
    )
    with Dissolve(0.8)
    $ renpy.pause(5.0, hard=True)
    hide screen creditos_categoria
    with Dissolve(0.8)

    # dibujo8/13: levemente panorámicas, proporción parecida (1.2-1.3) --
    # también apiladas por el mismo motivo que Programadores.
    show screen creditos_categoria(
        [
            ("mod_assets/bg/dibujo8.jpg", "Comandante Acuarion"),
            ("mod_assets/bg/dibujo13.png", "Ledezx_aa"),
        ],
        "PROMOCIONADORES",
        "Ema Blazer\nFalkner\nLeni",
        "#b5541f",
        imgw=360, imgh=288, apilar=True
    )
    with Dissolve(0.8)
    $ renpy.pause(5.0, hard=True)
    hide screen creditos_categoria
    with Dissolve(0.8)

    show screen creditos_categoria(
        [],
        "POEMAS",
        "Abuelita (Catador de Femboys)\nSetfet",
        "#9c5b2e"
    )
    with Dissolve(0.8)
    $ renpy.pause(5.0, hard=True)
    hide screen creditos_categoria
    hide credits_ambient_1
    hide credits_ambient_2
    hide credits_ambient_3
    with Dissolve(0.8)

    show screen creditos_final
    with Dissolve(0.8)
    $ renpy.pause(4.0, hard=True)
    hide screen creditos_final

    # Pantalla negra unos segundos, con la música apagándose de a poco,
    # antes de volver al menú -- así no se siente un corte brusco de
    # golpe cuando arranca la música del menú.
    stop music fadeout 4.0
    scene black
    with Dissolve(1.0)
    $ renpy.pause(4.0, hard=True)

    return
