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
    
    $ persistent.gallery_img_1_unlocked = True
    $ renpy.save_persistent()
    $ persistent.gallery_img_2_unlocked = True
    $ renpy.save_persistent()
    $ persistent.gallery_img_3_unlocked = True
    $ renpy.save_persistent()
    $ persistent.gallery_img_4_unlocked = True
    $ renpy.save_persistent()
    $ persistent.gallery_img_5_unlocked = True
    $ renpy.save_persistent()
    $ persistent.gallery_img_6_unlocked = True
    $ renpy.save_persistent()

    "escuché una ruidosa y conocida voz."

    show sayori turned uniform lup nerv om oe zorder 2 at t44

    s "jeje, disculpa por moverte un poco pero digamos que vamos tarde."

    player "\"¿vamos? ¿tarde?.\""

    "me estiré en mi asiento y al mirar a alrededor no habia nadie en el salón además de nosotros."

    show sayori 5b zorder 2 at t11
    
    s "te estaba esperando afuera del salón por un ratito, pero como no salias entonces entré."

    show sayori tap uniform nerv om ce  zorder 2 at t11

    s "Realmente... ¡¡estás peor que yo!!! el timbre suena unas 3 veces."

    player "\"de todos modos no necesitas esperarme seguro los de tu club se preocuparán por ti.\"" 

    show sayori tap uniform neut cm oe  zorder 2 at t11

    "antes Sayori estaba en el club de arte pero luego que se creara el club de literatura ella se unió, no tengo idea del porque."

    show sayori 1h zorder 2 at t21

    s "desvelarte viendo anime te está afectando la memoria... en la mañana me prometiste visitar algunos clubs y..."

    player "\"no visitaré el club de literatura Sayori…\""

    show sayori turned uniform ldown curi cm oe zorder 2 at t44

    s "¿¡eh!? pe-pero"

    player "\"sip, nos vemos mañana.\""

    "recogi algunos libros de mi pupitre para meterlos en mi mochila."

    "¿enserio me quedé dormido?"

    show sayori tap uniform dist cm ce  zorder 2 at t11

    s "pero me dijiste que lo harías!"

    player "\"¿porqué es tan importante para ti que lo haga?\""

    s "bueno yo..."

    show sayori turned uniform nerv om oe zorder 2 at t43

    s "ayer... les dije a todo el club que traería un nuevo miembro y además Natsuki hizo pastelitos."

    player "\"¿¡Hiciste un promesa de algo que no depende de ti!?\""

    show sayori 2c zorder 2 at t11

    s "como tú diciendo que visitarias algunos clubs?"

    player "\"...\""

    "debí de haberme ido en lugar de discutir."

    "suspiré."

    player "\"está bien... pero solo visitar no unirme.\""

    show sayori 4r zorder 2 at t21

    show sayori 4r zorder 2 at t22

    s "¡¡si!!! ¡¡vamos~!!"

    "Sayori me agarró fuertemente del brazo para arrastrarme fuera del salón."

    show sayori zorder 2 at thide
    hide s

    jump cap2

