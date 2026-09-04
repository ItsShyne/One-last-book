default ach_chapter2 = False
default ach_good_ending = False
default ach_secret_scene = False
default ach_all_yuri_poems = False

default seen_achievements_intro = False

# Galería de imágenes
default gallery_page = 0
default gallery_selected_image = 0

define GALLERY_IMAGES = [
    {
        "image": "gui/menu_bg.png",
        "name": "Menu BG",
        "description": "Imagen usada de fondo, creada por Ledezx.",
        "unlocked_var": "gallery_img_1_unlocked"
    },

    {
        "image": "gui/menu_art_y.png",
        "name": "Yuri del menú",
        "description": "Una versión de Yuri hecha para el menu, creada por Ledezx.",
        "unlocked_var": "gallery_img_2_unlocked"
    },

    {
        "image": "images/yuri/yuri_parraga_caraenojada.webp",
        "name": "yuri enojada",
        "description": "Sprite hecho por el artista parraga para la escena del baño.",
        "unlocked_var": "gallery_img_3_unlocked"
    },

    {
        "image": "images/yuri/yuri_parraga_carallorando.webp",
        "name": "yuri llorando",
        "description": "Sprite hecho por el artista parraga para la escena del baño.",
        "unlocked_var": "gallery_img_4_unlocked"
    },

    {
        "image": "images/yuri/yuri_parraga_carallorandofuerte.webp",
        "name": "yuri llorando fuerte",
        "description": "Sprite hecho por el artista parraga para la escena del baño.",
        "unlocked_var": "gallery_img_5_unlocked"
    },

    {
        "image": "images/yuri/yuri_parraga_carapensativa.webp",
        "name": "yuri pensativa",
        "description": "Sprite hecho por el artista parraga para la escena del baño.",
        "unlocked_var": "gallery_img_6_unlocked"
    },

    {
        "image": "images/yuri/yuri_parraga_caratriste.webp",
        "name": "yuri triste",
        "description": "Sprite hecho por el artista parraga para la escena del baño.",
        "unlocked_var": "gallery_img_7_unlocked"
    }


]
default seen_gallery_intro = False

transform gallery_hover:

    zoom 1.0

    on hover:
        linear 0.15 zoom 1.03

    on idle:
        linear 0.15 zoom 1.0

style ok_button_style is button:
    background "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]
    hover_background "#c79cff"
    hover_outlines [(2, "#8a4fff", 0, 0)]
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    xpadding 14
    ypadding 5

image copa_icono = "mod_assets/mod_extra_images/achievements.png"
image block_icono = "mod_assets/mod_extra_images/about.png"
image menu_azul = "gui/menu_bg_blue.png"

screen achievements_intro():

    tag menu
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 800
        padding (30, 30)

        vbox:
            spacing 15
            text "Bienvenido a Logros" size 34 color "#ffffff" outlines [(3, "#000000", 0, 0)]
            text "En esta sección habra unas pistas para desbloquear logros. Si los desbloqueas todos, quizá obtengas una recompensa." size 26 color "#ffffff" outlines [(3, "#000000", 0, 0)]
            textbutton "OK":
                style "ok_button_style"
                xalign 0.0
                xminimum 100
                yminimum 36
                action [SetVariable("seen_achievements_intro", True), ShowMenu("achievements")]

screen extras():

    tag menu

    use game_menu("Extras"):

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            textbutton "Logros":
                action If(not seen_achievements_intro,
                            true=ShowMenu("achievements_intro"),
                            false=ShowMenu("achievements"))

            textbutton "Galería de Imágenes":
                action ShowMenu("gallery")

