# Copyright 2019-2025 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains the Ren'Py code for displaying poems in DDLC.

# For the Python code, see `poems_ren.py` in the `py` directory.

# Transición de "pasar la página" para el libro compartido de MC y Yuri --
# mismo mecanismo que wipeleft_scene (ImageDissolve con una máscara
# degradada), pero con un barrido diagonal en vez de recto, para que se
# sienta como una página girando en vez de un wipe genérico de escena.
define page_flip_transition = ImageDissolve("mod_assets/bg/creditos/page_flip_mask.png", 0.6, ramplen=64)

screen poem(poem):
    style_prefix "poem"

    fixed:

        frame:
            style "poem_paper"

            add poem.paper:
                subpixel True align (0.5, 0.5)

        if poem.author == "libro":
            # El libro compartido reparte el texto en dos columnas, una por
            # hoja, en vez de un único bloque que atraviese el lomo. El
            # punto de quiebre entre hojas se marca a mano en el texto con
            # un carácter "\f" (ver poems_ren.py), en un salto de párrafo
            # elegido para que ambas hojas queden parejas.
            $ _libro_left, _libro_sep, _libro_right = poem.raw_text.partition("\f")
            $ _libro_left = _libro_left.strip()
            $ _libro_right = _libro_right.strip()

            hbox:
                xalign 0.5 yalign 0.5 xpos 300
                spacing 100

                vbox:
                    xsize 360

                    if poem.raw_title:
                        text poem.raw_title style "libro_text" bold True size 30

                        null height 14

                    text _libro_left style "libro_text"

                vbox:
                    xsize 360

                    text _libro_right style "libro_text"
        else:
            frame:
                background None

                hbox:
                    viewport id "poem_vp":
                        draggable True
                        mousewheel True

                        add poem

                    vbar value YScrollValue("poem_vp")

    if not persistent.first_poem:
        add "gui/poem_dismiss.png" xpos 1050 ypos 590

    if poem.author != "libro":
        key ["repeat_K_UP", "K_UP"] action Scroll("poem_vp", "vertical decrease", 20)
        key ["repeat_K_DOWN", "K_DOWN"] action Scroll("poem_vp", "vertical increase", 20)

    on "show" action SetVariable("poem_last_author", poem.author)

style poem_vscrollbar:
    xsize 20
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style poem_paper:
    modal True
    align (0.5, 0.5)

style poem_fixed:
    align (0.5, 0.5)
    xsize 720

style poem_frame:
    padding (4, 35)

style poem_hbox:
    xfill True

style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style yuri_text_3:
    font "gui/font/y3.ttf"
    size 18
    color "#000"
    outlines []
    kerning -8
    justify True

style mc_text:
    font "mod_assets/font/ReenieBeanie_Regular.ttf"
    size 36
    color "#000"
    outlines []

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 28
    color "#000"
    outlines []

# Estilo para fragmentos del libro que MC y Yuri leen juntos -- una serif
# de imprenta en vez de la caligrafía de algún personaje, ya que es un
# libro publicado, no un poema escrito a mano. Justificado como prosa
# normal en vez de centrado como los poemas.
style libro_text:
    font "mod_assets/font/PTSerif-Regular.ttf"
    size 18
    color "#000"
    outlines []
    text_align 0.0
    justify True
    line_leading 2

default poem_last_author = None

# Depreciation Warning
label showpoem(poem, **properties):
    python:
        text = "This feature is now depreciated. Please use " + ("'$ poem_db.show_poem(\"%s\", %s)'" % (poem, ", ".join("%s=%s" % (k, v) for k, v in properties.items())) if properties else "'$ poem_db.show_poem(\"%s\")'" % poem) + " instead.\nRefer to {u}poem_responses/py/poems_ren.py{/u} for more information."
    $ renpy.notify(text)
    return