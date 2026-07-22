# Aquí irá el día uno que a su vez es la continuación del cap1

# Contadores de la ruta común
default puntos_ruta = 0
default decision_secreta = False
# if para algunas decisiones
default decision_biblioteca = "nula"
default decision_sayori = "nula"
default decision_poema_my = "Nula"

label cap2:

    $ ach_chapter2 = True
    $ ach_good_ending = True
    $ ach_secret_scene = True
    $ ach_all_yuri_poems = True

    play music audio.t6 fadein 2.0
    scene bg corridor
    with dissolve_scene_full

    "Seguí a Sayori por los pasillos. Comúnmente subimos aquí por materiales."

    "Sé que es un club con poca gente, pero el que esté tan alejado no ayuda."

    play audio closet_open

    "Sayori abrió la puerta del salón con fuerza."

    mc "¿No era más fácil abrirla gentilmente?"

    scene bg club_day
    show sayori 1s zorder 2 at f11

    s "¡¡¡Chicas!!! ¡¡¡Traje a un nuevo miembro!!!"

    show sayori 1q zorder 2 at t11

    mc "No lo grites, Sayori..."

    "¿Chicas?"

    show sayori 1q zorder 2 at thide
    hide sayori
    with wipeleft_scene 

    "Mi mirada se centró en una estudiante de cabello morado."

    show yuri 2b zorder 2 at f11

    y "Bienvenido al club de literatura, es un placer conocerte [player]."

    show yuri turned rup uniform happ om ce zorder 2 at f11

    y "Sayori siempre nos habla bien de ti."

    y "Me alegra mucho poder conocerte."   

    show yuri turned lup rup uniform nerv cm oe zorder 2 at t11

    y "(¿Espera, por qué dije eso en voz alta?)"

    show yuri turned lup rup uniform nerv cm oe zorder 2 at f11

    y "Uh..." 

    show yuri turned lup rup uniform nerv cm oe zorder 2 at t11

    pause 1.0

    show yuri turned rup uniform lsur cm oe zorder 2 at t11

    "Dios... es como si viera a un ángel en persona."

    "Es tan linda."

    "Aunque recuerdo como si la hubiera visto fuera de la escuela..."

    "Su cabello es hermoso..."

    n "¿En serio era necesario un chico?"

    show yuri shy neut cm oe zorder 2 at t22
    show natsuki 1h zorder 2 at f21

    n "Qué incómodo será el club desde ahora."

    show yuri shy neut cm oe zorder 2 at t32
    show natsuki 2g zorder 2 at t31
    show monika 4b zorder 2 at f33

    m "¡Ey! Qué bonita sorpresa, [player]."

    show natsuki 2g zorder 2 at t31
    show monika 2k zorder 2 at f33

    m "Bienvenido al club de literatura."

    show monika 2j zorder 2 at t33

    "Sayori... Sayori me trajo a un club..."

    show monika zorder 2 at thide
    hide monika
    show natsuki zorder 2 at thide
    hide natsuki
    show yuri 1d zorder 2 at t11

    "¡Qué tiene a una chica tan linda!"

    show yuri 1e zorder 2 at t21
    show natsuki 2w zorder 2 at f22

    n "¿Qué, nunca has visto a una mujer?"

    show yuri 1e zorder 2 at t21
    show natsuki turned anno cm oe zorder 2 at t22

    mc "Dis-disculpa."

    show yuri 1w zorder 2 at t42
    show natsuki 2w zorder 2 at t44

    y "Natsuki... recuerda que es nuestro nuevo miembro."

    show yuri 1w zorder 2 at thide
    hide yuri
    show natsuki 3i zorder 2 at t11

    "Parece que la chica de cabello rosado es un poco difícil..."

    "Por su apariencia será alguien de primer año, así que no vale la pena enojarse con ella."

    "¿Le dijo Natsuki? Probablemente sea quien hizo los pastelitos."

    show yuri 2i zorder 2 at t32
    show natsuki 3i zorder 2 at t33
    show sayori turned happ om ce zorder 2 at f31

    s "Tranqui [player], solo ignórala cuando esté de mal humor."

    show sayori turned happ cm ce zorder 2 at t31

    "Sayori se acercó a mí, sonando sus pasos contra el suelo."

    show yuri 2i zorder 2 at thide
    show sayori turned happ om ce zorder 2 at thide 
    hide yuri
    hide sayori
    show natsuki 3f zorder 2 at f11

    s "¡De todos modos! Ella es Natsuki."

    show natsuki 3f zorder 2 at thide 
    hide natsuki 
    show yuri 3a zorder 2 at t11

    s "Yuri."

    hide yuri 
    show monika lean happ om ce zorder 2 at t11

    s "Monika."

    hide monika
    show sayori 1s zorder 2 at f11

    s "¡Y tú ya me conoces!"

    show sayori zorder 2 at thide
    hide sayori 
    show yuri shy happ cm oe zorder 2 at t11

    "Aunque Sayori me esté presentando a las demás chicas, no puedo quitar la mirada de Yuri..."

    "Monika se acercó a mí con una amable sonrisa."

    show yuri zorder 2 at thide
    hide yuri 
    show sayori turned lsur cm oe zorder 2 at t21 
    show monika forward lpoint happ om oe zorder 2 at f22

    m "De hecho, [player] y yo estuvimos en la misma clase el año pasado."

    show monika forward happ cm ce zorder 2 at t22

    "Ella es Monika. Recuerdo perfectamente que estuvimos en la clase de Química el año pasado..."
    
    "Prefiero olvidar lo que pensaba el año pasado."

    show monika forward happ om oe zorder 2 at f22

    m "Qué alegría es verte de nuevo, [player]."

    show monika forward happ cm oe zorder 2 at t22

    mc "Sí... es un gusto también."

    show sayori turned happ om oe zorder 2 at f21

    s "¡Ven, [player]! Ya tengo mucha hambre."

    show sayori zorder 2 at thide
    hide sayori 
    show monika zorder 2 at thide
    hide monika 

    "Las chicas formaron un círculo con los pupitres mientras que Sayori me sentó a su lado."

    "Al ver a las demás chicas excepto a Yuri, supe de quién era el asiento faltante a mi lado."

    show sayori tap nerv m1 zorder 2 at f21

    s "Ya regreso~"

    hide sayori
    with wipeleft_scene

    show sayori 4p zorder 2 at f11

    s "Realmente no me podía aguantar las ganas de comer los pastelitos. Natsuki es la mejor cocinera... ¿o pastelera?"

    show sayori 4q zorder 2 at t22
    show natsuki 3f zorder 2 at f21

    n "¡Sayori!"

    show natsuki 3f zorder 2 at t21
    stop music fadeout 2.0

    "La pelirrosa agarró bruscamente la bandeja, pero debido al movimiento terminó cayendo al suelo."

    play sound obj_fall
    show natsuki 3f zorder 2 at h21

    n "off...-{nw}"

    show natsuki zorder 2 at thide
    hide natsuki 
    show sayori 4m zorder 2 at t21
    show monika 1g zorder 2 at t22

    play music audio.t9

    mc "¿Te encuentras bien?"

    "Me levanté de mi asiento mientras Sayori ayudaba a Natsuki a levantarse. Recogí la bandeja."

    show sayori zorder 2 at thide
    hide sayori
    show monika zorder 2 at thide
    hide monika
    show natsuki 2b zorder 2 at f11

    n "U-uh... mi cabeza... ¿¡y los pastelitos!? [player] deja lo-"

    show natsuki turned curi cm oe zorder 2 at t11

    "Aunque un par de pastelitos estaban caídos en el suelo, logré rescatar algunos."

    show natsuki turned lsur cm oe zorder 2 at t11

    "Todos están decorados como si fueran gatitos, realmente se mira el talento."

    show natsuki turned fs neut om oe zorder 2 at f11

    n "L-lo siento... Quería mostrarlos por mí misma, realmente me esforcé mucho haciéndolos..."

    show natsuki turned fs neut cm oe zorder 2 at t11

    "Natsuki está muy centrada en los pastelitos del suelo."
    
    show sayori 1f zorder 2 at t21
    show natsuki turned fs neut cm oe zorder 2 at t22

    "Sayori también."

    "Cómo puedo ayudar... con la bandeja en mi mano me di cuenta que aún quedaban unos pastelitos."

    mc "Oigan, está bien... miren, no todos cayeron al piso..."

    show sayori 1l zorder 2 at t21
    show natsuki 1n zorder 2 at t22

    mc "Y... se miran muy deliciosos, ¿no?"

    show sayori 3b zorder 2 at t21
    show natsuki turned lhip rhip ff sad om oe zorder 2 at f22

    n "S-sí..."

    show natsuki 4b zorder 2 at t22
    show natsuki turned lhip rhip ff sad cm oe zorder 2 at t22
    show sayori turned happ om oe zorder 2 at f21

    s "¡Siii! Aún hay pastelitos."

    show natsuki turned lhip rhip ff pout cm oe zorder 2 at f22

    n "Ajá..."

    show natsuki zorder 2 at thide
    hide natsuki
    show monika 2m zorder 2 at t21
    show sayori 1q zorder 2 at t22

    "Natsuki se fue al clóset a buscar algo para limpiar el piso."

    "Mientras que Sayori se acercó a mi oído."

    show monika zorder 2 at thide
    hide monika
    show sayori 1c zorder 2 at f11

    s "[player]"

    show sayori 1a zorder 2 at t11

    mc "¿Eh?"

    show sayori 1c zorder 2 at f11

    s "Hiciste bien."

    show sayori 1a zorder 2 at t11

    mc "Tenía que hacer algo para animarlas, ¿no?"

    show sayori 3c zorder 2 at f11

    s "Como siempre, jeje..."

    show sayori 3b zorder 2 at t11

    mc "¿Siempre?"

    stop music fadeout 2.0
    play music audio.t8 
    show sayori 2r zorder 2 at f11

    s "¡Vamos a comer~!"

    show sayori 1a zorder 2 at t22
    show monika forward lpoint happ cm ce zorder 2 at t21

    "Después de hablar, agarró rápidamente un pastelito de la bandeja, seguida de Monika y luego de mí."

    show sayori turned happ om ce zorder 2 at h22

    s "Esh mu delichisosho~ hmm~"

    show monika forward lpoint happ cm oe zorder 2 at t21

    "Mientras Sayori comía, Natsuki salió del clóset con un trapo y empezó a limpiar el piso."

    "Después de que Natsuki terminara de limpiar el piso, se sentó al lado de Sayori."

    show sayori zorder 2 at thide
    hide sayori
    show monika zorder 2 at thide
    hide monika
    show natsuki 3n zorder 2 at t11

    "Noto cómo mira en mi dirección mientras comía el pastelito."

    mc "Sayori tenía razón, están muy deliciosos."

    show natsuki 3r zorder 2 at t11

    mc "Muchas gracias, Natsuki."

    show natsuki 3r zorder 2 at f11

    n "¡N-no es que los haya hecho para ti o algo así!"

    "Sayori dijo que eran para el nue- sabes... mejor sigo disfrutando de los dulces pastelillos."

    show natsuki zorder 2 at thide
    hide natsuki
    with wiperight_scene

    show yuri 2a zorder 2 at t33

    "Yuri regresó con un juego de té en la mano y me entregó una taza con té."

    mc "¿Los profesores no las regañan por tener esto?"

    show yuri 2b zorder 2 at f33

    y "Nos dieron permiso debido a ser un nuevo club."

    y "Además, una taza de té siempre va de la mano de un libro."

    show yuri 2o zorder 2 at t21
    show monika 3b zorder 2 at f22

    m "Tranquilo [player], solo intentan impresionarte."

    show monika 1h  zorder 2 at t22

    m "(¿Presumiendo?)"

    show yuri 2o zorder 2 at f21
    show monika 2j zorder 2 at t22

    y "¿Qu-qué...? Y-yo no intentaba..."

    show yuri 2o zorder 2 at t21

    "Yuri volteó su mirada hacia la nada."

    show yuri 2w zorder 2 at f21
    show monika forward lpoint rhip happ cm oe zorder 2 at t22

    y "T-tú me entiendes..."

    show yuri zorder 2 at thide
    hide yuri
    show monika lean happ om oe zorder 2 at f11

    m "Por cierto [player], me alegra que te hayas unido. Como presidenta del club me aseguraré de que te sientas cómodo."

    show monika lean happ om oe zorder 2 at t11
    stop music fadeout 2.0

    mc "¿Que me haya unido? Pero aún no me he decidido en unirme..."

    show monika zorder 1 at thide
    hide monika
    show sayori 2m zorder 2 at t11

    mc "Me refiero..."

    show sayori 2m zorder 2 at t21
    show yuri 2i zorder 2 at t22

    mc "Aún tengo que ver otros clubs..."

    show sayori 2m zorder 2 at t31
    show yuri 2i zorder 2 at t32
    show monika 1m zorder 2 at t33

    mc "Ver qué club me gusta más..."

    show sayori 2m zorder 2 at t41
    show yuri turned sad cm oe zorder 2 at t42
    show monika 1m zorder 2 at t43
    show natsuki 1h zorder 2 at t44

    "Vamos, no pueden mirarme todas así."

    "Después de conocer a Yuri tal vez las cosas no sean tan malas, además no quiero que Sayori siga acosándome con que entre a su club."

    "Tomé valor y miré a las chicas directamente."

    mc "Eh... tomé una decisión."

    "Todas las chicas me estaban viendo, esperando mi respuesta."

    show sayori 2q zorder 2 at t41
    show yuri 1a zorder 2 at t42
    show monika 1j zorder 2 at t43
    show natsuki 2f zorder 2 at t44
    play music audio.t8

    mc "Está bien... Sí, me uniré al club."

    show sayori 2r zorder 2 at h41

    s "¡Yeiiii! Por un momento pensé que no te unirías."

    "Sayori me agarró de las manos y empezó a saltar con mucha emoción."

    show natsuki 1e zorder 2 at f44

    n "Si hubieras dicho que no te unirías, te hubiera hecho pagar por el pastelito."

    show natsuki 1g zorder 2 at t44
    show yuri 1d zorder 2 at f42

    y "Me asustaste por un instante."

    show yuri 1d zorder 2 at t42
    show monika 1b zorder 2 at f43
    
    m "Me alegra que hayas tomado una buena decisión."

    show natsuki zorder 2 at thide
    hide natsuki
    show sayori zorder 2 at thide
    hide sayori
    show yuri zorder 2 at thide
    hide yuri
    show monika 2b zorder 2 at f11

    m "Tengo una idea. Ya que [player] se ha unido, podríamos organizar una actividad. Ayer me encontré con algo curioso..."

    show monika zorder 2 at thide
    hide monika
    show sayori 2n zorder 2 at f11

    s "¿Actividad?"

    show sayori zorder 2 at thide
    hide sayori
    show monika 3a zorder 2 at t11

    "Monika sacó una hoja."

    show monika 3b zorder 2 at f11

    m "No sabía que te gustaba escribir poemas, Natsuki." 

    show monika 3a zorder 2 at t21
    show natsuki turned lhip rhip vang cm ce zorder 2 at f22

    n "¡Dame eso, Monika!"

    "Natsuki agarró la hoja de las manos de Monika para luego meterla en su mochila."

    show natsuki zorder 2 at thide
    hide natsuki
    show monika forward lpoint happ om ce zorder 2 at f11

    m "Y bueno... estaba pensando en que podríamos compartir poemas, así para [player] será más fácil conocernos."

    show monika 2i zorder 2 at f11

    m "Pero no creas que te salvarás de escribir uno también, [player]."

    show monika 2m zorder 2 at f11

    mc "Uh... claro."

    show sayori turned lup rup happ om ce zorder 2 at f21
    show monika 2i zorder 2 at t22

    s "Cuando llegue a casa me pondré a escribir."

    show sayori 1a zorder 2 at t31
    show monika 2i zorder 2 at t32
    show natsuki cross vang om ce zorder 2 at f33

    n "Qué vergüenza... No me gustaría compartir mis poemas, estoy segura que el nuevo me entenderá."

    show sayori 1a zorder 2 at t41
    show monika 2i zorder 2 at t42
    show natsuki cross anno cm oe zorder 2 at t43
    show yuri shy neut om oe zorder 2 at f44

    y "Para mí... también sería difícil hacerlo."

    show monika forward rhip happ cm oe zorder 2 at t42

    "Monika se quedó en silencio por un momento, para luego mirarme con una sonrisa."

    mc "Supongo que... podría hacer un poema y decirlo y eso."

    show monika forward rhip happ om oe zorder 2 at f42

    m "Perfecto, yo también. Así que chicas y [player], doy por concluida la reunión del club por hoy."

    show natsuki zorder 2 at thide
    hide natsuki
    show monika zorder 2 at thide
    hide monika
    show yuri zorder 2 at thide
    hide yuri
    show sayori zorder 2 at thide
    hide sayori
    show yuri turned laug cm oe zorder 2 at t11

    "Siento mucha ansiedad por escribir un poema {i}y encima compartirlo con ellas... con ella.{/i}"

    "Yuri se levantó de su asiento para ayudar a limpiar a Natsuki."

    show yuri zorder 2 at thide
    hide yuri
    show sayori turned happ om oe zorder 2 at f11

    s "Oye [player], ya que desde ahora nos veremos todos los días, ¿quieres caminar conmigo a casa? Ya sabes, como lo hacíamos antes."

    "Es cierto, hace mucho tiempo que no caminaba con Sayori debido a lo tarde que salía, no solo de la escuela."

    menu irse_con_Sayori:
        "Irse con Sayori":
            $ decision_sayori = "Sayori"
            "Sí, debería ir con ella."
            $ puntos_ruta += 1
            jump ir_sayori
        "Mejor no":
            mc "Mejor no."
            jump sayori_insiste        

