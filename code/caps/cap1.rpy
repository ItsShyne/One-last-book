<<<<<<< HEAD
#aqui inicia el dia 1


=======
>>>>>>> 3da4df11d06dd09889e946a1bfcda428fb1ca342
label cap1:
    stop music fadeout 2.0
    #lo de scene es para mostrar el fondo, y el with es para hacer la transición entre escenas
    #el dissolve_scene_full es una transición que hace que la escena se disuelva completamente
    with dissolve_scene_full 
    play music audio.t2
    scene bg class_day at noche, sleepy_camera

    show top_lid at top_closed
    show bottom_lid at bottom_closed

    pause 0.8

    "???" "\"[player]...\""

    show top_lid at top_open
    show bottom_lid at bottom_open

    pause 0.15

    show top_lid at top_close
    show bottom_lid at bottom_close

    pause 0.15

    "???" "\"[player]\""

    show top_lid at top_open
    show bottom_lid at bottom_open

    pause 0.15

    show top_lid at top_close
    show bottom_lid at bottom_close

    pause 0.15

    "???" "\"¡[player]!\""

    show top_lid at top_open
    show bottom_lid at bottom_open

    pause 0.5

    hide top_lid
    hide bottom_lid

    scene bg class_day at noche with Dissolve(0.3)

    pause 1.0

    scene bg class_day with Dissolve(0.3)
    
    #$ persistent.gallery_img_1_unlocked = True
    #$ renpy.save_persistent()
    #$ persistent.gallery_img_2_unlocked = True
    #$ renpy.save_persistent()
    #$ persistent.gallery_img_3_unlocked = True
    #$ renpy.save_persistent()
    #$ persistent.gallery_img_4_unlocked = True
    #$ renpy.save_persistent()
    #$ persistent.gallery_img_5_unlocked = True
    #$ renpy.save_persistent()
    #$ persistent.gallery_img_6_unlocked = True
    #$ renpy.save_persistent()

    "Escuché una ruidosa y conocida voz."

    show sayori turned rup uniform nerv om oe zorder 3 at f44

    s "Jeje, disculpa por moverte un poco pero digamos que vamos tarde."

    show sayori turned rup uniform nerv cm oe zorder 2 at t44

<<<<<<< HEAD
    player "\"¿Vamos? ¿tarde?\""

    "Me estiré en mi asiento y miré alrededor, no había nadie en el salón además de nosotros."

    show sayori 5b zorder 2 at f11
    
    s "Te estaba esperando afuera del salón por un ratito, pero como no salías, entonces entré."

    show sayori tap om ce zorder 2 at f11

    s "Realmente... ¡¡estás peor que yo!!! El timbre suena unas 3 veces."

    show sayori tap nerv cm oe zorder 2 at t11
=======
    player "\"¿Vamos? ¿tarde?.\""

    "Me estiré en mi asiento y miré alrededor, no habia nadie en el salón además de nosotros."

    show sayori 5b zorder 2 at f11
    
    s "Te estaba esperando afuera del salón por un ratito, pero como no salias entonces entré."

    show sayori tap om ce zorder 2 at f11

    s "Realmente... ¡¡estás peor que yo!!! el timbre suena unas 3 veces."

    show sayori tap om ce zorder 2 at t11
>>>>>>> 3da4df11d06dd09889e946a1bfcda428fb1ca342

    player "\"Si bueno, de todos modos no necesitas esperarme seguro los de tu club se preocuparán por ti.\"" 

    show sayori tap cm oe zorder 2 at t11

<<<<<<< HEAD
    "Antes Sayori estaba en el club de arte pero, después de que se creó el club de literatura, ella se unió. no tengo idea del porqué."

    show sayori 1h zorder 2 at f21

    s "Desvelarte viendo anime te está afectando la memoria... en la mañana me prometiste visitar algunos clubes y..."
=======
    "Antes Sayori estaba en el club de arte pero luego que se creara el club de literatura ella se unió, no tengo idea del porque."

    show sayori 1h zorder 2 at f21

    s "Desvelarte viendo anime te está afectando la memoria... en la mañana me prometiste visitar algunos clubs y..."
>>>>>>> 3da4df11d06dd09889e946a1bfcda428fb1ca342

    show sayori turned uniform shoc cm oe zorder 2 at t11

    player "\"No visitaré el club de literatura Sayori…\""

    show sayori turned uniform vsur om oe zorder 2 at f22

<<<<<<< HEAD
    s "¿¡Eh!? ¡Pe-pero...!"
=======
    s "¿¡Eh!? pe-pero"
>>>>>>> 3da4df11d06dd09889e946a1bfcda428fb1ca342

    show sayori turned uniform vsur om oe zorder 2 at t22

    player "\"sip, nos vemos mañana.\""

<<<<<<< HEAD
    "Recogí algunos libros del pupitre para meterlos en mi mochila."

    "¿En serio me quedé dormido?"

    show sayori tap uniform pout om oe zorder 2 at f11

    s "Pero ¡me prometiste que lo harías!"

    show sayori tap uniform pout cm oe zorder 2 at t11

    player "\"¿En serio es importante para ti que lo haga?\""
=======
    "Recogi algunos libros del pupitre para meterlos en mi mochila."

    "¿Enserio me quedé dormido?"

    show sayori tap uniform pout om oe zorder 2 at f11

    s "Pero me prometiste que lo harías!"

    show sayori tap uniform pout om oe zorder 2 at t11

    player "\"¿Enserio es importante para ti qué lo haga?\""
>>>>>>> 3da4df11d06dd09889e946a1bfcda428fb1ca342

    show sayori turned rup uniform nerv om oe zorder 3 at f11

    s "bueno yo..."

    show sayori turned uniform nerv om oe zorder 2 at f43

<<<<<<< HEAD
    s "Ayer... le dije a todo el club que traería un nuevo miembro y además Natsuki hizo pastelitos."

    show sayori turned uniform nerv cm oe zorder 2 at t43
=======
    s "Ayer... les dije a todo el club que traería un nuevo miembro y además Natsuki hizo pastelitos."

    show sayori turned uniform nerv om oe zorder 2 at t43
>>>>>>> 3da4df11d06dd09889e946a1bfcda428fb1ca342

    player "\"¿¡Hiciste un promesa de algo que no depende de ti!?\""

    show sayori 2c zorder 2 at f11

<<<<<<< HEAD
    s "¿Cómo tú diciendo que visitarías algunos clubes?"

    show sayori turned neut cm oe zorder 2 at t11
=======
    s "Como tú diciendo que visitarias algunos clubs?"

    show sayori 2c zorder 2 at t11
>>>>>>> 3da4df11d06dd09889e946a1bfcda428fb1ca342

    player "\"...\""

    "Debí de haberme ido en lugar de discutir."

    "Suspiré."

    player "\"Está bien... pero solo visitar no unirme.\""

<<<<<<< HEAD
    show sayori 4r zorder 2 at f21

    s "¡¡sí!!! ¡¡vamos~!!"

    show sayori 4r zorder 2 at t22
=======
    show sayori 4r zorder 2 at t21

    s "¡¡si!!! ¡¡vamos~!!"

    pause 1.0

    show sayori 4r zorder 2 at f22
>>>>>>> 3da4df11d06dd09889e946a1bfcda428fb1ca342

    "Sayori me agarró fuertemente del brazo para arrastrarme fuera del salón."

    show sayori zorder 2 at thide
    hide s

<<<<<<< HEAD
    stop music fadeout 2.0
    call cap2

=======
    scene bg class_day
    with fade

    jump cap2
>>>>>>> 3da4df11d06dd09889e946a1bfcda428fb1ca342

