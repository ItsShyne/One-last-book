label chapter7:


    stop music fadeout 2.0
    scene bg splash2
    with dissolve_scene_half
    pause 3.0

    scene bg bedroom
    with fade
    play music t112

    "Me tallo mis ojos despierto."
    mc "Ugh..."
    "Miro hacia mi izquierda para ver el despertador de mi telefono sonar."
    "Yuri y yo hemos continuado nuestras {i}citas{/i} de lectura en nuestras casas."
    "Desconecto mi teléfono del cargador y verifico la hora."
    mc "¡Oh Dios mío! ¡Tengo que levantarme!"
    "No quiero llegar tarde al último dia de clases."
    "Escribo un mensaje a Yuri de la fecha."
    "Ella responde de manera traquila y acordamos para desayunar en mi casa."
    "Durante la temporada de vacaciones tenemos un par de semanas libres de la escuela."
    "Asi podré estar más tiempo con Yuri."
    "Muestro una lijera sonrrisa."

    scene bg kitchen
    with wipeleft_scene

    "Termino mi rutina y decido comenzar a preparar el desayuno."
    "Me pregunto, ¿Qué pasa con las chicas que tardan una eternidad en prepararse?"
    "¿Yuri hará lo mismo?"
    mc "Qué hacer, qué hacer..."
    "Abro la nevera y agarro un paquete de tiras de tocino sin abrir."
    mc "Bien."
    "Espero tener huevos también."
    mc "¡Bingo!"
    "Agarro el cartón de huevos y lo abro."
    "Todavía quedan alrededor de media docena de huevos."
    "Eso es más que suficiente."
    "Enciendo la estufa y empiezo a romper los huevos."
    # mira las psoes que hace yuri
    scene bg kitchen
    with wipeleft_scene
    "Tocan la puerta y es Yuri."
    "Ella entra a la cocina."
    show yuri zorder 2 at t11
    y 1b "Eso huele muy bien, [player]."
    mc "Parece que estás de buen humor."
    y 1c "¡Por supuesto! Sin escuela es un sueño para mí."
    y "Tengo más tiempo para leer, aprender cosas nuevas y no tengo que preocuparme por la interacción humana."
    mc "..."
    "Me detengo notablemente."
    "Yuri no se da cuenta, y yo sigo cocinando."
    mc "¿Estás diciendo que no vas a pasar tiempo conmigo durante el descanso?"
    y 3p "Uuuuh, no quise decir--"
    mc "¡Aja!"
    show yuri 3o
    mc "Sigues cayendo por mi sarcasmo, Yuri."
    mc "Imaginé que una chica inteligente como tú se daría cuenta."
    y 2g "{i}(Tu pensarias.){/i} "
    mc "¿Qué fue eso?"
    y 2f "Ahh, ¿ya están listos los huevos?"
    "Miro hacia abajo para ver mi desayuno ardiendo."
    mc "Oh mierd--{nw}"
    "Rápidamente agarro la espátula y recojo los huevos y el tocino en los platos."
    "Traigo los platos a la barra y tomo asiento."
    mc "Yuri... aqui esta su comida~"
    y 3d "Ufufu."
    y 2b "Gracias, [player]."
    "Quizás debería intentar comenzar una conversación."
    "..."
    "..."
    mc "¿Tienes algún plan para el descanso, Yuri, además de leer?"
    y 1f "Ahhh... bueno..."
    y 2q "Realmente no."
    mc "Bueno, siempre puedes pasar tiempo conmigo."
    y 2e "¿Estás... estás seguro?"
    mc "Quiero decir, ya hemos pasado el último mes juntos. Sin escuela podemos tener aún más tiempo."
    y 3g "..."
    mc "¿Bien?"
    y "Eso..."
    y 2b "Eso me gustaría de verdad."
    show yuri 2a
    "Ella me da una sonrisa suave."
    "Reviso la hora."
    mc "¡Oh! probablemente deberíamos comenzar a salir ahora. No queremos llegar tarde el último día."
    "Agarro nuestros platos y los pongo en el fregadero."
    "Yuri y yo salimos y comenzamos a caminar hacia la escuela."
