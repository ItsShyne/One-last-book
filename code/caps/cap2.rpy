label cap2:

    $ ach_chapter2 = True
    $ ach_good_ending = True
    $ ach_secret_scene = True
    $ ach_all_yuri_poems = True
    
    stop music fadeout 2.0
    play music audio.t6
    scene bg corridor

    with dissolve_scene_full

    "Seguí a Sayori por los pasillos, Comunmente subimos aqui por materiales."

    "Sé que es un club con poca gente pero el que este tan alejado no ayuda"

    play audio closet_open

    "Sayori abrió la puerta del salón con fuerza."

    mc "¿No era más fácil abrirla gentilmente?"

    scene bg club_day

    show sayori 1s zorder 2 at f11

    s "¡¡¡Chicas!!! ¡¡¡traje a un nuevo miembro!!!"

    show sayori 1s zorder 2 at t11

    mc "No lo grites sayori..."

    "¿Chicas?"

    hide sayori

    with wipeleft_scene 
    #sirve para hacer una transición de izquierda a derecha, también se puede usar wiperight_scene, wipeup_scene, wipedown_scene

    "Mi mirada se centró en una chica de pelo morado."

    show yuri 2b zorder 2 at f11

    y "Bienvenido al club de literatura, es un placer conocerte [player]."

    show yuri turned rup uniform happ om ce zorder 2 at f11

    y "Sayori siempre nos habla bien de ti."

    y "Me alegra mucho poder conocerte."   

    show yuri turned lup rup uniform nerv cm oe zorder 2 at t11

    y "(¿Espera por qué dije eso en voz alta?)"

    show yuri turned lup rup uniform nerv cm oe zorder 2 at f11

    y "Uh..." 

    show yuri turned lup rup uniform nerv cm oe zorder 2 at t11

    pause 1.0

    show yuri turned rup uniform lsur cm oe zorder 2 at t11

    "Dios... es como si viera un angel en persona."

    "Es tan linda."

    "Nunca la he visto en el instituto, hubiera recordado sus hermosos ojos violeta."

    "Su cabello largo y morado... Esa personalidad tan tierna."

    "Luce como un sueño..."

    n "¿Enserio era necesario un chico?"

    show yuri shy neut cm oe zorder 2 at t22

    

    show natsuki 1h zorder 2 at f21

    n "Qué incómodo será el club desde ahora."

    show yuri shy neut cm oe zorder 2 at t32

    show natsuki 2g zorder 2 at t31

    show monika 4b zorder 2 at f33

    m "¡Ey! que bonita sorpresa [player]"

    show natsuki 2g zorder 2 at t31

    show monika 2k zorder 2 at f33

    m "bienvenido al club de literatura"

    "Sayori... Sayori me trajo a un club..."

    show monika zorder 2 at thide
    hide monika

    show natsuki zorder 2 at thide
    hide natsuki

    show yuri 1d zorder 2 at t11

    "¡Qué tiene a una chica tan linda!"

    show yuri 1e zorder 2 at t21

    show natsuki 2w zorder 2 at f22

    n "¿Qué nunca has visto a una mujer?"

    show yuri 1e zorder 2 at t21

    show natsuki turned anno cm oe zorder 2 at t22

    mc "Dis-disculpa."

    show yuri 1w zorder 2 at t42

    show natsuki 2w zorder 2 at t44

    y "Natsuki... recuerda que es nuestro nuevo miembro."

    show yuri 1w zorder 2 at thide

    hide yuri

    show natsuki 3i zorder 2 at t11

    "Parece que la chica de cabello rosado es un poco dificil..."

    "Por su apariencia será alguien de primer año asi que no vale la pena enojarse con ella."

    "¿Le dijo Natsuki? probablemente sea quien hizo los pastelitos."

    show yuri 2i zorder 2 at t32

    show natsuki 3i zorder 2 at t33

    show sayori turned happ om ce zorder 2 at f31

    s "Tranqui [player], solo ignorala cuando esté de mal humor."

    show sayori turned happ om ce zorder 2 at f31

    "Sayori se acercó a mi sonando sus pasos contra el suelo."
    show yuri 2i zorder 2 at thide
    show sayori turned happ om ce zorder 2 at thide 

    hide yuri

    hide Sayori

    show natsuki 3f zorder 2 at f11

    s "¡De todos modos! ella es Natsuki."
    show natsuki 3f zorder 2 at thide 

    hide natsuki 

    show yuri 3a zorder 2 at t11

    s "Yuri."

    hide yuri 

    show monika lean happ om ce zorder 2 at t11

    s "Monika."

    hide monika

    show sayori 1s zorder 2 at f11

    s "¡Y tu ya me conoces!"

    show sayori zorder 2 at thide
    hide sayori 

    show yuri shy happ cm oe zorder 2 at t11

    "Aunque Sayori me este presentando a las demás chicas no puedo quitar la mirada de Yuri..."

    "Monika se acercó a mi con una amable sonrisa."

    show yuri zorder 2 at thide
    hide yuri 

    show sayori turned lsur cm oe zorder 2 at t21 

    show monika forward happ om oe zorder 2 at f22

    m "De hecho [player] y yo estuvimos en la misma clase el año pasado"

    show monika forward happ cm oe zorder 2 at t22

    "Ella es Monika recuerdo perfectamente que estuvimos en la clase de Quimica el año pasado..."
    
    "Prefiero olvidar lo que pensaba el año pasado."

    show monika forward happ om oe zorder 2 at f22

    m "Que alegria es verte de nuevo [player]"

    show monika forward happ cm oe zorder 2 at t22

    mc "Si... es un gusto también"

    show sayori turned happ om oe zorder 2 at f21

    s "¡Ven [player]! ya tengo mucha hambre."

    show sayori zorder 2 at thide
    hide sayori 

    show monika zorder 2 at thide
    hide monika 



    "Las chicas hicieron un circulo con los pupitres mientras que Sayori me sentó a su lado."

    "Al ver a las demas chicas excepto a Yuri supe de quien era el asiento faltante a mi lado."

    show sayori tap nerv m1 zorder 2 at f21

    s "Ya regreso~"
    hide sayori
    with wipeleft_scene

    show sayori 4p zorder 2 at f11

    s "Realmente no me podia aguantar las ganas de comer los pastelitos, Natsuki es la mejor cocinera... ¿o pastelera?"

    show sayori 4q zorder 2 at t22

    show natsuki 3f zorder 2 at f21

    n "¡Sayori!"

    show natsuki 3f zorder 2 at t21

    stop music fadeout 2.0

    "Le pelirosa agarró bruscamente la bandeja pero debido al movimiento ella terminó cayendo al suelo."

    play sound closet_close

    n "off..."

    show natsuki zorder 2 at thide
    hide natsuki 

    show sayori 4m zorder 2 at t21

    show monika 1g zorder 2 at t22

    play music audio.t9

    mc "¿Te encuentras  bien?"

    "Me levanté de mi asiento, mientra Sayori ayudaba a Natsuki a levantarse. Recogí la bandeja"

    show sayori zorder 2 at thide
    hide sayori

    show monika zorder 2 at thide
    hide monika

    show natsuki 2b zorder 2 at f11

    n "U-uh... mi cabeza... ¿¡y los pastelitos!? [player] deja lo-"

    show natsuki turned curi cm oe zorder 2 at t11

    "Aunque un par de pastelitos estaban caidos en el suelo logré rescatar algunos."

    show natsuki turned lsur cm oe zorder 2 at t11

    "Todos estan decorados como si fueran gatitos, realmente se mira el talento."

    show natsuki turned fs neut om oe zorder 2 at f11

    n "L-lo siento... Quería mostrarlo por mi misma realmente me esforcé mucho haciendolo..."

    show natsuki turned fs neut cm oe zorder 2 at t11

    "Natsuki está muy centrada en los pastelitos del suelo."
    
    show sayori 1f zorder 2 at t21

    show natsuki turned fs neut cm oe zorder 2 at t22

    "Sayori también."

    "Como puedo ayudar... con la bandeja en mi mano me di cuenta que aun quedaban unos pastelitos"

    mc "Oigan esta bien... miren no todos cayeron al piso..."

    show sayori 1l zorder 2 at t21

    show natsuki 1n zorder 2 at t22

    mc "Y... se miran muy delicisoso ¿no?"

    show sayori 3b zorder 2 at t21

    show natsuki 4b zorder 2 at f22

    n "S-si..."

    show natsuki 4b zorder 2 at t22

    show sayori  zorder 2 at f21

    s "¡Siii! aún hay pastelitos"

    n "Ajah..."

    show natsuki zorder 2 at thide
    hide natsuki

    show monika 2m zorder 2 at t21

    show sayori 1q zorder 2 at t22

    "Natsuki se fue al closet a buscar algo para limpiar el piso"

    "Mientras que Sayori se acerco a mi oido"

    show monika zorder 2 at thide
    hide monika

    show sayori 1a zorder 2 at t11

    s "[player]"

    mc "¿Eh?"

    s "Hiciste bien"

    mc "Tenia que hacer algo para animarlas ¿no?"

    show sayori 3b zorder 2 at t11

    s "Como siempre jeje.."

    mc "¿Siempre?"

    stop music fadeout 2.0

    play music audio.t8 

    show sayori 2r zorder 2 at t11

    s "¡Vamos a comer~!"

    show sayori 1a zorder 2 at t22

    show monika 1a zorder 2 at t21

    "Despues de hablar agarro rápidamente uno de la bandeja, seguida de Monika y despues de mi"
    show sayori turned happ om ce zorder 2 at h22
    s "Esh mu delichisosho~ hmm~"

    "Mientras Sayori comia Natsuki salió del closet con un trapo y empezó a limpiar el piso"

    "Despues de que Natsuki terminará de limpiar el piso se sentó al lado de Sayori"

    show sayori zorder 2 at thide
    hide sayori

    show monika zorder 2 at thide
    hide monika

    show  natsuki 3n zorder 2 at t11

    "Noto como mira en mi dirección mientras comía el pastelito"

    mc "Sayori tenia razón estan muy deliciosos"

    show natsuki 3r zorder 2 at t11

    mc "Muchas gracias, Natsuki"

    n "N-no es que los haya hecho para ti o algo"

    "Sayori dijo que eran para el nue- , sabes... mejor sigo disfrutando de los dulces pastelillos"

    show natsuki zorder 2 at thide
    hide natsuki

    with dissolve_scene_full 

    show yuri 2a zorder 2 at t33

    "Yuri regresó con un juego de té en la mano y me entregó una taza con té"

    mc "¿los profesores no las regañan por tener esto?"

    show yuri 2b zorder 2 at t33

    y "nos dieron permiso debido a ser un nuevo club"

    y "además, una taza de té siempre de la mano de un libro"

    show yuri 2a zorder 2 at t21

    show monika 3b zorder 2 at t22

    m "tranquilo [player], solo intentan impresionarte"

    show monika 1h  zorder 2 at t22

    m "(¿presumiendo?)"

    show yuri 2o zorder 2 at t21

    show monika 2j zorder 2 at t22

    y "¿qu-que...? y-yo no intentaba..."

    "Yuri volteó su mirada hacia la nada"

    show yuri 2w zorder 2 at t21

    y "t-tu me entiendes..."

    show yuri zorder 2 at thide
    hide yuri

    show monika 2i zorder 2 at t11

    m "por cierto [player], me alegra que te hayas unido, como presidenta del club me aseguraré que te sientas cómodo"

    stop music fadeout 2.0

    mc "¿que me haya unido? pero aun no me he decidido en unirme..."

    show monika zorder 1 at thide
    hide monika

    show sayori 2m zorder 2 at t11

    mc "me refiero..."

    show sayori 2m zorder 2 at t21

    show yuri 2i zorder 2 at t22

    mc "aún tengo que ver otros clubs..."

    show sayori 2m zorder 2 at t31

    show yuri 2i zorder 2 at t32

    show monika 1m zorder 2 at t33

    mc "ver que club me gusta mas..."

    show sayori 2m zorder 2 at t41

    show yuri turned sad cm oe zorder 2 at t42

    show monika 1m zorder 2 at t43

    show natsuki 1h zorder 2 at t44

    "Vamos no pueden mirarme todas asi"

    "Después de conocer a Yuri tal vez las cosas no sean tan malas, además no quiero que Sayori siga acosandome con que entre a su club"

    "Tome valor y mire a las chicas directamente"
    mc "eh... tomé una desición"

    "todas las chicas me estaban viendo esperando mi respuesta"

    show sayori 2q zorder 2 at t41

    show yuri 1a zorder 2 at t42

    show monika 1j zorder 2 at t43

    show natsuki 2f zorder 2 at t44
    play music audio.t8
    mc "esta bien... si me uniré al club"

    show sayori 2r zorder 2 at h41

    s "¡yeiiii! por un momento pensé que no te unirías"

    "Sayori me agarró de las manos y empezo a saltar con mucha emoción"

    show natsuki 1e zorder 2 at t44

    n "si hubieras dicho que no te unirías te hubiera hecho pagar por el pastelito"

    show yuri 1b zorder 2 at t42

    y "me asustaste por un instante"

    show monika 1b zorder 2 at t43
    
    m "me alegra que hayas tomado una buena desición"

    show natsuki zorder 2 at thide
    hide natsuki

    show sayori zorder 2 at thide
    hide sayori

    show yuri zorder 2 at thide
    hide yuri

    show monika 2j zorder 2 at t11

    m "Tengo una idea. Ya que [player] se ha unido, podriamos organizar una actividad, ayer me encontré con algo curioso"

    show monika zorder 2 at thide
    hide monika

    show sayori 2n zorder 2 at t11

    s "¿actvidad?"

    show sayori zorder 2 at thide
    hide sayori

    show monika 3a zorder 2 at t11

    "monika sacó una hoja"

    m "no sabía que te gustaba escribir poemas, Natsuki" 

    show monika 3a zorder 2 at t21

    show natsuki turned lhip rhip vang cm ce zorder 2 at t22

    n "¡dame eso Monika!"

    "natsuki agarro la hoja de las manos de Monika para luego meterla en su mochila"

    show natsuki zorder 2 at thide
    hide natsuki

    show monika 3a zorder 2 at t11

    m "y bueno... estaba pensando en que podriamos compartir poemas asi para [player] será mas fácil conocernos"

    show monika 2i zorder 2 at t11

    m "pero no creas que te salvarás de escribir uno también [player]"

    mc "uh... claro"

    show sayori 1a zorder 2 at t21

    show monika 2i zorder 2 at t22

    s "cuando llegue a casa me pondre a escribir"

    show sayori 1a zorder 2 at t31

    show monika 2i zorder 2 at t32

    show natsuki cross vang om ce zorder 2 at t33

    n "que verguenza... no me gustaria compartir mis poemas"

    show sayori 1a zorder 2 at t41

    show monika 2i zorder 2 at t42

    show natsuki cross anno cm ce zorder 2 at t43

    show yuri shy zorder 2 at t44

    y "para mi... tambien seria dificil hacerlo"

    show monika forward rhip happ cm oe zorder 2 at t42

    "monika se quedó en silencio por un momento, para luego mirarme con una sonrisa"

    mc "supongo que... podria hacer un poema y decirlo y eso"

    m "perfecto yo también, asi que chicas y [player] doy por concluida la reunion del club por hoy"

    show natsuki zorder 2 at thide
    hide natsuki

    show monika zorder 2 at thide
    hide monika

    show yuri zorder 2 at thide
    hide yuri

    show sayori zorder 2 at thide
    hide sayori

    show yuri turned laug cm oe zorder 2 at t11

    "siento mucha ansiedad por escribir un poema {i}y encima compartilo con ellas, ella{/i}"

    "yuri trato de ayudar a Natsuki a limpiar el piso"

    show yuri zorder 2 at thide
    hide yuri

    show sayori 3a zorder 2 at t11

    s "oye [player] ya que desde ahora nos veremos todos los dias, ¿quieres caminar conmigo a casa? ya sabes como lo haciamos antes"

    "es verdad, hace mucho tiempo que no caminaba con Sayori debido a lo tarde que salia, no solo de la escuela"

    mc "por supuesto Sayori"

    show sayori turned lup rup happ om ce zorder 2 at h11 
    s "yaaay~"
    mc "Dame un momento y tomo mis cosas"
    show sayori turned lup rup happ om ce zorder 2 at thide
    hide sayori 
    "Rapidamente guarde mis cosas y alcanzo a Sayori en la puerta del aula"
    mc "Listo Sayori, podemos irnos"
    s "¡¡¡Nos vemos mañana chicas!!!"
    stop music fadeout 2.0

    show bg residential_day
    with wipeleft_scene

    "Durante todo el camino a casa he pensado en ella"

    show yuri 3b zorder 2 at t11

    "En Yuri.{w} Quizas no esté pensando bien pero siento como si tuvieramos algo en común"

    "estoy seguro que me la pasaré muy bien todos los días con ella"
    "Y por supuesto con las demas chicas tambien"

    "Quiero conocerla un poco más, empezare acercame un poco a ella"

    show yuri zorder 2 at thide
    hide yuri

    "¡perfecto! solo necesito hacerlo bien y lo lograré"

    "asi que escribir un poema...{w} si hago un poema que a ella le guste será más facil acercarme"

    show sayori 1k zorder 2 at t11

    s "..."

    show sayori zorder 2 at thide
    hide sayori

    show bg bedroom
    with dissolve_scene_full
    play music audio.t8

    "agarré un lapiz y una hoja de papel"

    "un poema, poemas"

    "¿cómo siquiera se escribe un poema?"

    "Yuri luce como una chica madura por lo que imagino que le gustaran los poemas reflexivos o algo así"

    "golpeo repetidamente el lapiz contra el escritorio intendo hallar inspiración"

    "uff... si tan solo pudiera escribir palabras random que suenen bien..."

    "¡SI!"

    "la biblioteca a estas horas está abierta y puedo inspirarme, solo debo de buscar algo que le guste a Yuri..."
    "Sin pensarlo dos veces tomo un cuaderno y lapiz para guardarlos en mi mochila"
    "Si me apresuro llegare antes de que cierren la biblioteca"
    show black 
    with dissolve_scene_full
    "Un poco agotado y con algunas gotas de sudor tomo aire antes de entrar a la biblioteca"
    scene bg library_aft
    with dissolve_scene

    "Uff aun sigue abierta"
    "El silencio de la biblioteca siempre me tranquiliza"
    "A lo lejos veo un par de estudiantes leyendo unos cuantos libros, la bibliotecaria hablando con un señor mayor"
    "Parece querer llevarse un libro sobre cocina"
    "Como sea..."
    "Saliendo de mi trance empiezo mi busqueda de libros que podrian interesarle a Yuri"

    "agarro varios libros que parecen de terror y de superación"

    "La llamada de Cthulhu...{w} muy complicado"

    "¿Books of Blood?{w} suena como si fuera escrito por un adolescente edgy"

    "El hombre de arena.{w} ¿Ese no era un enemigo de un superhéroe?"

    "¿exit music: redux?{w} me suena de algo..."

    "Chico Friki" "Con permiso"

    "el tipo me arrebató el libro de la mano"

    "Chico Friki" "por favor dime que no lo vas a comprar... hace tiempo que lo he estado buscando es muy bueno"

    mc "eh... si está bien ¿lo entiendo?"

    "caminé al siguiente pasillo, iba a agarrar otro libro pero senti como alguien me dio un pequeño empujón"

    "me volteé rapidamente"

    show monika 1 zorder 2 at t11

    mc "ah... eres tu"

    m "perdona no queria asustarte"

    "por un momento sentí que me habia congelado"

    mc "no te procupes... y ¿que haces por aqui?"

    m forward lpoint happ om oe "busco algunas partituras de piano, ultimamente he intentado aprender a tocar el piano"

    mc "oh, eso suena genial"

    m forward lpoint happ om ce "ya que respondí, es mi turno preguntar ¿que hace [player] aqui?"

    "¿que estaba haciendo?{w}, ahh si"
    

    mc "estaba buscando algo, ya sabes como me uni al club queria estar más al tanto"

    m "ya veo. ¿Te gusta el terror, no?"

    mc "algo asi..."

    m forward lpoint rhip ma e1f b1a "dejame adivinar, quieres impresionar a alguien inspirandote en un libro, ¿cierto?"

    mc "eh..."

    m lean m1 e1 b1 "jeh, no fue tan dificil leerte"

    m "entonces pien-..."

    "monika me estuvo hablando, sin embargo vi a alguien a los lejos, una chica de pelo morado"

    m forward curi om oe "[player]"

    mc "Monika la chica de ahí ¿es Yuri?"
    show monika forward curi om oe zorder 2 at thide
    hide monika 
    show yuri turned anno om oe zorder 2 at t11

    "monika se volteó y efectivamente era Yuri con un par de libros"

    mc "y ahora entrará Sayori"

    "mencione con una sonrisa intentando hacer un chiste"
    stop music fadeout 2.0
    "monika no reaccionó ante lo que dije"
    show yuri turned anno om oe zorder 2 at t11
    hide yuri 
    show monika forward anno cm oe zorder 2 at t11
    mc "¿monika?"

    "monika inmediatamente volvió a la realidad"
    play music audio.t9
    m forward dist om oe "[player]... ¿hay un problema si te hago una pregunta?"

    mc "no tendria problema, adelante"

    m forward"¿qué opinas de las chicas del club?"

    "¿qué tipo de pregunta es esa?"

    "por alguna razón Monika me lo pregunta seriamente"

    mc "bueno... ehh las chicas... "

    mc "Sayori... si, Sayori y yo nos conocemos desde pequeños, somos amigos de la infancia y se podria decir que es mi mejor amiga"

    mc "tu pues me agradas, ya te conocía hace un tiemp-{nw}"

    m forward pout om oe "¿y yuri?"

    mc "¿yuri?"

    m forward nerv cm oe "bueno noté que la mirabas mucho"
    
    mc "no creo que haya pasado eso"

    m "pero pasó..."

    m "yuri es un poco timida con los demás sobre todo con nuevas personas"
    stop music fadeout 1.5
    m forward nerv om oe "y seria una pena si se fuera porque alguien la hace sentir incomoda en el club..."

    mc "monika entiendo eso pero yo nunca incomodaría a alguien y mucho menos a Yuri"

    m "..."

    m forward pout om oe "está bien... pero mantente alejado de ella. Creeme ella siempre está mejor sola"

    mc "..."
    
    "realmente no se que decir, como podria alejarme o evitar a Yuri"
    "No puedo hacer eso"

    m forward neut om oe "bueno me tengo que retirar, hasta mañana [player] cuidate"
    mc "Hasta pronto Monika"
    show monika forward neut om oe zorder 2 at thide 
    hide monika

    "Veo como monika camina hacia la salida"
    "No logro ver a Yuri en el mismo lugar que la vi antes"

    "Supongo que Yuri se ha ido"

    "no creo que realmente esté incomodando a Yuri... o que podria hacerlo"

    "quizás este sobrepensado, es la presidenta del club obviamente querrá lo mejor para... para el club"
    "N-no deberia darle tantas vueltas ahora"
    "Revise las estanterias y lleve conmigo unos cuantos libros para continuar con la tarea que me espera en casa"

    "El mismo silencio que me recibio antes me despide mientras camino fuera de la biblioteca de camino a casa"
    scene bg bedroom
    with dissolve_scene_full
    "Saco los libros de mi mochila y los apilo cerca de mi escritorio"
    "ver la pila de libros me hace sentir abatido"
    "Con papel y lapiz en mano, suspiro"
    mc "Me espera una laaarga noche"
    show black
    with dissolve_scene_full
    
    #al siguiente dia 
    scene bg club_day
    with dissolve_scene

    show monika lean zorder 2 at t11 
    play music audio.t6 
    m "hola [player]"

    m "me alegra saber que viniste"

    mc "soy alguien de promesa, que puedo decir."
    show monika lean zorder 2 at thide
    hide monika 

    "¿llegué tarde?, parece que las demas chicas ya llevaban un rato en el club"
    show yuri turned lup rup happ cm ce zorder 2 at t11
    
    y "sabia que cumplirias con tu promesa [player]"

    y "espero no te agobie el leer tanto libros, sé como se siente cuando no estas acostumbrado"
    show yuri turned lup rup happ cm ce zorder 2 at t21
    show natsuki cross neut om oe zorder 2 at t22
    n "no le tengas piedad, Sayori me dijo que aceptaste venir cuando mencionó los pastelitos"

    n cross doub om oe "asi que tómate enserio esto, si tienes hambre en el segundo piso está el club de cocina"

    y turned flus cm oe "disculpa Natsuki, estaba hablando con [player]..."

    n cross angr om ce "oye solo quiero que nos tome en serio, no permitire que arruine nuestro club"
    show yuri turned flus cm oe zorder 2 at t31
    show natsuki cross angr om ce zorder 2 at t32
    show monika lean zorder 2 at f33 
    m "no es un poco dificil hablar asi para alguien que tiene una coleccion completa de manga en el salón?"

    n n3 turned shoc om oe "¡¡MON-MAN-MON-MAN!!"

    "natsuki se quedo atascada en decir Monika o manga"
    show natsuki turned shoc om ce zorder 2 at f32
    n "el manga es literatura"
    show natsuki turned shoc om ce zorder 2 at thide
    hide natsuki

    "natsuki se giró y entro dentro del closet del salón"
    show monika forward happ cm oe zorder 2 at thide
    hide monika
    pause 0.8
    show sayori turned happ om oe zorder 3 at t21
    show yuri turned flus cm oe zorder 2 at t22
    

    s turned laug om oe "tranquilas chicas, [player] siempre apoya cuando algo le interesa... o le piden ayudas jeje..."

    "recuerdo todas las veces que ordené el gran desastre cuarto de Sayori"

    y lup rup happ cm ce "que considerado"

    mc "como me gustaria decir que no es dificil... como salvar una casa apunto de explotar"
    show sayori ml e4c b1c zorder 2 at f21
    s "¡eso jamás pasó!"

    mc "¿entonces lo estoy inventando?"

    s tap pout cm oe "ush si que eres malvado..."

    y turned ldown laug cm oe "¿son muy buenos amigos no?"

    y "quizas este un poco celosa"

    s turned happ om oe "¿celosa? ¡pero tu y [player] tambien pueden ser buenos amigos!"

    y flus cm oe "u-uhm..."

    mc "sayori..."

    s "¿si?"

    s "ahh por cierto Yuri te trajo un regalo"

    y turned lup pani om oe "n-no es importante"

    y shy neut om oe "pe-pero si prefieres no aceptar mi regalo esta bien..."

    s "ah..."

    "¿un regalo? ni siquiera en un sueño me imaginaria esto"
    
    mc "oye es una gran sorpresa, no pensaba que iba a recibir algo"

    mc "y cualquier cosa, es bienvenida"

    y shy happ om oe "..."
    show yuri shy happ om oe zorder 2 at thide
    hide yuri

    "Yuri caminó hacia su asiento buscando algo en su silla"

    s turned happ om ce "[player] estoy segura que te gustará el regalo jeje..."

    "¿seguimos hablando del regalo?"
    show sayori turned happ om ce zorder 2 at thide
    hide sayori

    "Yuri regresó con un libro en la mano"
    show yuri shy happ cm oe zorder 2 at t11

    y "queria regalarte un libro... pensé que te gustaría ya que eres nuevo"

    y shy neut om oe "y en cualquier momento"

    y "o cuando termines"
    
    y "podriamos..."

    y shy neut n5 "compartir opiniones"

    mc "¡muchas gracias Yuri! realmente no se mucho de literatura pero lo leeré con mucho detenimiento"
    show yuri turned lsur om ce zorder 2 at s11
    "agarré el libro y yuri se relajó"

    y turned happ om ce "estoy emocionada de saber que opinas"
    mc "No puedo esperar a empezar a leerlo"
    mc "De nuevo muchas gracias Yuri"
    show yuri turned happ om ce zorder 2 at thide
    hide yuri
    scene bg club_day
    with wipeleft_scene
    
    "llevó un tiempo sentando sin hablarle a nadie"

    "aunque quiero hablarle a Yuri no quiero incomodarla... está muy centrada en su libro"

    "¿qué estará leyendo?"

    "me centré en su libro, es muy parecido al que me regalo"
    show yuri turned pani om oe zorder 2 at h11
    y "uh-ah..."
    show yuri turned flus cm oe zorder 2 at s11
    "yuri noto mi mirada, cuando me miro a los ojos inmediatamente escondio su rostro bajo el libro"

    "Tal vez deberia pedirle disculpas"

    mc "perdona, solo estaba interesado en el libro"

    mc "Sobre que trata, si no te molesta que te pregunte"

    y "N-no te preocupes"
    show yuri turned flus om oe zorder 2 at s11
    y "fuh... el libro, basicamente trata sobre una mujer y su marido encerrados en un campamento"

    y turned lsur om ce "son torturados y custodiados por lo que hacen un plan para escapar, al tratar de escapar son descubiertos y como castigo"

    y "ordenaron al marido ver como su esposa era colgada por 10 minutos mientras su cadaver inerte se palidecia cada vez más"

    y "el marido fue confinado en un lugar donde la luz del sol era nula"

    y "Poco a poco el hombre sucumbia ante la locura"

    y "Mantenia alucinaciones sobre la muerte de su esposa, su desesperacion por la falta de aire, el dolor de la soga en su cuello"

    y "el hombre se ahorcaba con sus propias manos tratando de buscar la misma sensación que sintio su esposa"

    y "La soledad acompañada de una eterna oscuridad eran el martirio de aquel hombre que luchaba por mantener su cordura"

    "aunque la voz de Yuri ayuda a que no suene tan mal... es una historia muy oscura"

    show yuri turned nerv om oe zorder 2 at h11

    "yuri al ver mi rostro parece haber vuelto a la realidad"

    y "L-lo siento empece a divagar, seguro piensas que soy rara por leer este tipo de libro"

    y "ni siquiera estas acostumbrado a leer muchos libros y...{nw}"

    mc "No tienes de que preocuparte Yuri, no tienes que esconder la pasión que tienes por la lectura"

    mc "Despues de todo estamos en el club de literatura, ademas no me molesta en absoluto escucharte hablar"

    mc "Por favor continua"

    y turned sad om oe "Uh-Ah, suelo leer historias un tanto diferentes. Me gustan porque puedes ver la vida desde otro punto de vista"

    y "no siempre todo final malo es... malo{w}, algunos te hacen reflexionar y aprendes tantas cosas de los personajes sin tener que decirlas directamente"

    show yuri turned nerv om oe zorder 2 at h11

    y "¡perdón! aveces hablo demas de los temas que me interesan"

    mc "no, esta bien si hablas mucho de algo es porque te interesa, ¿cierto?"

    mc "ademas... suena interesante, podriamos leerlo"

    y turned laug om oe "bu-bueno"

    mc "tu libro se parece al que me regalaste ¿son del mismo autor?"

    y "en realidad es el mismo libro"

    mc "oh, entonces eso hace mas facil que podamos leerlo"

    show yuri turned laug om oe zorder 2 at thide
    hide yuri

    "saqué el libro de mi mochila y comencé a leerlo a la par de Yuri"

    show yuri shy m1 e3 b1 zorder 2 at t11

    "Mientras leia el libro podia ver de reojo como Yuri estaba viendome"
    show yuri shy m4 e3 b1 zorder 2 at h11
    y "lo-lo siento"

    mc "¿Yuri no crees que te disculpas demasiado?, no has hecho nada malo"

    show yuri turned rup flus cm oe zorder 2 at h11

    y "¿lo hago?, perdon... N-NO ¡quiero decir!-"

    mc "quizas asi ambos podemos leer mejor"

    "deslice mi pupitre hasta juntarlo con el de Yuri y agarré mi libro para sostenerlo de un lado"

    "yuri se inclinó un poco para sostener el libro con su mano izquierda"

    show yuri turned rup flus cm oe zorder 2 at thide
    hide yuri
    pause 0.8
    scene y_cg1_base
    show y_cg1_exp1

    mc "aunque no habia pensado en como cambiaremos de pagina"

    mc "¿lees rapido?"

    y "uh... suelo leer con calma..."
    hide y_cg1_exp1 with dissolve 

    "me quedé en silencio cuando sentí el hombro de Yuri. estamos mas cercanos que antes"

    "intenté concentrarme en leer"

    #probablemente poner libro

    with dissolve_scene_full

    show y_cg1_exp1 with dissolve 

    y "¿listo?"
    

    "yuri dejo de leer el libro para mirarme"

    mc "ah... en realidad no he terminado aún"

    y "¿no sueles leer mucho cierto?"
    show y_cg1_exp2 with dissolve 
    y "puedo ser paciente contigo, mostraste interés en la historia asi que es lo minimo que puedo hacer"

    mc "s-si"

    mc "muchas gracias Yuri"
    hide y_cg1_exp2 with dissolve 
    hide y_cg1_exp1 with dissolve 

    "Creo que Yuri ya había terminado antes de que yo acabara la primera página"

    with wipeleft_scene

    "terminé el capitulo, intuyo que Yuri también asi que intento pasar de página"

    "cuando intento mover la hoja Yuri me ayuda con su mano izquierda"

    mc "¿sabes? el personaje principal me recuerda a ti"
    show y_cg1_exp1 with dissolve
    y "¿enserio?"

    mc "buneo... por lo menos en algunos gestos que sueles hacer"
    show y_cg1_exp3 with dissolve
    y "y-ya v-veo"
    hide y_cg1_exp3 with dissolve
    hide y_cg1_exp1 with dissolve 
    "Yuri se mantuvo en silencio parece pensar en algo"
    scene bg club_day 
    with dissolve
    show yuri shy happ om oe zorder 2 at h11
    y "que digas eso... ¡es muy malo que me parezca a el!"

    "Yuri jugó con uno de sus mechones. creo que le dije algo que la avergonzó"

    mc "¡n-no intentaba decir algo malo!"

    "perfecto arruine todo en una linea"

    mc "no intentaba decirlo de manera negativa sino... como algo... algo lindo"

    y shy n3 m3 e1 b1 "¿Lin-lindo?"
    stop music fadeout 1.5

    y "yo..."
    show monika forward lpoint happ om oe zorder 2 at t32
    show yuri turned pani om oe zorder 2 at h31

    m "okay, todo el mundo"

    y "..!"
    play music audio.t8
    m "ya es hora de compartir nuestros poemas, si esperamos más quizas no tengamos tiempo de comentarlos"

    show yuri turned lsur om ce zorder 2 at s31

    y "si por supuesto..."

    m forward neut om oe "¿te encuentras bien Yuri?"

    m "pareces decepcionada"
    show yuri turned pani om oe zorder 2 at h31
    y "no... todo bien"
    m forward lpoint happ om oe "Ok, todo el mundo empieza la ronda de compartir poemas"
    show monika neut om oe zorder 2 at thide 
    pause 1.2
    hide monika 
    "juraria que Monika me estaba mirando mal antes de irse"

    show yuri turned lsur om ce zorder 5 at s11
    "Yuri suelta el libro"

    mc "¿continuamos mañana?"

    y turned n1 happ cm oe "está bien aunque también podrias avanzar un poco en casa también me gustaria que disfrutes del libro y podamos compartir opiniones sobre el"

    mc "Mhmmm, que tal si lo avanzo en casa y continuamos leyendo juntos por donde lo deje mañana"

    y turned happ om ce "Me parece una magnifica idea"

    mc "Esta hecho"

    show yuri turned happ cm oe zorder 2 at thide
    hide yuri

    "me levanté para meter el libro dentro de mi mochila"

    with wiperight_scene
    show monika forward rhip happ om oe zorder 2 at t11
    m "[player] ¿escribiste el poema?"
    mc "fué mas dificil de lo que me esperaba pero si"
    m "No puedo esperar a leer lo que escribiste"
    mc "no tengas tantas expectativas jeje"
    m "Vamos, ten un poco más de confianza en ti mismo"
    mc "Jejeje... seguro"
    show monika forward rhip happ om oe zorder 2 at thide
    hide monika
    with wipeleft
    pause 0.8
    show sayori turned happ cm oe zorder 2 at t11
    "hasta ahora no habia pensado en lo vergonzoso que es esto, seguramente la unica critica constructiva que reciba sea de Sayori"
    show sayori turned happ cm oe zorder 2 at t21
    show natsuki cross neut om oe zorder 2 at t22
    "Estoy seguro que natsuki aplastara mi poema"
    show sayori turned happ cm oe zorder 2 at t31
    show natsuki cross neut om oe zorder 2 at t33
    show monika forward dist om oe zorder 2 at t32
    "Monika tratara de ser comprensiva pero sabre cuando este mintiendo"
    show sayori turned happ cm oe zorder 2 at t41
    show monika forward dist om oe zorder 2 at t43
    show natsuki cross neut om oe zorder 2 at t44
    show yuri turned neut cm oe zorder 2 at t42
    "Y Yuri...{w} Es la que más me tiene ansioso, como reaccionara al ver mi poema"
    show sayori turned happ cm oe zorder 2 at thide
    show monika forward dist om oe zorder 2 at thide
    show natsuki cross neut om oe zorder 2 at thide
    show yuri turned neut cm oe zorder 2 at thide
    hide monika 
    hide yuri 
    hide natsuki 
    hide sayori 
    "¡AAAAAAAAAH! Me va explotar la cabeza"
    stop audio fadeout 2.0
    "Calmate [player], puedes con esto"
    "Solo debes mostrar tu poema con una sonrisa y escuchar con atencion a las chicas"
    play music audio.t5
    show monika forward lpoint happ cm oe zorder 2 at t11
    m "bueno, ya que eres nuevo en el club elijes tu primero con quien compartir. "
    m lean "Quizas pueda ser yo"
    show sayori turned happ om oe zorder 2 at t41 
    s "monikaaa ¿quieres leer mi poema?"
    show monika forward happ om ce zorder 2 at f11
    m "ah... por supuesto Sayori"
    show monika forward happ om ce zorder 2 at thide
    show sayori turned happ om oe zorder 2 at thide
    hide monika 
    hide sayori 


    "Gracias Sayori, con el camino despejado"

    "Deberia enseñarle mi poema primero a Yuri...?"

    menu poema_yuri1:
        "Mostrar mi poema a yuri":
            "Si, deberia ir con Yuri"
            jump mostrar_poema_yuri
        "Quizás no":
            "Tal vez podria mostrarselo luego"
            jump mostrar_poema_nat


    #poner tipo de elección en donde la unica elección sea Yuri o quizas no

    with dissolve_scene_full 
    label mostrar_poema_yuri:
    play music audio.t5
    "con poema en mano me acerque a Yuri"
    show yuri turned mf e1d b1c zorder 2 at t11

    mc "¿te gustaria compartir poemas?"
    show yuri turned n2 flus cm oe zorder 2 at t11
    y "p-por supuesto"

    mc "sinceramente me da verguenza compartir un poema"

    y turned rup anno om oe "A-a mi tambien, nunca habia hecho algo parecido"

    mc "si quieres puedo empezar"

    y turned neut om oe "¿en serio?"

    y "N-no tienes por-{nw}"

    mc "no, no te preocupes quiero hacerlo"
    show yuri turned n1 lsur om ce zorder 2 at s11
    y "gracias"

    mc "por cierto dime si no entiendes mi letra..."

    "Yuri no mecionó nada, tomo mi poema y empezó a leerlo detenidamente"
    $ poem_db.show_poem("poem_mc1")
    #poner poema de MC
    show yuri turned happ om oe zorder 2 at h11
    y "Tu grafía es excelente y el poema es increible"

    mc "Vamos puedes ser sincera, es mi primera vez después de todo"

    y turned happ om ce "lo digo en serio de hecho no esperaba que lo hicieras tan bien"

    y turned laug cm oe "es como si hubiera sido creado para mi, el ambiente, el tono, La prosa. Me recuerda tanto a mis poemas"
    show yuri turned n2 ml e1b b2a zorder 2 at s11
    y "..."
    show yuri turned n2 nerv om oe zorder 2 at h11
    y "n-no intento decir que el poema va dirigido a mi... so-solo que me gustó mucho"

    mc "bueno quizas tengamos algo en comun"
    show yuri turned flus cm oe zorder 2 at s11
    y "uuuh..."

    y turned n1 lsur om oe "una pregunnta ¿alguna vez has escrito otros poemas?"

    y "A lo que me refiero es que la estructura de las rimas y la profundidad de las metáforas no reflejan el trabajo de un principiante."

    mc "muchas gracias por todos los halagos, signfican mucho para mi viniendo de ti, pero no"
    
    mc "es mi primera vez escribiendo poemas"
    mc "Digamos que estuve en eso toda la noche"
    mc "no queria decepcionarlas"
    y turned happ cm ce "Valio la pena todo el esfuerzo, es un gran poema"
    y turned n2 flus om oe "supongo que es mi momento..."

    show yuri turned n2 flus om oe zorder 2 at thide
    hide yuri

    "yuri busca el poema entre las paginas"

    show yuri turned lup rup worr om oe zorder 2 at s11

    "yuri dudando me pasó un cuaderno de notas, al mirarlo noto que hay otros poemas y no puedo evitar sentir curiosidad al verlos"

    $ poem_db.show_poem ("poem_mlb_yuri")

    show yuri turned shoc om oe zorder 2 at h11
    
    y "¡¡disculpa por la letra!! es horrible"

    mc "¿horrible? para mi es linda, parece que si tenemos algo en común después de todo, ambos escribimos en cursiva"

    y "oh... entonces por qué lo leiste mucho tiempo...?"

    mc "porque me gusta tu caligrafía y el poema esconde un mensaje"
    mc "Tuve que leerlo un par de veces para enterderlo del todo"

    show yuri turned n1 shoc cm ce zorder 2 at s11

    "yuri suspiro"

    y turned sad om oe "¿no es muy corto?"

    mc "no, de hecho creo que fue la manera perfecta de transmitir el mensaje"

    y turned ldown neut om oe "usualmente los suelo hacer mas largos..."

    mc "oye el tamaño no importa ¿verdad?"

    "¿verdad?"

    y turned happ om ce "me siento mas confiada al saber que te gustó"

    y turned laug om oe "y... mañana haré uno largo, en mi cuaderno también tengo algunos poemas"

    mc "Pude darme cuenta mientras buscabas tu poema"
    show yuri turned pani om oe zorder 2 at h11
    y "¿¡y-y l-los leistes!?"

    #añadie dialogo sobre lo que trate el poema, todavia no decidido
    
    mc "no, tranquila solo lei el que me entregaste"
    show yuri turned n2 flus cm oe zorder 2 at t11
    mc "pero seguramente son igual de buenos como el que me enseñaste"

    "Yuri con timidez buscaria una página especifica"
    $ poem_db. show_poem("poem_borr_yuri1")
    #añadir poema-borrador

    mc "vaya... si tengo mucho que aprender para poder escribir asi"
    show yuri turned n1 flus cm oe zorder 2 at f11
    y "¿a qu-que te refieres?"

    mc "eh, elegí mostrarte mi poema primero porque siento que eres muy buena en la creación de poemas"

    mc "y porque no me diras solo \"es muy bueno\" como alguien del club"
    show yuri turned n3 laug cm oe zorder 2 at t11
    "noté que yuri me miró avergonzada"

    mc "pero en fin... me gustaria aprender de ti"

    y turned laug cm oe "¿enserio piensas eso?"

    mc "estoy seguro que las demás también"
    show yuri turned rup lup lsur om oe zorder 2 at s11
    y "uh..."

    y turned ldown laug cm oe "sentía muchos nervios de hacer esto"

    y turned laug rdown cm ce "pero lo estoy disfrutando por ti"

    y "quiero hacerlo lo mejor posible por ti [player]"

    mc "ah..."

    mc "yo tambien..."

    y turned n1 happ cm oe "cuento contigo"

    mc "Vale, contigo ayudandome a mejorar puedo con todo"

    show yuri turned rdown happ cm oe zorder 2 at thide
    hide yuri

    with dissolve_scene_full
    play music audio.t5
    "Parece que termine de compartir mi poema con las chicas"
    "Cada poema tuvo distintos significados y todos bastante interesantes"
    show sayori turned happ cm oe zorder 2 at t11
    "\"Querido sol\", no creo que la mancha de chocolate caliente en la hoja sea una representacion de los sentimientos"
    show sayori turned happ cm oe zorder 2 at t21
    show natsuki turned neut cm oe zorder 2 at t22
    "el poema de Natsuki tuvo una moraleja que no me esperaba, puedes tratar y tratar pero no significa que lo lograras. me esperaba algo diferente..."
    show sayori turned happ cm oe zorder 2 at t31
    show monika forward lpoint happ cm oe zorder 2 at t32
    show natsuki turned neut cm oe zorder 2 at t33
    "y al final con Monika "

    "\"Hoyo en la pared\""

    "aunque lo lei 3 veces no entendi nada, ¿una epifania? no sabia que existia esa palabra"

    "por un momento sentí como si Monika solo siguiera hablandome por compromiso"

    "fué mas estresante de lo que creia, por lo menos me lleve consejos aunque era imposible superar los de ellas"

    "soy nuevo despues de todo"
    show sayori turned happ cm oe zorder 2 at thide
    show monika forward lpoint happ cm oe zorder 2 at thide
    show natsuki turned neut cm oe zorder 2 at thide
    hide sayori    
    hide monika 
    hide natsuki 
    pause 1

    "las chicas aun siguen intercambiando poemas"
    stop music fadeout 2.0
    "Parece que Sayori y Monika terminaron de compartir con todos"

    show yuri turned rup lup anno om oe zorder 2 at t21 
    show natsuki turned doub om oe zorder 2 at t22
    "Yuri y Natsuki parecen ser las unicas que faltan"

    "centré mi mirada en Yuri"

    show yuri turned anno om oe zorder 2 at t21
    "Yuri parece todo lo contrario a Natsuki, tranquila, calmada y paciente"
    
    "Mientras Natsuki es una bomba que en cualquier momento puede explotar"
    show natsuki turned pout om oe zorder 2 at t22
    n "(como es que leyeron esto)"

    "natsuki sostiene el poema con una de sus manos"

    n turned rhip pout om oe "se podria decir que está bien"

    y turned neut om oe "muchas gracias... el tuyo es, lindo"
    show natsuki lhip vang om ce zorder 2 at f22
    play music audio.t7
    n "¿lindo? estuviste leyendolo tanto tiempo y el unico comentario que se te ocurre es ¿está lindo?"

    show natsuki turned vang om ce zorder 2 at f22
    n "enserio ¿no pudiste comprender el obvio mensaje de que mas que intentes aveces no conseguiras lo que quieres?"
    show yuri turned anno om oe zorder 2 at f21
    show natsuki turned vang om ce zorder 2 at t22
    y "disculpa no creí que te ofenderia... intentaba hablar del lenguaje no que el poema sea infantil"
    show natsuki turned vang cm oe zorder 2 at f22
    show yuri turned anno om oe zorder 2 at t21
    n "¿¡Estas intentando vacilarme!?"
    show yuri turned doub om oe zorder 2 at f21
    show natsuki turned vang cm oe zorder 2 at t22
    y "bueno no fue malo más sin embargo puedo darte algunos consejos"
    show natsuki turned vang om oe zorder 2 at f22
    show yuri turned doub om oe zorder 2 at t21
    n "¿¡Consejos!?"

    n "¿¡Consejos de alguien que no le gustó mi poema!? ¡nunca los aceptaria!"

    n "y hay algunas personas a quien les gustó como Sayori, Monika"
    show natsuki turned vang om oe zorder 2 at f22
    n "y tambien [player] asi que dejame ser yo quien te de conse-{nw}"
    show yuri turned vang om ce zorder 2 at f21
    show natsuki turned vang om oe zorder 2 at t22
    y "no necesito tus consejos Natsuki, he tenido años desarrollando mi estilo propio"

    y "además, no pienso en cambiarlo a menos que encuentre algo mucho mejor"
    show natsuki turned angr om oe zorder 2 at f22
    show yuri turned vang om ce zorder 2 at t21
    n "vaya no sabia que eras tan egocentrica Yu-{nw}"
    show yuri turned rup lup vang cm oe zorder 2 at f21
    show natsuki turned angr om oe zorder 2 at t22
    y "y tambien a [player] le gustó mi poema y el si acepto mis consejos"
    show natsuki turned angr om oe zorder 2 at f22
    show yuri turned rup lup vang cm oe zorder 2 at t21
    n "¡WOW!, como remarcaste a [player] creia que el era el unico que trataba de impresionar a alguien pero veo que tu tambien"

    y turned pani om oe "¡¡y-yo no trate de decir eso!!{w} lo que pasa es que estas celosa"

    show natsuki turned n3 shoc om oe zorder 2 at f22
    "natsuki intento hablar molesta pero fue interrumpida por Sayori"
    show natsuki turned n3 shoc om oe zorder 2 at t33
    show yuri turned rup lup vang cm oe zorder 2 at t31
    show sayori turned flus om oe zorder 2 at t32

    s "chicas está todo bien?"

    #aqui hablan nat y yu
    show natsuki turned vang cm oe zorder 2 at f33
    show yuri turned rup lup vang cm oe zorder 2 at f31
    show sayori turned pani om oe zorder 2 at s32
    ny "¡NO TE METAS!"
    show sayori turned pani om oe zorder 2 at thide
    hide sayori 
    show yuri turned rup lup vang cm oe zorder 2 at f21
    show natsuki turned vang cm oe zorder 2 at t22
    y "dijiste la unica..?"

    n turned vang cm ce "gmhp"

    "natsuki colocó el poema en uno de los escritorios"

    "para luego levantarse firmemente "
    show natsuki cross vang cm ce zorder 2 at f22
    show yuri turned rup lup vang cm oe zorder 2 at t21
    n "por lo menos a mi no se me levantó el pecho inmediatamente que [player] entro al club"
    show yuri turned n3 pani om oe zorder 2 at h21
    show natsuki cross vang cm ce zorder 2 at t22
    y "¡N-n-natsuki!"
    show natsuki cross vang cm oe zorder 2 at t33
    show yuri turned n1 angr om oe zorder 2 at t32
    show monika forward rhip neut om oe zorder 2 at t31
    m "natsuki creo que no deberias de de-{nw}"

    #nat y yuri
    show natsuki cross vang cm oe zorder 2 at f33
    show yuri turned pani om oe zorder 2 at f32
    show monika forward rhip neut om oe zorder 2 at t31
    
    ny "¡ESTO NO TE INCUMBE!"

    show natsuki cross vang cm oe zorder 2 at t22
    show yuri turned pani om oe zorder 2 at t21
    show monika forward rdown sad om oe zorder 2 at thide
    hide monika

    y turned angr om ce "nunca haria algo tan v-vergonzoso... como tratar de hacer tierno todo!"

    "Parece que esta pelea esta escalando demasiado"

    "Tengo miedo de intervenir, no veo forma de parar este torbellino"

    "Como si el destino estuviera en mi contra ambas chican postran su mirada en mi"
    show yuri turned rdown flus cm oe zorder 2 at f21
    y "¡no le creas [player], Natsuki me está haciendo quedar mal!"

    y "J-jamas podría hacer eso"

    show natsuki turned vang om ce zorder 2 at t22
    show yuri turned n1 rdown flus cm oe zorder 2 at t21
    n "la unica que intenta hacer quedar mal a otra perosna eres tu yuri, tu empezaste todo esto"

    n turned angr om oe "¿verdad [player]?"
    show natsuki turned vang om ce zorder 2 at f22
    show yuri turned rdown flus cm oe zorder 2 at f21
    #ambas
    ny "Entonces!?"

    "..."

    "¿cómo es que todo pasó tan rapido?"

    "¿y porque se dirigen a mi?"

    "¿que deberia de hacer?"

    menu decision_ruta:
        "Hacerte el desentendido e intentar calmar las aguas.":
            "Es mejor que evite todo esto desastre"
            jump ruta_neutra_1


    #poner opciones por el momento se desarrolará la ruta neutral hasta el acto 2

    #pretender que no estabas escuchando e intentar calmar la sitaucíon son opciones originales
    label ruta_neutra_1:
    "me levanté de mi asiento con un poco de miedo"

    mc "ambas son buenas escribi-{nw}"

    n cross n1 angr om ce "si ibas a dar una opinión tan mala mejor no hubieras dicho nada"

    "me senté rapidamente en mi asiento"

    y turned n1 angr om oe "natsuki no deberias de hablarle asi a [player] es una total falta de respeto"
    show natsuki turned angr om oe zorder 2 at f22
    show yuri turned angr om oe zorder 2 at t21
    n "S-silencio, Yuri"
    stop music fadeout 2.0
    n "sabes que pienso de ti, Yuri?"

    n turned angr om ce "al inicio pensaba que iba a ser increible tener una amiga con mis mismos gustos..."

    "natsuki se detuvo unos segundos"

    "Esta a punto de estallar la bomba"
    
    n turned vang om oe "¡pero ahora pienso que eres un perra engreida!"
    with vpunch
    show natsuki turned vang om oe zorder 2 at h22
    n "a nadie le sorprende que no tengas amigos"
    show yuri turned me e1g b1b zorder 2 at s21

    y "..."
    show natsuki sad om oe zorder 2 at s22
    pause 2
    show yuri turned cry cm ce zorder 2 at s21
    n "..."
    window hide
    show yuri shy sad om oe zorder 2 at t21
    pause 2
    show yuri shy sad om oe zorder 2 at correr_izquierda

    pause 0.4
    hide yuri 
    play audio closet_open
    window show
    "Yuri salió del club cubriendo sus ojos con una de sus mangas"

    "El club se queda en un silencio por un par de segundos"

    show natsuki turned fs cry om oe zorder 2 at t11


    "miro a Natsuki, parece arrepentida"

    n "yo.... ya regreso..."

    show natsuki turned fs cry cm ce zorder 2 at correr_izquierda
    pause 0.8
    hide natsuki 
    play audio closet_close
    "natsuki caminó hacia la puerta del salón y la cerro de un portazo, miré a Sayori"

    show sayori turned sad om oe zorder 2 at t11
    s "oh... se-seguramente todo se arreglará [player]"
    show monika forward sad om oe zorder 2 at t21
    show sayori turned sad om oe zorder 2 at t22
    m "si yo tambien pienso que estará todo bien, solo denles espacio"
    show monika forward sad om oe zorder 2 at thide
    show sayori turned sad om oe zorder 2 at thide
    hide sayori 
    hide monika 
    "tal vez pueda ayudar un poco en la situación"

    "caminé hacia la puerta del club pero senti como alguien me agarro del brazo"
    show monika forward anno om oe zorder 2 at t11
    m "[player] quedate aqui, soy la presidenta conozco a mis miembros asi que"

    m "confia en mi"

    "¿porque monika actua tan extraño?"

    hide monika 
    with dissolve_scene_full

    #escena transición 
    play music audio.t5
    show monika forward lpoint happ om oe zorder 2 at f42
    show sayori turned happ cm oe zorder 2 at t43
    show yuri shy neut cm oe zorder 2 at t41
    show natsuki cross dist cm oe zorder 2 at t44
    m "¡okay, todo el mundo! ya es hora de irnos a casa, ¿qué tal les pareció la actividad?"
    show sayori turned happ om oe zorder 2 at f43
    s "¡me encanto!"
    show yuri shy neut cm oe zorder 2 at s41
    y "..."
    show natsuki cross dist om oe zorder 2 at f44
    n "entretenido supongo"

    mc "supongo que estuvo bien"

    m "¡muy bien!"

    m "mañana traigan un poema diferente y asi podremos aprender más de nosotros"

    show monika forward lpoint happ om oe zorder 2 at thide
    show sayori turned happ cm oe zorder 2 at thide
    show yuri shy neut cm oe zorder 2 at thide
    show natsuki cross dist cm oe zorder 2 at thide
    hide sayori 
    hide monika 
    hide natsuki 
    hide yuri 

    "es cierto, gracias a la actividad pude saber que tipo de poemas le gustan a cada una"


    "quizas si hago un tipo de poema especifico pueda impresionar a alguien"

    "siento la determinación en mi mismo"

    show sayori turned flus cm oe zorder 2 at s11

    s "¿[player]? holaa, tierra a [player]"

    mc "¿sayori?"

    s turned neut om oe "¿ya estas listo para irnos?"

    mc "claro vamonos"
    show sayori turned happ cm ce zorder 2 at t11
    "sayori me sonrie honestamente. Hace mucho tiempo que no veia a Sayori pero luce mas alegre desde que me uní"
    show sayori turned happ cm ce zorder 2 at thide
    hide sayori
    #transición ah esata weada donde salen casas
    scene bg street1_aft
    with wipeleft_scene
    show sayori turned dist cm oe zorder 2 at t11
    mc "sayori"
    show sayori turned neut om oe zorder 2 at t11
    mc "lo que ocurrió hoy en el club ¿Ocurre con frecuencia?"

    s turned flus om oe "¿¡Eh!? ¿por supuesto que no!"

    s nerv cm oe "nunca las habia visto pelear, de hecho son muy buenas amigas"

    s "no..."

    s turned sad cm oe "¿no las odias... o si?"

    mc "no las odio, llevo dos dias en el club y me gustaria saber tu opinion"

    s turned worr om oe "bueno, quizas hayan tenido un mal dia y por eso hayan reaccionado mal"

    s "espero no estés pensando en salirte..."


    mc "¿no? aunque lleve poco tiempo me gusta estar en el club"

    s turned happ om ce "me hace muuuuuy feliz que te guste estar en el club"

    s "¡además a todas les fascinas!"

    "Sayori no piensa 2 segundos antes hablar"

    s turned happ cm oe "te prometo que cada dia será mejor"

    "suspiro"

    "sayori aún no entiende como me siento"

    mc "Espero todo mejore mañana"

    s "Todo estara bien, ya verás"
    show sayori turned happ cm oe zorder 2 at thide
    hide sayori
    #cambio de escena a la casa de TN
    scene bg bedroom
    with wipeleft_scene

    "hoy me siento mucho mas inspirado que ayer"

    "asi que un poema con simbolismo y una buena metrica"

    "Se me ocurren un par de ideas"

    "Los consejos de Monika estan dando sus frutos"

    stop music fadeout 1.0

    scene bg club_day
    with dissolve_scene_full
    play music audio.t8

    #cambio de escena de fondo abriendose para mostrar image (no se haga we)

    "llegué junto a Sayori al club"

    "como ayer, Natsuki está encerrada en el closet, Monika organizando papeles sobre el club"
    show yuri turned anno om oe zorder 2 at t11
    "y Yuri leyendo un libro, es difenrente al que leiamos ayer"

    "\"La anatomía del silencio\" murmuro, intentando descifrar la perturbadora ilustración de la portada."

    "Me pregunto cómo su cerebro puede procesar historias tan densas mientras toma té de lo más tranquila."

    #poner nombre de libro 
    show turned happ cm oe zorder 2 at t11
    "me acerqué a Yuri, cuando me acerque a ella parecia un poco emocionada"

    y turned happ cm ce "ho-hola [player]"

    mc "hola Yuri, disculpa no queria interrumpirte al leer"

    y "de hecho te estaba esperando para continuar"

    "yuri aun estaba en la primera página"

    mc "ah entonces... ¿leemos?"

    y turned happ om oe "por supuesto. Aunque primero me gustaria me gustaria hacer un poco de té ¿te parece bien?"

    mc "me parece"

    y turned rup"si hay algo que mejore la lectura es una buena taza de té"

    y "(además de ti)"
    show yuri turned happ zorder 2 at thide
    hide yuri 
    "yuri se levanto del asiento para dirigirse al closet, cuando regresa trae una jarra de agua"
    show yuri turned happ om oe zorder 2 at t11
    y "sostenlo porfavor"

    "yuri me entregó la jarra junto a una tetera elecetrica"

    y "conectaré esto y luego necesitariamos un poco de agua"
    show yuri turned dist om oe zorder 2 at s11
    "ella encendió la tetera elecetrica, Yuri es tan elegante incluso en sus movimientos"

    "yuri me pidió la jarra y se la entegué"

    y happ cm oe "ya regreso traeré agua"

    mc "¿te puedo aconpañar?"

    y turned laug om oe "ah... bueno ¿porqué no?"

    y turned n2 flus om oe "A-acompañame"

    show monika forward lpoint happ om ce zorder 2 at t32
    show yuri turned n2 flus om oe zorder 2 t33

    "cuando iba a salir con Yuri de clases Monika se puso enfrente mio"


    mc "¿hola?"

    m "¿a dónde van ustedes?"

    y turned lup neut om oe "vamos a llenar la jarra de agua, Monika"

    m "me parece bien, pero eso lo podria hacer una sola persona, ¿no?"

    stop music fadeout 1.0

    m "y es u-{nw}"
    show yuri turned angr om oe zorder 2 at f33
    y turned angr om oe "¿Monika puedes amablemente retirarte y dejarnos en paz?"

    y "o ¿te parece mal involucrar a [player] más que tu en las actividades del club?"

    m forward vsur om oe "¿eh?"

    mc "..."

    m forward ldown me e1b b1a "yo..."

    m "no hay nada de malo en eso"

    "yuri suspiró para luego salir rapidamente del club"

    play audio closet_open
    show yuri turned angr om oe zorder 2 at thide
    hide yuri  
    show monika forward neut cm oe zorder 2 at t11
    "acompañé a Yuri pero miré atras y vi a monika, me asusta un poco esa mirada"

    pause 1.0

    "rápidamente seguí el paso de Yuri"

    play audio closet_close

    pause 0.5

    scene bg corridor
    with wipeleft_scene

    "yuri tenia la cara cubierta con sus manos"

    y "l-lo dije sin pensar... como no pude pensar en que sonaría tan agresiva"

    mc "yuri..."

    y "me molestó como Monika lo dije... cpero no es justificación"

    y "¿será que al abrirme con los demas ya esto mostrando lo insopotable que soy?"

    mc "no yuri, no hiciste mal, no has hecho mal. pienso que lo has estado manejando bien todo"

    y "porque..."

    y "¿porqué me tratas tan amable?"

    mc "porque nada lo de que haces es tan malo, nadie es perfecto. Todos cometemos errores incluyendome"

    mc "hay veces en la que pienso sin hablar, pero de todos modos ¿soy humano cierto?"

    mc "sobrepiensas mucho acerca de lo que dices"

    y "t-tu..."

    y "¿porqué no me odias? incluso podria actuar mal contigo..."

    mc "¿estás segura de eso ultimo?"

    y "no..."

    mc "no puedo odiarte por expresarte de todos modos, los amigos se apoyan"

    y "¿¡am-amigo!?"

    y "m-me gusta que podamos... ¡qué podamos ser amigos!"

    mc "gracias Yuri"

    "me pregunto como podré avanzar mas en la relación, por el momemnto me centraré en hacer que yuri se sienta mejor"
    
    #cambio de escena a una tipo de escaleras o un lugar donde se encuentre un bebereo 

    "llegamos la fuente de agua, yuri me estaba ayudando a llenarla aunque nuestras manos se tocaban mucho"

    y "[player] ¿piensas que Monika se haya molestado?"

    "vino a mi mente la mirada de monika"

    mc "no creo que Monika sea el tipo de Chico Frikis que se enoja o que guarde rencor por algo asi"

    y "quiero disculparme con ella"

    mc "me parece buena idea de hecho"

    y "se que no soy buena expresandome... me gustaria mejorar en eso"

    y "algunas veces incluso me da miedo hablar con otras Chico Frikis, la primera vez que te conocí sentí eso"

    mc "¿enserio? ¿porqué?"

    y "supongo que nunca he tenido muchas experiencias sociales, algunas veces me molestaban"

    y "solia leer en receso y me veian raro por eso"

    mc "yuri, quizas no soy del tipo de Chico Frikis que lee en receso per-"

    "senti que la jarra estaba mojando mis manos"

    "yuri mira la jarra y cerro la fuente"

    y "¡uuuu-!"

    y "el piso está mojado"

    y "perdón no estaba prestando atención de-de"

    mc "yuri, esta bien lo limpiaremos, juntos"

    "yuri aun parecia preocupada"

    mc "Yuri no hiciste nada malo"

    y "pero por hablar demás cayó mucha agua en el suelo"

    mc "no hablo del agua, hablo sobre Monika, no debes de preocuparte por ello estoy seguro que Monika tambien te pedirá disculpas"

    y "¿tu crees?"

    mc "estoy seguro, te lo prometo. Prometo siemore ayudarte incluso en el mas minimo problema"

    y "..."

    "es un poco raro decirle esto a una chica que conozco hace media semana, pero si lo pienso"

    mc "asi que... ¿volvemos?"

    y "gracias [player]"

    y "volvamos al club probablemente se pregunten dond estamos"

    "logré calmar la ansiedad de Yuri pero ahora me siento un poco ansioso de estar cerca de ella"

    #cambio de escena vuelta al club o incluso agregar escena en el pasillo (no muy preferible)

    "al entrar sentí las miradas de los demas miembros"

    y "¿conoces el té de oolong? es muy saludable y también ayuda a tener un mejor estado de animo"

    mc "oolong suena como el nombre de un dragon mitlogico..."

    y "bueno un dia me gustaría enseñarte el arte de hacer un buen té"

    mc "es una buena idea de cita"

    y "...-"

    mc "y... ¿cuál es el primer paso para hacer té?"

    "intento cambiar de tema al ver la reacción de Yuri"

    y "Yuri se dirigió a la tetera elcentrica para el poner la temperatura en 200 grados"

    y "ahora se pone la tetera"

    "yuri tomó la tetera y empezó a tomar las hojas de té"

    "para mi soprensa ella estuvo tarareando una canción"

    mc "¿disfrutas de hacer te no?"

    y "también pero andaba pensando en eso, quiero expresarme mas con los demás no es tan difick como pensaba"

    y "y cuando estás tu me es más fácil expresarme"

    mc "¡eso es muy bueno Yuri! solo no te sobreesfuerces"

    y "siempre te procupas por mi..."

    y "es muy lindo de tu parte"

    "espera necesito un respiro de esto"

    #transición de wey

    "Yuri pone dos tazas para cada uno"

    y "¿te gustaria leer en el suelo hoy?"

    mc "claro pero ¿porqué?"

    y "se lee mejor con la espalda apoyada en la pared"

    mc "perdon no me habia dado cuenta pero tienes razón"

    y "tranquilo casi siempre tengo dolores de espalda asi que puedo soportarlo"

    y "es por mi-"

    y "ah...-!"

    mc "tu postura al leer cierto?"

    y "s-si es eso"

    "no creo que haya sido eso, pero prefiero no indagar en el tema"

    mc "no te encorves mucho al leer supongo"

    y "¡si! tengo una terrible postura"

    "nos sentamos en una de las paredes cerca de la ventana"

    "sostengo con una de mis manos el libro Yuri hace lo mismo de la parte contraria"

    "por el cambio siento lo cerca que se encuentra Yuri de mi, puedo sentir su respiración"

    "sentí que no podia respirar cuando Yuri choco su hombro con el mio"

    #empezar a leer el libro que todavia no esta definido si saldra o si debemos de cambiar algo, en dado caso si existe poner escena del libro


    #terminar escena de libro debido a lo anterior mencionado

    m "¡okay todo el mundo!"

    mc "¿¡EEEH!?"

    "por el susto terminé ahogandome con el chocolate"

    y "¡[player]!"

    #añadir escena de transición

    mc "cof cof"

    m "disculpen no pensaba en asustarlos me imagino que habrán estado muy concentrados"

    mc "menos mal aun quedaba un poco de té"

    m "uh... es tiempo de compartis poemas chicos"

    m "porcierto debido al tiempo Yuri te sugiero que guardes las cosas de té"

    y "está bien"

    "Yuri aun parecia un tanto preocupada asi que me acerque para ayudarle a guardar el juego de té"

    #añadir transiciión

    "luego de terminar de limpiar, era momento de compartir mi poema aunque no si se este listo, lo que paso hace unos minutos..."

    "espero no lo tome a mal..."

    #añadir eleccion de poemas a Yuri (pensar si serviria esto)

    "me acerque a Yuri"

    mc "¿lista?"

    y "por su puesto, quiero ver como seguiste mis consejos"

    "espero no me destruya..."

    "alze mi mano para darle el poema a Yuri"

    #añadir poema 

    y "[player]..."

    mc "¿s-si?"

    "siento que va a notar que lo escribí en la noche... Supongo que no vale la pena sobrepensar, eso no soluciona nada"
    
    #añadir escena de interrumpir dependiendo de la reescritura 

    y "es mejor que el de ayer"

    "¿qué?"

    y "añadiste muy bien el simbolismo y esta vez intentaste algo nuevo, experimentaste y realmente te salió bien"

    y "si sigues mejorando puedes incluso podrias ser el mejor escritor del club"

    mc "no creo que sea tan bueno como mencionas Yuri pero si sirvió tus consejos"

    y "tu poema es tan fantastico... ¿t-te importaria si me lo quedo?"

    mc "pero aun tengo que compartilo Yuri..."

    mc "pero si no tengo problemas"

    "yuri me sonrio alegremente"

    y "con mas practica podrías incluso expresar tus sentimientos o como te sientes, yo... aveces lo hago"

    mc "seria muy dificil plasmar mis pensaiemtos"

    y "¿a qué te refieres?"

    mc "no me sentiría tan comodo describiendome a los demas"

    y "bueno no tiene que ser a todos puede ser con alguien especial"

    y "como yo"

    mc "suena a una buena idea para mi proximo poema"

    "Yuri me paso su poema. Era una hoja suelta"

    #añadir poema 

    #añadir escena del poema, salto final de escena 

    "¿enserio termine de compartir mi poema con las demas? ellas aun  siguen compartiendo opiniones"

    "mis ojos se centra en Yuri, ella está compartiendo su poema con Monika aunque parece mas timida de lo normal"

    "luce como si pidiera perdón por algo"

    m "¿entendido?"

    y "s-si..."

    "yuri asintió con la cabeza"

    "¿será algo importante?"

    "una chica interrumpe mi pensamientos"

    m "¡okay todo mundo!"

    m "con esto se concluye el compartir de poemas"

    s "Monika me tendré que ir temprano nos vemos mañana"

    s "adiositiooo"

    n "si yo también mi padre me está esperando"

    m "bueno, cuidense hasta mañana"

    "solo quedamos yo, yuri y monika en el club, quizas pueda invitarla a que nos vayamos juntos"

    mc "oye yuri ¿quie-"

    y "¡ahh!"

    y "¡disculpa [player] me tengo que ir!"

    "yuri salió rapidamente del club sin siquiera voltearme a ver"

    "definitivamente ha pasado algo con ella, esta actuando raro quizas Monika sepa algo"

    #transición

    m "oh, ¡hola [player]! ¿necesitas algo?"

    mc "si ¿has notado que Yuri ha estado un poco rara luego de..."

    m "bueno quizas deberías de ignorarla"

    mc "¿disculpa?"

    m "quizás me di a mal entender, me refiero a que Yuri no habla frecuentemente con otros"

    m "es más solitaria"

    "La expresión de Monika cambia al ver la mia"

    m "no me refiero a que no le hables, solo que es mejor tener una pequeña charla con ella y dejarla respirar"

    mc "pensaba que nos llevabamos bien en realidad"

    m "Yuri puede ser un poco obsesiva con algunas cosas..."

    "¿obsesiva? quizas un poco de razon tenga, suele disculparse mucho"

    mc "¿obsesiva en?"

    "Monika suspiró"

    m "mira [player] solo no estes tanto tiempo con Yuri, además también puedes pasar tiempo con las demás"

    m "como yo"

    "¿qué me está intentando decir? Monika la presidenta del club ¿me está pidiendo que pase el tiempo con ella?"

    mc "digo... pensaba que Yuri y yo nos llevabamos bien"

    "monika desvió la mirada para luego verme"

    m "realmente no conoces a Yuri"

    mc "quizás solo llevo unos dias hablando con ella, pero cada dia aprendo mas de ella"

    "me detuve unos segundos para formular mi pregunta"

    mc "vi que le dijiste algo a Yuri hace un rato"

    m "¿enserio?"

    mc "si recuerdo que le susurraste y-"

    m "oh... tranquilo es una cosa entre nosotras, ya sabes cosas de chicas"

    "siento que me esta mintiendo"

    mc "..."

    m "bueno tengo unas cosas que hacer, asi que nos vemos mañana [player]"

    "que manera tan amable de decir, largate"

    mc "esta bien, adios Monika"

    #cambiar a escena de casa de TN

    "cosas de chicas"

    "aún recuerdo su cara parecia una mezcla de ansiedad y miedo"

    "y solo me ignoro para irse de la habitación..."

    "mañana deberia de preguntarle... obsesiva... obsesión..."

    "creo que ya tengo la suficiente inspiración para poder escribir otro poema"

    "no pienso que ella la este pasando mal conmigo... cada dia la entiendo mejor"

    "yo también me he abierto a ella"

    mc "..."

    mc "no estoy llegando a ni un punto"

    "agarré un boligrafo y empecé a escribir"

    #transición

    "realmente no me interesa si a Monika le parece bien o mal que hablemos"

    "aunque siento que hay algo mas profundo, no creo que Monika sea ese tipo de Chico Frikis"

    #transición

    "antes de abrir la puerta del club escuche como se elevaba la vos adentro"

    mc "que..."

    "abrí la puerta"

    #transicion

    y "perdoname Monika no intentaba faltarte al res-"

    m "no acepto tus disculpas Yuri"

    m "desde que estas en el club has sido igual de tóxica"

    m "ni siquiera te comunicas con nosotras, vienes lees tus estupidos libros y te vas"

    m "si sabes que existen las bibliotecas Yuri"

    "Yuri puso apreto su mano como si intentara decir algo"

    m "¿qué? ¿quieres decir algo?"

    y "y-yo...."

    y "pienso que eres una maldita egocentrica"

    y "¿enserio piensas que está bien tratar como un estorbo a un miembro de tu club?"

    y "te crees que eres la mejor solo por popular cuando en realidad eres una player narcisista"

    y "con el ego mas frágil que una rosa"

    y "asi que... ¡piensa dos veces ant6es de hablar!"

    y "porque cuando acabe contigo, ni si quiera tus padres podran reconocer-"

    m "que si Yuri, que si"

    m "¿porqué no muestras a los demás como realmente eres?"

    m "he intenado ayudarte incluso hablandole a los demas"

    "Monika voltea a verme"


    m "vamos, muestrale a [player] como realmente eres"

    "Yuri se da cuentan de mi presencia"

    y "¿[player]...? N-no espera, no intentaba decir eso!"

    y "¡No soy asi!"

    y "y-yo solo..."

    "monika le toca el hombro a Yuri haciendo que ella la voltee a ver"

    m "tranquila, siempre puedes tener un consejo de mi parte incluso en los momentos malos"

    m "¿has considerado acabar con tu vida?"

    m "ayudaria a que dejes de hacer esas cosas!"

    y "..."

    "como ayer, Yuri salio de la habitación con lagrimas en los ojos, estoy asustado por las plabaras de Monika"

    "realmente no se que decir, pero iré a ver a Yuri antes que salga del club Monika llama mi atención"

    m "oye, dejala ella necesita estar sola pa-"

    mc "que carajo pasa contigo Monika un consejo, matate. ¿en serio?"

    "noto a mi alrededor, Sayori esta en una silla curbriendose los oidos"

    "está llorando"

    m "oh bueno gritame y hazme ver como la mala"

    m "ya has visto como es Yuri, solo me defendí frente a lo que me dijo"

    mc "estas enferma... Yuri no es asi sacaste su peor lado, ire con ella"

    m "espera"

    "no me detuve y abri la puerta"

    m "lo digo enserio, no creo que te guste lo que estas aputno de ver"

    mc "callate maldita insoportable"

    #transición 

    "intente seguir el ritmo de Yuri pero ella corria demasiado rapido"

    #transicioón 

    "cuando bajaba las escalera termine cayendo en el suelo golpeandome la cabeza"

    mc "mierda..."

    "intente levantarme con dificultad, ha este punto probablementer Yuri ya se haya ido"

    "me sostuvo de una parte de las escalera, logré esuchcar unos sollozos cercanos en el silecioso pasillo"

    "seguí el sonido de los sollozos, venian del baño"

    "es el baño de las mujeres dudo que pueda entrar..."

    "prefiero que me expulsen antes que dejar sola a Yuri!"

    #transición

    #añadir escena prespectiva de Yuri 

    mc "yu-yuri?"

    y "-!"

    "no puedo evitar mirar el brazo de Yuri"

    "tiene tantas marcas de cortes... recientes..."

    y "[player] n-no se supone que deberia de estar aqui..."

    "no tengo la suficiente confianza de decir algo, di unos pasos hacia Yuri"

    y "¡No!"

    y "alejate... porfavor..."

    y "soy peor que un fenómeno..."

    "Yuri apreto su mano derecha y volvió a cortarse"

    mc "por-porfavor... Yo solo quiero ayudarte"

    mc "estas sangrando mucho... quizas alguna enfermera aun no se haya ido"

    y "yo... no merezco ser ayudada, me esuchaste... esuchaste como soy"

    y "tan"

    y "tan desagradable"

    "di unos pasos, acercandome a ella"

    "se que Yuri también estuvo mal diciendo eso... pero fue por la insensibilidad de Monika"

    "no puedo juzgarte"

    y "hay tantas emociones... que la he guardado por tanto tiempo..."

    y "pero por si fuera poco no puedo contenerlas..."

    "Yuri se levanta del suelo al ver como me acerco a ella"

    y "¡alejate de mi!"

    "no se que hacer... pero haré todo lo que pueda"

    "para ayudarla"

    mc "Yuri... dejame ayudarte"

    "los gotas de sangre cayeron en el suelo poco a poco mientras ella se volteba evitando verme"

    y "¡ya te dije que no quiero tu ayuda!"

    y "no se si un dia no pueda controlarme y termine haciendole daño a los demas... a ti"

    y "no puedo luchar con esto, no puedo controlarme"

    y "y no puedo dejar que los demas vean como realmente soy..."

    y "yo no quiero aceptar quien realmente soy... porque se que solo soy"

    y "una enferma"

    "mientras Yuri hablaba me acerque por detras de ella"

    y "¿¡escuchame, no merezco ser ayudada mucho menos por ti!?"

    y "¡¡¡¡SOLO DÉJAME EN PAZ!!!!"

    "cuando porfin estaba cerca de ella"

    "cerca de sus heridas"

    "ella corrió fuera del baño"

    mc "¡Yuri espera!"

    #transición

    "aunque intente alcanzarla, el dolor en mi cabeza incrementaba por los movimientos bruscos"

    "la he perdido..."

    "me siento en una banca cerca de uno de los salones vacios"

    mc "Yuri... dejame ayudarte"

    "mientras descanso siento como si mi cabeza estuviera por explotar"

    "no puedo quedarme aqui sin hacer nada"

    "me levante y mientras recorria el pasillo me choque con una figura pequeña"

    mc "¡auch!"

    "esucho como caen unas monedas en el suelo"

    n "carajo..."

    mc "oh disculpa Natsuki no te habia visto"

    n "de que hablas si por poco pasasbas atropellandome"

    n "la próxima no te perdonaré"

    mc "ya pedí perdon Nat- y esas monedas son tuyas, ¿verdad?"

    n "¡que te importa!"

    mc "esta bien disculpa..."

    "Natsuki observa las monedas en el suelo para luego voltear a ver"

    n "está bien losiento, estaba buscando algunas monedas para ayudar a mi padre con el dinero"

    n "aunque sea solo unas monedas ayuda mas de lo que parece"

    mc "oh..."

    "natsuki se queda en silencio por unos segundos"

    n "ugh, ya solo olvidalo, porcierto ¿porqué no estas en el club?"

    mc "bueno es un poco dificl de encontrar pero necesito encontrar a Yuri"

    n "oh"

    n "¿la estas acosando?"

    "no creo que esto se considere acoso..."

    mc "porfavor Natsuki, es un problema real"

    n "uhm..."

    n "creo que la vi saliendo del colegio"

    mc "¿¡si!? y donde podra haber ido?"

    n "no estoy segura, pero cada vez que nos vamos juntas solemos despedirnos en la casa de ella, vivimos cerca"

    mc "y crees que haya ido ahi?"

    n "ni idea"

    mc "y podrias llevarme ahi?"

    n "asi que ahora tengo que ayudar a un rarito a acosar a mi amiga"

    mc "Natsuki esto es en serio, no es por mi es por la seguridad de ella"

    n "ya..."

    n "supongo que si es por eso te ayudaré, pero no menciones que fui yo"

    "Natsuki me lleva afuera de la escuela"

    #transición a la casa de Yuri

    "¿enserio Natsuki estaba buscando monedas para eso? se que no deberia de meterme pero que tan mal estará"

    "para tener que hacerlo... siento como si en realidad me ocultara algo mas"

    "la pelirosa me saca de mis pensamientos al darme un pequeño empujon"

    n "oye ya llegamos, si te estas arrepitiendo mejor largate"

    mc "muchas gracias Natsuki realmente me ayudaste mucho"

    n "si bueno, de nada, espero este bien"

    "Natsuki se alejo de mi vista"

    "me acerque a la puerta, es una casa muy grande para solo una Chico Friki espero no esten sus padres"

    "cuando mi mano se dirige a tocar el timbre pienso en Yuri... presione el timbre con fuerza"

    "pero nadie vino"

    "lo presioné denuevo"

    mc "¡Yuri! ¿te encuentras en casa?"

    "resonó el sonido de las cortinas al cerrarse desde la segunda planta"

    mc "solo quiero hlabar contigo..."

    "por lo menos se que está aquí"

    "¿pero que puedo hacer?"

    #okay como tal aqui pongo la base pero siento que aqui vendria hiper bien una elección

    "no quiere ayuda..."

    "toque la puerta"

    mc "¡Yuri traje nuestro libro, para que podamos leerlo... quizas en otro lugar como tu casa"

    "los segundo se sienten eternos"

    "luego de mas de un minuto escucho la cerradura abrirse lentamente"

    "aunque la puerta se abria se detuvo abruptamente"

    y "¿[player]...?"

    y "¿qu-que haces aqui?"

    mc "como te fuiste temprano del club pensaba en que podriamos ya sabes leer"

    y "... deberías de irte"

    "la puerta se empezo a cerrar lentamente, inmediatamente puse mi pie bloqueandola"

    mc "lo siento Yuri pero no pienso en dejarte sola, quieras o no estaré para ti"

    "sonaba mejor en mi cabeza..."

    "pero no quiero que algun dia no pueda volverla a ver por culpa de esto"

    "la puerta se abre denuevo"

    mc "gracias..."

    "entré dentro de la casa, en la sala puedo ver a Yuri"

    "puedo ver sus antebrazos, llenos de cortes aunque alguno aun sigue abiertos... o nuevos"

    mc "Yuri..."

    y "losiento... No queria mostrarte como realmente soy y... que me dejaras de hablar..."

    mc "no te dejaré de hablar Yuri"

    "saco el libro de mi mochila"

    mc "¿continuamos donde lo dejamos?"

    y "okay.."

    "ya no está tratando de evitarme, Yuri dudo unos segundos antes de hablar"

    y "necesito subir a limpiarme"

    mc "claro, tómate tu tiempo"

    "ella subió las escaleras no sin antes verme, nuestros ojos chocaron otra vez. Continuó subiendo las escaleras"

    "tomo asiento en el sofa y abro el libro en la ultima pagina que leimos"

    "como puedo ayudarla..."

    "me toque la cabeza y senti un dolor punzante, suspire esperando a Yuri"

    #transición

    "*bzzt*"

    "*bzzt*"

    "mi celular empezo a vibrar desde mi bolsillo ¿sera Sayori?"

    "atiendo el mensaje"

    #agregar el ??? y el sondio de bzzt para no hacerse wey

    "???" "deja de evitarme"

    "¿qué?"

    "???" "ella no te merece, creeme es una loca"

    "quizas te estes confundiendo de numero, soy [player]"

    "no recibi respuesta en un minuto"

    "¿quien ere-"

    y "¿[player]?"

    "del susto tire mi celular al suelo"

    y "dis-disculpa no queria asustarte"

    y "estabas haciendo algo importante? creo que te vi chateando con alguien"

    "noto que mi celular esta tirado en el suelo, me asustó mas el mensaje que Yuri"

    mc "No, es solo que me tomaste de sorpresa"

    "recogí mi celular del suelo, el numero desconocido estaba escribiendo, mas sin embargo guardé mi celular"

    "anque aun me pregunto quien será, realmente me importa mas Yuri en estos momentos"

    mc "de hecho te estaba esperando"

    "Todo ha estado pasando muy rapido"

    "todo ha sido demasiado rápido y aunque quiero ayudar me siento cansado"

    #añadir el efecto de panico aunque me critiquen 

    y "pe-perdona te hice esperar mucho timepo"

    "Yuri se sentó a mi lado, la miré unos segundo a los ojos"

    "saqué el libro"

    mc "deberiamos de continuar ¿no?"

    #añadir la historia aunque me critiquen

    #porcierto dependiendo de la historia este dialogo cambiará debido a que todavia no hay una historia definida, aunque me critiquen

    "despues de leer esa linea deje de concentrarme en la historia, miro a Yuri. Pero ella no hace lo mismo"

    "\"el Chico Frikije de la historia me recuerda a ti Yuri\""

    #si no me hago wey añado el efecto de recuerdos, aunque me critiquen

    "Yuri... sus ojos violetas estan llorando"

    y "¿sabes porque elegí este libro para que podamos leerlo [player]?"

    "..."

    y "porque no se como hablar con los demás"

    y "no sé como describir mis sentimientos"

    y "mis problemas... Solo sé leer libros"

    y "creí que al compartir este libro podria mostrarte un vistazo de como soy en realidad"

    y "pero... fué un terrible error porque ahora"

    y "ves como realmente soy..."

    mc "yo..."

    "las palabras no salieron de mi, intento acercarme a Yuri pero ella retrocedió"

    y "sé porque estas aqui"

    y "no querías leer... tu viniste porq- porque..."

    "Yuri no pudo continuar hablando"

    "¿por qué vine aqui?"

    "recientemente conocí a Yuri, pero es alguien importante para mi"

    mc "es cierto, no vine aqui para continuar leyendo"

    "levanta la mirada hacia mis ojos, yo tambien hacia los suyos"

    mc "no vine porque sentía pena por ti"

    mc "vine porque..."

    mc "quisiera ayudar, pero ayudarte a ti, Yuri"

    mc "lo que haces es peligroso"

    mc "un dia podrías equivocarte y... no podria volverte a ver"

    y "[player]..."

    y "no puedo parar"

    y " ya lo he intentado varias veces"

    y " se lo que me podria pasar si me llegara a equivocar por un centimetros mas sin embargo"

    y "no"

    y "puedo"

    y "ᵈᵉʲᵃʳ ᵈᵉ ʰᵃᶜᵉʳˡᵒ"

    "regrso a acercarme a Yuri pero en lugar de retroceder ella se queda quieta"

    "suavemente agarro su mano con la mia. sostuve su palida y fria mano"

    mc "pero esta vez no estas sola"

    mc "prometo ayudarte en todo lo posible, para que juntos puedas superar esto"

    mc "tu y yo"

    y "pero... yo solo te he arrastrado hasta aqui"

    y "estuviste en el momento en cuando le dije a Monika... ES-estabas ahi y aun asi decidiste en seguir"

    "porque te amo Yuri"

    mc "porque es lo que deberia de hacer Yuri, ayudarte sin importar la circunstacia"

    "te amo"

    "pero"

    "no sé que es amar..."

    y "[player]... yo no tengo amigos"

    mc "eso no es cierto"
  
    mc "me tienes a mi. Prometo hacer todo lo posible con tal que nada ni nadie te lastime"

    y "..."

    "quizás este sea un momento indicado"

    "agarro mi mochila y de ella saco una hoja de papel"

    mc "sé que no estamos en el club, pero"

    mc "escribí esto... para ti"

    y "¿para mi?"

    mc "es un sentimiento que queria plasmarlo"

    y "pe-pero, no escribí nada"

    mc "esta bien ¿te gustaría leerlo?"

    "estiro mi mano para darle el poema a Yuri"

    "ella asiente y sostiene la carta"

    #aqui se agrega el poema 

    "derrepente, ella empieza a lagrimear. Sus mejillas quedan mojadas por las gotas de sus ojos"

    mc "Yuri, realmente quisiera apoyarte"

    mc "Ayer vi como Monika te dijo algo en voz baja y como me evitaste"

    y "y-yo..."

    "La voz de Yuri se quebró, su manga se volvió rojiza. Ella no habia limpiado sus brazos"

    "Yuri se levantó, antes que siguiera la agarré de la mano"

    y "[player] por favor..."

    mc "confia en mi"

    "aunque no muy segura, me dio suavemente su mano. la manga de su mano bajo sola"

    "Yuri..."

    "Yuri tiene varios cortes... nuevos, viejos... ligeros y... profundos"

    "Cicatrices sobre cicatrices"

    "no puedo quedarme quiero observando"

    mc "¿tienes un botiquin o curas?"

    y "creo que si..."

    #transición casa de MC 

    "10:43 AM"

    "Este sábado es lo que necesito luego de una semana tan complicada"

    "Yuri, pudo confiar en mi y yo en ella e incluso me dió su número"

    "pero aun me inquieta las demás"

    "Sayori evadiendome aunque seamos mejores amigos... eso creo"

    "Natsuki también parece tener un problema que aún no puedo saber"

    "desde ayer he estado recibiendo mensajes de un numero miesterioso"

    "se me está complicando seguir el ritmo a todo..."

    "pero Yuri"

    "luego de curar su heridas quedamos en que ibamos a salir a salir hoy"

    "me fui con ansiedad de su casa, que ella no pudiera controlar sus impulsos..."

    "es un dia nublado hayá afuera"

    #cambio de escena a la cocina

    "saqué mi telefono para escribirle a Yuri, desde que me fuí de su casa no hemos hablado."

    mc "Hola Yuri, estoy saliendo de mi casa pero antes de ir quería saber como estás"

    "Se que este día será bueno para ambos"

    "*bzzt*"

    y "Ya me encuentro lista, gracias por preguntar."

    #cambio de escena suave

    "me acerqué a la puerta de la casa"

    "toque el timbre"

    #pausa de unos 5 segundos con sonido de timbre

    "escuché como la puerta se abria"

    y "hola [player]"

    mc "pensaba que me ibas a dejar plantando"

    y "u-uh no claro que no haria eso"

    mc "no lo digo enserio... ?deberiamos irnos?"

    y "¡si! porsupuesto"

    #escena de transición 

    "Yuri continua mi paso"

    "aunque un poco detrás de mi"

    "hay muchas plazas en la ciudad"

    "restaurantes, tiendas, centros comerciales ¿a donde le gustará ir a Yuri?"

    "mientras seguimos recoriendo noto una cafeteria, a el ella le gusta el té y tranquilidad"

    mc "¿te gustaría ir a esa cafeteria?"

    y "me parece bien, en realidad suelo visitar este lugar frecuentemente"

    "entramos, mientras esperamos en la fila miro el menú escrito arriba"

    mc "ya que sueles ir aqui ¿alguna recomendación?"

    y "uh, hay demasiadas cosas para probar, no quisiera elegir mal"

    mc "tranquila, no soy tan exigente"

    y "supongo que... podrías beber un té blanco"

    mc "me parece bien y que escogerás?"

    y "un té Oolong"

    mc "oh creo que ese fué el bebimos mientras estavamos en el club"

    y "si..."

    "si, el club"

    "Sayori, despues de terminar esta cit... salida iré a ver como está ella"

    y "(hola me da un té Oolong)"

    y "(¿hola me podria dar un té OOlong?)"

    "me volteo hacia Yuri"

    mc "¿me estabas diciendo algo?"

    y "estaba practicando lo que iba pedir"

    y "¿no te sueles preparar mentalmente para pedir algo?"

    mc "¿qué?"

    y "oh si... que verguenza..."

    y "que que vergonzoso"

    "mierda, como podría recuperar la situación"

    #aqui una elección 

    mc "oye tranquila, tu ya habías decidido por mi y supongo que es más dificil elegir por cuenta propia"

    mc "ademas es muy lindo"

    y "¡que!"
    
    "vendedor" "siguiente"

    "vendedor" "buenos días ¿qué les gustaría ordenar?"

    mc "un té blanco para mi porfavor"

    "vendedor" "anotado y usted señorita?"

    y "uhhh... u-un"

    y "u-un... t-... té OO-"

    "cliente" "¿oigan podrían apurarse? tengo un tiempo limitado"

    "vendedor" "un té ¿de?"

    "el vendedor deja de mirar a Yuri y voltea a ver a la fila de atrás"

    #aqui eleccion de si pedir por yuri o deja que Yuri elija, la hisotira como tal seguira aqui por una manera de la ruta buena

    mc "a ella le gustaría tun té Oolong"

    "vendedor" "té Oolong y blanco ¿sería todo?"

    mc "si, gracias"

    "pago la orden, luego junto a Yuri vamos a una mesa vacia"

    y "l-lo hice terrible... y seguramente te hice pasar pena, losiento"

    mc "no hay de que disculparse Yuri"

    y "pe-pero ese señor nos grito..."

    y "te avergonzé ¿verdad?"

    mc "Yuri, si quieres saber mi respuesta deja de voltear la mirada"

    mc "Yuri está bien, no estoy avergonzado ni nada parecido y sobretodo"

    mc "a quien le importa las Chico Frikis que gritan por cualquier minima cosa"

    mc "no te preocupes por lo que digan los demás"

    y "me preocupo por lo que digas tu..."

    mc "entonces todoe está bien, en realidad yo deberia de pedir perdón"

    mc "te distraje mientras te preparabas para pedi"

    y "gracias... ordenaste por mi, enserio lo aprecio"

    mc "no hay problema"

    "*bzzt*"

    "el camarero pone las ordenes en la mesa"

    "*bzzt*"

    mc "y ¿ya ha-"

    "*bzzt*"

    y "puedes contestar, no me molesta"

    mc "no, solo lo apagaré un rato, dame un momento"

    "agarré mi celular y vi los mensajes del numero desconocido"

    "???" "ya vas a responder o estas ocupado \"bebiendo té\""

    mc "jodete"

    "apagué mi celular"

    mc "sabes, me gustaba pasar tiempo en el club contigo"

    y "a mi tambien, era agradable... eres"

    mc "me uní al club por unos cupcakes y Sayori"

    y "siendo honesta, cuando me uní al club pensé que podria encontrar Chico Frikis con gustos similares a los mios"

    y "como la pasión que tengo por lo libros, siempre me he sentido un poco aislada de los demas"

    y "tenia la esperanza de poder deja de ser tan indiferente de los demas..."

    y "parece que no salió como me esperaba"

    y "Monika"

    y "ella me invitó al club primeramente"

    y "no quisiera que la odies... por mi culpa"

    y "sé que es una buena Chico Friki..."

    "¿una buena Chico Friki?"

    "una buen Chico Friki no diría que te suicides"

    "pero, una buena Chico Friki tampoco diria que va a matar a alguien..."

    mc "prefiero de no hablar de ella pero"

    mc "estas equivocada en lo de socializar, me refiero. Estas aquí conmigo"

    mc "tienes a Natsuki que si excluyes las diferencias estoy seguro que serian buenas amigas"

    mc "también a Sayori quien estoy seguro te considera su amiga"

    mc "me encanta estar contigo hoy, pero odio que la razon por la que estemos aqui sea Monika"

    y "tienes razón, denuevo"

    "Yuri me sonrie, dejando su timidez atrás"





















    




    







    



    return



    















    












    return




























    





    



    
















    







   


    














    















