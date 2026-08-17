

transform creditos_scroll:
    yoffset 3500
    linear 40.0 yoffset -2500


screen creditos():

    # Fondo negro
    add Solid("#000000")

    # Créditos
    vbox:
        xalign 0.5
        yalign 1.0
        spacing 28

        at creditos_scroll

        # Espacio inicial
        null height 700



        text "ARTISTAS":
            xalign 0.5
            size 45
            color "#ffcc66"
            bold True

        text "Setfet\nCalvo\nArtful\nSin Cereal\nGerson\nAjolote\nLedezx\nParraga\nSaorin\nMr Bachi":
            xalign 0.5
            text_align 0.5
            size 32
            color "#ffffff"

        null height 50

        text "Todo el presupuesto se fue en artistas":
            xalign 0.5
            text_align 0.5
            size 28
            color "#ffcc66"
            italic True

        null height 100

        text "PROGRAMADORES":
            xalign 0.5
            size 45
            color "#66ccff"
            bold True

        text "Leni\nFalkner\nShyne\nSkert":
            xalign 0.5
            text_align 0.5
            size 32
            color "#ffffff"

        null height 100


        text "GUIONISTAS":
            xalign 0.5
            size 45
            color "#cc99ff"
            bold True

        text "Edumon\nJeshu\nRusky\nNatsuki Lover\nLuytenx":
            xalign 0.5
            text_align 0.5
            size 32
            color "#ffffff"

        null height 100

        text "COMPOSITORES":
            xalign 0.5
            size 45
            color "#66ff99"
            bold True

        text "EMI.chr\nJona\nRadkarvk":
            xalign 0.5
            text_align 0.5
            size 32
            color "#ffffff"

        null height 100


        text "PROMOCIONADORES":
            xalign 0.5
            size 45
            color "#ff6699"
            bold True

        text "Falkner\nLeni\nEma Blazer":
            xalign 0.5
            text_align 0.5
            size 32
            color "#ffffff"

        null height 150


        text "Gracias por jugar":
            xalign 0.5
            text_align 0.5
            size 50
            color "#ffffff"
            bold True

        null height 100

        text "leni puto":
            xalign 0.5
            size 50

        null height 700


label creditos:

    scene black
    stop music fadeout 2.0


    show screen creditos

    # Espera hasta que termine el desplazamiento
    $ renpy.pause(35.0, hard=True)

    hide screen creditos


    return
