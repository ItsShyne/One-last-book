label chapter6:

    stop music fadeout 2.0
    scene bg splash2
    with dissolve_scene_half
    pause 3.0

    scene bg bedroom
    with fade
    play music t112

    "Hoy he despertado en mi propia cama."
    "No leímos la ultima noche juntos, así que ella está sola en su casa."
    "En realidad, no hemos hablado la ultima semana, desde que le dije que estaba pensando en un doctor para ayudarla."
    "Yuri se ve a si misma como una especie de {i}loca{/i}, y estoy seguro que probablemente un Psicológo ayudara a quitarle esa imagen."
    "De igual forma, esto es importante."
    "Le recorde a Yuri por mensaje que después de la escuela iremos a una cita de un psicólogo."
    "Miro afuera de mi ventana."
    "Esta un poco nublado, pero eso no va a pararme."
    "Continuo mí aburrida rutina de bañarme, cepillar mis dientes, y vestirme."

    scene bg kitchen
    with wipeleft_scene

    mc "Que como... ¿que como?"
    "Repetidamente abro y cierro varios gabinetes, descartando comidas que no son desayuno..."
    mc "Oh."
    mc "¡Entonces será Cereal!"
    "Lleno un tazón de cereal de maiz."
    "Y despues abro la never--"
    mc "No, no, no, no, no, no no-- {nw}"
    "Ya no tengo leche."
    "Este es muy probablemente el peor dia de mi vida."
    mc "..."
    mc "Tal vez pueda encontrar un substituto."
    "Miro entre lo más profundo de la nevera."
    "Un envase de jugo de naranja..."
    "Miro de nuevo a la tazón..."
    "Miro al jugo de naranja..."
    "Miro de nuevo el tazón..."
    "Esto es terrible, pero no tengo opción..."
    mc "..."
    mc "Señor, perdóname... por lo que estoy a punto de comer..."

    stop music fadeout 2.0
    scene bg class_day
    with wipeleft_scene
    play music t3

    "La ultima clase del día, casi termina."
    "Miro el Reloj de la pared, veo como la aguja de los segundos se mueve lentamente."
    "La profesora ha dicho algo sobre la Segunda Guerra Mundial."
    "No nesesito saber historia."
    "Ya tengo todo mi futuro planificado."
    "Escribiré una canción y me convertire en un gran rapero."
    "Tal vez de titulo debería ponerle..."
    "\"Dracukeo.\""
    "Ummmmm."
    "Supongo que puedo repetir un montón de veces esa frase y llamarle {i}musica.{/i}"
    "..."
    play sound schoolbell
    "La campana suena."
    "Parece que el dia de escuela ha terminado."
    "Le dije a Yuri que nos veamos en frente del Instituto."

    scene bg courtyard
    with wipeleft_scene

    "Tomo un atajo entre el Patio para ir a verme con Yuri."
    "Mi mente esta quemándose ahora mismo."
    "No tengo la menor idea de lo que podría pasar si llevo a Yuri a un doctor."
    "???" "\"¡[player]!\""
    "Me paro al escuchar a alguien diciendo mi nombre, esa voz..."
    show bg courtyard:
        subpixel True
        linear 1.0 xalign 1.0
    "Me giro para ver quien esta llamandom--{nw}"
    mc "Oh no..."
    show monika zorder 2 at t11
    m 2b "¡Hola [player]!"
    mc "Umm... h-hola, Monika."
    mc "¿A donde vas?"
    m 1b "Casa."
    mc "Oh...uh, lo mismo..."
    m "Bueno, entonces si no tienes planes..."
    m 5a "No estaría mal si caminaramos juntos a casa~"
    mc "..."
    "Me quedo parado como un tonto-perdido."
    "¿Cómo podría tan de repente Monika pedirme que caminemos juntos a casa cuando siquiera ni le he hablado por un mes?"
    "Y no es como si hubieramos hecho la {i}paz{/} de lo ultimo que paso en el Club."
    "Esto realmente lo pone más incómodo..."
    mc "E-en realidad recorde que iré a otro lugar."
    mc "Asi que no pued--{nw}"
    m 5b "Dijiste que ibas a casa."
    m "Tu nunca me mentirias, verdad [player]?"
    mc "N-No, es solo que..."
    show monika zorder 1 at thide
    hide monika
    show bg courtyard:
        xalign 1.0
        subpixel True
        linear 0.5 xalign 0.0
    "Miro alrededor buscando una ruta de salida."
    "En la distancia puedo ver una figura morada."
    show bg courtyard:
        subpixel True
        linear 0.5 xalign 1.0
    "Vuelvo hacía Monika."
    show monika zorder 2 at t11
    show monika 1i
    "Su mirada intensa sigue la mía, y ella también nota la figura morada."
    m "Ya veo."
    mc "Monika, nunca te mentiría..."
    m "Estoy segura de que no lo hiciste [player]."
    m "Me iré y te dejaré caminar a {i}casa.{/i}"
    m "Adiós."
    show monika zorder 1 at thide
    hide monika
    "Monika se va."
    "..."
    "Iré a por Yuri."

    scene bg schoolgate
    with wipeleft_scene

    mc "Estoy aquí."
    show yuri zorder 2 at t11
    y 1f "Allí estas. Me estaba preguntando donde estarias."
    mc "Perdóname si te hice esperar. Intente tomar un camino mas corto."
    mc "¿Supongo que no pude {i}cortarlo{/i} muy bien no?"
    y 2g "..."
    "Dejo salir una risa incómoda, pero Yuri sigue teniendo esa expresión algo seria."
    "Supongo que la palabra {i}cortarlo{/i} no fue una buena expresión suponiendo hacia donde vamos..."
    "Pongo mi mano en su hombro."
    mc "Yuri mírame."
    y 2t "..."
    mc "Todo estará bien. Lo prometo."
    "Allá vamos..."

    stop music fadeout 2.0
    scene bg waiting_room
    with wipeleft_scene
    play music t108

    mc "Vale, aquí es."
    "Miro al reloj colgando encima de la puerta."
    mc "Justo a tiempo."
    mc "El doctor debería estar aquí en cualquier segund--"
    play sound closet_open
    "Sin tiempo para terminar mi oración, un hombre sale de una habitación."
    "Es un hombre en la edad de Adulto, no es tan joven ni tan {i}señor{/i}, con un cabello negro que empieza por un gris."
    "El viste unos de esos trajes de {i}moda{/i}, un traje típico de una revista de ropa."
    "Unos buenos zapatos elegantes, una corbata negra, incluso tiene un reloj de oro, parece real..."
    d "Doctor Peter Lankton, psiquiatra."
    d "Es un placer conocerlo."
    "Tenemos un apretón de manos."
    d "Tu debes de ser [player], correcto?"
    mc "Si señor, y esta es Yuri."
    show yuri zorder 2 at t33
    show yuri 4a
    "El aprieta la mano de Yuri."
    y 4c "..."
    "Bueno, esto es incómodo."
    "El Dr. Lankton agarro la mano de Yuri... espero que ella no lo tome mal..."
    d "Ah, te entiendo. Puede que estes nerviosa por que soy doctor, Lo sé."
    d "Pero quiero que sepas que no hay nada que temer."
    d "Este es un lugar seguro."
    show yuri 4a
    "El señala con su brazo su oficina."
    d "Entonces, ¿Quieres pasar e iniciamos la sesión?"
    mc "Esta bien, vamos."
    d "Oh, lo siento joven, pero por ahora solo quisiera hablar con la chica."
    mc "¿Qué? ¿Enserio?"
    d "Solo por ahora. En las proximas secciones podrás pasar, pero para la primera es mejor que sea entre doctor y paciente."
    "Supongo que puedo entender eso..."
    mc "Okay...esperaré aquí."
    d "Gracias por entenderlo."
    "El se dirige a Yuri, quién no ha dicho una sola palabra desde que llegamos."
    d "¿Deberíamos pasar?"
    y 4d "..."
    "..."
    d "..."
    mc "..."
    mc "Doc, le importaría si hablara con ella por un momento?"
    d "No. Tomense su tiempo. Estaré en mi oficina, que entre cuando este lista."
    play sound closet_close
    "El entra a su oficina y cierra la puerta."
    show yuri zorder 2 at t11
    mc "¿Que estas pensando ahora mismo?"
    y 3o "N-no... no p-puedo hacerlo."
    mc "No digas eso."
    show yuri 4a
    "La miro directamente."
    mc "Escúchame."
    mc "Eres fuerte, puedes pasar esto."
    mc "Y estaré todo el tiempo aquí esperándote."
    mc "El Dr. Lankton solo quiere ayudarte."
    mc "Pero nesesito que me ayudes a ayudarte..."
    "Yuri me mira fijamente."
    y 3w "Okay..."
    y 3s "Lo hare lo mejor que pueda."
    mc "Eso es todo lo que pido."
    show yuri a thide zorder 1
    hide yuri
    "Me despido, y después, entra en la oficina."
    "..."
    mc "Bueno, supongo que me quedaré esperando."

    scene bg waiting_room
    with wipeleft_scene

    "Tomo asiento, y miro alrededor."
    "La sala de espera esta llena de posters motivacionales, imagenes y otras cosas estúpidas."
    "Miro hacía otra pared."
    mc "Un certificado de psicológo, Dr. Peter Lankton, blah, blah, blah, Universidad de Standord, blah, blah, blah..."
    "Se ve que este tipo sabe totalmente de esto."
    "Esto es perfecto."
    "Por primera vez en esté mes puedo relajarme..."
    "Realmente estoy logrando la ayuda que Yuri realmente nesesit--"
    stop music fadeout 1.0
    "{i}*bzzt* {/i}"
    mc "Pero que..."
    "Saco el teléfono de mi bolsillo."
    "¿Un mensaje de un numero desconocido?"
    play music t113
    "???" "{i}No puedes sanar lo que está roto. {/i}"
    mc "¿Que coño...?"
    "Esta es la misma persona de hace algunas semanas."
    "¿Que es lo que quiere?"
    "???" "{i}No te preocupes. Una vez que tu novia no este, no tendremos que preocuparnos por ella. {/i}"
    "???" "{i}No es como si fuera importante. {/i}"
    "Esto ha ido muy lejos."
    "Furiosamente le escribo una respuesta."
    mc "{i}Mira, no se quien eres, pero deja de escribir mensajes, no sé de qué estas hablando. {/i}"
    "???" "{i}Ambos sabemos de que chica estamos hablando, [player], la unica que prestas atención. {/i}"
    "¿Quién es esta persona?"
    "¿Como mierda sabe mi nombre?"
    "¿Tiene que ver con Yuri?"
    "Mis manos estan temblando..."
    mc "{i}¿¡Quien eres!? {/i}"
    "???" "{i}Ya no hará falta preocuparse, lo sabrás pronto.{/i} "
    "Apago mi teléfono para evitar más mensajes de esta persona."
    mc "¿Quien es esta persona?"
    "La unica persona que puedo recordar que tiene mi numero es Sayo---{nw}"
    stop music fadeout 1.0
    play sound closet_open
    "El Dr. Lankton y Yuri salen de la oficina."
    "Empujando a un lado mis pensamientos, me paro de la silla para hablar con él."
    mc "¿Todo bien Doctor?"
    d "Tu amiga esta en buena salud."
    "Lo miro de forma confusa."
    mc "¿Enserio?"
    d "Sí. Ella tiene el caso común de la Ansiedad Social."
    d "Es totalmente común, ella esta sana mentalmente."
    d "Tal vez deberían hacer otra citación, para poder ayudarle un poco con eso."
    mc "¿Entonces como hacemos?"
    d "Hay casos asi, con esa edad, la ansiedad se va apartando poco a poco."
    d "También hay algunas terapias, y médicos profesionales como yo estan al servicio para ustedes."
    mc "¿Tan simple como eso?"
    d "Tan simple como eso."
    "El me da una sonrisa."
    mc "Gracias Doc."
    mc "Y que hay de lo de ella de...usted sabe..."
    d "¿Saber qué?"
    show yuri zorder 2 at t44
    show yuri 4b
    "Miro a Yuri, esta arrinconada cerca de la puerta."
    "Ella no pudo decirle a el sobre sus cortes."
    show yuri zorder 1 at thide
    hide yuri
    mc "Doc, ¿Exactamente de que hablaron?"
    d "Lo siento pero esa es información privada a la cual no puedo revelar."
    mc "Confidencialidad entre Paciente y Doctor..."
    "Hay un extraño cambio en mi voz cuando dirigo ese termino a el."
    d "Por supuesto, si ella quiere revelarte esa información, es la elección de ella."
    mc "Gracias Doc."
    d "Un placer."
    "Le doy un último apretón de mano, y salgo con Yuri del edificio."

    scene bg residential_day
    with wipeleft_scene

    "El resto del caminar a casa es tranquilo..."
    "Ninguno de nosotros elige decir una palabra."
    "No puedo creer que después de toda la ayuda que le he dado a Yuri... ella hace esto."
    "¡Ella no pudo decirle a alguien lo que esta mal en ella!{fast}"
    "..."
    "......"
    "Nesesito calmarme."
    "No es su culpa. Yo tenía que tener el presentimiento de que esto iba a ocurrir."
    "No debí forzarla a ver un psiquiatra."

    scene bg living_room
    with wipeleft_scene

    show yuri zorder 2 at t11
    show yuri 4b
    "Caminamos adentro de la casa y Yuri toma asiento en el sofa."
    "Me paro enfrente de ella, antes de sentrarme y hablar con ella."
    "Nesesito disculparme."
    mc "Yuri, Yo--"
    y 3p "Lo siento."
    "Ella cubre su cara con sus manos, y empieza a llorar."
    y 3o "Te he fallado, como siempre lo hago con todos los demas."
    "Pongo mi brazo alrededor de ella."
    mc "No Yuri...Yo te he fallado."
    mc "Yo debí saber que esta mal forzarte a hacer algo como eso."
    show yuri 3t
    "Ella baja su cabeza y se acerca más a mí."
    "Sus ojos lavanda estan llenos de lágrimas."
    y "No... tu tienes r-razón para a-ayudarme..."
    y "Y-yo... quiero volver."
    y "¿Puedes programar otra cita?"
    "Estoy desconcertado."
    mc "¿Enserio?"
    y 2v "Yo se que esto es lo mejor para mí...y tú estás de mí lado..."
    y 2s "Yo pienso que podemos superarlo..."
    mc "Estoy de tú lado, Yuri."
    "La miro fijamente."
    y 3v "¿Puedes hacerme un favor, [player]?"
    mc "Por supuesto."
    y 3t "No se como podría explicarle todo al doctor."
    mc "Bueno..."
    mc "Soy todo oidos si me nesesitas."
    y 3w "Gracias."
    play music t101
    "Yuri se toma un momento para organizar sus pensamientos."
    y 3t "¿Sabés por qué lo haré?"
    mc "Supondré qué no sientes que tienes algún tipo de control sobre tus emociones."
    y 3v "No podría decir que no estas acertado en eso."
    y "..."
    y 3t "[player], en toda mi vida entera he permitido a las personas que sean la pega, las pegatinas, y las vendas que se mantienen unidas a mí."
    y "Y cada vez se han reabierto sin ninguna complicación."
    y 2w "..."
    y 2t "Solo era una niña pequeña cuando vi por primera vez como este mundo puede ser tan despiadado."
    y "Mi madre y mi padre podían ser capaces de discutir sin parar. Estaba asustada de que algún dia podían lastimarse entre sí."
    y 3v "He usado a los libros para apartarme."
    y "Yo hubiera esperado enterrar mi propia realidad para construir una nueva."
    y 3t "Eventualmente mi madre se separo de mi padre y de mí, y mi madre tuvo que tener un trabajo extra para soporte."
    y "Con todo eso pasando yo sólo continúe reprimiendo mis sentimientos y leyendo mis libros."
    y 3w "Asi he estado toda mi vida..."
    "Ella se detiene otra vez para respirar lentamente y reunir más sus pensamientos."
    y 2v "La secundaria han sido los peores años de mi vida."
    y "Todos son tan crueles e injustos."
    show yuri 2t
    "Ella mira profundamente mis ojos."
    y 2s "O asi fue antes de que te conocí..."
    y 2v "Pero aún asi, los niños del instituto siempre me han llamado con tontos apodos, o esparcian falsos rumores de mí."
    y 3n "Los chicos siempre me ignoraban, o se alejaban de mí cuándo caminaba, o me decían apodos obsenos..."
    "Ella esta empezando a tener pánico."
    "Puedo ver el miedo creciendo en sus ojos mientras recuerda."
    mc "Yuri, creo que deberíamos dejar esto por ahor--"
    y 2p "¡No!"
    y 2o "Tengo que dejar salir esto..."
    y 2t "...Por favor."
    "Sus lágrimas continúan cayendo."
    "Lentamente asiendo y la dejó continuar."
    y 3v "No pude encontrar una forma para liberarme de este dolor."
    y 3t "No existe algo como la cura para el dolor."
    y "Asi que intente encontrarla."
    "Intento comprender lo que ella esta diciendo."
    mc "¿Asi que asi fue? Los libros, fueron para apartarte."
    y 2v "Esos fueron el comienzo."
    "¿El comienzo?"
    y "Al principio estaba muy asustada."
    y "Pero ese primer momento que lo hice..."
    y 2y6 "El sentir de la hoja separando mi piel..."
    y "El acero frío chocando contra mis sentidos."
    y "La belleza de esas gotas cayendo de mi brazo."
    y "Eso es tan..."
    "¿Qué?"
    y 2w "No me costó tanto llegar a apostar con el dolor."
    y 2v "Mas bien, he sido seducida por el."
    y "Se siente tan bien...cortarse..."
    y 3o "Yo se que esto esta mal, pero no soy capaz de detenerme."
    y "Mi mente ya esta totalmente pérdida. No fui lo suficientemente fuerte para parar con esto."
    y 3t "Si siento un sentimiento que realmente no puedo entender, solo soy capaz de gritar para parar de sentirlo."
    y "Cuando me corto, se siente como si estuviera en mi propio mundo."
    y "Es el mismo sentimiento como cuando leo mis libros."
    y 3v "Excepto que las palabras estan escritas en rojo."
    y "Y la hoja es mi pluma."
    y 3w "Pero un libro se puede terminar. Mi brazo puede sanar, y puedo revivir ese momento de verdadera libertad continua..."
    "Esto es peor de lo que imaginé."
    "Siempre pense que era una manera de olvidarse de la vida, pero me doy cuenta de que es más como un tipo de droga."
    "Ella ha formado una adicción incontrolable que me desgrada un poco."
    mc "Yuri..."
    mc "Esto es mucho para digerir pero... solo quería decir..."
    mc "No te juzgo."
    y 2t "¿Q-Qué?"
    mc "Nada de lo que te ha pasado es tu culpa."
    "Agarro su mano contra la mía."
    mc "No podemos controlar lo que pasa en nuestras vidas, y a veces no podemos controlar lo que sentimos."
    mc "A veces se puede sentir una poderosa fuerza controlandonos, empujandonos, y obligandonos a hacer cosas terribles."
    mc "...Como marionetas atadas a sus hilos."
    y 2v "..."
    mc "Nunca podré entender lo que sucede en tu cabeza..."
    mc "Pero estoy bien con eso."
    mc "Por qué aún seguire mi promesa de nunca dejarte."
    mc "Juntos podremos resolverlo."
    mc "Porque somos amigos y eso es lo que hacen los amigos, apoyarse."
    "..."
    "Otro pensamiento se cruza en mi mente."
    mc "Yuri, donde obtienes esos cuchillos?"
    y 3t "Te refieres mis c-cortes... Y-Yo tengo..."
    y 4c "Una colección de cuchillos..."
    "¿Una colección de cuchillos?"
    y "Los he estado escondiendo cada vez que has venido, porque pense que te enojarias, y lo encontrarías desagradable."
    "En cualquier otro caso diría que tener una colección de cuchillos esta muy interesante."
    "Pero por el bienestar de Yuri, no es lo correcto tenerlos."
    mc "Yuri, lo siento pero... tendrás que deshacerte de esos cuchillos."
    y 3n "P-pero..."
    y 3o "..."
    "Ella se pone a pensar por un momento."
    y 2v "Tienes razón..."
    y "Se por que lo decides, pero es difícil..."
    mc "Se que lo es, pero confía en mí. Sí realmente quieres ponerte bien, tendremos que deshacernos de todo lo afilado."
    mc "Prometeme que los tirarás Yuri. "
    show yuri 3w
    "Sus lágrimas continúan saliendo. Ella ha llorado tanto que probablemente ya no tenga mas lágrimas en sus lagrimales."
    show yuri at face with dissolve
    "Ella acuesta su cabeza contra mí pecho y continúa llorando."
    "La abrazo, y ella también me abraza."
    mc "Estarás bien, Yuri. Te prometí que nadie más te volvería a lastimar."
    y 3v "[player]...tu has oído mi historia."
    y "Ahora has visto que soy un monstruo."
    y 3o "Soy débil, no puedo controlar mis emociones. Agarro todos mis sentimientos y los suelto dentro de mí propia piel."
    y "¿Quién podría pensar que eso está bien?"
    mc "Nadie puede..."
    y 3t "¿Eh?"
    "Ella me mira, sus humedos ojos se fijan en los míos."
    mc "Porque realmente no está bien..."
    mc "Pero lo que no estaría bien para mí, es quedarme de brazos cruzados y dejarte seguir lastimandote tu misma."
    mc "No voy a parar hasta que te encuentres mejor."
    y "¿Pero... por qué?"
    mc "Porque, Yuri..."
    "Todo mí alrededor se vuelve borroso."
    "Lo unico que mis ojos son capaces de ver son a ella."
    stop music fadeout 4.0

    menu:
        mc "Porque..."
        "Te amo.":

            mc "Porque te amo, Yuri."

    play music t103
    "Lo dije."
    pause 2.0
    "La unica palabra que me hizo dudar por mucho tiempo salió de mi boca."
    pause 1.0
    "Amor."
    "Una palabra de alien para mí."
    "Esta palabra es lo unico importante en este momento."
    "Siento que todo lo que ha pasado en este último mes ya no importa."
    mc "Te amo más que cualquier cosa de este mundo."
    mc "Y cuando amas a alguien sientes que no puedes rendirte."
    y "[player]..."
    y 3v "Y-yo..."
    y "..."
    mc "..."
    y "..."
    "No me digas que no siente lo mismo."
    "Me sentiria destrozado por dentro, por todo el esfuerzo que hice por ella."
    y 3w "...Te...amo"
    "...!"
    show yuri 4b
    "Yuri se acerca lentamente y me abraza nerviosamente."
    y "...G-Gracias."
    mc "Me agradecerás una vez más cuando esa colección desaparezca."
    "Le doy una sonrisa esperanzadora."
    "Pasamos un rato en silencio."
    mc "¿Pues entonces somos...?"
    y "..."
    y "Supongo que sí."
    y "Pero empecemos despacio."
    mc "De acuerdo."
    show yuri 3w
    "Me acerco lo suficiente para apreciar sus ojos amatista."
    "Ella cierra sus ojos y se acerca nerviosamente aun más."
    show yuri zorder 1 at thide
    hide yuri
    show y_cg7 at cgfade
    with dissolve_scene_full
    $ persistent.cg_viewed[2] = True

    "Puedo sentir sus labios contra los míos."
    "Todos mis sentidos están descontrolandose."
    "El sabor vainilla de sus labios."
    "El sentir de su pelo lavanda en mis dedos."
    "El sonido de la pura armonia de nuestros corazones latiendo."
    "Mis brazos la toman suavemente, ella se tensa pero al final cede."
    "Todo lo demás en este mundo ya no existe."
    "Cada uno de los pensamientos que hacían tormenta en mí mente han sido calmados."
    "Solo somos Yuri y yo en este momento del tiempo."
    "Siento una extraña sensación en mi estomago."
    "¿Tal vez son mariposas?"
    "No puedo describir mas que solo saber que es una sensación satisfactoria."
    "Como si todas mis preocupaciones hayan sido alejadas."
    pause 10.0
    "Yuri se aparta lentamente."

    scene bg living_room
    with dissolve_scene_half

    show yuri zorder 2 at t11
    show yuri 4c

    "Eso se sintió como una eternidad, pero solo fueron unos cuantos segundos."
    "Pero esa sensación sigue estando alli."
    mc "..."
    y 4b "..."
    "Nos sentamos en silencio por un momento."
    mc "Y-Yo... uhhh... supongo que tengo que agradecerte."
    y 3q "Te tenia que agradecer de alguna forma."
    y 3a "Mejor preparemonos para el próximo encuentro con el Dr. Lankton."
    "Ella lanza una suave sonrisa, y por un momento..."
    "...Puedo sentir que todo estara bien."

    stop music fadeout 3.0
    scene black
    with dissolve_scene_full
    pause 1.0


    jump chapter7