screen achievements():

    tag menu

    use game_menu("Logros"):

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.1

            label "Logros"

            frame:

                xfill True
                ymaximum 520
                padding (20, 20)

                viewport:
                    id "achievements_vp"
                    draggable True
                    mousewheel True
                    scrollbars "vertical"

                    vbox:
                        spacing 20
                        xalign 0.5

                        if ach_chapter2:
                            hbox:
                                spacing 20
                                add "copa_icono"
                                vbox:
                                    text "Primer Paso" size 35
                                    text "Algunas historias apenas están comenzando..." size 22
                                    text "DESBLOQUEADO" color "#00AA00"
                        else:
                            hbox:
                                spacing 20
                                add "block_icono"
                                vbox:
                                    text "???" size 35
                                    text "Todavía hay páginas por descubrir..." size 22
                                    text "BLOQUEADO" color "#AA0000"

                        if ach_good_ending:
                            hbox:
                                spacing 20
                                add "copa_icono"
                                vbox:
                                    text "Segundo Paso" size 35
                                    text "Otra descripción del logro..." size 22
                                    text "DESBLOQUEADO" color "#00AA00"
                        else:
                            hbox:
                                spacing 20
                                add "block_icono"
                                vbox:
                                    text "???" size 35
                                    text "quizas este final sea diferente" size 22
                                    text "BLOQUEADO" color "#AA0000"

                        if ach_secret_scene:
                            hbox:
                                spacing 20
                                add "copa_icono"
                                vbox:
                                    text "mi angel" size 35
                                    text "pasa todo el tiempo posible con Yuri" size 22
                                    text "DESBLOQUEADO" color "#00AA00"
                        else:
                            hbox:
                                spacing 20
                                add "block_icono"
                                vbox:
                                    text "???" size 35
                                    text "pasa todo el tiempo posible con Yuri" size 22
                                    text "BLOQUEADO" color "#AA0000"

                        if ach_all_yuri_poems:
                            hbox:
                                spacing 20
                                add "copa_icono"
                                vbox:
                                    text "los poemas" size 35
                                    text "leiste todos los poemas de Yuri" size 22
                                    text "DESBLOQUEADO" color "#00AA00"
                        else:
                            hbox:
                                spacing 20
                                add "block_icono"
                                vbox:
                                    text "???" size 35
                                    text "sigue ESCRIBIENDO" size 22
                                    text "BLOQUEADO" color "#AA0000"

screen gallery():

    tag menu

    add gui.main_menu_background

    fixed:

            textbutton "Volver":
                xalign 0.05
                ypos 30
                action Return()

            $ images_per_page = 6 
            $ total_pages = (len(GALLERY_IMAGES) + images_per_page - 1) // images_per_page

            $ start_index = gallery_page * images_per_page
            $ end_index = min(start_index + images_per_page, len(GALLERY_IMAGES))

            grid 3 2:

                xalign 0.5
                yalign 0.48

                spacing 35

                for i in range(start_index, end_index):

                    $ img_data = GALLERY_IMAGES[i]
                    $ is_unlocked = getattr(persistent, img_data["unlocked_var"], False)

                    if is_unlocked:

                        button:

                            xysize (360, 220)

                            idle_background "#222222"
                            hover_background "#444444"

                            action [SetVariable("gallery_selected_image", i), ShowMenu("image_viewer")]

                            add img_data["image"] at gallery_hover:
                                xsize 340
                                ysize 200
                                xalign 0.5
                                yalign 0.5

                    else:

                        button:

                            xysize (360, 220)

                            idle_background "#222222"
                            hover_background "#444444"

                            action ShowMenu("blocked_message")

                            add Transform(img_data["image"], blur=25, size=(280, 160)) xalign 0.5 yalign 0.5

                            text "???":
                                xalign 0.5
                                yalign 0.5
                                size 55
                                color "#FFFFFF"
                                outlines [
                                (4, "#000000", 0, 0)
                            ]
                                

            hbox:

                xalign 0.5
                ypos 650

                spacing 20

                textbutton "◄":

                    action If(
                        gallery_page > 0,
                        SetVariable("gallery_page", gallery_page - 1),
                        NullAction()
                    )

                for p in range(total_pages):

                    textbutton "[p+1]":

                        action SetVariable("gallery_page", p)

                textbutton "►":

                    action If(
                        gallery_page < total_pages - 1,
                        SetVariable("gallery_page", gallery_page + 1),
                        NullAction()
                    )


screen image_viewer():

    tag menu
    modal True

    $ img_data = GALLERY_IMAGES[gallery_selected_image]

    frame:

        xsize 1180
        ysize 680

        xalign 0.58
        yalign 0.5

        background Solid("#111111")

        vbox:

            spacing 15

            text img_data["name"]:

                xalign 0.5
                size 35

            add img_data["image"]:

                xpos 80

                xsize 1050
                ysize 500

            text img_data.get("description", "imagen usada de fondo, creada por Ledezx."):

                xalign 0.5
                text_align 0.5
                size 24

            hbox:

                spacing 40
                xalign 0.5

                textbutton "← Anterior":

                    action SetVariable(
                        "gallery_selected_image",
                        max(0, gallery_selected_image - 1)
                    )

                textbutton "Cerrar":
                    action ShowMenu("gallery")

                textbutton "Siguiente →":

                    action SetVariable(
                        "gallery_selected_image",
                        min(len(GALLERY_IMAGES)-1, gallery_selected_image + 1)
                    )

screen blocked_message():

    tag menu
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 600
        padding (30, 30)
        background Solid("#1a1a1a")

        vbox:
            spacing 20

            text "Bloqueado por el momento" size 28 color "#ffcccc" outlines [(2, "#000000", 0, 0)] xalign 0.5

            text "Continúa avanzando en el juego para desbloquear esta imagen." size 20 color "#ffffff" xalign 0.5

            textbutton "OK":
                style "ok_button_style"
                xalign 0.5
                xminimum 85
                yminimum 100
                action Return()