#hasta aca
    stop music fadeout 2.0
    scene bg courtyard
    with wipeleft_scene
    play music t3

    "Nosotros llegamos al patio."
    "Nuestras primeras clases son en diferentes lados de la escuela."
    "Nos despedimos y nos dirigimos a nuestras respectivas aulas."

    scene bg class_day
    with wipeleft_scene

    "La clase sigue siendo tan aburrida como siempre."
    "b negativa, más o menos la raíz cuadrada de b al cuadrado, menos cuatro ac, todo entre 2a."
    "Sí, nunca voy a usar eso en toda mi vida."
    "Hasta luego, matemáticas."
    play sound schoolbell
    "La campana de la escuela me saca de mi aturdimiento."
    "Hora de ir a la casa de Yuri."
    "Me pongo la mochila al hombro y me dirijo a la puerta."
    with vpunch
    mc "Oof."
    "Accidentalmente choco con alguien."
    show natsuki zorder 2 at t11
    show natsuki 4s
    mc "¿Natsuki?"
    "Esto es embarazoso."
    n "Ey."
    mc "Eso es para caballos."
    n 1w "¿Puedes ser serio por una vez?"
    mc "Está bien, lo siento."
    n 1c "Así que supongo que fue bien con Yuri."
    mc "¿Qué te hace decir eso?"
    n 3k "Los vi a los dos en el patio."
    mc "Oh..."
    mc "Sí, todo salió bien."
    n 3u "...Bien."
    "No sé si Natsuki sabe sobre las cortadas de Yuri, así que me abstengo de mencionarlo."
    mc "Uhhh...¿cómo te fue?"
    n 1b "Me fui a casa y me fui a la cama."
    "Esta conversación no va a ninguna parte."
    mc "Natsuki, yo actual--"
    stop music fadeout 2.0
    n 2m "¡Espera!"
    n 2n "Quería hablar sobre {i}ese día{/i}."
    play music t6
    "No me gusta a dónde va esto."
    n 5u "Puede que accidentalmente te haya dado demasiada información sobre mi vida hogareña."
    mc "Natsuki, está bien. Entiendo si tus padres están pasando por algunos problemas financieros."
    n 4u "Padres..."
    "Oh..."
    mc "Lo siento, no--"
    n 4e "Mira, cállate y déjame sacar esto de mi pecho."
    n 1i "Solo necesito desahogarme con alguien."
    mc "¿Y por qué yo?"
    n 2q "Porque eres la única persona lo suficientemente tonta como para escuchar."
    "Lo suficientemente justo."
    mc "Muy bien, continúa entonces."
    n 1q "Como estaba diciendo..."
    n 1m "La siguiente parte te corresponde."
    "Uh oh."
    n "Mucha gente ve a mi padre como un monstruo abusivo, pero no lo es."
    n "Simplemente lucha con ahorrar dinero."
    n 5h "Tiene estallidos de ira, pero se esfuerza por mantenerse."
    n 5n "Ha estado tomando medicamentos para mantenerse estable, pero incluso esos cuestan dinero."
    n "Asi que..."
    n 12c "Decidimos que es mejor si no vivo con él."
    "Lo que escucho me rompe el corazón."
    "Debe ser difícil separarse de alguien que has conocido toda tu vida."
    mc "Espera Natsuki. ¿Cómo me concierne esto?"
    mc "¿Quieres quedarte en mi casa?"
    show natsuki 1i
    "Natsuki se calma."
    n 5y "Sabía que eras un acosador."
    "Pongo los ojos en ella."
    "Natsuki vuelve a su modo serio nuevamente después de su rápido comentario."
    n 2q "Bueno, me preguntaba si podrías preguntarle a Sayori si podía vivir con ella."
    mc "..."
    "Considerando la última vez que hablé con Sayori, no creo que tenga problema alguno."
    mc "Umm...Bueno creo que--"
    n 1c "¿Ustedes son vecinos no?"
    n "¿No puedes solo pasar por su casa camino a tú casa?"
    "Pienso para mí."
    #asddfgrrgbfgg??????????????????????????????????
    "Sería moralmente incorrecto para mí dejar que Natsuki se quede sin hogar."
    "No me haria problema preguntar."
    "Pero por otro lado, quería llevar a Yuri a casa pero ella entenderá."
    mc "*suspiro*"
    "Tengo que hacer lo correcto."
    mc "Bien."
    mc "Preguntaré."
    n 5s "Gracias."
    mc "..."
    n "..."
    "Creo que la conversación ya termino."
    mc "Bueno, iré a hacer eso ahora."
    n 5u "Uhhh, sí."
    show natsuki zorder 1 at thide
    hide natsuki
    "Salgo del aula."
    "Una vez que doblo la esquina, corro locamente hacia las puertas."
    mc "Espero no llegar tarde."

    stop music fadeout 2.0
    scene bg schoolgate
    with wipeleft_scene
    play music t3

    "Llego a la puerta, pero no hay señales de Yuri."
    "Saco mi teléfono para llamarla, pero parece que ya me envió un mensaje de texto."
    y "{i}Traté de esperar, pero necesitaba llegar temprano a casa.{/i} "
    y "{i}Lo siento. Te veré mañana.{/i} "
    mc "¡Maldición!"
    "Me apoyo contra los ladrillos que componen las paredes del campus."
    "Estoy decepcionado de no poder ver a Yuri hoy."
    "Oh bueno, al menos la veré mañana."
    "Hago mi viaje solitario a casa."
    "Canto para mí mismo para apartar mi tristeza."
    mc "Mi sombra es la única que camina a mi lado..."

    stop music fadeout 2.0
    scene bg residential_day
    with wipeleft_scene
    
    "Me detengo frente a la casa de Sayori."
    mc "Bien preguntaré."
    "Me dirijo a la puerta."
    "Después de tres golpes fuertes, Sayori abre la puerta."
    play sound closet_open
    show sayori zorder 2 at t11
    show sayori 1ba
    mc "Hey."
    s 1bx "Hola [player], ¿Cómo estás?"
    mc "Sayori, Yo--"
    play music t8
    mc "Te va a sonar raro pero Natsuki necesita de tu ayuda."
    s 1bh "¿Ehh? ¿Que sucede?"
    show sayori 1bg
    "Ella parece un poco preocupada."
    mc "No puedo decir mucho pero ella necesita un lugar donde vivir."
    s 1bh "No puede ser eso es terrible."
    s 1bg "¿Pero que es de su padre?"
    mc "El tiene ciertos problemas que hizo que Natsuki tenga que separarse."
    show sayori 1bk
    "Sigo contandole a Sayori lo demás de mi encuentro con Natsuki."
    "Parece que refleja una mirada de compasión en sus ojos."
    "Pero finalmente ella habla."
    s 1bg "Entiendo lo que está pasando."
    "Mi corazón se vuelve un poco más ligero."
    s "Natsuki merece un lugar donde pueda sentirse segura. Dile que puede vivir conmigo."
    mc "Muchas gracias. Se lo diré tan pronto como pueda."
    "Ella va a cerrar la puerta."
    "No me doy cuenta que mis dedos están apoyados en ella."
    with vpunch
    "La puerta de Sayori se estrella contra mis dedos."
    show sayori a h11 zorder 2
    s 4bm "¡[player]!"
    "Mis dedos comienzan a latir e intento calmar el dolor."
    s 4bu "Lo siento mucho."
    mc "No te disculpes fui yo quien puso mis dedos."
    "Nos depedimos de nuevo y esta vez sin apoyar los dedos"
    "Sus ojos azules brillan, y lentamente ella cierra la puerta."

    show sayori zorder 1 at thide
    hide sayori
    play sound closet_close
    stop music fadeout 2.0
    "Y una vez más, me quedo solo."
    "Supongo que podría ponerme al día con algunos programas de televisión antes de acostarme."

    scene bg living_room_night
    with wipeleft_scene


    "Las horas pasaron rápidamente."
    "La luz de la luna desde mi ventana me dice que ya es de noche."
    "Me siento mal por no poder ver a Yuri hoy, pero espero poder compensarla mañana."
    "Sin embargo, me alegro de haber podido ayudar a Natsuki."
    "Tal vez Natsuki pueda ayudar a Sayori con su depresión, algo que también quiero apoyar."
    "Aturdidamente subo las escaleras y me voy a dormir."


    scene black
    with dissolve_scene_full
    pause 1.0






    scene bg bedroom
    with dissolve_scene_half
    play music t112

    "Me despierto dentro de la comividad de mis cobijas."
    "El primer día de descanso, cuando cada estudiante se olvida del mundo."
    "Me tomo un momento para mirar mi techo; el resplandor de la mañana asomandose por mis persianas."
    "No puedo evitar tener una sonrisa en mi cara."
    "Tengo un fuerte presentimiento de que hoy será un buen día..."
    "Ojalá tenga razón."
    "Después de disfrutar la sensación de despertar naturalmente, salgo de la cama."
    "Hago mis estiramientos de la mañana y me dirijo al baño."

    scene bg kitchen
    with wipeleft_scene

    "Mientras estoy desayunando, decido llamar a Yuri."
    mc "Contesta, contesta, contesta, contesta."
    "..."
    y "Hola."
    mc "Buenos dias, Yuri."
    y "Buenos dias, [player]."
    "A pesar de que todavía es bastante temprano, la voz de Yuri no muestra signos de cansancio."
    "Ella debe ser una persona mañanera."
    mc "Parece que dormiste bien."
    y "Ujuju. Eso hice."
    "Yuri se detiene el tiempo suficiente para que yo hable."
    mc "Oye, siento lo de ayer."
    mc "Me quedé involucrado en algo después de clase."
    mc "Juro que intenté salir, pero fue--"
    y "[player], está bien. Estoy seguro de que tenías una buena razón."
    y "Además...No...No podría estar enojada contigo."
    "Empiezo a sonrojarme."
    mc "Bueno, en ese caso quería preguntarte algo."
    y "Ok, pregunta lo que quieras."
    mc "Bueno, pensé que podríamos... uhhh..."
    y "¿Nosotros podríamos que?"
    "Siento que Yuri por su tono siente intriga por mi pregunta, y eso no me ayuda."
    mc "Ahh, que podrías venir hoy."
    mc "Quizás podamos ver una película o... algo."
    stop music fadeout 2.0
    y "..."
    "Hay un momento de silencio mientras Yuri reflexiona sobre la pregunta."
    y "Yo...no...¿Tu crees...?"
    mc "No te escucho bien."
    "Eso hace que haya un silencio incomodo mientras como."
    mc "Tambien está la opción de no aceptar Yuri no tengas miedo."
    y "No es eso, Estaré allí en aproximadamente una hora si está bien."
    mc "Sí, eso está bien."
    mc "Te veré luego."
    y "A-adios, [player]."
    mc "Adiós."
    "Cuelgo el teléfono."
    play music t112
    "Aprieto el puño con entusiasmo antes de darme cuenta..."
    "Algo no se siente bien."
    "Le dije a Yuri que veríamos una película."
    "Pensó demasiado en ello, será por los años de vacaciones que la pasó sola."
    "Son solo dos amigos, de géneros opuestos, solos en una casa."
    "Maldición."
    mc "Muy bien, necesito calmarme."
    "Yuri y yo hemos pasado mucho tiempo juntos."
    "Nos dimos un beso."
    "Demonios, incluso dormimos en la misma cama."
    "Aunque era una cama muy grande..."
    "Pero la misma cama, no obstante."
    "Entonces, ¿por qué me siento tan diferente?"
    "Se siente como si nuestra relación hubiera crecido de alguna manera."
    "Ya no veo a Yuri como la chica se presenta a sí misma como timida."
    
    "Ella es solo una chica normal."
    "Claro, ella todavía necesita ayuda, y todavía necesitamos deshacernos de su colección de cuchillos."
    "Pero mi mente se relaja cuando siento que realmente he progresado."
    "Estoy pensando demasiado en esto, ¿no?"

    scene bg living_room
    with wipeleft_scene

    "He preparado algunos pequeños bocadillos y vasos para que podamos ver la película."
    "Yuri debería llegar en cualquier momento."
    mc "Bocadillos."
    mc "Listo."
    mc "Desodorante."
    mc "*oler*"
    mc "Listo."
    mc "Ropa limpia."
    mc "Listo."
    mc "Película."
    mc "..."
    mc "Uh oh."
    "Todavía no he elegido una película."
    "Que voy a--{nw}"
    play sound doorbell
    stop music fadeout 2.0
    "Uh oh."
    "Me levanto para abrir la puerta."

    scene bg entrance
    with wipeleft_scene

    "Abro la puerta."
    play music t6
    show yuri zorder 2 at t11
    show yuri 1bg
    "Puse mi sonrisa más acogedora."
    mc "Hola."
    y 1bf "Hola, [player]."
    "Le hago un gesto para que entre."

    scene bg living_room
    with wipeleft_scene

    show yuri zorder 2 at t11
    show yuri 2bb
    y "Gracias por invitarme, [player]."
    "Agito mi mano delante de mi cara."
    mc "No te preocupes por eso."
    mc "Es lo menos que puedo hacer por acompañarte a casa ayer."
    y 2bj "Que caballeroso."
    "Empiezo a sonrojarme mientras mi cara se calienta."
    "Juro que encendí mi aire acondicionado."
    mc "Supongo que la caballerosidad no está muerta después de todo."
    "Le hago un gesto para que se siente en el sofá mientras camino hacia el soporte de la televisión."
    y 1be "[player], no me dijiste lo que íbamos a ver."
    mc "{i}(Y ahí está la pregunta que pone el clavo en el ataúd.){/i}"
    y 3be "Lo siento, ¿qué fue eso?"
    mc "Oh, acabo de decir que será una sorpresa."
    show yuri 3bg
    "Será una sorpresa para los dos, aunque por su mirada siento que sabe que no lo preparé."
    "A Yuri le gusta el terror, tal vez debería poner eso."
    "O tal vez acción. ¿Quién no ama las películas de superhéroes?"
    "O tal vez de romance..."
    "No seas tonto [player], eso solo funciona en películas y juegos."
    "¿Qué tal una comedia?"
    "Podré ver a Yuri reír."
    "O tal vez esa película donde todo fue un sueño:"
    "Titanic."
    y 2bf "¿Está todo bien?"
    mc "Uhhhhh."
    mc "Si."
    y "¿Hay algo mal?"
    "En este punto estoy empezando a sudar."
    "¿Qué debo hacer?"
    "¡Ajá!"
    mc "Idea."
    y "¿Qué fue eso?"
    "Me giro y la miro."
    mc "Ahh, tienes que adivinar qué película veremos."
    y 2bh "Uuuh..."
    y "No soy buena adivinando."
    mc "Haz tu mejor intento."
    y 2bk "..."
    "Yuri piensa por un momento."
    "La tengo justo donde la quiero."
    y 1bj "Bueno, he tenido muchas ganas de ver la película {i}Miseria{/i}."
    y 1bb "Leí la novela y tenía ganas de compararla con la película."
    mc "Oh, Miseria."
    y 2bg "..."
    "Yuri me da una mirada de decepción."
    "¿Por qué soy así?"
    show yuri zorder 1 at thide
    hide yuri
    "Regreso a la base del televisor."
    "Por favor ten Miseria, ten Miseria, ten Miseria."
    "Miro hacia atrás, donde guardo las películas que mis padres solían tener."
    "De repente la veo."
    show yuri zorder 2 at t11
    show yuri 3be
    mc "Eres una buena adivinadora, Yuri."
    y 3bf "¿Eh?"
    #vodfjvbndfnbdfnbdfnb
    "Me doy la vuelta y le presento el estuche."
    "Sus ojos color lavanda se iluminan y reflejan la luz del sol que se filtra desde la ventana."
    y 2bh "Como..."
    "Ella suena desconcertada como si no pudiera creer que acertó."
    "La verdad es, que cualquier película que ella \"adivinará\" iba a ser la que yo escogiera."
    "Y, por supuesto, la suerte estava relacionada con si tenía o no la película a la mano."
    "Es lo que me gusta llamar: el truco de {i}un paso adelante{/i}."
    "Pongo el disco en la bandeja y lo reproduzco, mientras Yuri reúne los aperitivos en la mesa de café."
    "Espera, se supone que debo sentarme en el sofá con Yuri, o sentarme en el otro."
    "Esta es una cita, ¿verdad?"
    "Supongo que no lo dije, pero estaba muy implícito."
    "¿Estoy pensando demasiado en esto?"
    y 2bf "[player]."
    "Salgo de mis pensamientos y me vuelvo hacia Yuri."
    y 2bt "¿Está todo bien?"
    mc "Sí... sí, todo está bien."
    "Camino hacia el sofá en el que Yuri está sentada."
    mc "¿Está ocupado este asiento?"
    show yuri 2bc
    "Yuri sonríe lindamente."
    y 2bd "Adelante [player]."
    "Me dejo caer a su lado."

    scene bg living_room
    with wipeleft_scene

    show yuri zorder 2 at t11
    show yuri 3be
    "A mitad de la película, Yuri y yo ya hemos consumido todos los bocadillos que puse."
    "La película esta muy buena, pero mi visión se desvía hacia Yuri inconscientemente."
    "¿Por qué ver una película sobre un escritor con las piernas rotas, cuando en cambio puedo mirar a Yuri todo el día?"
    "Ella se vuelve hacia mí un poco."
    y 3bf "En el libro ella le cortó el pie."
    mc "¿Eh?"
    y "Oh, solo estaba señalando las diferencias entre la novela y la película."
    mc "Oh..."
    "Eso salió un poco más desentusiasmadamente de lo que deseaba."
    y 3bo "Esto no es aburrido para ti, ¿verdad [player]?"
    mc "¿Qué? No, realmente estoy disfrutando la película hasta ahora."
    show yuri 2bg
    "Yuri toma el control remoto y baja un poco el volumen."
    y 2bh "Entonces, ¿cuál es el nombre del personaje principal?"
    mc "¿Qué?"
    y 2br "El personaje principal, ¿cómo se llama?"
    mc "Uhh..."
    "Muy bien, lo sé."
    "Piensa, [player]."


    menu:
        "Vamos nena, ¿cómo se llama?"
        "Paul":

            "¡Eso es!"
            mc "Paul. Paul Sheldon."
            show yuri 2bf
            "Yuri se ve sorprendida."
            y 3bv "Si-siento haber dudado de ti."
            mc "No hay problema, Yuri."
            "Ambos nos volteamos a la pantalla."
        "Thomas":

            "Aquí no pasa nada."
            mc "¿Thomas?"
            y 2bg "..."
            y 1bh "Se llama Paul, Paul Sheldon."
            mc "Lo-lo sabía."
            mc "Solo estaba probando para ver si lo sabías."
            y 2bj "¿Como no?"
            "Yuri ahoga una risa suave antes de regresar a la película."


    show yuri 2bf
    "..."
    "..."
    "¿Ahora es mi oportunidad?"
    "Esta distraída. Debería hacer mi movimiento."
    "¿Sería raro si lo hiciera?"
    "¿O sería más raro si no lo hiciera?"
    "Quiero decir nos besamos, ¿qué es una envoltura de brazo en comparación con eso?"
    "Maniobro mi brazo muy lentamente como si se moviera a través de la melaza."
    "Pongo suavemente mi mano sobre el hombro de Yuri."
    show yuri 2bv
    pause 0.6
    show yuri 2bq
    "Ella se tensa un poco y me mira."
    "No se oye una sola palabra."
    show yuri zorder 2 at s11
    show yuri 3bu
    "Ella simplemente sonríe y se inclina nerviosamente hacia mí."
    "Su cabeza descansa suavemente sobre mi hombro."
    "No puedo evitar sentir la saliva en mi garganta también."
    "Continuamos terminando la película en un silencio reconfortante."

    scene bg living_room_afternoon
    with wipeleft_scene

    "Los créditos pasan."
    show yuri zorder 2 at t11
    show yuri 1ba
    "Yuri se mueve de mi brazo que ahora se ha quedado dormido."
    y 1bb "¿Qué te pareció?"
    mc "Estuvo bien. Una historia de suspenso y bien pensada."
    mc "Estoy contento de haberlo elegido."
    y 1bd "Igual yo."
    "O no entendió mi truco o no quiere avergonzarme."
    y 2bh "Aunque, no pudé evitar notar todas las diferencias del libro."
    mc "¿Cómo qué?"
    "Después de decir eso, instantáneamente me arrepiento de esas líneas."
    y 2bf "Bien para empezar..."
    "Yuri se va en una tangente incomprensible sobre la película."
    "Intento seguirla, pero no puedo entender lo que está diciendo."
    "Estoy demasiado ocupado mirando la forma en que sus ojos reflejan el sol naranja que se asoma por la ventana."
    y "¿Verdad, [player]?"
    "Uh oh."
    mc "Ummm, uh...si."
    mc "Estoy completamente de acuerdo."
    y 3be "..."
    "Yuri me mira como si fuera uno de sus libros."
    y 3bb "Me alegra que lo veas a mi manera."
    "Yo exhalo silenciosamente."
    "Gracias a Dios, ella no entrometió una pregunta más."
    y 2bh "Supongo que debería irme a casa ahora."
    y 2bv "Si espero más tiempo tendré que caminar en la oscuridad."
    mc "Ese es el momento más seguro, Yuri."
    y 2bt "¿Eh?"
    "Yuri me da una mirada confusa."
    mc "Porque de noche, si te pones en peligro, puedes encender una luz en el cielo y llamar a Batman."
    mc "No puedes hacer eso durante el día."
    show yuri 1bg
    "Yuri intenta contener la risa..."
    show yuri 1bi
    "Pero finalmente cede."
    y 1bd "Ujuju"
    y 2bb "Lo digo en serio, [player]. Me tengo que ir."
    mc "¿No puedes pasar la noche?"
    stop music fadeout 4.0
    y 1bj "Ni siquiera tengo un cambio de ropa."
    mc "Pero..."
    play music t103
    "Me detengo antes de decir: {i}¿Quién dijo que vamos a necesitar ropa?{/i}"
    #viejo pendejo no sabe q la ruta es neutral
    mc "Entiendo."
    show yuri zorder 2 at f11
    show yuri 2ba
    "Yuri se pone de pie."
    y 2bs "Gracias por el día de hoy, [player]."
    y "Esta fue una tarde encantadora."
    
    show yuri zorder 1 at thide
    hide yuri
    "Pasamos un silencio comodo y ella se desvanece en los postes y la oscuridad de la noche."
    "Me quedo sentado en el sofá mirando el techo fijamente."
    "Si me dijera hace un año que tendría una relación con una chica, habría llenado los papeles para ser llevado al manicomio."
    "Pero ahora he cambiado."
    "Me siento seguro, como si pudiera enfrentar cualquier cosa que el mundo me ponga enfrente."
    "Supongo que tendremos que ver a dónde mas caminamos."

    stop music fadeout 3.0
    scene black
    with dissolve_scene_full
    pause 1.0





    jump chapter9