label biblioteca:

    show bg bedroom
    with dissolve_scene_full
    play music audio.t8

    "Agarré un lápiz y una hoja de papel."

    "Poemas, poemas..."

    "¿Cómo siquiera se escribe un poema?"

    "Yuri luce como una chica madura, por lo que imagino que le gustarán los poemas reflexivos o algo así."

    "Golpeo repetidamente el lápiz contra el escritorio intentando hallar inspiración."

    "Uff... Si tan solo pudiera escribir palabras random que suenen bien..."

    "¡SÍ!"
  
    "La biblioteca a estas horas está abierta y puedo inspirarme, solo debo de buscar algo que le guste a Yuri..."
    "Si me apresuro, llegaré antes de que cierren."
    
    stop music fadeout 1.5
    show black 
    with dissolve_scene_full

    "Un poco agotado y con algunas gotas de sudor, tomo aire antes de entrar a la biblioteca."
    
    scene bg library_aft
    with dissolve_scene
    play music audio.heartbreaking2 fadein 2.0

    "Uff, aún sigue abierta."
    "El silencio de la biblioteca siempre me tranquiliza."
    "A lo lejos veo a un par de estudiantes leyendo unos cuantos libros y a la bibliotecaria hablando con un señor mayor."
    "Parece querer llevarse un libro sobre cocina."
    "Como sea..."
    "Saliendo de mi trance, empiezo mi búsqueda de libros que podrían interesarle a Yuri."

    "Agarro varios libros que parecen de terror y reflexivos."

    "Espero no estarme guiando por una apariencia..."

    "La llamada de Cthulhu...{w} Muy complicado."

    "¿Books of Blood?{w} Suena como si fuera escrito por un adolescente edgy."

    "El hombre de arena.{w} ¿Ese no era un enemigo de un superhéroe?"

    "¿Exit Music: Redux?{w} Me suena de algo..."

    show silueta zorder 2 at f11

    "Chico Friki" "Con permiso."

    show silueta zorder 2 at t11

    "El tipo me arrebató el libro de la mano."

    show silueta zorder 2 at f11

    "Chico Friki" "Por favor, dime que no lo vas a comprar... Hace tiempo que lo he estado buscando, es muy bueno."

    show silueta zorder 2 at t11

    mc "Eh... Sí, está bien. ¿Lo entiendo?"

    show silueta zorder 2 at thide
    hide silueta

    "Caminé al siguiente pasillo. Iba a agarrar otro libro pero sentí cómo alguien me dio un pequeño empujón."

    "Me volteé rápidamente."

    show monika 1 zorder 2 at t11

    mc "Ah... Eres tú."

    show monika forward neut n2 mg e1a b2b zorder 2 at f11

    m "Perdona, no quería asustarte."

    show monika forward neut n1 ma e1a b2b zorder 2 at t11

    "Por un momento sentí que me había congelado."

    mc "No te preocupes... ¿Y qué haces por aquí?"

    show monika forward lpoint happ om oe zorder 2 at f11
    
    m "Busco algunas partituras de piano. Últimamente he intentado aprender a tocar el piano."

    show monika forward lpoint happ cm oe zorder 2 at t11

    mc "Oh, eso suena genial."

    show monika forward lpoint happ om ce zorder 2 at f11
    
    m "Ya que respondí, es mi turno de preguntar. ¿Qué hace [player] aquí?"

    show monika forward lpoint happ cm ce zorder 2 at t11

    "¿Qué estaba haciendo?{w} Ahh, sí."

    mc "Estaba buscando algo, ya sabes... como me uní al club quería estar más al tanto."

    show monika forward lpoint happ om oe zorder 2 at f11

    m "Ya veo. ¿Te gusta el terror, no?"

    show monika forward lpoint happ cm oe zorder 2 at f11

    mc "Algo así..."

    show monika lean m3 e4 b1 zorder 2 at f11
    
    m "Déjame adivinar, quieres impresionar a alguien inspirándote en un libro, ¿cierto?"

    show monika lean m1 e4 b1 zorder 2 at t11

    mc "Eh..."

    show monika lean m3 e1 b1 zorder 2 at f11
    
    m "Jeh, no fue tan difícil leerte."

    m "Entonces pien-..."

    show monika lean m1 e1 b1 zorder 2 at thide
    hide monika
    show yuri shy neut cm oe zorder 2 at t33
    "Monika me estuvo hablando. Sin embargo, vi a alguien a lo lejos: una chica de cabello morado."

    show yuri shy neut cm oe zorder 2 at thide
    hide yuri

    show monika forward curi om oe zorder 2 at f11
    
    m "[player]"

    mc "Esa chica... ¿es Yuri?"
    show monika forward curi om oe zorder 2 at thide
    hide monika 
    show yuri turned anno om oe zorder 2 at t11

    "Monika se volteó, y efectivamente era Yuri con un par de libros."

    mc "Y ahora entrará Sayori."

    "Mencioné con una sonrisa, intentando hacer un chiste."
    
    "Monika no reaccionó ante mi intento de chiste."
    show yuri turned anno om oe zorder 2 at t11
    hide yuri 
    show monika forward anno cm oe zorder 2 at t11
    menu hablar_yuri:
        "Ir hablar con Yuri":
            $ decision_biblioteca = "Yuri"
            $ puntos_ruta += 1
            "Que raro encontrar a Yuri aqui"
            "No creo que Monika se tome esto personal, ¿verdad?"
            mc "Monika, disculpa tengo que irme"
            "Antes de que pueda darme una respuesta trato de alejarme pero me agarra de la camisa"
            m forward dist om oe "Espera"
            m "¿Iras hablar con Yuri verdad?"
            mc "Lo siento, Monika"
            m forward flus om oe "Esta bien no pasa nada..."
            mc "Nos vemos mañana, Monika"
            m "Adios [player]"
            show monika forward flus om oe zorder 2 at thide
            hide monika 
            jump hablar_yuri_biblioteca
        "Quedarse con Monika":
            $ decision_biblioteca = "Monika"
            $ puntos_ruta -= 1
            "Seria muy grosero de mi parte dejar a Monika"
            jump no_hablar_yuri_biblioteca
    
    label noche_poem1:
    scene bg bedroom
    with dissolve_scene_full
    "Saco los libros de mi mochila y los apilo cerca de mi escritorio."
    "Ver la pila de libros me hace sentir abatido."
    "Con papel y lápiz en mano, suspiro."
    mc "Me espera una laaarga noche."
    stop music fadeout 2.0

    # Al siguiente día
    # Día 2
    label dia2:
    scene bg club_day
    with dissolve_scene_full

    play music audio.t6 
    show monika lean happ om oe zorder 2 at f11 
    m "Hola, [player]."
    m "Me alegra saber que no escapaste."
    show monika lean happ cm oe zorder 2 at t11

    mc "Soy alguien de palabra, ¿qué puedo decir?"
    show monika lean zorder 2 at thide
    hide monika 

    "¿Llegué tarde? Parece que las demás chicas ya llevaban un rato en el club."
    show yuri turned lup rup happ om ce zorder 2 at f11
    
    y "Sabía que cumplirías con tu promesa, [player]."
    y "Espero que no te agobie leer libros, sé cómo se siente cuando no estás acostumbrado."
    show yuri turned lup rup doub cm ce zorder 2 at t21
    show natsuki cross neut om oe zorder 2 at f22
    n "No le tengas piedad. Sayori me dijo que aceptaste venir cuando mencionó los pastelitos."

    show natsuki cross doub om oe zorder 2 at f22
    n "Así que tómate esto en serio. Si tienes hambre, en el piso de abajo está el club de cocina."
    show natsuki cross doub cm oe zorder 2 at t22

    show yuri turned flus cm oe zorder 2 at f21
    y "Disculpa, Natsuki, estaba hablando con [player]..."
    show yuri turned flus cm oe zorder 2 at t21

    show natsuki cross angr om ce zorder 2 at f22 
    n "Oye, solo quiero que nos tome en serio, no permitiré que arruine nuestro club."
    show yuri turned happ cm oe zorder 2 at t31
    show natsuki cross angr om ce zorder 2 at t32
    show monika lean happ om oe zorder 2 at f33 
    m "¿No es un poco difícil hablar así para alguien que tiene una colección completa de manga en el salón?"
    show monika lean happ om oe zorder 2 at t33 

    show natsuki n3 turned shoc om oe zorder 2 at f11
    n "¡¡MON-MAN-MON-MAN!!"
    show natsuki n3 turned shoc om oe zorder 2 at t11

    "Natsuki se quedó atascada intentando decir Monika o manga."
    show natsuki turned shoc om ce zorder 2 at f32
    n "El manga es literatura."
    show natsuki turned shoc om ce zorder 2 at thide
    hide natsuki

    "Natsuki se giró y entró al clóset del salón."
    show monika forward happ cm oe zorder 2 at thide
    hide monika


    if decision_sayori == "insistir":
        
        show yuri turned flus cm oe zorder 2 at t22
    
        show sayori turned happ om ce zorder 2 at f21
        s "Tranquilas, chicas. [player] siempre apoya cuando algo le interesa... o le piden ayuda, jeje..."
        show sayori turned happ om oe zorder 2 at t21

        "Como ordenar tu cuarto."

        show yuri lup rup happ om ce zorder 2 at f22
        y "Qué considerado."
        show yuri lup rup happ cm ce zorder 2 at t22

        mc "Cómo me gustaría decir que no es difícil... como salvar una casa a punto de incendiarse."
        show sayori ml e4c b1c zorder 2 at f21
        s "¡Eso jamás pasó!"
        show sayori mk e4c b1c zorder 2 at t21

        mc "¿Entonces lo estoy inventando?"

        show sayori tap pout om oe zorder 2 at f21
        s "Ush, sí que eres malvado..."
        show sayori tap pout cm oe zorder 2 at t21

        show yuri turned ldown happ om oe zorder 2 at f22
        y "¿Son muy buenos amigos, no?"

        y "Quizás esté un poco celosa."

        show sayori turned happ om oe zorder 2 at f21
        s "¿Celosa? ¡Pero tú y [player] también pueden ser buenos amigos!"
        show sayori turned happ cm oe zorder 2 at t21

        show yuri turned flus cm oe zorder 2 at f22
        y "U-uhm..."
        show yuri turned flus cm oe zorder 2 at t22

        mc "Sayori..."

        show sayori turned happ om oe zorder 2 at f21

        s "¿Sí?"

        s "Ah, por cierto, Yuri te trajo un regalo."
        show sayori turned happ cm oe zorder 2 at t21

        show yuri turned lup pani om oe zorder 2 at f22
        y "N-no es importante."

        show yuri shy neut om oe zorder 2 at f22
        y "Pe-pero si prefieres no aceptar mi regalo, está bien..."
        show yuri shy neut cm oe zorder 2 at t22

        "¿Un regalo? Ni siquiera en un sueño me imaginaría esto."
        
        mc "Oye, es una gran sorpresa. No pensaba que iba a recibir algo."

        mc "Y cualquier cosa es bienvenida."

        show yuri shy happ om oe zorder 2 at t22
        y "..."
        show yuri shy happ om oe zorder 2 at thide
        hide yuri

        "Yuri caminó hacia su asiento buscando algo en su escritorio."

        show sayori turned happ om ce zorder 2 at f21
        s "[player], estoy segura de que te gustará, jeje..."
        show sayori turned happ cm oe zorder 2 at t21

        "¿Seguimos hablando del regalo?"
        show sayori turned happ om ce zorder 2 at thide
        hide sayori

        "Yuri regresó con un libro en la mano."
        show yuri shy happ cm oe zorder 2 at f11

        y "Quería regalarte un libro... Pensé que te gustaría ya que eres nuevo."

        show yuri shy neut om oe zorder 2 at f11
        
        y "Y en cualquier momento..."

        y "O cuando termines..."
        
        y "Podríamos..."

        show yuri shy neut n5 zorder 2 at f11
        y "Compartir opiniones."
        show yuri shy neut cm oe zorder 2 at t11

        mc "¡Muchas gracias, Yuri! Realmente no sé mucho de literatura, pero lo leeré."
        show yuri turned lsur om ce zorder 2 at t11
        "Agarré el libro y Yuri se relajó."

        show yuri turned happ om ce zorder 2 at f11
        s "Estoy emocionada de saber qué opinas."
        show yuri turned happ cm oe zorder 2 at t11
        mc "No puedo esperar a empezar a leerlo."
        mc "De nuevo, muchas gracias, Yuri."
        show yuri turned happ om ce zorder 2 at thide
        hide yuri
    elif decision_sayori == "Sayori":
        show yuri turned n3 flus cm oe zorder 2 at t11
        y "D-Disculpa [player] tienes un segundo"

        "Que extraño Yuri parece esconder algo tras su espalda, parece un poco nerviosa"

        mc "Hola Yuri, por supuesto"

        show yuri turned n2 flus cm oe zorder 2 at t11

        "Una pequeña gota de sudor cae por el rostro de Yuri"

        "Parece estar atrapada en decirme algo o no"

        "Sera mejor que salve un poco la situación, quisiera saber que quiere decirme"

        mc "Yuri hay algo que quieras decir-"

        show yuri shy neut om oe zorder 2 at f11

        y "T-T-Toma [player] es para ti, eres nuevo en el mundo de la literatura y creí que este libro seria una buena introducción"

        show yuri shy neut cm oe zorder 2 at t11
        "Sin mirarme a los ojos, Yuri saca un libro de detrás de su espalda que lleva un gran ojo en el centro de la portada."

        "Me cuesta tener una reacción que pueda tranquilizar a Yuri"

        "Ver el ojo de la portada me estremece un poco pero es más que interesante"

        show yuri shy neut om oe zorder 2 at f11

        y "Es un gran libro, uno de mis favoritos, cuando menos te lo esperes estarás sumergido entre sus paginas"

        show yuri shy neut om oe zorder 2 at t11
        mc "Muchas gracias Yuri, aprecio mucho este gesto"

        mc "Es muy amable de tu parte el escoger un libro para mi, no debiste tomarte la molestia"

        show yuri turned n2 shoc cm ce zorder 2 at s11

        "Al escuchar mis palabras Yuri parece tranquilizarse y recupera su postura"

        show yuri turned sedu cm oe zorder 2 at t11

        "Yuri me entrega el libro"

        "'El retrato de Markov' un libro de tapa dura y de color rojo sangre"

        "Parece algún tipo de edición de coleccionista"

        mc "No puedo esperar a comenzar a leerlo"

        mc "De nuevo muchas gracias Yuri"

        show yuri turned n1 happ om ce zorder 2 at f11

        y "Espero lo disfrutes, es un libro fantástico"



        y turned happ om oe "[player] quisiera pedirte una cosa más"

        show yuri turned n1 happ om ce zorder 2 at t11

        mc "por supuesto Yuri, soy todo oídos"

        show yuri turned n1 happ om ce zorder 2 at f11

        y "Una vez que termines el libro me gustaría que discutiéramos sobre el"

        y turned happ cm ce "Estoy esperando escuchar tu opinión sobre el libro"

        "Yuri parece muy emocionada de compartir este libro conmigo debo corresponder de igual manera"

        show yuri turned happ cm ce zorder 2 at t11
        mc "Me encantaría si, tenme un poco de paciencia a la hora de discutirlo, suelo ser un poco tonto con los mensajes ocultos que dejan los autores"

        show yuri turned happ om ce zorder 2 at f11
        y turned happ om ce "Ni más faltaba, si tienes problemas con algún hilo de la historia no dudes en contarme"

        show yuri turned happ om ce zorder 2 at t11
        mc "Dalo por hecho"

        show yuri turned happ om ce zorder 2 at thide
        hide yuri 


        "Regreso a mi escritorio y guardo el libro en mi mochila"
    elif decision_sayori == "no ir":
        show yuri turned n3 flus cm oe zorder 2 at f11
        "D-Disculpa [player], ¿tienes un segundo?"
        "Qué extraño. Yuri parece esconder algo tras su espalda, se nota un poco nerviosa"
        mc "Hola, Yuri. Por supuesto"
        "Una pequeña gota de sudor cae por el rostro de Yuri"
        "Parece estar atrapada entre decirme algo o no"
        "Será mejor que salve un poco la situación, quisiera saber qué quiere decirme"
        mc "Yuri, ¿hay algo que quieras decir—?"
        show yuri shy neut om oe zorder 2 at f11
        y "T-T-Toma, [player], es para ti. Eres nuevo en el mundo de la literatura y creí que este libro sería una buena introducción"
        show yuri shy neut cm oe zorder 2 at t11
        "Sin mirarme a los ojos, Yuri saca de su espalda un libro con un gran ojo en el centro de la portada."
        "Me cuesta tener una reacción que pueda tranquilizar a Yuri"
        "Ver el ojo de la portada me estremece un poco, pero es más que interesante"
        show yuri shy neut om oe zorder 2 at f11
        y "Es un gran libro, uno de mis favoritos. Cuando menos te lo esperes, estarás sumergido entre sus páginas"
        show yuri shy neut om oe zorder 2 at t11
        mc "Muchas gracias, Yuri. Aprecio mucho este gesto"
        mc "Es muy amable de tu parte el escoger un libro para mí, no debiste tomarte la molestia"
        show yuri turned n2 shoc cm ce zorder 2 at s11
        "Al escuchar mis palabras, Yuri parece tranquilizarse y recupera su postura"
        "Yuri me entrega el libro"
        "'El retrato de Markov', un libro de tapa dura y de color rojo sangre"
        "Parece algún tipo de edición de coleccionista"
        mc "No puedo esperar a comenzar a leerlo"
        mc "De nuevo, muchas gracias, Yuri"
        show yuri turned n1 happ om ce zorder 2 at f11
        y "Espero que lo disfrutes, es un libro fantástico"



        y turned happ om oe "[player], quisiera pedirte una cosa más"

        y "Podríamos—{nw}"
        show yuri turned pani om oe zorder 2 at h43
        show monika forward lpoint happ om oe zorder 2 at f41
        m "[player], ¿podría hablar contigo un momento?"
        "Yuri suelta un pequeño grito ahogado ante la aparición de Monika"
        m "Necesito que firmes tu formulario de inscripción al club"
        m ldown forward pout cm oe "Disculpen, ¿interrumpo algo?"
        show monika ldown forward pout cm oe zorder 2 at t41
        show yuri turned n2 pani om oe zorder 2 at f43
        y turned n2 pani om oe "P-Por supuesto que no, Monika. [player] y yo no hablábamos de nada importante"
        y "Es importante que [player] complete su inscripción al club"
        show yuri turned n2 pani om oe zorder 2 at t43
        mc "Pero, Yuri—"
        show yuri turned n2 pani om oe zorder 2 at thide
        hide yuri
        "Antes de pedirle que continúe, Yuri huye hacia un escritorio que está en la otra punta del salón y hunde su rostro en un libro"
        show monika forward n2 worr om oe zorder 2 at f11
        m "Oh, creo que sí vine en un mal momento"
        show monika forward n2 worr om oe zorder 2 at t11
        mc "No te preocupes, Monika. Cualquier cosa que quería decirme Yuri puede decírmelo después"
        mc "¿Debo rellenar algún papel para la inscripción?"
        show monika forward n1 lpoint happ om oe zorder 2 at f11
        m forward n1 lpoint happ om oe "Oh, sí, por supuesto. Tengo los papeles en mi escritorio, ven conmigo"
        "Monika saca unos cuantos papeles de su mochila y me los entrega"
        m "Por favor, rellena todo esto cuando puedas y entregámelos para concluir tu inscripción lo más pronto posible"
        show monika forward n1 lpoint happ om oe zorder 2 at t11
        mc "Los rellenaré enseguida"
        show monika forward lpoint happ om oe zorder 2 at thide
        hide monika
        "Camino hacia mi escritorio"
        "Me pregunto qué fue lo último que Yuri quería decirme, supongo que le preguntaré luego"
        "Reviso mi mochila, saco un lápiz y empiezo a rellenar los papeles que me entregó Monika"

    scene bg club_day
    with wipeleft_scene
    
    "Llevo un tiempo sentado sin hablarle a nadie."

    "Aunque quiero hablarle a Yuri, no quiero incomodarla... Está muy centrada en su libro."

    "¿Qué estará leyendo?"

    "Me centré en su libro; es muy parecido al que me regaló."
    show yuri turned pani om oe zorder 2 at h11
    y "Uh-ah..."
    show yuri turned flus cm oe zorder 2 at s11
    "Yuri notó mi mirada. Cuando me miró a los ojos, inmediatamente escondió su rostro bajo el libro."

    "Tal vez debería pedirle disculpas."

    mc "Perdona, solo estaba interesado en el libro."

    mc "De qué trata, si no te molesta que te pregunte."

    show yuri turned flus om oe zorder 2 at f11
    y "N-no te preocupes."
    show yuri turned flus om oe zorder 2 at s11
    y "Fuh... El libro básicamente trata sobre una mujer y su marido encerrados en un campamento."

    show yuri turned lsur om ce zorder 2 at f11
    y "Son torturados y custodiados, por lo que hacen un plan para escapar. Al tratar de escapar son descubiertos y, como castigo..."

    y "Ordenaron al marido ver cómo su esposa era colgada mientras poco a poco su cadáver inerte se palidecía cada vez más sumida en la desesperación."

    y "El marido fue confinado en un lugar donde la luz del sol era nula."

    y "Poco a poco, el hombre sucumbía ante la locura."

    y "Mantenía alucinaciones sobre la muerte de su esposa, su desesperación por la falta de aire, el dolor de la soga en su cuello..."

    y "El hombre se ahorcaba con sus propias manos tratando de buscar la misma sensación que sintió su esposa."

    y "La soledad, acompañada de una eterna oscuridad, era el martirio de aquel hombre que luchaba por mantener su cordura."

    show yuri turned lsur cm ce zorder 2 at t11

    "Aunque la voz de Yuri ayuda a que no suene tan mal... es una historia muy oscura."

    "Yuri, al ver mi rostro, parece haber vuelto a la realidad."

    show yuri turned nerv om oe zorder 2 at f11

    y "L-lo siento, empecé a divagar. Seguro piensas que soy rara por leer este tipo de libros."

    y "Ni siquiera estás acostumbrado a leer muchos libros y... {nw}"

    mc "No tienes de qué preocuparte, Yuri. No tienes que esconder la pasión que tienes por la lectura."

    mc "Después de todo, estamos en el club de literatura; además, no me molesta en absoluto escucharte hablar."

    mc "Por favor, continúa."

    y turned sad om oe "Uh-Ah, suelo leer historias un tanto diferentes. Me gustan porque puedes ver la vida desde otro punto de vista."

    y "No siempre todo final malo es... malo {w}; algunos te hacen reflexionar y aprendes tantas cosas de los personajes sin tener que decirlas directamente."

    show yuri turned nerv om oe zorder 2 at h11

    y "¡Perdón! Volvi a empezar a hablar de más."

    mc "No, está bien. Si hablas mucho de algo es porque te interesa, ¿cierto?"

    mc "Además... suena interesante. Podríamos leerlo."

    y turned laug om oe "Bue-bueno."

    mc "Tu libro se parece al que me regalaste, ¿son del mismo autor?"

    y "En realidad, es el mismo libro."

    mc "Oh, entonces eso hace más fácil que podamos leerlo."

    show yuri turned laug om oe zorder 2 at thide
    hide yuri

    "Saqué el libro de mi mochila y comencé a leerlo a la par de Yuri."

    show yuri shy m1 e3 b1 zorder 2 at t11

    "Mientras leía el libro, podía ver de reojo cómo Yuri me estaba mirando."
    show yuri shy m4 e3 b1 zorder 2 at h11
    y "Lo-lo siento."

    mc "¿Yuri, no crees que te disculpas demasiado? No has hecho nada malo."

    show yuri turned rup flus cm oe zorder 2 at h11

    y "¿Lo hago? Perdón... ¡N-NO, quiero decir!-"

    mc "Quizás así ambos podemos leer mejor."

    "Deslicé mi pupitre hasta juntarlo con el de Yuri y agarré mi libro para sostenerlo de un lado."

    "Yuri se inclinó un poco para sostener el libro con su mano izquierda."

    show yuri turned rup flus cm oe zorder 2 at thide
    hide yuri
    pause 0.8
    scene y_cg1_base
    show y_cg1_exp1

    mc "Aunque no había pensado en cómo cambiaremos de página."

    mc "¿Lees rápido?"

    y "Uh... suelo leer con calma..."
    hide y_cg1_exp1 with dissolve 

    "Me quedé en silencio cuando sentí el hombro de Yuri. Estamos más cerca que antes."

    "Intenté concentrarme en leer."

    # Probablemente poner libro

    with dissolve_scene_full

    show y_cg1_exp1 with dissolve 

    y "¿Listo?"
    
    "Yuri dejó de leer el libro para mirarme."

    mc "Ah... en realidad no he terminado aún."

    y "¿No sueles leer mucho, cierto?"
    show y_cg1_exp2 with dissolve 
    y "Puedo ser paciente contigo. Mostraste interés en la historia, así que es lo mínimo que puedo hacer."

    mc "S-sí."

    mc "Muchas gracias, Yuri."
    hide y_cg1_exp2 with dissolve 
    hide y_cg1_exp1 with dissolve 

    "Creo que Yuri ya había terminado antes de que yo acabara la primera página."

    with wipeleft_scene

    "Terminé el capítulo. Intuyo que Yuri también, así que intento pasar de página."

    "Cuando intento mover la hoja, Yuri me ayuda con su mano izquierda."

    mc "¿Sabes? El personaje principal me recuerda a ti."
    show y_cg1_exp1 with dissolve
    y "¿En serio?"

    mc "Bueno... por lo menos en algunos gestos que sueles hacer."
    show y_cg1_exp3 with dissolve
    y "Y-ya v-veo."
    hide y_cg1_exp3 with dissolve
    hide y_cg1_exp1 with dissolve 
    "Yuri se mantuvo en silencio, parece pensar en algo."
    scene bg club_day 
    with dissolve
    show yuri shy happ om oe zorder 2 at h11
    y "Que digas eso... ¡Es muy malo que me parezca a él!"

    "Yuri jugó con uno de sus mechones. Creo que le dije algo que la avergonzó."

    mc "¡N-no intentaba decir algo malo!"

    "Perfecto, arruiné todo en una línea."

    mc "No intentaba decirlo de manera negativa sino... como algo... algo lindo."

    y shy n3 m3 e1 b1 "¿Lin-lindo?"
    stop music fadeout 1.5

    y "Yo..."
    show monika forward lpoint happ om oe zorder 2 at t32
    show yuri turned pani om oe zorder 2 at h31

    m "Okay, todo el mundo."

    y "..!"
    play music audio.t8
    m "Ya es hora de compartir nuestros poemas. Si esperamos más, quizás no tengamos tiempo de comentarlos."

    show yuri turned lsur om ce zorder 2 at s31

    y "Sí, por supuesto..."

    m forward neut om oe "¿Te encuentras bien, Yuri?"

    m "Pareces decepcionada."
    show yuri turned pani om oe zorder 2 at h31
    y "No... todo bien."
    m forward lpoint happ om oe "Ok, todo el mundo empieza la ronda de compartir poemas."
    show monika neut om oe zorder 2 at thide 
    pause 1.2
    hide monika 
    "Juraría que Monika me estaba mirando mal antes de irse."

    show yuri turned lsur om ce zorder 5 at s11
    "Yuri suelta el libro."

    mc "¿Continuamos mañana?"

    y turned n1 happ cm oe "Está bien, aunque también podrías avanzar un poco en casa. También me gustaría que disfrutes del libro y podamos compartir opiniones sobre él."

    mc "Mhmmm, ¿qué tal si lo avanzo en casa y continuamos leyendo juntos por donde lo deje mañana?"

    y turned happ om ce "Me parece una magnífica idea."

    mc "Hecho."

    show yuri turned happ cm oe zorder 2 at thide
    hide yuri

    "Me levanté para meter el libro dentro de mi mochila."

    with wiperight_scene
    show monika forward rhip happ om oe zorder 2 at t11
    m "[player], ¿escribiste el poema?"
    mc "Fue más difícil de lo que me esperaba, pero sí."
    m "No puedo esperar a leer lo que escribiste."
    mc "No tengas tantas expectativas, jeje."
    m "Vamos, ten un poco más de confianza en ti mismo."
    mc "Jejeje... seguro."
    show monika forward rhip happ om oe zorder 2 at thide
    hide monika
    with wipeleft
    pause 0.8
    show sayori turned happ cm oe zorder 2 at t11
    "Hasta ahora no había pensado en lo vergonzoso que es esto. Seguramente la única crítica constructiva que reciba sea de Sayori."
    show sayori turned happ cm oe zorder 2 at t21
    show natsuki cross neut om oe zorder 2 at t22
    "Estoy seguro de que Natsuki aplastará mi poema."
    show sayori turned happ cm oe zorder 2 at t31
    show natsuki cross neut om oe zorder 2 at t33
    show monika forward dist om oe zorder 2 at t32
    "Monika tratará de ser comprensiva, pero sabré cuándo esté mintiendo."
    show sayori turned happ cm oe zorder 2 at t41
    show monika forward dist om oe zorder 2 at t43
    show natsuki cross neut om oe zorder 2 at t44
    show yuri turned neut cm oe zorder 2 at t42
    "Y Yuri... {w} Es la que más me tiene ansioso. Cómo reaccionará al ver mi poema."
    show sayori turned happ cm oe zorder 2 at thide
    show monika forward dist om oe zorder 2 at thide
    show natsuki cross neut om oe zorder 2 at thide
    show yuri turned neut cm oe zorder 2 at thide
    hide monika 
    hide yuri 
    hide natsuki 
    hide sayori 
    "¡AAAAAAAAAH! Me va a explotar la cabeza."
    stop audio fadeout 2.0
    "Cálmate, [player], puedes con esto."
    "Solo debes mostrar tu poema con una sonrisa y escuchar con atención a las chicas."
    play music audio.t5
    
    if decision_biblioteca == "Yuri":
        show monika forward lpoint happ cm oe zorder 2 at t11
        m "Bueno, ya que eres nuevo en el club, eliges tú primero con quién compartir."
        m lean "Quizás pueda ser yo."
        show sayori turned happ om oe zorder 2 at t41 
        s "¡Monikaaa! ¿Quieres leer mi poema?"
        show monika forward happ om ce zorder 2 at f11
        m "Ah... por supuesto, Sayori."
        show monika forward happ om ce zorder 2 at thide
        show sayori turned happ om oe zorder 2 at thide
        hide monika 
        hide sayori 
        "Gracias, Sayori. Con el camino despejado..."
    elif decision_biblioteca == "Monika":
        show monika lean zorder 2 at t11
        m "[player] Te gustaría compartir tu poema conmigo?"

        "Monika me sonrie como es de costumbre"
        "Asiento, sacando el poema de mi mochila."
        jump mostrar_poema_monika

    "¿Debería enseñarle mi poema primero a Yuri?"
    menu poema_yuri1:
        "Mostrar mi poema a Yuri":
            "Sí, debería ir con Yuri."
            jump mostrar_poema_yuri
        "Quizás no":
            "Tal vez podría mostrárselo luego."
            $ puntos_ruta += 0
            jump mostrar_poema_natsukis

    with dissolve_scene_full 
    label mostrar_poema_yuri:
        play music audio.t5
        "Con poema en mano, me acerqué a Yuri."
        show yuri turned mf e1d b1c zorder 2 at t11

        mc "¿Te gustaría compartir poemas?"
        show yuri turned n2 flus cm oe zorder 2 at t11
        y "P-por supuesto."

        mc "Sinceramente, me da vergüenza compartir un poema."

        y turned rup anno om oe "A-a mí también. Nunca había hecho algo parecido."

        mc "Si quieres, puedo empezar."

        y turned neut om oe "¿En serio?"

        y "N-no tienes por-{nw}"

        mc "No, no te preocupes, quiero hacerlo."
        show yuri turned n1 lsur om ce zorder 2 at s11
        y "Gracias."

        mc "Por cierto, dime si no entiendes mi letra..."

        "Yuri no mencionó nada, tomó mi poema y empezó a leerlo detenidamente."
        $ poem_db.show_poem("poem_mc1")
        # Poner poema de MC
        show yuri turned happ om oe zorder 2 at h11
        y "Tu grafía es excelente y el poema es increíble."

        mc "Vamos, puedes ser sincera. Es mi primera vez, después de todo."

        y turned happ om ce "Lo digo en serio. De hecho, no esperaba que lo hicieras tan bien."

        y turned laug cm oe "Es como si hubiera sido creado para mí: el ambiente, el tono, la prosa... Me recuerda tanto a mis poemas."
        show yuri turned n2 ml e1b b2a zorder 2 at s11
        y "..."
        show yuri turned n2 nerv om oe zorder 2 at h11
        y "N-no intento decir que el poema va dirigido a mí... s-solo que me gustó mucho."

        mc "Bueno, quizás tengamos algo en común."
        show yuri turned flus cm oe zorder 2 at s11
        y "Uuuh..."

        y turned n1 lsur om oe "Una pregunta, ¿alguna vez has escrito otros poemas?"

        y "A lo que me refiero es que la estructura de las rimas y la profundidad de las metáforas no reflejan el trabajo de un principiante."

        mc "Muchas gracias por todos los halagos, significan mucho para mí viniendo de ti. Pero no..."
    
        mc "Es mi primera vez escribiendo poesia."
        mc "Digamos que estuve en eso toda la noche."
        mc "No quería decepcionarlas."
        y turned happ cm ce "Valió la pena todo el esfuerzo, es un gran poema."
        y turned n2 flus om oe "Supongo que es mi turno..."

        show yuri turned n2 flus om oe zorder 2 at thide
        hide yuri

        "Yuri busca el poema entre las páginas."

        show yuri turned lup rup worr om oe zorder 2 at s11

        "Yuri, dudando, me pasó un cuaderno de notas. Al mirarlo, noto que hay otros poemas y no puedo evitar sentir curiosidad al verlos."

        $ poem_db.show_poem("poem_mlb_yuri")

        show yuri turned shoc om oe zorder 2 at h11
    
        y "¡¡Disculpa por la letra!! Es horrible."

        mc "¿Horrible? Para mí es linda. Parece que sí tenemos algo en común después de todo: ambos escribimos en cursiva."

        y "Oh... entonces, ¿por qué lo leíste tanto tiempo?"

        mc "Porque me gusta tu caligrafía y el poema esconde un mensaje."
        mc "Tuve que leerlo un par de veces para entenderlo del todo."

        show yuri turned n1 shoc cm ce zorder 2 at s11
 
        "Yuri suspiró."

        y turned sad om oe "¿No es muy corto?"

        mc "No, de hecho creo que fue la manera perfecta de transmitir el mensaje."

        y turned ldown neut om oe "Usualmente los suelo hacer más largos..."

        mc "Oye, el tamaño no importa, ¿verdad?"

        "¿Verdad?"

        y turned happ om ce "Me siento más confiada al saber que te gustó."

        y turned laug om oe "Y... mañana haré uno largo. En mi cuaderno también tengo algunos poemas."

        mc "Pude darme cuenta mientras buscabas tu poema."
        show yuri turned pani om oe zorder 2 at h11
        y "¿¡Y-y l-los leiste!?"

        # Añadir diálogo sobre lo que trate el poema, todavía no decidido
    
        mc "No, tranquila, solo leí el que me entregaste."
        show yuri turned n2 flus cm oe zorder 2 at t11
        mc "Pero seguramente son igual de buenos como el que me enseñaste."

        "Yuri con timidez buscaría una página específica."
        $ poem_db.show_poem("poem_borr_yuri1")
        # Añadir poema-borrador

        mc "Vaya... sí que tengo mucho que aprender para poder escribir así."
        show yuri turned n1 flus cm oe zorder 2 at f11
        y "¿A qu-qué te refieres?"

        mc "Eh, elegí mostrarte mi poema primero porque siento que eres muy buena en la creación de poemas."

        mc "Y porque no me dirás solo \"es muy bueno\" como cualquiera del club."
        show yuri turned n3 laug cm oe zorder 2 at t11
        "Noté que Yuri me miró avergonzada."

        mc "Pero en fin... me gustaría aprender de ti."

        y turned laug cm oe "¿En serio piensas eso?"

        mc "Estoy seguro de que las demás también."
        show yuri turned rup lup lsur om oe zorder 2 at s11
        y "Uh..."

        y turned ldown laug cm oe "Sentía muchos nervios de hacer esto."

        y turned laug rdown cm ce "Pero lo estoy disfrutando por ti."

        y "Quiero hacerlo lo mejor posible por ti, [player]."

        mc "Ah..."

        mc "Yo también..."

        y turned n1 happ cm oe "Cuento contigo."

        mc "Vale, contigo ayudándome a mejorar, puedo con todo."

        show yuri turned rdown happ cm oe zorder 2 at thide
        hide yuri

    with dissolve_scene_full
    play music audio.t5
    "Parece que terminé de compartir mi poema con las chicas."
    "Cada poema tuvo distintos significados, y todos bastante interesantes."
    show sayori turned happ cm oe zorder 2 at t11
    "\"Querido sol\"... No creo que la mancha de chocolate caliente en la hoja sea una representación de los sentimientos."
    show sayori turned happ cm oe zorder 2 at t21
    show natsuki turned neut cm oe zorder 2 at t22
    "El poema de Natsuki tuvo una moraleja que no me esperaba: puedes tratar y tratar, pero no significa que lo lograrás. Me esperaba algo diferente..."
    show sayori turned happ cm oe zorder 2 at t31
    show monika forward lpoint happ cm oe zorder 2 at t32
    show natsuki turned neut cm oe zorder 2 at t33
    "Y al final, con Monika."

    "\"Hoyo en la pared\"."

    "Aunque lo leí tres veces, no entendí nada. ¿Una epifanía? No sabía que existía esa palabra."

    "Por un momento sentí como si Monika solo siguiera hablándome por compromiso."

    "Fue más estresante de lo que creía. Por lo menos me llevé consejos, aunque era imposible superar los de ellas."

    "Soy nuevo, después de todo."
    show sayori turned happ cm oe zorder 2 at thide
    show monika forward lpoint happ cm oe zorder 2 at thide
    show natsuki turned neut cm oe zorder 2 at thide
    hide sayori    
    hide monika 
    hide natsuki 
    pause 1

    "Las chicas aún siguen intercambiando poemas."
    stop music fadeout 2.0
    "Parece que Sayori y Monika terminaron de compartir con todos."

    show yuri turned rup lup anno om oe zorder 2 at t21 
    show natsuki turned doub om oe zorder 2 at t22
    "Yuri y Natsuki parecen ser las únicas que faltan."

    "Centré mi mirada en Yuri."

    show yuri turned anno om oe zorder 2 at t21
    "Yuri parece todo lo contrario a Natsuki: tranquila, calmada y paciente."
    
    "Mientras que Natsuki es una bomba que en cualquier momento puede explotar."
    show natsuki turned pout om oe zorder 2 at t22
    n "(¿Cómo es que leyeron esto?)"

    "Natsuki sostiene el poema con una de sus manos."

    show natsuki turned rhip pout cm oe zorder 2 at f22
    n "Se podría decir que está bien."
    show natsuki turned rhip pout cm oe zorder 2 at t22

    show yuri turned neut om oe zorder 2 at f21
    y "Muchas gracias... El tuyo es... lindo."
    show natsuki lhip vang cm ce zorder 2 at t22
    play music audio.t7
    n "¿Lindo? ¡Estuviste leyéndolo tanto tiempo y el único comentario que se te ocurre es \"está lindo\"!"

    show natsuki turned vang om ce zorder 2 at f22
    n "En serio, ¿no pudiste comprender el obvio mensaje de que, por más que lo intentes, a veces no conseguirás lo que quieres?"
    show yuri turned anno om oe zorder 2 at f21
    show natsuki turned vang om ce zorder 2 at t22
    y "Disculpa, no creí que te ofendería... Intentaba hablar del lenguaje, no de que el poema sea infantil."
    show natsuki turned vang cm oe zorder 2 at f22
    show yuri turned anno om oe zorder 2 at t21
    n "¿¡Estás intentando vacilarme!?"
    show yuri turned doub om oe zorder 2 at f21
    show natsuki turned vang cm oe zorder 2 at t22
    y "Bueno, no fue malo. Sin embargo, puedo darte algunos consejos."
    show natsuki turned vang om oe zorder 2 at f22
    show yuri turned doub om oe zorder 2 at t21
    n "¿¡Consejos!?"

    n "¿¡Consejos de alguien a quien no le gustó mi poema!? ¡Nunca los aceptaría!"

    n "Y hay algunas personas a las que sí les gustó, como Sayori y Monika."
    show natsuki turned vang om oe zorder 2 at f22
    n "Y también a [player], así que déjame ser yo quien te dé conse-{nw}"
    show yuri turned vang om ce zorder 2 at f21
    show natsuki turned vang cm oe zorder 2 at t22
    y "No necesito tus consejos, Natsuki. He pasado años desarrollando mi propio estilo."

    y "Además, no pienso cambiarlo a menos que encuentre algo mucho mejor."
    show natsuki turned angr om oe zorder 2 at f22
    show yuri turned vang om ce zorder 2 at t21
    n "Vaya, no sabía que eras tan egocéntrica, Yu-{nw}"
    show yuri turned rup lup vang cm oe zorder 2 at f21
    show natsuki turned angr om oe zorder 2 at t22
    y "Y también a [player] le gustó mi poema, y él sí aceptó mis consejos."
    show natsuki turned angr om oe zorder 2 at f22
    show yuri turned rup lup vang cm oe zorder 2 at f21
    n "¡Wow! Cómo remarcaste a [player]... Creía que él era el único que trataba de impresionar a alguien, pero veo que tú también."

    y turned pani om oe "¡¡Y-yo no traté de decir eso!!{w} Lo que pasa es que estás celosa."

    show natsuki turned n3 shoc om oe zorder 2 at f22
    "Natsuki intentó hablar molesta, pero fue interrumpida por Sayori."
    show natsuki turned n3 shoc om oe zorder 2 at t33
    show yuri turned rup lup vang cm oe zorder 2 at t31
    show sayori turned flus om oe zorder 2 at t32

    s "Chicas, ¿está todo bien?"

    # Aquí hablan Nat y Yu
    show natsuki turned vang cm oe zorder 2 at f33
    show yuri turned rup lup vang cm oe zorder 2 at f31
    show sayori turned pani om oe zorder 2 at s32
    ny "¡NO TE METAS!"
    show sayori turned pani om oe zorder 2 at thide
    hide sayori 
    show yuri turned rup lup vang cm oe zorder 2 at f21
    show natsuki turned vang cm oe zorder 2 at t22
    y "¿Dijiste la única...?"

    show yuri turned rup lup vang cm oe zorder 2 at t21

    show natsuki turned vang cm ce zorder 2 at f22
    n "¡Hmpf!"

    "Natsuki colocó el poema en uno de los escritorios."

    "Para luego levantarse firmemente."
    show natsuki cross vang cm ce zorder 2 at f22
    show yuri turned rup lup vang cm oe zorder 2 at t21
    n "Por lo menos a mí no se me levantó el pecho inmediatamente cuando [player] entró al club."
    show yuri turned n3 pani om oe zorder 2 at h21
    show natsuki cross vang cm ce zorder 2 at t22
    y "¡N-n-natsuki!"
    show natsuki cross vang cm oe zorder 2 at t33
    show yuri turned n1 angr om oe zorder 2 at t32
    show monika forward rhip neut om oe zorder 2 at t31
    m "Natsuki, creo que no deberías de-{nw}"

    # Nat y Yuri
    show natsuki cross vang cm oe zorder 2 at f33
    show yuri turned pani om oe zorder 2 at f32
    show monika forward rhip neut om oe zorder 2 at t31
    
    ny "¡ESTO NO TE INCUMBE!"

    show natsuki cross vang cm oe zorder 2 at t22
    show yuri turned pani om oe zorder 2 at t21
    show monika forward rdown sad om oe zorder 2 at thide
    hide monika

    y turned angr om ce "Nunca haría algo tan v-vergonzoso... ¡como tratar de hacerlo todo tierno!"

    "Parece que esta pelea está escalando demasiado."

    "Tengo miedo de intervenir; no veo forma de parar este torbellino."

    "Como si el destino estuviera en mi contra, ambas chicas postran su mirada en mí."
    show yuri turned rdown flus cm oe zorder 2 at f21
    y "¡No le creas, [player]! ¡Natsuki me está haciendo quedar mal!"

    y "J-Jamás podría hacer eso."

    show natsuki turned vang om ce zorder 2 at t22
    show yuri turned n1 rdown flus cm oe zorder 2 at t21
    n "La única que intenta hacer quedar mal a otra persona eres tú, Yuri. Tú empezaste todo esto."

    n turned angr om oe "¿Verdad, [player]?"
    show natsuki turned vang om ce zorder 2 at f22
    show yuri turned rdown flus cm oe zorder 2 at f21
    # Ambas
    ny "¿¡Y bien!?"

    "..."

    "¿Cómo es que todo pasó tan rápido?"

    "¿Y por qué se dirigen a mí?"

    "¿Qué debería hacer?"

    menu decision_ruta:
        "Fingir que no escuchabas.":
            "Es mejor que evite todo este desastre."
            $ puntos_ruta -= 1
            jump ruta_bad_1
        "Apoyar a Yuri":
            "Natsuki no deberia reaccionar así"
            $ puntos_ruta += 1
            jump apoyar_yuripoem
    # Escena de transición 
    label final_discusion:
        play music audio.t5
        show monika forward lpoint happ om oe zorder 2 at f42
        show sayori turned happ cm oe zorder 2 at t43
        show yuri shy neut cm oe zorder 2 at t41
        show natsuki cross dist cm oe zorder 2 at t44
        m "¡Okay, todo el mundo! Ya es hora de irnos a casa. ¿Qué tal les pareció la actividad?"
        show monika forward lpoint happ cm oe zorder 2 at t42
        show sayori turned happ om oe zorder 2 at f43
        s "¡Me encantó!"
        show sayori turned happ cm oe zorder 2 at t43
        show yuri shy neut cm oe zorder 2 at s41
        y "..."
        show natsuki cross dist om oe zorder 2 at f44
        n "Entretenido, supongo."
        show natsuki cross dist cm oe zorder 2 at t44

        mc "Supongo que estuvo bien."

        show monika forward lpoint happ om oe zorder 2 at t42

        m "¡Muy bien!"

        m "Mañana traigan un poema diferente y así podremos aprender más de nosotros."

        show monika forward lpoint happ cm oe zorder 2 at t42

        show monika forward lpoint happ cm oe zorder 2 at thide
        show sayori turned happ cm oe zorder 2 at thide
        show yuri shy neut cm oe zorder 2 at thide
        show natsuki cross dist cm oe zorder 2 at thide
        hide sayori 
        hide monika 
        hide natsuki 
        hide yuri 

    "Es cierto, gracias a la actividad pude saber qué tipo de poemas le gustan a cada una."

    "Quizás si hago un tipo de poema específico pueda impresionar a Yuri."

    "Siento la determinación en mí mismo."

    show sayori turned flus cm oe zorder 2 at s11

    s "¿[player]? Holaaa, tierra llamando a [player]."

    mc "¿Sayori?"

    if decision_sayori == "no ir":
        
        show sayori turned happ om ce zorder 2 at f11
        s "Hoy no creas que te escaparás de mí, jeje."
        show sayori turned happ cm ce zorder 2 at t11
        "Sayori me sonríe honestamente. Hace un tiempo ni siquiera hablábamos, pero luce más alegre desde que me uní."
        show sayori turned happ cm ce zorder 2 at thide
        hide sayori
    elif decision_sayori == "Sayori" or "insistir":
        show sayori turned happ om ce zorder 2 at f11
        s "¿Listo para caminar a casa?"
        show sayori turned happ cm ce zorder 2 at t11
        "Sayori me sonríe honestamente. Hace un tiempo ni siquiera hablábamos, pero luce más alegre desde que me uní."
        show sayori turned happ cm ce zorder 2 at thide
        hide sayori
    scene bg street1_aft
    with wipeleft_scene
    show sayori turned dist cm oe zorder 2 at t11
    mc "Sayori..."
    show sayori turned neut om oe zorder 2 at t11
    mc "Lo que ocurrió hoy en el club... ¿ocurre con frecuencia?"

    show sayori turned flus om oe zorder 2 at f11
    s "¿¡Eh!? ¡Por supuesto que no!"

    show sayori turned nerv om oe zorder 2 at f11 
    s "Nunca las había visto pelear; de hecho, son muy buenas amigas."

    s "No..."

    show sayori turned sad om oe zorder 2 at f11
    s "¿No las odias... o sí?"
    show sayori turned sad cm oe zorder 2 at t11

    mc "No las odio, llevo dos días en el club y me gustaría saber tu opinión."

    show sayori turned worr om oe zorder 2 at f11
    s "Bueno, quizás hayan tenido un mal día y por eso reaccionaron mal."
    show sayori turned worr om oe zorder 2 at s11
    s "Espero que no estés pensando en salirte..."
    show sayori turned worr cm oe zorder 2 at s11

    mc "¿No? Aunque lleve poco tiempo, me gusta estar en el club."

    show sayori turned happ om ce zorder 2 at f11
    s "Me hace muuuuuy feliz que te guste estar en el club."

    s "¡Además, a todas les fascinas!"
    show sayori turned happ cm oe zorder 2 at t11

    "Sayori no piensa dos segundos antes de hablar."

    show sayori turned happ om oe zorder 2 at f11
    s "Te prometo que cada día será mejor."
    show sayori turned happ om oe zorder 2 at t11

    "Suspiro."

    "Sayori aún no entiende cómo me siento."

    mc "Espero que todo mejore mañana."
    show sayori turned happ om oe zorder 2 at f11
    s "Todo estará bien, ya verás."
    show sayori turned happ cm oe zorder 2 at t11
    show sayori turned happ cm oe zorder 2 at thide
    hide sayori

    scene bg bedroom
    with wipeleft_scene
    stop music fadeout 1.0

    "Hoy me siento mucho más inspirado que ayer."

    "Así que haré un poema con simbolismo y una buena métrica."

    "Se me ocurren un par de ideas."

    "Los consejos de Monika están dando sus frutos."

    stop music fadeout 1.0

    scene bg club_day
    with dissolve_scene_full
    play music audio.t8

    "Llegué junto a Sayori al club."

    show sayori turned lup rup happ om ce zorder 2 at f11
    s "¡Compártelos, jeje~!"  
    show sayori turned lup rup happ cm ce zorder 2 at thide
    hide sayori

    "Como ayer, Natsuki está encerrada en el clóset y Monika está organizando papeles sobre el club."
    show yuri turned anno om oe zorder 2 at t11
    "Y Yuri está leyendo un libro; es diferente al que leíamos ayer."

    "\"La anatomía del silencio\", murmuro, intentando descifrar la perturbadora ilustración de la portada."

    "Me pregunto cómo su cerebro puede procesar historias tan densas mientras toma té de lo más tranquila."

    show yuri turned happ cm oe zorder 2 at t11
    "Me acerqué a Yuri. Al estar cerca de ella, parecía un poco emocionada."

    show yuri turned happ om ce zorder 2 at f11
    y "Ho-hola, [player]."
    show yuri turned happ cm oe zorder 2 at t11

    mc "Hola, Yuri. Disculpa, no quería interrumpir tu lectura."

    show yuri turned happ om oe zorder 2 at f11
    y "De hecho, te estaba esperando para continuar."
    show yuri turned happ cm oe zorder 2 at t11

    "Yuri aún estaba en la primera página."

    mc "Ah, entonces... ¿leemos?"

    show yuri turned happ om oe zorder 2 at f11
    y "Por supuesto. Aunque primero me gustaría preparar un poco de té, ¿te parece bien?"
    show yuri turned happ cm oe zorder 2 at t11

    mc "Me parece bien."

    show yuri turned rup happ om oe zorder 2 at f11
    y "Si hay algo que mejore la lectura, es una buena taza de té."
    show yuri turned rup happ om oe zorder 2 at s11
    y "(Además de ti)."
    show yuri turned rup happ om oe zorder 2 at thide
    hide yuri 
    "Yuri se levantó del asiento para dirigirse al clóset. Cuando regresa, trae una jarra de agua."
    show yuri turned happ om oe zorder 2 at f11
    y "Sostenla, por favor."
    show yuri turned happ cm oe zorder 2 at t11

    "Yuri me entregó la jarra junto a una tetera eléctrica."
    show yuri turned happ om oe zorder 2 at f11
    y "Conectaré esto y luego necesitaríamos un poco de agua."
    show yuri turned dist cm oe zorder 2 at s11
    "Ella encendió la tetera eléctrica. Yuri es tan elegante incluso en sus movimientos."

    "Yuri me pidió la jarra y se la entregué."

    show yuri turned happ om oe zorder 2 at f11
    y "Ya regreso, traeré agua."
    show yuri turned happ cm oe zorder 2 at t11

    mc "¿Te puedo acompañar?"

    show yuri turned laug om oe zorder 2 at f11 
    y "Ah... bueno, ¿por qué no?"

    show yuri turned n2 flus om oe zorder 2 at f11
    y "Está bien, a-acompáñame."

    show monika forward lpoint happ cm ce zorder 2 at t32
    show yuri turned n2 flus cm oe zorder 2 at t33

    "Cuando iba a salir del aula con Yuri, Monika se puso enfrente de mí."

    mc "¿Hola?"

    show monika forward lpoint happ om ce zorder 2 at f32
    m "¿A dónde van ustedes?"
    show monika forward lpoint happ cm ce zorder 2 at t32

    show yuri turned lup neut om oe zorder 2 at f33 
    y "Vamos a llenar la jarra de agua, Monika."
    show yuri turned lup neut cm oe zorder 2 at t33
    show monika forward lpoint happ om oe zorder 2 at f32
    m "Me parece bien, pero eso lo podría hacer una sola persona, ¿no?"
    show monika forward lpoint happ om oe zorder 2 at f32

    stop music fadeout 1.0

    m "Y es u-{nw}"
    show yuri turned angr om oe zorder 2 at f33
    y "Monika, ¿puedes amablemente retirarte y dejarnos en paz?"

    y "¿O te parece mal involucrar a [player] más que tú en las actividades del club?"

    show monika forward vsur om oe zorder 2 at f32
    m "¿Eh?"

    mc "..."

    m forward ldown me e1b b1a "Yo..."

    m "No hay nada de malo en eso."

    "Yuri suspiró para luego salir rápidamente del club."

    play audio closet_open
    show yuri turned angr om oe zorder 2 at thide
    hide yuri  
    show monika forward neut cm oe zorder 2 at t11
    "Acompañé a Yuri, pero miré atrás y vi a Monika. Me asusta un poco esa mirada."

    pause 1.0

    "Rápidamente seguí el paso de Yuri."

    play audio closet_close

    pause 0.5

    scene bg corridor
    with wipeleft_scene
    play music audio.t9

    "Yuri tenía la cara cubierta con sus manos."

    show yuri turned vsur om oe zorder 2 at f11
    y "L-Lo dije sin pensar... ¿Cómo no pude pensar en que sonaría tan agresiva?"
    show yuri turned vsur cm oe zorder 2 at t11

    mc "Yuri..."

    show yuri turned vsur om oe zorder 2 at f11
    y "Me molestó cómo lo dijo Monika... Pero no es justificación."

    y "¿Será que al abrirme con los demás ya estoy mostrando lo insoportable que soy?"

    show yuri turned worr om oe zorder 2 at f11
    y "Quizás debería irme a mi casa..."
    show yuri turned lsur cm oe zorder 2 at t11

    mc "No, Yuri, no hiciste mal. No has hecho nada malo, pienso que lo has manejado bien."

    mc "No necesitas explicarle a otras personas lo que haces o no haces."

    mc "Te culpas demasiado, incluso por cosas que no son tu culpa."

    show yuri turned anno om oe zorder 2 at f11
    y "Porque..."

    show yuri turned vsur om ce zorder 2 at f11
    y "¿Por qué eres tan amable conmigo?"
    show yuri turned worr cm oe zorder 2 at t11

    mc "Porque nada de lo que haces es tan malo. Nadie es perfecto, todos cometemos errores."
   
    mc "Incluyéndome."

    mc "Hay veces en las que hablo sin pensar, pero de todos modos, soy humano, ¿cierto?"

    mc "Sobrepiensas mucho acerca de lo que dices."

    show yuri turned nerv cm oe zorder 2 at f11
    y "T-Tú..."

    show yuri turned lsur om oe zorder 2 at f11
    y "¿Por qué no me odias? Incluso podría actuar terrible contigo..."
    show yuri turned lsur cm oe zorder 2 at t11

    mc "¿Estás segura de eso último?"

    show yuri turned sad om oe zorder 2 at f11
    y "No..."
    show yuri turned sad cm oe zorder 2 at t11

    mc "No puedo odiarte por expresarte. De todos modos, los amigos siempre se apoyan."

    show yuri shy neut n5 m4 zorder 2 at f11
    y "¿¡Am-Amigo!?"

    y "¡M-Me gusta que podamos... ¡que podamos ser amigos!"
    show yuri shy neut n5 m1 zorder 2 at t11

    mc "Gracias, Yuri."

    "Me pregunto cómo podré avanzar más en esta relación. Por el momento, me centraré en hacer que Yuri se sienta mejor."

    show yuri shy neut n5 m1 zorder 2 at thide
    hide yuri
    stop music fadeout 1.5
    scene bg escaleras
    with dissolve_scene_full
    
    show yuri turned neut n4 md e1c zorder 2 at t11

    "Llegamos a la fuente de agua. Yuri me estaba ayudando a llenar la jarra."

    "Debido al acercamiento, nuestras manos se sobreponían un poco."

    show yuri turned neut n4 mi e1c zorder 2 at f11
    y "[player], ¿piensas que Monika se haya molestado?"
    show yuri turned neut n4 md e1c zorder 2 at t11

    "Vino a mi mente la mirada de Monika."

    mc "No creo que Monika sea el tipo de persona que se enoja o que guarde rencor por algo tan..."

    mc "...tan tonto."

    show yuri turned neut n4 mi e1d zorder 2 at f11
    y "Quiero disculparme con ella."
    show yuri turned neut n4 md e1d zorder 2 at f11

    mc "Me parece buena idea, de hecho."

    show yuri turned neut n4 mi e1d zorder 2 at f11
    y "Sé que no soy buena expresándome... Me gustaría mejorar en eso."

    y "Algunas veces incluso me da miedo hablar con otras personas."
    show yuri turned neut n4 md e1d zorder 2 at t11

    y "..."

    show yuri turned curi om ce zorder 2 at f11
    y "La primera vez que te conocí, sentí eso."
    show yuri turned laug cm oe zorder 2 at t11

    mc "¿En serio? ¿Por qué?"

    show yuri turned worr om oe zorder 2 at f11
    y "Cuadno era niña, mis compañeros solían molestarme..."

    show yuri turned flus om oe zorder 2 at f11
    y "Solía leer en el receso y me veían raro por eso."
    show yuri turned lsur cm oe zorder 2 at t11

    mc "Yuri, quizás no sea la persona más amable, pero sien-"

    show yuri turned shoc om oe zorder 2 at t11
    "Sentí cómo el agua de la jarra estaba mojando nuestras manos."

    "Yuri miró la jarra y cerró el grifo de la fuente."

    show yuri turned pani om oe zorder 2 at f11
    y "¡Uuuuh!"

    y "El piso está mojado."

    y "¡Pe-Perdón!"
    
    y "No estaba prestando atención, de-de..."

    y "E-Es mi cu-"
    show yuri turned shoc cm oe zorder 2 at t11

    mc "Yuri, está bien. Lo limpiaremos juntos."

    "Yuri aún parecía preocupada."

    show yuri turned lsur cm oe zorder 2 at t11

    mc "Yuri, no hiciste nada malo."

    show yuri shy neut n4 m4 e3 b1 zorder 2 at f11
    y "Pero por hablar de más se desbordó mucha agua en el suelo..."
    show yuri shy neut n4 m1 e3 b1 zorder 2 at t11

    mc "No hablo del agua, hablo de Monika. No debes preocuparte por ello, estoy seguro de que Monika también te pedirá disculpas."

    mc "Sé que solo llevo unos días de conocerlas, pero confía en ti, como yo lo hago en ti, Yuri."

    show yuri shy neut n4 m4 e5 b2 zorder 2 at f11
    y "¿Tú crees?"

    mc "Estoy seguro, te lo prometo."
    
    mc "Prometo siempre ayudarte, incluso en el más mínimo problema."

    show yuri shy neut n4 m3 e3 b1 zorder 2 at t11
    y "..."

    "Es un poco raro decirle esto a una chica que conozco hace un par de dias."
    
    "Sin embargo, sí lo pienso."

    mc "Así que... ¿volvemos?"

    show yuri shy happ om oe zorder 2 at f11
    y "Gracias, [player]."

    y "Volvamos al club, probablemente se pregunten dónde estamos."
    show yuri shy happ cm oe zorder 2 at f11

    "Logré calmar la ansiedad de Yuri. Siento que lo he manejado bien."

    scene bg club_day 
    with dissolve_scene_full

    play sound closet_open
    play music audio.tyuri

    "Al entrar, sentí las miradas de los demás miembros."

    show yuri turned rup curi om oe zorder 2 at f11
    y "¿Conoces el té oolong? Es muy saludable y también ayuda a tener un mejor estado de ánimo."
    show yuri turned rup curi cm oe zorder 2 at t11

    mc "Oolong suena como el nombre de un dragón mitológico..."

    show yuri turned rup curi om oe zorder 2 at f11
    y "Bueno, un día me gustaría enseñarte el arte de hacer un buen té."

    y "Estoy segura de que te gustará, sobre todo beberlo."
    show yuri turned happ om ce zorder 2 at t11

    mc "Es una buena idea de cita."

    show yuri turned lsur cm oe zorder 2 at t11
    y "...-"

    mc "Y... ¿cuál es el primer paso para hacer té?"

    "Intento cambiar de tema al ver la reacción de Yuri."

    with dissolve_scene_full
    show yuri lup lsur cm oe zorder 2 at thide
    hide yuri 
    scene bg club_day 

    "Yuri conectó la tetera eléctrica, aumentando la temperatura a 180°F."

    show yuri turned lup rup mb e1a b1a zorder 2 at f11
    y "Ahora se pone la tetera."
    show yuri turned lup rup ma e1d b1a zorder 2 at t11

    "Yuri tomó la tetera y empezó a agarrar las hojas de té."

    "Para mi sorpresa, estuvo tarareando una canción."

    mc "Disfrutas hacer té, ¿no?"

    show yuri turned lup happ om oe zorder 2 at f11

    y "También, más sin embargo, estuve pensando en lo que te comenté antes."
    
    y "Quiero expresarme más con los demás, no es tan difícil como lo pensaba."

    show yuri turned laug om oe zorder 2 at f11

    y "Por lo menos contigo."

    show yuri turned laug cm oe zorder 2 at t11

    y "..."

    show yuri turned flus om oe zorder 2 at t11

    y "Cuando paso tiempo contigo, me es más fácil expresarme."

    show yuri turned flus cm oe zorder 2 at t11
    
    mc "¡Eso es muy bueno, Yuri! Solo no te sobreesfuerces."

    show yuri turned lup nerv om oe zorder 2 at f11

    y "Siempre te preocupas por mí..."

    show yuri turned lup lsur cm oe zorder 2 at f11

    y "Es muy lindo de tu parte."

    show yuri turned lup lsur cm ce zorder 2 at f11

    "Espera, necesito un respiro de esto."

    scene bg club_day
    with dissolve_scene_full

    "Yuri pone dos tazas para cada uno."

    show yuri turned rup happ om oe zorder 2 at f11

    y "¿Te gustaría leer en el suelo hoy?"

    show yuri turned rup happ cm oe zorder 2 at t11

    mc "¿Está bien? Pero ¿por qué?"

    show yuri turned rup happ om oe zorder 2 at f11

    y "Se lee mejor con la espalda apoyada en la pared."

    show yuri turned rup happ cm oe zorder 2 at f11

    mc "Oh, disculpa. Ahora que lo pienso, sí es un poco incómodo leer en los escritorios."

    show yuri turned happ om oe zorder 2 at f11

    y "Tranquilo, casi siempre tengo dolores de espalda, así que puedo soportarlo."

    y "Es por mi—"

    show yuri turned pani om oe zorder 2 at f11

    y "Ah... ¡!"

    show yuri turned lup rup pani cm ce zorder 2 at f11
    pause 0.5
    show yuri turned rup pani om oe zorder 2 at f11
    pause 0.5
    show yuri turned pani cm ce zorder 2 at f11
    pause 0.5
    show yuri shy neut n5 m2 zorder 2 at f11


    mc "Tu postura al leer... ¿cierto?"

    show yuri shy neut n3 m4 e2 b1 zorder 2 at f11

    y "S-sí, es eso."

    show yuri shy neut n3 m2 e1 b1 zorder 2 at t11

    "No creo que haya sido eso, pero prefiero no indagar en el tema."

    show yuri shy neut n3 m4 e1 b1 zorder 2 at t11

    mc "Te encorvas mucho al leer, supongo."

    show yuri turned nerv om oe zorder 2 at f11

    y "¡Sí! Tengo una terrible postura."

    hide Yuri
    scene y_cg2_bg1
    show y_cg2_dust1
    show y_cg2_base
    show y_cg2_nochoc
    with dissolve_scene_full



    "Nos sentamos en una de las paredes cerca de la ventana."

    "Sostengo con una de mis manos el libro; Yuri hace lo mismo de la parte contraria."

    "Sentí que no podía respirar cuando Yuri chocó su hombro con el mío."

    #empezar a leer el libro que todavia no esta definido si saldra o si debemos de cambiar algo, en dado caso si existe poner escena del libro
    y "[player], ten."

    "Yuri me pasó una taza de té."

    mc "Gracias, Yuri."

    "Realmente estamos más cerca de lo que esperaba, puedo escuchar su respiración."

    show y_cg2_exp3

    #libro

    mc "Oh, se me había olvidado."

    "Saqué una pequeña bolsa de mis bolsillos."

    mc "Sayori me había dado unos chocolates y creo que es una buena ocasión para comerlos."

    mc "Creo que el chocolate con té sabrá bien, ¿no?"

    y "¿Chocolate?"

    mc "Sí, ten."

    "Yuri intentó agarrar el chocolate, pero debido a la postura era muy difícil sin hacerlo incómodo."

    y "[player], no puedo agarrar los chocolates sin que el libro se caiga."

    "Dudé unos segundos en seguir mis pensamientos."

    mc "Entonces... ¿así está bien?"

    y "..."

    "Levanté el chocolate hacia Yuri."

    "Yuri se inclinó lentamente mordiendo el chocolate. Nuestras miradas se cruzaron."

    "Pero no es un momento incómodo, es más tranquilo..."

    "Aparté la mirada."

    y "Es-eso..."

    m "¡Okay, todo el mundo!"

    mc "¿¡EEEH!?"

    "Por el susto terminé ahogándome con el chocolate."

    scene bg club_day
    show yuri turned shoc om oe zorder 2 at f11

    y "¡[player]!"



    #añadir escena de transición

    show yuri turned shoc cm oe zorder 2 at t11

    mc "Cof, cof."

    show yuri turned shoc cm oe zorder 2 at t21
    show monika forward rhip anno om oe zorder 2 at f22

    m "Disculpen, no pensaba asustarlos. Me imagino que habrán estado muy concentrados."

    show monika forward happ cm oe zorder 2 at t22

    mc "Menos mal aún quedaba un poco de té."

    show yuri turned dist cm oe zorder 2 at t21

    "Terminé de beber toda la taza de té."

    show monika forward lpoint neut om oe zorder 2 at f22

    m "Uh... Es tiempo de compartir poemas, chicos."

    show monika forward lpoint neut om ce zorder 2 at f22

    m "Por cierto, debido al tiempo, Yuri, te sugiero que guardes las cosas del té."

    show yuri turned dist om oe zorder 2 at t21

    y "Está bien."

    "Yuri aún parecía un tanto preocupada, así que me acerqué para ayudarle a guardar el juego de té."
    show yuri turned dist om oe zorder 2 at t21
    hide yuri

    show monika forward lpoint neut om ce zorder 2 at f22
    hide monika

    with wipeleft_scene 

    "Luego de terminar de limpiar, era momento de compartir mis poemas."
    
    "Aunque no sé si sea buena idea compartirlo con Yuri... por lo que pasó hace unos minutos..."

    "Espero no lo tome a mal..."

    with wipeleft_scene

    if decision_biblioteca == "Monika":
        show yuri turned neut cm oe zorder 2 at  t11
        y "H-Hola, [player]... ¿Te encuentras bien?"
        mc "¿Por qué lo dices?"
        mc "Oh... Sí, sí. Es solo que no esperaba que Monika apareciera de la nada."
        y turned happ cm ce "Yo también me llevé una gran sorpresa... Jujuju."
        "Yuri parece contener una pequeña risa, tapándose la boca con timidez."
        mc "¿De qué te ríes, Yuri?"
        y turned happ om oe "Uh, lo siento... Es que hiciste una expresión muy graciosa cuando apareció Monika."
        mc "Uuuuh, no sabía que era tan divertido verme a punto de ahogarme con un chocolate."
        y turned happ om ce "Jujuju, es que si hubieras visto tu rostro..."
        mc "Sí, sí, muy gracioso."
        "Ambos terminamos riendo suavemente después de la situación tan bochornosa que acabamos de vivir."
        "No sabía que Yuri fuera capaz de burlarse de mí de esa manera."
        "Es algo nuevo en ella y, para ser sincero, no me molesta en absoluto."
        show yuri turned pani om oe zorder 2 at h22
        show monika lean zorder 2 at t21
        m "Parece que se están divirtiendo mucho por aquí."
        "Nuestras risas se detienen en seco con la repentina aparición de Monika."
        show yuri turned dist om oe zorder 2 at t22
        show monika lean zorder 2 at f21
        m "Veo que no están compartiendo sus poemas, así queee..."
        m "[player], ¿quieres leer el mío?"
        m "Escribí algo que estoy segura de que te fascinará."
        show monika lean zorder 2 at t21
        show yuri turned neut om oe zorder 2 at f22
        y "D-Disculpa, Monika... pero [player] y yo estábamos a punto de intercambiar nuestros poemas."
        show monika lean anno om oe zorder 2 at f21
        show yuri turned neut om oe zorder 2 at t22
        stop music fadeout 0.5
        play music audio.t7 fadein 1
        m "¿Estás segura de eso? Me pareció haber visto que solo estaban riendo y jugando."
        m "Entooonces... dudo que le hayas pedido a [player] compartir sus poemas todavía."
        m "Tendrás que esperar tu turno ahora."
        show monika lean anno om oe zorder 2 at t21
        show yuri turned neut om oe zorder 2 at f22
        y "P-Pero... ¡[player], dile a Monika que estábamos a punto de compartirlos!"
        show monika lean anno om oe zorder 2 at f21
        show yuri turned neut om oe zorder 2 at t22
        m "Yuri, espera tu turno. Vas a interrumpir la lectura de [player]."
        show monika lean anno om oe zorder 2 at t21
        show yuri turned angr om oe zorder 2 at f22
        y "La única que está interrumpiendo y haciendo de mal tercio eres tú. [player] y yo estábamos charlando tranquilamente y solo apareciste para arruinarlo."
        show monika lean anno om oe zorder 2 at f21
        show yuri turned angr om oe zorder 2 at t22
        m "¿Ah, sí? Es la hora de compartir poemas y me parece que USTEDES no lo estaban haciendo."
        m "Así que, si me disculpas... Toma, [player]."
        m lean "Ayer tuve una gran inspiración gracias a alguien, jeje."
        mc "Ch-Chicas, no hay por--{nw}"
        show monika lean anno om oe zorder 2 at t21
        show yuri turned angr om oe zorder 2 at f22
        y "¡Suficiente!"
        y "No permitiré que arruines nuestro intercambio de poemas."
        y "[player], dile que vas a leer mi poema primero."
        show monika lean anno om oe zorder 2 at f21
        show yuri turned angr om oe zorder 2 at t22
        m "Yuri, estás tomando una postura muy inmadura."
        show monika lean anno om oe zorder 2 at t21
        show yuri turned pout om oe zorder 2 at f22
        y "¡S-Silencio, Monika! [player] me dará la razón, ¿verdad?"
        show monika lean anno om oe zorder 2 at f21
        show yuri turned pout om oe zorder 2 at t22
        m "¿Por qué estás tan segura de eso?"
        m "[player], ¿estás de acuerdo con ella?"
        show monika lean anno om oe zorder 2 at t21
        show yuri turned pout om oe zorder 2 at t22
        "No de nuevo... ¿Por qué siempre me ponen en este tipo de posiciones?"
        "Monika tiene un punto: Yuri y yo no estábamos compartiendo nuestros poemas en ese momento."
        "Pero es completamente cierto que nos interrumpió de golpe mientras platicábamos."
        "Estoy seguro de que, después de terminar de hablar, nos habríamos mostrado los poemas de todos modos."
        show monika lean anno om oe zorder 2 at f21
        show yuri turned angr om oe zorder 2 at f22
        my "Y bien... ¿[player]?"
        menu discusion_moniyuri:
            "Compartir mi poema con Monika":
                $ decision_poema_my = "Monika"
                $ puntos_ruta -= 2
                "Monika tiene razón Yuri y yo no estabamos compartiendo nuestros poemas"
                mc "Esta bien Monika"
                mc "Yuri podemos compartir poemas luego"
                show monika lean zorder 2 at f21
                show yuri turned sad cm ce zorder 2 at f22
                y "Uh, s-seguro"
                "Yuri se aleja de manera calmada y con aura de melancolia"
                show monika lean zorder 2 at thide
                show yuri turned sad cm ce zorder 2 at thide
                hide yuri 
                hide monika 
                with wipeleft_scene
                jump mostrar_poema_monika2
            "Compartir mi poema con Yuri":
                $ decision_poema_my = "Yuri"
                $ puntos_ruta += 1
                "No se que se le metio en la cabeza a Monika, Yuri y yo estabamos por compartir nuestros poemas tarde o temprano"
                mc "Lo siento, Monika pero Yuri y yo ibamos a comparit nuestros poemas luego de charlar"
                show monika forward neut om oe zorder 2 at f21
                show yuri turned angr om oe zorder 2 at t22
                m "Oh esta bien"
                m "Lo siento por interrumpir chicos"
                "Puedo ver como Monika me mira con unos ojos amenazadores antes de irse"
                show monika forward neut om oe zorder 2 at thide
                show yuri turned angr om oe zorder 2 at thide
                hide yuri 
                hide monika
                with wipeleft_scene
                
                jump mostrar_poema_yuri2
    elif decision_biblioteca == "Yuri":
        jump mostrar_poema_yuri2



    #añadir eleccion de poemas a Yuri (pensar si serviria esto)
    ######################POEMA DE YURI AQUI
    

    #añadir poema 

    #añadir escena del poema, salto final de escena 


    label pelea:

        "¿En serio terminé de compartir mi poema con las demás? Ellas aún siguen compartiendo opiniones."

        "Fue muy notable cómo mejoraron todos sus poemas. El que más me sorprendió fue el de Sayori." #aqui poner un poco mas de textos sobre los podemas de Yuri, MOnika y Natsuki

        "Ese poema me dejó pensando luego de leerlo..."

        "Me senté en uno de los pupitres."

        "Mis ojos se centran en Yuri. Ella está compartiendo su poema con Monika, aunque parece más tímida de lo normal."
        

        show yuri turned flus om oe zorder 2 at t21
        show monika forward rhip anno cm oe zorder 2 at t22

        stop music fadeout 1.5

        "Luce como si pidiera perdón por algo."

        show yuri shy angr cm oe zorder 2 at t21
        show monika forward rhip anno om oe zorder 2 at f22

        m "¿Entendido?"

        show yuri shy angr om oe zorder 2 at f21
        show monika forward rhip anno cm oe zorder 2 at f22

        y "S-sí..."

        show yuri shy angr om oe zorder 2 at thide
        hide yuri
        show monika forward rhip anno cm oe zorder 2 at thide
        hide monika


        "Yuri asintió con la cabeza."

        "¿Será algo importante?"

        "Parecía muy triste o indiferente... Qué será lo que estab—"

        show monika forward lpoint rhip happ om oe zorder 2 at f11

        play music audio.t8 fadein 0.5

        m "¡Okay, todo el mundo!"

        show monika forward lpoint rhip happ om ce zorder 2 at f11

        m "Con esto se concluye el compartir de poemas."

        show sayori turned lup neut om oe zorder 2 at f22
        show monika forward rhip happ cm oe zorder 2 at f21

        s "Monika, me tendré que ir temprano. Nos vemos mañana."

        show sayori turned lup happ om ce zorder 2 at f22
        show monika forward rhip happ cm oe zorder 2 at f21

        s "¡Adiositooo!"

        show sayori turned lup neut om ce zorder 2 at thide
        hide sayori
        show natsuki cross dist om oe zorder 2 at f22
        show monika forward rhip happ cm oe zorder 2 at t21

        n "Sí, yo también. Mi padre me está esperando."

        show natsuki cross dist om oe zorder 2 at thide
        hide natsuki
        show monika forward rhip happ cm ce zorder 2 at f21

        m "Bueno, cuídense. Hasta mañana."

        show monika forward rhip happ cm ce zorder 2 at thide
        hide monika

        "Solo quedamos yo, Yuri y Monika en el club. Quizás pueda decirle si me acompaña a irme a casa."

        show yuri turned dist cm oe zorder 2 at t11

        mc "Oye, Yuri, ¿quie—"

        show yuri turned pani om oe zorder 2 at f11

        y "¡Ahh!"

        show yuri turned sad om oe zorder 2 at f11

        y "¡Disculpa, [player], me tengo que ir!"

        show yuri turned sad om oe zorder 2 at thide
        hide yuri

        "Yuri salió rápidamente del club sin siquiera voltearme a ver."

        "Definitivamente ha pasado algo con ella. Está actuando raro. Quizás Monika sepa algo."

        "Monika estaba sentada en el escritorio junto a una computadora."

        "Quizás la interrumpa... Pero Yuri es mi prioridad."

        show monika forward happ om oe zorder 2 at f11

        if decision_poema_my == "Monika":

            m "Oh, ¡hola, [player]! ¿Necesitas algo?"

            show monika forward happ cm oe zorder 2 at t11

            mc "Sí, ¿has notado que Yuri ha estado un poco rara luego de...?"

            show monika forward flus om oe zorder 2 at f11

            m "Bueno, quizás deberías ignorarla."

            show monika forward flus cm oe zorder 2 at t11

            mc "¿Disculpa?"

            show monika forward worr om oe zorder 2 at f11

            m "Quizás me di a mal entender. Me refiero a que Yuri no habla frecuentemente con nosotros u otras personas."

            m "Es más solitaria, incluso en el club."

            show monika forward worr cm oe zorder 2 at t11

            "La expresión de Monika cambia al ver la mía."

            show monika forward nerv om oe zorder 2 at f11

            m "No me refiero a que no le hables, solo que es mejor tener una pequeña charla con ella y dejarla sola."

            show monika forward happ om ce zorder 2 at f11

            m "Créeme, conozco perfectamente a mi miembros."

            show monika forward dist cm oe zorder 2 at t11

            mc "Pensaba que nos llevábamos bien, en realidad."

            show monika forward neut om oe zorder 2 at f11

            m "Yuri puede ser un poco obsesiva con algunas cosas..."

            show monika forward neut cm oe zorder 2 at f11

            "¿Obsesiva? Quizás sí tenga un poco de razón... Ella suele disculparse mucho, incluso por lo mínimo."

            mc "¿Obsesiva en qué?"

            show monika forward worr om ce zorder 2 at t11

            "Monika suspiró."

            show monika forward anno lpoint om oe zorder 2 at f11

            m "Mira, [player], solo no estés tanto tiempo con Yuri. Además, también puedes pasar tiempo con las demás."

            show monika forward rhip happ om oe zorder 2 at f11

            m "Como yo."

            show monika forward rhip happ cm oe zorder 2 at t11

            "¿Qué me está intentando decir? Monika, la presidenta del club, ¿me está pidiendo que pase el tiempo con ella?"

            show monika lean happ cm oe zorder 2 at t11

            mc "Digo... Pensaba que Yuri y yo nos llevábamos bien."

            show monika lean anno cm oe zorder 2 at f11
            pause 1.0
            show monika lean neut om oe zorder 2 at f11

            m "Realmente no conoces a Yuri."

            show monika lean anno om oe zorder 2 at t11

            mc "Quizás solo llevo unos días hablando con ella, pero cada día intento aprender más de ella."

            "Me detuve unos segundos para formular mi pregunta."

            show monika forward vsur cm oe zorder 2 at t11

            mc "Vi que le dijiste algo a Yuri hace un rato."

            show monika forward nerv cm oe zorder 2 at f11

            m "¿En serio?"

            show monika forward nerv cm oe zorder 2 at t11

            mc "Sí, recuerdo que le susurraste y—"

            show monika forward laug om oe zorder 2 at f11

            m "Oh... Tranquilo, es una cosa entre nosotras. Ya sabes, cosas de chicas."

            show monika forward laug cm oe zorder 2 at t11

            "Siento que me está mintiendo."

            mc "..."

            show monika forward laug om oe zorder 2 at f11

            m "Bueno, tengo unas cosas que hacer, así que nos vemos mañana, [player]."

            show monika forward laug cm oe zorder 2 at t11

            "Qué manera tan amable de decir: 'lárgate'."

            show monika forward worr cm oe zorder 2 at t11

            mc "Está bien. Adiós, Monika."

            show monika forward worr cm oe zorder 2 at thide 
            hide monika 
        elif decision_poema_my == "Yuri":
            m "Oh, ¡hola, [player]! ¿Necesitas algo?"

            show monika forward happ cm oe zorder 2 at t11

            mc "Sí... ¿Has notado que Yuri ha estado un poco rara luego de...?"

            show monika forward flus om oe zorder 2 at f11

            m "Bueno, quizás deberías ignorarla."

            show monika forward flus cm oe zorder 2 at t11

            mc "¿Disculpa?"

            show monika forward worr om oe zorder 2 at f11

            m "Quizás me di a entender mal. Me refiero a que Yuri no suele hablar muy seguido con nosotros ni con otras personas."
            m "Es alguien más solitaria... incluso aquí en el club."

            show monika forward worr cm oe zorder 2 at t11

            "La expresión de Monika cambia de inmediato al notar mi incomodidad."

            show monika forward nerv om oe zorder 2 at f11

            m "No me refiero a que no le hables en absoluto, solo... que es mejor tener una pequeña charla casual con ella y luego dejarla sola."
            show monika forward nerv om oe zorder 2 at t11
            mc "Monika, creo que no te entiendo."
            mc "Yuri es una chica muy amable y una buena amiga."

            show monika forward nerv om oe zorder 2 at f11

            m "Puede que tengas razón... pero yo también conozco a Yuri."

            m forward neut om oe "Deberías pasar más tiempo con los demás integrantes del club."
            m forward happ cm oe "Ahora que comparten una actividad juntos, tú y Sayori podrían charlar más."
            m forward neut om oe "Natsuki tal vez no te ha dado la mejor impresión al principio, pero en el fondo es una chica muy dulce."
            m lean "También... puedes pasar tiempo conmigo si así lo quieres, jeje."
            m "Estaría muy contenta de que hiciéramos más actividades juntos..."
            m "Solos."
            m "Tú y yo."
            m forward dist om oe "Aléjate de Yuri, créeme."
            m forward happ cm oe "Y pasa más tiempo conmi-- "
            m forward laug om oe "con las demás chicas."
            show monika forward happ cm oe zorder 2 at t11

            mc "Ehhh, no estaría mal, sí... claro."

            

            "Es sumamente extraño."
            "Durante todo este tiempo, Monika parece querer alejarme de Yuri a toda costa."
            "Supongo que podría pasar más tiempo con las demás, pero la manera en que actúa Monika me da muy mala espina."
            "Tal vez solo estoy exagerando y Monika solo quiere que me lleve bien con todos en el club..."

            mc "Claro, Monika. Tomaré en cuenta tu consejo."

            "Espero que Monika deje de insistir tanto después de escuchar esto."

            mc "Ehh, como sea, Monika... Quería hacerte una pregunta."

            show monika forward happ cm oe zorder 2 at f11

            m "Por supuesto, dime. Siempre estoy disponible para los miembros de mi amado club."

            "Me detengo unos segundos para formular bien mi pregunta en la cabeza."

            show monika forward vsur cm oe zorder 2 at t11

            mc "Vi que le dijiste algo a Yuri hace un rato."

            show monika forward nerv cm oe zorder 2 at f11

            m "¿En serio?"

            show monika forward nerv cm oe zorder 2 at t11

            mc "Sí... Recuerdo perfectamente que le susurraste algo y—"

            show monika forward laug om oe zorder 2 at f11

            m "Oh... Tranquilo, es un asunto entre nosotras. Ya sabes, cosas de chicas."

            show monika forward laug cm oe zorder 2 at t11

            "Siento que me está mintiendo descaradamente."

            mc "..."

            show monika forward laug om oe zorder 2 at f11

            m "Bueno, tengo algunas cosas que organizar todavía, así que nos vemos mañana, [player]."

            show monika forward laug cm oe zorder 2 at t11

            "Qué manera tan sutil de decir: 'lárgate'."

            show monika forward worr cm oe zorder 2 at t11

            mc "Está bien... Adiós, Monika."

            show monika forward worr cm oe zorder 2 at thide
            hide monika
        elif decision_poema_my == "yuriyuri":
            m "Oh, ¡hola, [player]! ¿Necesitas algo?"

            show monika forward happ cm oe zorder 2 at t11

            mc "Sí... ¿Has notado que Yuri ha estado un poco rara luego de...?"

            show monika forward flus om oe zorder 2 at f11

            m "Bueno, quizás deberías ignorarla."

            show monika forward flus cm oe zorder 2 at t11

            mc "¿Disculpa?"

            show monika forward worr om oe zorder 2 at f11

            m "Quizás me di a entender mal. Me refiero a que Yuri no suele hablar muy seguido con nosotros ni con otras personas."
            m "Es alguien más solitaria... incluso aquí en el club."

            show monika forward worr cm oe zorder 2 at t11

            "La expresión de Monika cambia de inmediato al notar mi incomodidad."

            show monika forward nerv om oe zorder 2 at f11

            m "No me refiero a que no le hables en absoluto, solo... que es mejor tener una pequeña charla casual con ella y luego dejarla sola."
            show monika forward nerv om oe zorder 2 at t11
            mc "Monika, creo que no te entiendo."
            mc "Yuri es una chica muy amable y una buena amiga."

            show monika forward nerv om oe zorder 2 at f11

            m "Puede que tengas razón... pero yo también conozco a Yuri."

            m forward neut om oe "Deberías pasar más tiempo con los demás integrantes del club."
            m forward happ cm oe "Ahora que comparten una actividad juntos, tú y Sayori podrían charlar más."
            m forward neut om oe "Natsuki tal vez no te ha dado la mejor impresión al principio, pero en el fondo es una chica muy dulce."
            m lean "También... puedes pasar tiempo conmigo si así lo quieres, jeje."
            m "Estaría muy contenta de que hiciéramos más actividades juntos..."
            m "Solos."
            m "Tú y yo."
            m forward dist om oe "Aléjate de Yuri, créeme."
            m forward happ cm oe "Y pasa más tiempo conmi-- "
            m forward laug om oe "con las demás chicas."
            show monika forward happ cm oe zorder 2 at t11

            mc "Ehhh, no estaría mal, sí... claro."

            

            "Es sumamente extraño."
            "Durante todo este tiempo, Monika parece querer alejarme de Yuri a toda costa."
            "Supongo que podría pasar más tiempo con las demás, pero la manera en que actúa Monika me da muy mala espina."
            "Tal vez solo estoy exagerando y Monika solo quiere que me lleve bien con todos en el club..."

            mc "Claro, Monika. Tomaré en cuenta tu consejo."

            "Espero que Monika deje de insistir tanto después de escuchar esto."

            mc "Ehh, como sea, Monika... Quería hacerte una pregunta."

            show monika forward happ cm oe zorder 2 at f11

            m "Por supuesto, dime. Siempre estoy disponible para los miembros de mi amado club."

            "Me detengo unos segundos para formular bien mi pregunta en la cabeza."

            show monika forward vsur cm oe zorder 2 at t11

            mc "Vi que le dijiste algo a Yuri hace un rato."

            show monika forward nerv cm oe zorder 2 at f11

            m "¿En serio?"

            show monika forward nerv cm oe zorder 2 at t11

            mc "Sí... Recuerdo perfectamente que le susurraste algo y—"

            show monika forward neut om oe zorder 2 at f11

            m "No fue nada importante."

            "Monika me interrumpe justo antes de que pueda terminar mi pregunta, con una rapidez que me resulta casi ensayada."

            m forward lpoint pout om oe "Fue solo algo de chicas, de verdad. Nada de lo que un chico deba preocuparse o saber, jeje."
            show monika forward lpoint pout om oe zorder 2 at t11
            mc "¿Segura? Es que... parecía algo más que eso."
            mc "La expresión de Yuri cuando te alejaste no era la habitual."

            "Monika asiente con un leve movimiento de cabeza, manteniendo su sonrisa perfectamente intacta, aunque sus ojos se entrecierran apenas un milímetro."

            mc "No lo sé, Monika... Fue muy raro."
            mc "Quería hablar con ella, preguntarle algo sobre el libro que estamos leyendo."
            mc "Pero antes de que pudiera decir una sola palabra, me miró con pánico y huyó de inmediato."
            mc "Antes de eso lucía perfectamente bien... Si no fue por lo que hablaron, ¿qué otra cosa podría ser?"
            mc "De verdad espero que no se haya retirado porque se siente mal o algo parecido. Me preocupa."
            show monika forward ldown rhip nerv cm oe zorder 2 at f11
            m "Oh, no, no... Yuri está perfectamente bien, [player]. Solo que... bueno, ya sabes cómo es ella."
            m "Yuri es una chica extremadamente tímida, retraída y... propensa a malinterpretar las intenciones de los demás."
            m "Probablemente se sintió muy abrumada por tener un contacto tan cercano contigo el día de hoy, se puso nerviosa y decidió huir en cuanto te vio acercarte."
            m "A veces su mente trabaja demasiado rápido y se asusta sola."

            show monika forward ldown rhip nerv cm oe zorder 2 at t11

            mc "No lo creo... Yuri no se ha comportado de esa manera conmigo antes."
            mc "La conozco desde hace pocos días, pero sé que es muy madura cuando conversamos a solas. Sé que no es así... al menos, no lo era conmigo."
            show monika forward ldown rhip pout om oe zorder 2 at f11
            m "Mhmm... Bueno, yo la conozco desde hace mucho antes que tú, [player], así que créeme en esto."
            m "Ella tiene... facetas que aún no has visto. Comportamientos un tanto obsesivos y difíciles de manejar."
            m "Deberías darle un poco más de espacio, en serio. Terminarás intimidándola o haciéndola sentir acorralada si te le acercas demasiado."
            m "No querrás ser una molestia para ella, ¿verdad?"

            show monika forward ldown rhip pout om oe zorder 2 at t11

            "Las palabras de Monika caen como un balde de agua fría y me hacen dudar seriamente sobre mis acciones hacia Yuri."
            "Sé que Yuri es bastante tímida, pero nunca noté que se sintiera incómoda en lo más mínimo mientras hablábamos en la esquina del salón."
            "Al contrario, parecía feliz... ¿O acaso solo estaba siendo amable?"
            "Si ese es el caso, debe de ser increíblemente buena escondiendo su incomodidad, o tal vez le da demasiada vergüenza demostrarme que la agobio..."
            "¿Y si de verdad la estoy presionando sin darme cuenta?"
            show monika forward ldown rhip neut om oe zorder 2 at f11
            m "[player]... ¿[player]? ¿Estás ahí?"

            "Monika da un paso hacia mí y chasquea sus dedos suavemente cerca de mi rostro, sacándome de mi espiral de dudas."

            m "Te quedaste congelado. ¿Ves a lo que me refiero? Te tomas las cosas demasiado a pecho."
            m "Solo relájate y dale su espacio. Deja que las cosas fluyan."

            "Me preocupa mucho todo esto... De verdad espero no estar asustando o incomodando a Yuri. La sola idea de hacerla sentir mal me revuelve el estómago."
            show monika forward ldown rhip pout om oe zorder 2 at t11
            mc "M-Monika... Sí, aquí estoy. Lo siento, me perdí en mis pensamientos."
            mc "Tienes razón, tal vez deba pensar las cosas con más calma..."
            mc "Como sea, se está haciendo tarde y tengo que irme a casa pronto."
            mc "Adiós, Monika."

            show monika forward rdown mb e1e b1a zorder 2 at f11

            m "¡Adiós, [player]! Ve con cuidado a casa."
            m "¡¡Y no olvides escribir el poema de mañana!! Estaré esperando ansiosa sobre qué escribaras esta vez... preferiblemente algo más propio de ti, ¿sí?"
            show monika forward ldown rhip pout om oe zorder 2 at thide
            hide monika


        #cambiar a escena de casa de 
        scene bg bedroom
        with dissolve_scene_full

        "'Cosas de chicas'."

        "Aún recuerdo su cara; parecía una mezcla de ansiedad y miedo."

        "Y solo me ignoró para irse del club..."

        "Mañana debería preguntarle... obsesiva... obsesión..."

        "Creo que ya tengo la suficiente inspiración para poder escribir otro poema."

        "No pienso que ella la esté pasando mal conmigo... Cada día la entiendo mejor."

        "Yo también me he abierto a ella."

        "Pero Monika..."

        mc "..."

        mc "No estoy llegando a ningún punto."

        
        scene bg corridor
        with dissolve_scene_full

        #transición

        "Realmente no me interesa si a Monika le parece bien o mal que hablemos."

        "Aunque siento que hay algo más... más..."

        #transición

        "Antes de abrir la puerta del club, escuché cómo se elevaba la voz adentro."

        mc "Qué..."

        "Abrí la puerta."
        play sound closet_open
        scene bg club_day
        with dissolve_scene_full

        #transicion

        show yuri turned pani om oe zorder 2 at h22
        show monika forward anno cm oe zorder 2 at t21

        y "Peróname, Monika, no intentaba faltarte al res—"

        show yuri turned lsur cm oe zorder 2 at t22
        show monika forward anno om oe zorder 2 at f21

        m "No acepto tus disculpas, Yuri."

        show yuri turned lsur cm oe zorder 2 at t22
        show monika forward anno om ce zorder 2 at f21

        m "Desde que estás en el club has sido igual de tóxica."

        show yuri turned lsur cm oe zorder 2 at t22
        show monika forward angr om ce zorder 2 at f21

        m "Ni siquiera te comunicas con nosotras, vienes, lees tus estúpidos libros y te vas."

        show yuri turned dist cm oe zorder 2 at t22
        show monika forward angr om ce zorder 2 at f21

        m "¡Sí sabes que existen las bibliotecas, Yuri!"

        show yuri turned lup angr cm oe zorder 2 at f22
        show monika forward angr cm oe zorder 2 at t21

        "Yuri apretó su mano como si intentara decir algo."

        show yuri turned lup angr cm oe zorder 2 at t22
        show monika forward anno om oe zorder 2 at f21

        m "¿Qué? ¿Quieres decir algo?"

        show yuri turned lup anno om oe zorder 2 at f22
        show monika forward anno cm oe zorder 2 at t21

        y "Y-yo..."

        show yuri turned lup vang cm oe zorder 2 at f22
        show monika forward anno cm oe zorder 2 at t21

        y "Pienso que eres una maldita egocéntrica."

        show yuri turned lup vang cm ce zorder 2 at f22
        show monika forward pout cm oe zorder 2 at t21

        y "¿En serio piensas que está bien tratar como un estorbo a un miembro de tu club?"

        show yuri turned lup vang cm ce zorder 2 at f22

        y "Te crees que eres la mejor solo por ser popular, cuando en realidad eres una puta narcisista."

        show yuri turned lup vang cm oe zorder 2 at f22

        y "Con el ego más frágil que una rosa."

        show yuri turned lup yand cm ce zorder 2 at f22

        y "Así que... ¡piensa dos veces antes de hablar!"

        show yuri turned lup yand om ce zorder 2 at f22

        y "Porque cuando acabe contigo, ni siquiera tus padres podrán reconocer—"

        show yuri turned yand cm ce zorder 2 at t22
        show monika forward sedu om oe zorder 2 at f21

        m "Que sí, Yuri, que sí."

        show yuri turned yand cm ce zorder 2 at t22
        show monika forward lpoint sedu om ce zorder 2 at f21


        m "¿Por qué no muestras a los demás cómo realmente eres?"

        show yuri turned yand cm ce zorder 2 at t22
        show monika forward lpoint sedu cm oe zorder 2 at t21

        "Monika voltea a verme; ella ya sabía que estaba aquí."

        show yuri turned yand om ce zorder 2 at t22
        show monika forward lpoint rhip sedu cm oe zorder 2 at f21

        m "Vamos, muéstrale a [player] cómo realmente eres."

        show yuri turned shoc cm oe zorder 2 at h22
        show monika forward lpoint rhip sedu cm oe zorder 2 at t21

        "Yuri se da cuenta de mi presencia."

        show yuri turned shoc om oe zorder 2 at f22
        show monika forward lpoint rhip sedu cm oe zorder 2 at t21

        y "¿[player]...? N-no, espera, ¡no intentaba decir eso!"

        show yuri turned cry om ce zorder 2 at f22

        y "¡No soy así!"

        show yuri turned cry om oe zorder 2 at f22

        y "Y-yo solo..."

        show yuri turned cry cm oe zorder 2 at t22

        "Monika le tocó el hombro a Yuri, haciendo que ella la voltée a ver."

        show monika forward happ om oe zorder 2 at f21

        m "Tranquila, siempre puedes tener un consejo de mi parte, incluso en los momentos malos."

        show monika forward happ om ce zorder 2 at f21

        m "¿Has considerado acabar con tu vida?"

        show monika forward flus om oe zorder 2 at f21

        m "¡Ayudaría a que dejes de hacer esas cosas!"
        show yuri turned cry cm oe zorder 2 at t22
        show monika forward flus cm oe zorder 2 at f21

        stop music 

        y "..."
        show yuri turned cry cm oe zorder 2 at thide
        hide yuri 
        show monika forward flus cm oe zorder 2 at thide
        hide monika 

        "Como ayer, Yuri salió de la habitación. No tenía los ojos llorosos."
        
        "Ella estaba llorando. Estoy asustado por las palabras de Monika."

        "Realmente no sé qué decir."
        
        "..."

        "Iré a ver a Yuri. Cuando iba a salir del club, Monika me detuvo."

        show monika forward lpoint worr om oe zorder 2 at f11

        m "Oye, déjala, ella necesita estar sola pa—"

        show monika forward vsur cm oe zorder 2 at t11

        mc "¿Qué mierda pasa contigo, Monika? Un consejo: 'mátate'. ¿En serio?"

        "Noto a mi alrededor. Sayori está en un escritorio cubriéndose los oídos con sus manos."

        "Ella..."

        "Está sollozando."

        show monika forward anno om oe zorder 2 at f11

        m "Oh, bueno, grítame y hazme ver como la mala."

        show monika lean anno om oe zorder 2 at f11

        m "Ya has visto cómo es Yuri, solo me defendí frente a lo que me dijo."

        show monika lean angr cm oe zorder 2 at t11

        mc "Estás enferma... Yuri no es así, sacaste su peor lado. Iré con ella."

        show monika forward neut om oe zorder 2 at f11

        m "Espera."

        show monika forward neut cm oe zorder 2 at t11

        "No me detuve y abrí la puerta."

        show monika forward neut om oe zorder 2 at f11

        m "Lo digo en serio, no creo que te guste lo que estás a punto de ver."

        show monika forward neut cm oe zorder 2 at f11

        mc "Cállate, maldita insoportable."

        scene bg escaleras
        with dissolve_scene_full
        
        #transición 

        "Intenté seguir el ritmo de Yuri, pero ella corría demasiado rápido."

        #transición 

        "Cuando bajaba las escaleras terminé cayendo al suelo, golpeándome la cabeza."

        mc "Mierda..."

        "Intenté levantarme con dificultad. A este punto, probablemente Yuri ya se haya ido."

        "Me sostuve de una parte de las escaleras, logré escuchar unos sollozos cercanos en el silencioso pasillo."

        "Seguí el sonido de los sollozos, venían del baño."

        "Es el baño de las mujeres, dudo que pueda entrar..."

        "¡Prefiero que me expulsen antes que dejar sola a Yuri!"


        show yuri turned lup rup cry om oe zorder 2 at t11
        mc "¡Yuri, espérame!"
        show yuri turned lup rup cry om oe zorder 2 at thide
        hide yuri 
        "Intenté seguirla, pero terminé resbalándome y golpeándome la cabeza."
        mc "¡Agh!..."
        "Me levanté rápidamente, aunque intenté seguir el ritmo, no pude."

        with dissolve_scene_full

        #añadir escena perspectiva de Yuri 
        play music audio.t10 fadein 2.0
        with dissolve_scene_full
        scene bg bano_Yuri_nocuchillo
        "???" "¿No crees que deberías dejar de huir de tus problemas?"
        show yuri_pequena seria zorder 2 at f11
        "(Yuri)" "Sí, creo que sería la mejor idea."
        show yuri_pequena neut zorder 2 at t11
        y "[player] m-me vio actuando así... É-el va a despreciarme... soy un fenómeno."

        show yuri_pequena tired zorder 2 at f11
        "(Yuri)" "Él no te odia, solo estará un poco sorprendido..."

        show yuri_pequena neut zorder 2 at t11
        y "No puedo soportarlo más... Monika, Monika..."

        show yuri_pequena sad2 zorder 2 at f11
        "(Yuri)" "Yuri, espera, creo que deberías... ¡N-no! ¡Espera!"
        show yuri_pequena sad2 zorder 2 at thide
        hide yuri_pequena sad2
        with dissolve_scene_full
        scene bg bano_Yuri_nocuchillo

        ############################

        mc "¿Yu-yuri?"

        scene bg bano_Yuri
        show yuri_sentada zorder 2 at t11:
            xalign 0.3

        y "¡—!"

        "No pude evitar mirar el brazo de Yuri."

        "Tiene tantas marcas de cortes... algunas recientes... otras no."


        y "[player], n-no se supone que deberías estar aquí..."

        "No tengo la suficiente fuerza para decir algo, di unos pasos para poderme acercar."

        y "¡No!"

        y "Aléjate... por favor..."

        y "Soy peor que un fenómeno..."

        "Yuri apretó su mano derecha y volvió a cortarse."

        mc "Por-por favor... Yo solo quiero ayudarte."

        mc "Estás sangrando mucho... Quizás te puedan atender en la enfermería, yo te llevaré..."

        y "Yo... no merezco ser ayudada. No quiero tu ayuda. ¿Me escuchaste? Escuchaste cómo soy realmente."

        y "Tan..."

        y "Desagradable."

        "Volví a acercarme a ella."

        "Sé que Yuri también estuvo mal diciendo eso... pero fue por la insensibilidad de Monika."

        mc "No puedo juzgarte, Yuri..."

        "Por unos segundos nuestras miradas chocaron."

        "Sus ojos lavanda se tiñieron de lágrimas que no dejaban de salir."

        "Su expresión era completamente diferente... era de desesperación."

        y "Hay tantas emociones... Que las he guardado por tanto tiempo... Tantos años."

        y "Por si fuera poco, no puedo contenerlas..."

        hide yuri_sentada

        #show yuri_parada zorder 2 at t11 este sprite le falta

        "Yuri se levantó del suelo al ver cómo me acerco a ella."

        y "¡Aléjate de mí!"

        "No sé qué hacer... pero haré todo lo que pueda."

        "Para ayudarla."

        mc "Yuri... Escúchame, por favor. Yo realmente te quiero ayudar, no me importa lo que le dijiste a Monika."

        mc "Yo quiero, no me importa tu pasado. Me importas tú, Yuri, por eso me encuentro aquí ahora."

        mc "Intentándolo..."

        "Sus gotas de sangre cayeron en el suelo poco a poco mientras ella se volteaba, evitando verme."

        "No sé cómo acabe esto... Pero haré lo que sea con tal de que Yuri esté bien."

        y "¡Ya te dije que no quiero tu ayuda!"

        y "No sé si un día no pueda controlarme y termine haciendo daño a los demás... haciéndote daño a ti."

        y "No puedo luchar con esto, no lo puedo controlar, soy un títere de mis sentimientos..."

        y "No puedo dejar que los demás vean cómo realmente soy..."

        y "Yo no quiero aceptar quién realmente soy... porque sé que solo soy..."

        y "Una maldita enferma."

        "Mientras Yuri hablaba, lentamente me acerqué a ella."

        y "¡Escúchame, no merezco ser ayudada, mucho menos por ti!"

        y "¡¡¡¡SOLO DÉJAME EN PAZ!!!!"

        "Logré estar cerca de ella e intenté agarrar sus manos."

        "Por unos segundos lo logré, Yuri parecía más calmada."

        mc "Yuri, todo va a estar bien... Estoy seguro de que no solo yo quiero lo mejor para ti."

        mc "También Natsuki, Sayori..."

        y "Monika... L-lo siento."

        #show yuri_parada zorder 2 at t11
        #hide yuri_parada

        mc "¡Yuri, espera!"
        stop music fadeout 2.0

        #transición
        with dissolve_scene_full
        scene corridor

        "Aunque intente alcanzarla, el dolor en mi cabeza incrementaba por los movimientos bruscos."

        "La he perdido..."

        "Casi nunca he visitado mucho los pasillos, aunque lleve un tiempo no conozco todos los lugares."

        mc "Yuri... déjame ayudarte."

        "Me senté en una banca y llevé mis manos a mi cara."

        "Mientras descanso, siento como si mi cabeza estuviera por explotar."

        "No puedo quedarme aquí sin hacer nada."

        "Me levanté y empecé a caminar con un poco de dificultad."

        "Pestañé y, de un momento a otro, me había chocado con una pequeña figura."

        mc "¡Auch!"

        "Unas monedas cayeron en el suelo luego del golpe repentino."

        play music audio.t6 fadein 1.5

        show natsuki turned lhip rhip ff angr om oe zorder 2 at f11

        n "Las monedas... ¡Idiota, fíjate por dónde vas!"

        show natsuki turned rhip ff anno cm oe zorder 2 at t11

        mc "¿Natsuki? Disculpa, Natsuki, no te había visto."

        show natsuki turned rhip ff anno om oe zorder 2 at f11

        n "¿De qué hablas? Si por poco pasas atropellándome. ¿De casualidad no estás borracho?"

        n "La próxima no te perdonaré."

        show natsuki turned ff curi cm oe zorder 2 at t11

        mc "Ya pedí perdón, Nat... Y esas monedas son tuyas, ¿verdad?"

        show natsuki turned lhip rhip ff angr om oe zorder 2 at f11

        n "¡Qué te importa!"

        show natsuki turned ff worr cm oe zorder 2 at t11

        mc "Está bien, disculpa..."

        show natsuki turned ff dist cm oe zorder 2 at t11

        "Natsuki observa las monedas en el suelo para luego voltear a ver."

        pause 1.0

        show natsuki turned lhip ff sad om oe zorder 2 at f11

        n "Está bien, lo siento. Estaba buscando algunas monedas para ayudar a mi padre con su trabajo."

        n "Aunque sean solo unas monedas, ayuda más de lo que parece."

        show natsuki turned ff sad cm oe zorder 2 at t11

        mc "Oh..."

        show natsuki turned ff sad om ce zorder 2 at t11

        "Ambos estuvimos en silencio. ¿Por qué hoy parece que todos están mal?"

        "O en realidad... hoy me doy cuenta de quiénes están mal."

        show natsuki turned ff dist om oe zorder 2 at f11

        n "Ugh, ya solo olvídalo."

        show natsuki turned ff curi om oe zorder 2 at f11
        
        n "Por cierto, ¿por qué no estás en el club?"

        show natsuki turned ff neut cm oe zorder 2 at f11

        mc "Bueno, es un poco difícil de explicar, pero necesito encontrar a Yuri."

        show natsuki cross ff neut om oe zorder 2 at f11

        n "Oh."

        show natsuki cross ff happ om oe zorder 2 at f11

        n "¿La estás acosando?"

        show natsuki cross ff happ cm oe zorder 2 at t11

        "No creo que esto se considere acoso..."

        show natsuki cross ff lsur cm oe zorder 2 at t11

        mc "Por favor, Natsuki, es un problema real."

        show natsuki cross ff lsur om oe zorder 2 at f11

        n "Uhm..."

        show natsuki turned ff worr om oe zorder 2 at f11

        n "Creo que la vi saliendo de la escuela."

        show natsuki turned ff lsur cm oe zorder 2 at t11

        mc "¿¡Sí!? ¿Y dónde podría haber ido?"

        show natsuki turned ff neut om oe zorder 2 at f11

        n "No estoy segura, pero cada vez que nos vamos juntas solemos despedirnos en la puerta de su casa."

        n "Nunca la he visto desviarse. De todos modos, vivimos a unas casas."

        show natsuki turned ff neut cm oe zorder 2 at t11

        mc "¿Y crees que haya ido ahí?"

        show natsuki turned ff curi om oe zorder 2 at f11

        n "Ni idea."

        show natsuki turned ff curi cm oe zorder 2 at t11

        mc "¿Y podrías llevarme ahí?"

        show natsuki turned lhip rhip ff vsur om ce zorder 2 at f11

        n "Así que ahora tengo que ayudar a un rarito a acosar a mi amiga."

        show natsuki cross ff pout cm oe zorder 2 at t11

        mc "Natsuki, esto es en serio. No es por mí, es por la seguridad de ella."

        show natsuki cross ff flus cm oe zorder 2 at f11

        n "Ya..."

        n "Supongo que si es por eso te ayudaré, pero no menciones que fui yo."

        show natsuki cross ff flus cm oe zorder 2 at t11

        "Natsuki me lleva afuera de la escuela."

        #transición a la casa de Yuri
        
        scene bg street1_morn
        with dissolve_scene_full

        "¿En serio Natsuki estaba buscando monedas por eso? Sé que no debería de meterme, pero qué tan mal estará."

        "Para tener que hacerlo... Podría intentar habl—"

        show natsuki cross ff dist om oe zorder 2 at f11

        n "¿Qué sucede con Yuri?"

        show natsuki cross ff neut cm oe zorder 2 at t11

        mc "Hubo una pelea en el club y ella salió rápidamente."

        show natsuki turned ff pout om oe zorder 2 at f11

        n "Pelea de... ¿de golpes?"

        show natsuki turned ff pout cm oe zorder 2 at t11

        mc "No, fue más una discusión. Disculpa, es que me golpeé la cabeza mientras intentaba buscar a Yuri."

        "Natsuki suspiró."

        show natsuki turned ff pout cm oe zorder 2 at f11

        n "Oye."

        show natsuki turned ff sad om oe zorder 2 at f11

        n "Si Yuri necesita hablar con alguien o la está pasando mal, dile que..."

        show natsuki turned ff angr om oe zorder 2 at f11

        n "La puedo apoyar, somos amigas de todos modos."

        show natsuki turned ff sad cm oe zorder 2 at t11

        mc "Sí, se lo diré."


        scene bg casa_yuri

        with dissolve_scene_full

        "Seguí caminando junto a ella. Me pregunto cómo estará Yuri... ya llevamos caminando un tiempo."

        "El suficiente tiempo para que ell—"

        show natsuki turned ff anno om oe zorder 2 at f11

        n "Oye, ya llegamos. Si te estás arrepitiendo, mejor lárgate a tu casa."

        show natsuki turned ff anno cm oe zorder 2 at t11

        "Natsuki me sacó de mis pensamientos empujándome."

        mc "Muchas gracias, Natsuki, realmente me ayudaste mucho."

        show natsuki cross angr om ce zorder 2 at f11

        n "Sí, bueno, de nada. Espero esté bien y tú también."

        show natsuki cross angr om ce zorder 2 at thide
        hide natsuki

        "Natsuki se alejó de mi vista."

        stop music fadeout 1.5

        "Me acerqué a la puerta, es una casa muy grande para solo una persona. Espero no estén sus padres."

        "¿Cuánto tiempo llevará Yuri lidiando con esto sola...?"

        "Presioné el timbre con fuerza."

        "Pero nadie vino."

        "Lo presioné de nuevo."

        mc "¡Yuri! ¿Te encuentras en casa?"

        "Resonó el sonido de las cortinas al cerrarse desde la segunda planta."

        mc "Solo quiero hablar contigo..."

        "Por lo menos sé que está aquí."

        "¿Pero qué puedo hacer?"

        #okay como tal aqui pongo la base pero siento que aqui vendria hiper bien una elección
        #agregar sonido de timbre o de tocar puertya

        "No quiere ayuda..."

        "Toqué la puerta."

        mc "¡Yuri, traje nuestro libro para que podamos leerlo... quizás en otro lugar como tu casa!"

        "Los segundos se sienten eternos."

        "Luego de más de un minuto, escucho la cerradura abrirse lentamente."

        "Aunque la puerta se abría, se detuvo abruptamente."

        play music audio.heartbreaking2 fadein 2.0

        y "¿[player]...?"

        y "¿Qu-qué haces aquí?"

        mc "Como te fuiste temprano del club, pensaba en que podríamos, ya sabes, leer."

        y "Deberías de irte."

        "La puerta se empezó a cerrar lentamente e inmediatamente puse mi pie bloqueándola."

        mc "Lo siento, Yuri, pero no pienso dejarte sola. Quieras o no, estaré para ti."

        "Sonaba mejor en mi cabeza..."

        "Pero no quiero que algún día no pueda volverla a ver por culpa de esto."

        "La puerta dejó de poner resistencia."

        mc "Gracias..."

        scene bg yuri_sala
        with wipeleft_scene

        "Entré dentro de la casa, aunque en la entrada no vi a Yuri."

        "Pasé a la sala con preocupación y ahí estaba ella..."

        show yuri turned casual rcut worr cm oe zorder 2 at t11

        "Pude ver su antebrazo, lleno de cortes, aunque algunos aún siguen abiertos... o nuevos."

        mc "Yuri..."

        "Esta pobre chica ha estado lidiando con esto todo este tiempo."

        show yuri turned rcut worr om oe zorder 2 at f11

        y "Lo siento... No quería mostrarte cómo realmente soy y... que me dejaras de hablar..."

        show yuri turned rcut worr cm oe zorder 2 at t11

        mc "No te dejaré de hablar, Yuri."

        show yuri turned rcut lsur om oe zorder 2 at t11

        "Saco el libro de mi mochila."

        show yuri turned rcut lsur cm oe zorder 2 at t11

        mc "¿Continuamos donde lo dejamos?"

        show yuri turned rcut lsur om oe zorder 2 at f11

        y "O-okay..."

        show yuri turned rcut lsur cm oe zorder 2 at t11

        "Ya no está tratando de evitarme. Yuri dudó unos segundos antes de hablar."

        show yuri turned rcut flus om oe zorder 2 at f11

        y "Necesito subir a limpiarme."

        show yuri turned rcut flus cm oe zorder 2 at t11

        mc "Claro, tómate tu tiempo."

        show yuri turned rcut flus cm oe zorder 2 at thide
        hide yuri

        stop music fadeout 2.0

        "Ella subió las escaleras, no sin antes verme. Nuestros ojos chocaron otra vez, pero esta vez..."

        "No fue como en la escuela. Ella está confiando en mí..."

        "Tomo asiento en el sofá y abro el libro en la última página que leímos."

        "¿Cómo puedo ayudarla...?"

        "Me toqué la cabeza y sentí un dolor punzante. Suspiré esperando a Yuri."

        #transición y sonido del bzzt

        with wipeleft_scene

        "*bzzt*"

        "*bzzt*"

        "Mi celular empezó a vibrar desde mi bolsillo. ¿Será Sayori?"

        "Atiendo el mensaje."

        #agregar el ??? y el sondio de bzzt para no hacerse wey
        #añadir escena de Yuri con Yuri chiquita

        "???" "Deja de evitarme."

        mc "¿Qué?"

        "???" "Ella no te merece, créeme, es una loca."

        mc "Quizás te estés confundiendo de número, soy [player]."

        "No recibí respuesta."

        "¿Quién er—"

        y "¿[player]?"

        play music audio.heartbreaking2 fadein 2.0

        "Del susto, tiré mi celular al suelo."

        show yuri turned casual lup rup flus om oe zorder 2 at f11

        y "Dis-disculpa, no quería asustarte."

        y "¿Estabas haciendo algo importante? Creo que te vi chateando con alguien."

        show yuri turned casual lup rup flus cm oe zorder 2 at t11

        "Noto que mi celular está tirado en el suelo. Me asustó más el mensaje que Yuri."

        mc "No, es solo que me tomaste de sorpresa."

        "Recogí mi celular del suelo. El número desconocido estaba escribiendo; sin embargo, guardé mi celular."

        "Aunque aún me pregunto quién será, realmente me importa más Yuri en estos momentos."

        mc "De hecho, te estaba esperando."

        show yuri turned casual rup lsur cm oe zorder 2 at t11

        "Todo ha estado pasando muy rápido."

        "Todo ha sido demasiado rápido y, aunque quiero ayudar, mi cuerpo se siente cansado."

        #añadir el efecto de panico aunque me critiquen 

        show yuri turned casual rup worr om oe zorder 2 at f11

        y "Pe-perdona, te hice esperar mucho tiempo."

        show yuri turned casual rup worr cm oe zorder 2 at t11

        "Yuri se sentó a mi lado. La miré unos segundos a los ojos."

        "Saqué el libro."

        mc "Deberíamos de continuar, ¿no?"

        #añadir la historia aunque me critiquen

        #porcierto dependiendo de la historia este dialogo cambiará debido a que todavia no hay una historia definida, aunque me critiquen

        "Después de leer esa línea dejé de concentrarme en la historia. Miré a Yuri, pero ella no hizo lo mismo."

        "\"El chico de la historia me recuerda a ti, Yuri.\""

        #si no me hago wey añado el efecto de recuerdos, aunque me critiquen

        "Yuri... sus ojos violetas están llorando."

        show yuri turned casual sad om oe zorder 2 at f11

        y "¿Sabes por qué elegí este libro para que podamos leerlo, [player]?"

        show yuri turned casual sad cm oe zorder 2 at t11

        "..."

        show yuri turned casual flus om oe zorder 2 at f11

        y "Porque no sé cómo hablar con los demás."

        y "No sé cómo describir mis sentimientos."

        y "Mis problemas... Solo sé leer libros."

        y "Creí que al compartir este libro podría mostrarte un vistazo de cómo soy en realidad."

        show yuri turned casual cry om ce zorder 2 at f11

        y "Pero... fue un terrible error porque ahora..."

        show yuri turned casual cry om oe zorder 2 at f11

        y "Ves cómo realmente soy..."

        show yuri turned casual cry cm oe zorder 2 at t11

        mc "Yo..."

        show yuri turned casual rup cry cm oe zorder 2 at t11

        "Las palabras no salieron de mí. Intento acercarme a Yuri, pero ella retrocedió."

        show yuri turned casual rup cry om ce zorder 2 at f11

        y "Sé por qué estás aquí."

        show yuri turned casual rup cry om oe zorder 2 at f11

        y "No querías leer... tú viniste porq- porque..."

        show yuri turned casual rup cry cm oe zorder 2 at t11

        "Yuri no pudo continuar hablando."

        show yuri turned casual neut me e1g b1b zorder 2 at t11

        "¿Por qué vine aquí?"

        "Recientemente conocí a Yuri, pero es alguien importante para mí."

        mc "Es cierto, no vine aquí para continuar leyendo."

        "Levantó la mirada hacia mis ojos, yo también hacia los suyos."

        mc "No vine porque sentía pena por ti."

        mc "Vine porque..."

        mc "Quisiera ayudar, pero ayudarte a ti, Yuri."

        mc "Lo que haces es peligroso."

        mc "Un día podrías equivocarte y... no podría volverte a ver."

        show yuri turned casual cry cm ce zorder 2 at f11

        y "[player]..."

        show yuri turned casual neut mi e1g b1b zorder 2 at f11

        y "No puedo parar."

        y "Ya lo he intentado varias veces."

        show yuri turned casual rup neut mi e1g b1b zorder 2 at f11

        y "Sé lo que me podría pasar si me llegara a equivocar por un centímetro; sin embargo..."

        y "No."

        y "Puedo."

        y "dejar de hacerlo."

        show yuri turned casual rup neut md e1g b1b zorder 2 at t11

        "Regresé a acercarme a Yuri, pero en lugar de retroceder, ella se quedó quieta."

        "Suavemente agarré su mano con la mía. Sostuve su pálida y fría mano."

        mc "Pero esta vez, no estás sola."

        mc "Prometo ayudarte en todo lo posible para que juntos podamos superar esto."

        mc "Tú y yo."

        show yuri turned casual rup cry om oe zorder 2 at f11

        y "Pero... yo solo te he arrastrado hasta aquí."

        y "Estuviste en el momento cuando le dije a Monika... Es-estabas ahí y aun así decidiste seguir."

        show yuri turned casual rup cry cm oe zorder 2 at t11

        "Porque te amo, Yuri."

        mc "Porque es lo que debería de hacer, Yuri: ayudarte sin importar la circunstancia."

        "Te amo."

        "Pero..."

        "No sé qué es amar..."

        show yuri turned casual rup cry om oe zorder 2 at f11

        y "[player]... yo nunca he tenido amigos."

        show yuri casual rup cry cm oe zorder 2 at t11

        mc "Eso no es cierto."
    
        mc "Me tienes a mí. Prometo hacer todo lo posible con tal de que nada ni nadie te lastime."

        show yuri turned casual rup sad cm ce zorder 2 at t11

        y "..."

        show yuri turned casual sad cm oe zorder 2 at t11

        "Quizás este sea el momento indicado."

        "Agarré mi mochila y de ella saqué una hoja de papel."

        mc "Sé que no estamos en el club, pero..."

        mc "Escribí esto... para ti."

        show yuri turned casual lup rup worr om oe zorder 2 at f11

        y "¿Para mí?"

        show yuri turned casual lup rup worr cm oe zorder 2 at t11

        mc "¿Recuerdas lo que me dijiste acerca de plasmar mis pensamientos? Lo hice expresando..."

        mc "Lo que siento por ti."

        show yuri turned casual lup rup sad om oe zorder 2 at f11

        y "Pe-pero, no escribí nada."

        show yuri turned casual lup rup sad cm oe zorder 2 at t11

        mc "Está bien. ¿Te gustaría leerlo?"

        "Estiro mi mano para darle el poema a Yuri."

        "Ella asiente y sostiene la carta."

        #aqui se agrega el poema 

        show yuri turned casual lup cry cm ce zorder 2 at t11

        "De repente, ella empieza a lagrimear. Sus mejillas quedan mojadas por las gotas de sus ojos."

        show yuri turned casual lup cry cm oe zorder 2 at t11

        mc "Yuri, realmente quisiera apoyarte."

        mc "Ayer vi cómo Monika te dijo algo en voz baja y cómo me evitaste."

        show yuri turned casual lup cry om oe zorder 2 at f11

        y "Y-yo..."

        show yuri turned casual lup cry cm oe zorder 2 at t11

        "La voz de Yuri se quebró, su manga se volvió rojiza. Ella no había limpiado sus brazos..."

        "Yuri se levantó. Antes de que siguiera, la agarré de la mano."

        show yuri turned casual lup cry om oe zorder 2 at f11

        y "[player], por favor..."

        show yuri turned casual lup cry cm ce zorder 2 at f11

        mc "Confía en mí."

        show yuri turned casual lup cry cm oe zorder 2 at f11


        #añadir Yuri con cortes casual

        show yuri turned casual lup rcut cry cm oe zorder 2 at f11


        "Aunque no muy segura, me dio suavemente su mano. La manga bajó sola."

        "Yuri..."

        "Yuri tiene varios cortes... nuevos, viejos... ligeros y... profundos."

        "Cicatrices sobre cicatrices."

        "No puedo quedarme quieto observando."

        mc "¿Tienes un botiquín o curas?"

        y "Creo que sí..."
        stop music fadeout 2.0
        
        scene bg bedroom
        with dissolve_scene_full
        play sound closet_open

        "10:43 AM"

        "Este sábado es lo que más necesito luego de una semana tan complicada."

        "Yuri pudo confiar en mí e incluso me pudo dar su número."

        "Pero aún me inquieta todo lo demás..."

        "Sayori llorando en el club y yo, siendo su mejor amigo, no pude apoyarla..."

        "Natsuki también parece tener un problema que aún no puedo saber."

        "Desde ayer he estado recibiendo mensajes de un número extraño."

        "Se me está complicando seguir el ritmo a todo... Siento que en algún momento solo caeré en el suelo."

        "Pero Yuri..."

        "Luego de curar sus heridas, quedamos en que íbamos a salir hoy."

        "Aunque estuve nervioso luego de irme de su casa, yo confío en Yuri."

        "Es un día hermoso allá afuera."

        #cambio de escena a la cocina
        
        scene kitchen
        with wipeleft_scene

        "Saqué mi teléfono para escribirle a Yuri. Desde que me fui de su casa no hemos hablado mucho."

        mc "Hola Yuri, estoy saliendo de mi casa, pero antes de ir quería saber cómo estás."

        "Sé que hoy será un día bueno para ambos."

        "*bzzt*"

        y "Ya me encuentro lista, gracias por preguntar."

        #cambio de escena suave
        
        scene house
        with wipeleft_scene 

        "Me acerqué a la puerta de la casa."

        "Toqué el timbre."

        pause 0.5
        #agregar sonido de timbre

        "Escuché cómo la puerta se abrió."

        #agregar ropa de Yuri

        show yuri 1cb zorder 2 at f11

        play music audio.t6 fadein 2.0

        y "Hola [player]."

        show yuri 1ca zorder 2 at t11
        
        mc "Pensaba que me ibas a dejar plantado."

        show yuri 1co zorder 2 at f11

        y "U-uh, no, claro que no haría eso."

        show yuri 1ca zorder 2 at t11

        mc "No, lo digo en serio... Entonces... ¿me acompañas?"

        show yuri 1cd zorder 2 at f11

        y "¡Sí! Por supuesto."

    

        #escena de transición 
        show yuri 1cd zorder 2 at thide
        hide yuri

        scene bg ciudad_calle_nublado
        with wipeleft_scene 

        show yuri 1cu zorder 2 at t11

        "Estuvimos caminando juntos por la calle."

        "Aunque Yuri seguía mi paso lentamente."

        "Hay muchas plazas en la ciudad."

        "Restaurantes, tiendas, centros comerciales... ¿A dónde le gustará ir a Yuri?"

        "Mientras seguimos recorriendo la ciudad noto una cafetería. A ella le gusta el té, supongo que es buena idea."

        show yuri 1ce zorder 2 at t11

        mc "¿Te gustaría ir a esa cafetería?"

        show yuri 1cd zorder 2 at f11

        y "Me parece bien. En realidad, suelo visitar este lugar frecuentemente."

        scene bg cafe
        with wiperight_scene

        show yuri 1ce zorder 2 at t11

        "Mientras estábamos en el menú, me puse a analizarlo."

        mc "Ya que sueles ir aquí, ¿alguna recomendación?"

        show yuri 1cf zorder 2 at t11

        y "Uh, hay demasiadas cosas para probar. No quisiera elegir algo que no te guste."

        show yuri 1cf zorder 2 at t11

        mc "Tranquila, no soy tan exigente."

        show yuri 1cb zorder 2 at f11

        y "Supongo que... podrías beber un té blanco."

        show yuri 1ca zorder 2 at t11

        mc "Me parece bien. ¿Y qué escogerás?"

        show yuri 1cb zorder 2 at f11

        y "Un té Oolong."

        show yuri 1cc zorder 2 at t11

        mc "Oh, creo que ese fue el que bebimos mientras estábamos en el club."

        show yuri 1cd zorder 2 at f11

        y "Sí, es ese mismo."

        show yuri 1ca zorder 2 at t11

        "Sí, el club."

        "¡Sayori! Después de terminar esta cit... salida, iré a ver cómo está ella."

        "Me he olvidado completamente de ella... de cómo ha estado."

        show yuri 1cv zorder 2 at f11

        y "(Hola, ¿me da un té Oolong?)"

        y "(¿Hola, me podría dar un té Oolong?)"

        y "(¿Podría pedir un té Oolong?)"

        show yuri 1co zorder 2 at t11

        "Me volteé hacia Yuri."

        mc "¿Me estabas diciendo algo?"

        show yuri 1cq zorder 2 at f11

        y "Estaba practicando lo que iba a pedir."

        y "¿No te sueles preparar mentalmente para pedir algo?"

        show yuri 1cu zorder 2 at t11

        mc "¿Qué?"

        show yuri 1cq zorder 2 at f11

        y "Oh, sí... qué vergüenza... Yo suelo hacerlo seguido."

        show yuri 1cw zorder 2 at t11

        "Mierda, ¿cómo podría recuperar la situación?"

        ##################
        show yuri 1cs zorder 2 at t11
        mc "No suelo hacerlo, pero siento que todos nos preparamos para algo en cierta medida."



        #aqui una elección. mas arriba quizas 

        show yuri 1cn zorder 2 at t11

        mc "Además, es lindo."

        show yuri 1cn zorder 2 at f11

        y "¡Qué!"

        stop music fadeout 2.0

        show yuri 1ce zorder 2 at t11
        
        "Camarero" "Siguiente."

        "Camarero" "Buenos días, ¿qué les gustaría ordenar?"

        mc "Un té blanco para mí, por favor."

        "Camarero" "Anotado. ¿Y usted, señorita?"

        show yuri 1co zorder 2 at f11

        y "Uhhh... u-un..."

        y "U-un... té... té OO—"

        show yuri 1cn zorder 2 at t11

        "Cliente" "¿Oigan, podrían apurarse? Tengo un tiempo limitado."

        "Camarero" "Señorita, ¿un té de?"

        "El vendedor deja de mirar a Yuri y voltea a ver a la fila de atrás."

        "Camarero" "¿Podría apurarse, por favor?"

        #aqui eleccion de si pedir por yuri o deja que Yuri elija, la hisotira como tal seguira aqui por una manera de la ruta buena

        show yuri 1ck zorder 2 at t11
        mc "A ella le gustaría un té Oolong."

        "Camarero" "Té Oolong y blanco. ¿Sería todo?"
        show yuri 1ck zorder 2 at thide
        hide yuri

        mc "Sí, gracias."

        "Pagué la orden y, junto a Yuri, nos sentamos en una mesa vacía, cerca de las ventanas del lugar."

        show yuri 1cv zorder 2 at f11

        y "L-lo hice terrible... y seguramente te hice pasar pena. Lo siento."

        show yuri 1cu zorder 2 at t11

        mc "No hay de qué disculparse, Yuri."

        show yuri 1cw zorder 2 at f11

        y "Pe-pero ese señor nos gritó..."

        show yuri 1cv zorder 2 at f11

        y "Te avergoncé, ¿verdad?"

        show yuri 1cv zorder 2 at t11

        mc "Yuri, si quieres saber mi respuesta, deja de voltear la mirada."

        show yuri 1cs zorder 2 at t11

        mc "Yuri, está bien. No estoy avergonzado ni nada parecido y, sobre todo..."

        mc "A quién le importan las personas que gritan por cualquier mínima cosa."

        mc "No te preocupes por lo que digan los demás."

        show yuri 1ct zorder 2 at f11

        y "Me preocupo por lo que digas tú..."

        show yuri 1cs zorder 2 at t11


        mc "Entonces todo está bien. En realidad, yo debería de pedir perdón."

        mc "Te distraje mientras te preparabas para pedir."

        show yuri 1cf zorder 2 at f11

        y "Gracias por ordenar por mí, en serio lo aprecio."

        show yuri 1ca zorder 2 at t11

        mc "No hay problema."

        "*Bzzt*"

        "El camarero pone las órdenes en la mesa."

        "*Bzzt*"

        mc "Y ¿ya ha—"

        "*Bzzt*"

        show yuri 1cb zorder 2 at f11

        y "Puedes contestar, no me molesta."

        show yuri 1ca zorder 2 at t11

        mc "No, solo lo apagaré un rato. Dame un momento."

        "Agarré mi celular y vi los mensajes del número desconocido."

        "???" "¿Ya responderás? ¿Estás ocupado \"bebiendo té\"?"

        mc "Jódete."

        "Apagué mi celular."

        show yuri 1ce zorder 2 at t11

        mc "Sabes, me gustaba pasar tiempo en el club contigo."

        show yuri 1cd zorder 2 at f11

        y "A mí también, era agradable... Eres..."

        show yuri 1ca zorder 2 at t11

        mc "Honestamente, me uní al club por los cupcakes y Sayori."

        show yuri 1cj zorder 2 at f11

        y "Siendo sincera, cuando me uní al club pensé que podría encontrar amigos con gustos similares a los míos."

        show yuri 1ct zorder 2 at f11

        y "Como la pasión que tengo por los libros. Siempre me he sentido un poco aislada de los demás."

        y "Tenía la esperanza de poder dejar de ser tan indiferente..."

        y "Parece que no salió como me esperaba."

        show yuri 1cw zorder 2 at f11

        y "Monika."

        y "Ella me invitó al club primeramente."

        show yuri 1cv zorder 2 at f11

        y "No quisiera que la odies... por mi culpa."

        y "Sé que es una buena persona..."

        show yuri 1cu zorder 2 at t11

        "¿Una buena persona?"

        "Una buena persona no diría que te suicides."

        "Pero una buena persona tampoco diría que va a matar a alguien..."

        show yuri 1cu zorder 2 at t11

        mc "Prefiero no hablar de ella, pero..."

        show yuri 1cs zorder 2 at t11

        mc "Estás equivocada en lo de socializar, me refiero. Estás aquí conmigo."

        mc "Tienes a Natsuki que, si excluyes las diferencias, estoy seguro de que serían buenas amigas."

        mc "También a Sayori, quien estoy seguro de que te considera su amiga."

        mc "Me encanta estar contigo hoy, pero odio que la razón por la que estemos aquí sea Monika."

        show yuri 1ct zorder 2 at f11

        y "Tienes razón, de nuevo."

        show yuri 1cb zorder 2 at t11

        "Yuri me sonríe, dejando su pena atrás."

        "Tomé un sorbo de mi taza de té."

        show yuri 1cd zorder 2 at t11

        mc "Elegiste bien, Yuri."

        show yuri 1ce zorder 2 at t11

        mc "Oye, Yuri, ahora que lo pienso, ¿te gustaría acompañarme a la casa de Sayori?"

        show yuri 1cf zorder 2 at f11

        y "No tengo problema, pero suenas preocupado por algo."

        show yuri 1ct zorder 2 at t11

        mc "Ella se veía muy decaída el día que nos fuimos temprano del club."

        mc "Y quería pasar por lo menos a saludarla y que no se sienta sola en esto."

        show yuri 1cw zorder 2 at f11

        y "Por estar discutiendo no me di cuenta de cómo los demás la estaban pasando a mi alrededor..."

        show yuri 1ct zorder 2 at f11

        y "Personas que la están pasando peor que yo..."

        show yuri 1cq zorder 2 at f11

        y "Me gustaría acompañarte y espero poder hablar con Sayori acerca de..."

        y "De lo que pasó."

        show yuri 1ca zorder 2 at t11

        mc "Estoy seguro de que ella se pondrá súper feliz de vernos a ambos."

        "Luego de finalizar nuestras bebidas, salimos de la cafetería para dirigirnos a la casa de Sayori."

        
        scene residential
        with wipeleft_scene 

        show yuri 1cu zorder 2 at t11

        "Llegamos a la casa de Sayori y toqué la puerta."

        "..."

        "Sin respuesta."

        "..."

        show yuri 1ct zorder 2 at f11

        y "Quizás ella no esté en casa."

        show yuri 1cn zorder 2 at t11

        "Abrí la puerta de la casa."

        show yuri 1cn zorder 2 at f11

        y "¿Oy-Oye, estás seguro de hacer eso?"

        show yuri 1cn zorder 2 at t11

        mc "¿Por qué no?"

        mc "Ella solía hacer lo mismo cuando no quería salir a jugar."

        show yuri 1cb zorder 2 at f11

        y "Recuerdo que Sayori nos solía hablar de anécdotas parecidas."

        show yuri 1ca zorder 2 at t11

        "Brrr"

        "Brrr"

        show yuri 1ci zorder 2 at f11

        y "Disculpa, [player], ¿puedes adelantarte? Atenderé la llamada."

        mc "Está bien, de todos modos veré si está Sayori."

        show yuri 1ci zorder 2 at thide
        hide yuri
        
        
        scene black 
        with dissolve_scene_full

        mc "¿Sayori?"

        "Es extraño el silencio o no tener una bienvenida de Sayori."

        "Quizás sí le haya afectado el ánimo lo que ocurrió..."

        "Subí las escaleras y me dirigí a su puerta."

        "..."

        mc "¿Sayori, puedo entrar?"

        "..."

        mc "Oye, en serio quiero hablar contigo, así que espero que no estés dorm—"

        show sayori turned casual rup flus om oe zorder 2 at f11

        scene bg sayori_bedroom
        with dissolve_scene_full

        s "¿¡[player]!?"


        s "Qué... ¿Qué haces aquí?"

        show sayori turned casual rup flus cm oe zorder 2 at t11

        mc "Bueno, quería visitarte y no vengo solo, también Yuri."

        show sayori turned casual dist om oe zorder 2 at f11

        s "Oh, Yuri... Qué bueno."

        show sayori turned casual dist cm oe zorder 2 at t11

        "Sí, definitivamente Sayori está desanimada."

        "Me quedé parado en el umbral de la puerta, en un silencio incómodo."

        show sayori turned casual laug om oe zorder 2 at f11

        s "Así que ¿tú y Yuri, no?"

        show sayori turned casual happ cm oe zorder 2 at t11

        mc "N-No lo malinterpretes, solo estamos aquí como amigos."

        show sayori turned casual neut om oe zorder 2 at f11

        s "Es difícil ocultar los sentimientos, sobre todo cuando los ves todos los días."

        s "Desde el primer día noté esa conexión entre ustedes."

        show sayori turned neut n2 md e1b b1b zorder 2 at t11

        "Esto... no suena como lo diría Sayori. Parece más... ¿honesto?"

        mc "Sea lo que sea que intentes decir, estoy seguro de que estás equivocada."

        show sayori turned sad om oe zorder 2 at f11

        s "Me alegra que sean amigos... Y-Yo... Estoy feliz por eso."

        show sayori turned sad cm ce zorder 2 at t11

        mc "¿Sayori?"

        play music audio.t10

        show sayori turned neut n1 mj e1g b1c zorder 2 at t11

        "Ella tiene los ojos lagrimosos, no sé qué está pasando."

        mc "¿Sayori, sucede algo?"

        "Entré a su cuarto."

        mc "Sé que está pasando algo."

        mc "Como mencionas, es difícil ocultar los sentimientos y más si te conozco desde la infancia."

        show sayori turned neut n1 mb e1g b1c zorder 2 at t11

        "Sayori se limpió los ojos."

        show sayori turned neut n1 mb e4d b1c zorder 2 at f11

        s "Jejeje..."

        show sayori turned neut n2 mg e1g b1c zorder 2 at f11

        s "Estás equivocado, [player]."

        s "Siempre he sido así, pero por primera vez no puedo ocultarlo."

        show sayori turned neut n2 me e1g b1c zorder 2 at t11

        mc "¿Ocultar qué, Sayori?"

        show sayori turned worr om oe zorder 2 at f22

        s "Ocultar... N-No... Creo que deberías de irte, no debes de verme así..."

        show sayori turned worr cm oe zorder 2 at t22

        "Sayori..."

        "Siento la misma sensación de cuando vi a Yuri cortándose... Puedo ver en Sayori esa misma expresión."

        mc "Sayori, si hay algún problema que haya ocurrido, solo dime. ¿Es por lo del clu—"

        show sayori turned sad om oe zorder 2 at f11

        s "No creo que lo entiendas, [player]. Yo no quiero ser ayudada."

        show sayori turned sad cm oe zorder 2 at t11

        "\"No quiero tu ayuda.\""

        show sayori turned sad om ce zorder 2 at f11

        s "La ayuda solo es para quienes se lo merecen."

        show sayori turned sad cm oe zorder 2 at t11

        "Mi mente no está soportando las palabras de Sayori."

        mc "Sayori, sé honesta conmigo, por favor. ¿Qué sucede?"

        show sayori turned sad om ce zorder 2 at f11

        s "Jeh... ¿En serio quieres que lo diga, verdad?"

        s "[player]..."

        show sayori turned laug cm ce zorder 2 at f11

        s "He pasado toda mi vida lidiando con la depresión."

        s "Siempre he tenido esos pensamientos en mi mente; que no debería de ser feliz, que no debería de continuar."

        show sayori turned cry om oe zorder 2 at f11

        s "¿Sabes por qué salgo tarde para la escuela?"

        s "Porque todos los días no encuentro una razón para levantarme de la cama y caminar."

        s "Todos los días no encuentro una razón para comer, para continuar."

        s "Cuando llego al instituto, solo pienso en irme."

        show sayori turned cry om ce zorder 2 at f11

        s "¿Por qué cuando despierto no puedo ver el sol? Solo veo unas nubes grises."

        show sayori turned cry om oe zorder 2 at f11

        s "¿Por qué cuando salgo de mi casa empieza a llover?"

        s "Dime por qué todos los días tengo que fingir una personalidad que no soy con tal de no afectar a los demás."

        s "¿Por qué hacer amigos cuando todos ellos solo me usan para poderse sentir mejor consigo mismos?"

        show sayori turned cry cm ce zorder 2 at f11

        s "Cuando siempre eres vista como \"la tonta.\""

        s "La chica que siempre está forzando una sonrisa."

        show sayori turned cry om oe zorder 2 at f11

        s "Por qué abrir los ojos todas las mañanas..."

        s "Cuando la única persona y razón por la cual intento aguantar todo este dolor y continuar..."

        show sayori turned neut om oe zorder 2 at f11

        s "¡Está enamorado de otra chica!"

        show sayori turned neut cm oe zorder 2 at t11

        "Siento como si mi mundo se estuviera destruyendo por cada palabra de Sayori."

        "He estado ignorando... a la chica que siempre me ha intentado ayudar..."

        show sayori turned neut cm oe zorder 2 at thide
        hide sayori 

        scene black
        with dissolve_scene

        s "¿E-Eh?"

        "Abracé a Sayori, realmente no pude aguantar las lágrimas del momento."

        mc "Perdóname..."

        mc "Siento no haber estado contigo todo este tiempo..."

        mc "Siento no haberme dado cuenta de esto..."

        mc "Te prometo que a partir de hoy haré todo lo posible para que te sientas me—"

        s "[player]..."

        "Sayori no me devolvió el abrazo."

        "Ella puso sus manos en mi pecho para alejarme."

        s "No lo entiendes."

        scene bg sayori_bedroom
        with wipeleft_scene
        show sayori turned casual lup rup cry cm oe zorder 2 at f11

        s "Nadie puede entenderlo."

        s "No quiero que tú... que alguien se preocupe por mí."

        s "Es agridulce conocerlo... ¿cierto?"

        show sayori turned casual lup rup neut n1 ma e1h b2c zorder 2 at t11

        "Mi corazón está latiendo muy fuerte y... quiero ayudarla, pero mi mente no coopera..."

        show sayori turned casual lup rup neut n1 mc e1h b2c zorder 2 at f11

        s "A veces logro sentirme bien, pero inmediatamente siento como si la culpa me estuviera aplastando sin cesar."

        s "Ya entendí por qué realmente viniste."

        show sayori turned casual lup rup neut n1 mc e4e b2c zorder 2 at f11

        s "Es el universo castigándome, sé que lo merezco... pero es tan horrible... tener este sentimiento."

        s "Verte aquí con Yuri..."

        show sayori turned casual lup rup neut n1 mc e1h b2b zorder 2 at f11

        s "Es como si me intentaras mantener viva mientras me incrustas una lanza en el pecho."

        s "Y tú, [player]..."

        s "Eres todo para mí, eres mi mundo. Cada vez que caminamos, cada vez que hablamos..."

        s "Me hace querer llorar por todo el dolor que siento."

        show sayori turned casual lup rup neut n1 mc e4e b2c zorder 2 at t11

        mc "Sayori..."

        show sayori turned casual lup rup neut n1 mc e1h b2c zorder 2 at t11

        "Quité sus manos de mi pecho y puse las mías en sus hombros."

        mc "Para mí es difícil poder entenderte y sé que he sido un estúpido todos estos años..."

        mc "Pero yo haré todo por ti, Sayori. Estaré siempre a tu lado..."

        show sayori turned casual lup rup neut n1 mh e1h b2c zorder 2 at f11

        s "Pero [player]..."

        show sayori turned casual lup rup neut n1 mj e1h b2c zorder 2 at f11

        mc "Sayori."

    # Mierda, no quiero continuar esta parte :(

    menu Sayori_eleccion:
        "Siempre serás mi mejor amiga.":
            "\"Tú siempre serás mi mejor amiga.\""
            jump siempre_serás_mi_mejor_amiga
        "Te quiero, Sayori.":
            mc "Sayori... Yo honestamente te quiero en mi vida."
            jump te_quiero_sayori

    label siempre_serás_mi_mejor_amiga:
        show sayori turned casual lup rup cry om ce zorder 2 at f11
        s "Vete..."

        show sayori turned casual lup rup cry om ce zorder 2 at t11

        mc "Pero, Sayori..."

        show sayori turned casual lup rup cry om oe zorder 2 at f11

        s "¡Vete de mi casa, por favor!"

        show sayori turned casual lup rup cry cm oe zorder 2 at t11

        "Intenté volverme a acercar a Sayori y ella tiró un espejo cerca de mí."

        show sayori turned casual lup rup cry om oe zorder 2 at f11

        s "¡Lárgate ahora mismo!"

        show sayori turned casual lup rup cry cm ce zorder 2 at t11

        mc "..."

        "Me fui de la habitación."
        show sayori turned casual lup rup cry cm ce zorder 2 at thide
        hide sayori
        


        jump yuri_continuación

    label te_quiero_sayori:
        
        scene black
        with dissolve_scene_full
        s "[player]..."
        s "Tú eres la única razón por la cual continúo viviendo todos los días."

        mc "Tranquila, Sayori... Siento que, a su vez, deberías de ir a un psicólogo."
        mc "Te acompañaré en cada terapia."

        s "[player]..."
        s "Gracias por estar aquí."
        s "No sé qué hubiera pasado en unos días..."

        "Abracé de nuevo a Sayori."
        "Y ella me devolvió el abrazo."
        with dissolve_scene_full


        jump yuri_continuación

    label yuri_continuación:
        stop music fadeout 1.5
        scene residential
        with dissolve_scene_full
        play music audio.t6 fadein 1.5
        "Salí de la casa de Sayori y cerré la puerta."

        "Yuri aún seguía en la llamada, pero luego de unos segundos colgó."

        show yuri 1ct zorder 2 at f11

        y "Y... ¿se encuentra bien Sayori?"

        show yuri 1ci zorder 2 at t11

        "Cómo quisiera poder mentirte en estos momentos..."

        mc "Sí, se encuentra en su habitación."

        show yuri 1cj zorder 2 at f11

        y "Entonces, ¿por qué cerraste la puerta de la casa? Te miras agitado..."

        show yuri 1co zorder 2 at t11

        mc "Sayori no quiere hablar en estos momentos."

        show yuri 1cn zorder 2 at f11

        y "¿Por qué?"

        show yuri 1ck zorder 2 at t11

        "Suspiré."

        mc "Es largo de explicar, pero Sayor—"

        # Añadir sonido de cerradura, de cuando se cierra una puerta

        mc "Será mejor irnos, Yuri..."

        show yuri 1ce zorder 2 at f11

        y "Está bien, [player]."

        y "Quizás solo necesite un tiempo para poder acomodar sus pensamientos. Espero lo mejor para ella."

        show yuri 1ca zorder 2 at t11

        mc "Sí..."

        "Sayori, mi mejor amiga, se confesó conmigo... Todos sus sentimientos, lo que llevaba cargando todo este tiempo."

        "Nunca pude llegar a pensar en que ella sufriría depresión."

        show yuri 1cg zorder 2 at t11

        "Siempre le he hecho bromas o me he burlado de ella por llegar tarde, estar despeinada... llevar el uniforme mal..."

        "Qué depresión tan fuerte tendrá ella... para costarle levantarse de la cama."

        "Todo ha sido mi culpa..."

        show yuri 1cg zorder 2 at f11

        y "¿[player]?"

        show yuri 1cg zorder 2 at t11

        mc "Perdóname... me perdí en mis pensamientos."

        show yuri 1ch zorder 2 at f11

        y "Hmm... Comúnmente, cuando me pasa eso, suelo ir a la biblioteca. Me ayuda a despejar la mente."

        show yuri 1ck zorder 2 at t11

        mc "Quizás un buen libro me ayude."

        mc "Entonces, ¿vamos?"

        show yuri 1cb zorder 2 at f11

        y "Por supuesto."

        show yuri 1cb zorder 2 at thide
        hide Yuri
        


        # Poner la escena de la biblioteca
        scene bg library_aft
        with dissolve_scene_full

        show yuri 1cb zorder 2 at f11

        y "Oye, [player], mira: es Guía del Sakura, la continuación de Insolación Infinita."

        show yuri 1ca zorder 2 at t11

        mc "¿Guía del Sakura? No suena como la continuación del libro que leemos."

        mc "¿Por qué Sakura?"

        show yuri 1ch zorder 2 at f11

        y "La chica se colgó en un árbol de Sakura."

        show yuri 1ck zorder 2 at t11

        mc "Sí... cierto."

        show yuri 1cm zorder 2 at t11


        # Aquí podemos hacer una especie de referencia a Sayori y que eso haga que Sayori lo recuerde

        mc "Cómpralo, así cuando terminemos el libro empezamos a leer el nuevo."

        show yuri 1cq zorder 2 at f11

        y "Sobre eso, todavía no ha salido. Solo es como una muestra de exhibición."

        show yuri 1ce zorder 2 at t11

        mc "Oh, qué curioso. Ir soltando pequeños adelantos de una historia para ir emocionando al público y recibir apoyo."

        mc "*Cof, cof*"

        show yuri 1ce zorder 2 at thide
        hide yuri

        "Estuve acompañando a Yuri por la biblioteca buscando un libro ideal."

        # Aquí quizás podríamos alargar un poco la escena agregando como que se encuentran x libro pero después...

        "Después de leer con Yuri, fuimos a dejar el libro en su lugar antes de retirarnos."

        "Vendedor" "Ey, Yuri, ¿cómo estás?"

        show yuri 1cq zorder 2 at t11

        "E inmediatamente Yuri salió de la biblioteca. Miré al vendedor y me quedé confundido."

        show yuri 1cq zorder 2 at thide
        hide yuri

        # Aquí poner escena de la ciudad
        
        scene bg ciudad_calle_nublado
        with wipeleft_scene 
        show yuri 1cq zorder 2 at t11

        mc "¿Oye, ese tipo te hizo algo?"

        show yuri 1cv zorder 2 at f11

        y "N-No es eso."

        show yuri 1cu zorder 2 at t11

        mc "¿Lo conoces?"

        show yuri 1cq zorder 2 at f11

        y "Y-Yo..."

        show yuri 1cq zorder 2 at t11

        "Creo que estoy poniendo más nerviosa a Yuri en lugar de ayudar."

        show yuri 1cu zorder 2 at t11

        mc "Está bien, tómate el tiempo que necesites."

        pause 5.0

        show yuri 1ct zorder 2 at f11

        y "Él suele intentar entablar conversaciones conmigo."

        show yuri 1ct zorder 2 at t11

        mc "Pero no te ha hecho nada malo, ¿cierto?"

        show yuri 1cw zorder 2 at f11

        y "N-No... Solo intento evitarlo cada vez que vengo aquí. Incluso cuando está atendiendo, espero a que acabe su turno."

        show yuri 1cq zorder 2 at t11

        mc "Bueno, quizás puedas decirle que no quieres hablar."

        show yuri 1cq zorder 2 at f11

        y "Decir..."

        show yuri 1cq zorder 2 at t11

        "Esto es un poco... surrealista. Estar con ella tanto tiempo no me ha permitido ver lo reservada que es."

        # Ahora casa de Yuri
        stop music fadeout 2.0
        
        scene bg casa_yuri
        with dissolve_scene_full
        play music audio.heartbreaking2 fadein 2.0
        show yuri 1cd zorder 2 at t11

        mc "Hoy fue un día increíble, Yuri. Quizás podríamos salir en otro momento."

        mc "Hasta luego, cuí—"

        show yuri 1cq zorder 2 at f11
        
        y "O-Oye, [player]..."

        y "¿No te gustaría entrar a mi casa y leer un rato?"

        show yuri 1cq zorder 2 at t11

        mc "..."

        show yuri 1cq zorder 2 at f11

        y "Olvídalo, has—"

        show yuri 1cn zorder 2 at f11

        mc "Por supuesto, Yuri, el gusto es mío."

        show yuri 1cn zorder 2 at thide
        hide yuri 


        # Casa de Yuri
        
        scene bg yuri_sala
        with wipeleft_scene

        "Ahora que lo recuerdo, no traje mi mochila donde tengo el libro."

        mc "Oye, Yuri, se me olvidó traer el libro."

        show yuri 1cb zorder 2 at f11

        y "Yo tengo una copia en la repisa."

        show yuri 1ca zorder 2 at t11

        mc "Ah, cierto, lo había olvidado."

        # Añadir fondo de la casa de Yuri de noche
        
        scene bg yuri_sala_noche
        with dissolve_scene_full

        show yuri 1cm zorder 2 at t11

        "Estuvimos leyendo una gran parte de la tarde. Creo que Yuri está dormida."

        mc "Yuri, despierta."

        "La moví un poco y lentamente ella abrió los ojos."

        show yuri 1co zorder 2 at f11

        y "A-Ah, disculpa, me quedé completamente dormida. ¿Qué hora es?"

        show yuri 1cs zorder 2 at t11

        "Revisé mi celular."

        "Sin carga."

        show yuri 1cg zorder 2 at f11

        y "21:59. Es muy tarde para que regreses solo."

        show yuri 1co zorder 2 at t11

        mc "Tampoco quisiera ser un intruso en tu casa, ¿sabes?"

        show yuri 1cb zorder 2 at f11

        y "Para mí está bien que te quedes."

        show yuri 1ca zorder 2 at t11

        mc "¿En serio? ¿Y dónde dormiría?"

        show yuri 1ch zorder 2 at f11

        y "(No puedo dejar que duermas en la sala, él es mi invitado...)"

        show yuri 1ch zorder 2 at t11

        "Espera, ¿en serio pasará lo que estoy pensando?"

        show yuri 1ch zorder 2 at f11

        y "Sé que sonará un poco ridículo, pero..."

        show yuri 1ch zorder 2 at t11
        
        "¿Yuri en serio me pedirá... que duerma con ella?"

        show yuri 1cq zorder 2 at f11

        y "Mi cama es bastante grande y cómoda..."

        show yuri 1cq zorder 2 at t11

        "Mi boca no responde."

        show yuri 1cv zorder 2 at f11

        y "Disculpa, dormiré aquí y tú en mi cuarto..."

        show yuri 1ca zorder 2 at t11

        mc "N-No, de hecho, no veo algún problema en que durmamos ambos."

        show yuri 1cc zorder 2 at f11
    
        y "Gracias, [player]."

        y "Por ti, mi día ha sido increíble."

        show yuri 1ca zorder 2 at t11

        mc "Gracias, Yuri, opino lo mismo de hoy."

        "Yuri me llevó a su cuarto."
        stop music fadeout 1.5
        
        with dissolve_scene_full

    return