label chapter9:


    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_half
    play music t112

    "Abro los ojos cuando el sol arroja su luz sobre mí cara."
    mc "Ugh..."
    "La luz del sol crea un suave brillo."
    "Por lo general, eso significa que hay nubes pesadas que se ciernen."
    "Probablemente la lluvia me duchará más tarde."
    "Agarro mi telefono y miro la hora."
    mc "¡Mierda, voy a llegar tarde!"
    "Saltando de la cama, comienzo mi rutina diaria."

    scene bg living_room
    with wipeleft_scene

    "Hoy es nuestro segundo encuentro con el Dr. Lankton."
    "El estaba entusiasmado por seguir trabajando con Yuri, y creo que el realmente puede ayudarla."
    "Me pregunto que dirá el cuando ella le diga sobre sus cortes."
    "Yuri me prometió que iba a decirselo al doctor."
    "Asi que, haré lo que pueda para apoyarla."

    scene bg kitchen
    with wipeleft_scene

    "Continuo mi camino hacía la cocina."
    "Saco mi teléfono, y miro la hora."
    mc "Ya no me queda mucho tiempo."
    "Agarro una barra de cereal de la mesa y después abro la puerta."
    "Con suerte, tengo leche que compré recientemente."
    "Echo la leche en un tazón y suelto la barra de cereal adentro."
    "..."
    mc "..."
    "Barra de cereal..."
    mc "¿Por qué no funciona?"
    "Reviso el paquetico de la barra de cereal."
    mc "Oh... ésto demuestra lo retrasado que soy."
    "Me como la barra de cereal mojada de leche."
    "Nota mental: leer los empaques de comida."
    mc "Uno de estos días voy a tener un desayuno apropiado..."
    "Una vez más agarro mi telefono y le envío un mensaje a Yuri."
    mc "{i}Voy caminando{/i}"
    "Casi inmediatamente, Yuri responde."
    y "{i}Okay. Estaré esperando.{/i} "
    "No estoy seguro de si Yuri siente que es nesesario escribir tan formal, pero supongo que es un poco lindo."
    "Termino mi increíblemente perfecto desayuno y salgo de mi casa."

    stop music fadeout 2.0
    scene bg yuri_house
    with wipeleft_scene
    play music t6

    "Me acerco a la puerta y toco el timbre."
    play sound doorbell
    "..."
    "Yuri abre la puerta."
    show yuri 1ca zorder 2 at t11
    play sound closet_open
    y "Hola [player]."
    mc "¿Estás lista?"
    y 3cq "Supongo que sí..."
    mc "Esta bien que te sientas nerviosa. Solo recuerda, estaré todo el tiempo al lado de ti."
    y 3cs "Gracias [player]. Realmente aprecio todo lo que has hecho por mí."
    "Mi cara empieza a ponerse roja."
    mc "Ehh, no lo menciones."
    "Yuri cierra la puerta y empezamos a caminar a la oficina del Dr. Lankton."

    stop music fadeout 2.0
    scene bg waiting_room
    with wipeleft_scene
    play music t108

    "Llegamos al lugar. El Dr. Lankton esta parado en la puerta esperándonos."
    d "Ah, justo a tiempo. Es un placer verlos otra vez."
    "Una vez más aprieto su mano firmemente."
    "El se dirige a Yuri."
    show yuri 4ca zorder 2 at t22
    "Tímidamente, Yuri extiende su mano."
    "El Dr. Lankton la sacude."
    d "Un placer verle otra vez señorita."
    d "¿Deberíamos empezar?"
    ###
    y 4cb "..."
    d "..."
    y "*Suspiro* S-Si..."
    d "Bien entronces acompañame."
    mc "Hey Yuri."
    "Ella se voltea hacia mi con una expresión neutral."
    y 3cf "¿Que pasa [Player]?"
    show yuri 3cs
    mc "Te estaré esperando como la vez pasada."
    show yuri zorder 2 at thide
    hide yuri
    "Asiente y ella entra con el doctor."
    mc "Te estaré esperado..."
    "Vuelvo a la sala de espera y veo los alrededores."
    "Todo parece que nada ha cambiado desde la vez pasada."
    "Tanto el cuarto como Yuri, pero hay una diferencia."
    "Yuri almenos quiere cambiar, como su pareja es mi necesidad cuidarla."
    "Intento distraerme con el celular."
    mc "Que puedo ver..."
    "En los mensajes veo que ese numero extraño me ha seguido mandando mensajes."
    "Podria bloquearla de todos modos."
    "Lo haré un dia de estos."
    mc "Seria bueno saber como ser una buena pareja."
    "Busco algunas recomendaciones viendo videos."
    "Uno diciendo \"¿Cómo dejar de ser migajero?\""
    "En serio, esos videos parecen superación y estima mas que conocer a tu pareja."
    mc "Mejor espero en silencio."
    #######aihhbsihbgibiyhb
    ###esta es perspectiva de Yuri
    scene bg office
    with wipeleft_scene

    "Sigo al doctor a la habitación."
    #show yuri zorder 2 at s11
    "Tomo asiento."
    d "Bueno Yuri, ¿Te gustaría empezar a compartir algo?"
    #show yuri 3cn
    "Bajo la mirada nerviosamente."
    d "No te preocupes, tomate el tiempo que sea necesario."
    "Es por mi bien tengo que hacerlo por mi, por [Player], no quiero decepcionarlo."
    "¿Por qué me siento en deuda con él?"
    "Eso me ha llevado a tomar desiciones sin pensar demasiado."
    "No debo decirle, quedaria destrozado..."
    "El doctor Lankton me sigue viendo."
    ####
    "*Suspiro.*"
    y "Yo... y-yo quiero mostrarle..."
    y "Hay... a-algo que aún no le he d-dicho a usted."
    "Dr. Lankton me mira curiosamente pero frialdad de un profesional."
    "Empiezo a subir la manga de mi brazo."
    #show yuri zorder 1 at thide
    #hide yuri
    "Le explico todo lo que le dije a [Player] hace algunos días."
    "La historia de mis cortes, y el cómo lo desarrollé hasta llegar a ser una adicción."
    "Mis ojos se sienten humedos mientras que él anota de vez en cuando."
    "Eventualmente tuve lo que tenia que sacar."
    #show yuri 3cw zorder 2 at t11
    d "Esto es... es realmente algo serio."
    d "Denme un momento."
    #show yuri 3cv
    "El Dr. Lankton se levanta de su asiento y se dirige a su computadora."
    "El empieza a escribir algo."
    "Una hoja de papel sale de su impresora."
    "Él después se acerca."
    #show yuri 3ct
    d "Esta es una prescripción para algunos antidepresivos."
    d "Son usados para reprimir algunas emociones y para relajar el cuerpo."
    d "Estos te ayudarán a controlar algunos sentimientos que puedas tener."
    "Tomo la receta y me acerco a la puerta."
    y "G-gracias."
    ##grfgfd
    scene bg waiting_room
    with wipeleft_scene
    #perspectiva d mc ahora
    show yuri 3cv zorder 2 at t11
    "Después de un tiempo Yuri sale acompañada del doctor."
    d "Gracias a los dos por haber venido hoy."
    d "Yuri..."
    show yuri 3ct
    "El se inclina para estar a la altura de sus ojos."
    d "Todo estará bien."
    "El le da una gran sonrisa a ella, pero Yuri continúa mirándolo sin comprender."
    "Este día tal vez ha sido mucho para ella."
    "El Dr. Lankton regresa a su oficina."
    play sound closet_close
    "Miro a Yuri y puedo ver que ella esta notablemente temblando."
    "Miro el reloj de la habitación."
    mc "Yuri, por que no vamos a algún lugar a relajarnos?"
    mc "Tuvimos un día bastante tenso, no crees?"
    y 3cv "Ehh...o-okay."
    "Ambos salimos del edificio."
    ########
    stop music fadeout 2.0
    scene bg park
    with wipeleft_scene
    play music t109

    "Caminamos por un parque público."
    "Me dirijo a ella."
    show yuri 3ca zorder 2 at t11
    mc "Esto está muy bien, no Yuri?"
    y 3cb "Podría decir que, está bien tener un poco de aire fresco."
    y "Parece que el peso del mundo finalmente se ha quitado de mis hombros."
    mc "Hey Yuri, creo que ya se que podemos hacer."
    y 3cf "Y que podemos--"
    y 3cp "¡Ahh!"
    show yuri zorder 1 at thide
    hide yuri
    "Tomo la mano de Yuri y corro hacía los arboles."

    scene bg lake_day1
    with dissolve_scene_half
    show bg lake_day1:
        subpixel True
        linear 4.0 xalign 1.0
    pause 5.0

    scene bg lake_day
    with fade

    "Me perdí un poco, pero después de unos minutos llegamos a un claro."
    "Ha pasado tanto tiempo desde la última vez que visite este lugar."
    mc "¡Aquí es!"
    "Agito mis brazos en una exhibición teatral."
    "Este lugar me vuelve a revivir un montón de buenos recuerdos."
    "Sayori y yo nos topamos con este lugar cuando éramos niños."
    "Fue nuestro pequeño lugar secreto en el que podíamos jugar."
    "Una vez ella se cayo al río y tuve que saltar adentro y agarrarla."
    "Sus padres estaban realmente molestos ese día."
    show yuri 3cf zorder 2 at t11
    y "[player]..."
    y "Esto es impresionante."
    show yuri 3ce
    "Yuri se para en el claro con vista al agua."
    "Yo también miro, pero no con las mismas vistas que ella."
    "Para mí ella es aún más bella que esto."
    "Puedo ver como el viento sopla suavemente su cabello morado."
    "Sus ojos brillan como estrellas mientras mira al paisaje aparentemente infinito."
    "Ella se siente calmada, con una expresión en su rostro."
    "No sé si mi mente está jugando trucos conmigo, pero... parecíera que un rayo de sol brilla sobre ella."
    "Y solamente en ella."
    "Un rayo de luz, viajando millones de kilometros solo para reflectar en su rostro."
    "Se hace ver como si ella estuviera brillando."
    "Ambos permanecemos en el claro, perdidos en el tiempo, tomando nuestras respectivas vistas."
    "Solo puedo imaginar lo que ella estará pensando."


    scene bg lake_afternoon
    with wipeleft_scene

    "El sol se baja de las nubes, la luna empieza a aparecer."
    "Eventualmente rompemos el silencio."
    show yuri 3ci zorder 2 at t11
    mc "Deberíamos regresar."
    mc "Se esta haciendo tarde."
    y 3cf "..."
    "Yuri me mira como si acabará de empujarla a un portal."
    y 3ct "¿En serio...?"
    "Ella se ve algo decepcionada."
    "La noto temblando."
    "Con el sol cayendo, la brisa es más y más fría."
    mc "Volveremos alguna vez. Lo prometo."
    y 3cs "Okay."
    "Yuri suavemente sonrie."
    "Ya es hora de volver."

    scene bg park
    with wipeleft_scene

    show yuri 3cv zorder 2 at t11
    "Continuamos nuestro camino en silencio."
    mc "Sabes, podemos tener un picnic aquí algún día."
    show yuri 3cf zorder 2 at h11
    "Yuri se emociona."
    y "¡¿De verdad?!"
    "No puedo evitar reírme de la emoción en la voz de Yuri."
    "Es probablemente la primera vez que la escucho expresarse genuinamente."
    mc "Por supuesto."
    mc "Podemos preparar comida, tal vez algo de té, un libro, y vendriamos cuando este soleado y sin nubes."
    y 3cj "Me..."
    y 3cb "Me gustaría."
    show yuri 3ca
    "Pongo mi brazo alrededor de Yuri."
    "Ella ni siquiera rechaza."
    "Puedo sentir su cuerpo tenso relajarse como si todos los momentos que han llevado a ésto se hayan borrado de la existencia."
    "Si solo un {i}chasquido{/i} pueda borrar la mitad de todo fuera de la existencia..."
    "Me río un poco para mí mismo."
    "Y por un segundo me siento de nuevo como una persona normal."

    stop music fadeout 2.0
    scene bg yuri_house_afternoon
    with wipeleft_scene
    play music t112
    ######uygbvsdhubdfcihdfbcv
    mc "Bueno, ya llegamos."
    show yuri 1cb zorder 2 at t11
    y "Gracias por caminar conmigo a casa [player]."
    mc "No hay problema."
    mc "Yo...me iré entonces."
    y 3cq "¿Estás seguro?"
    mc "Quiero decir..."
    "Nop, no tendré esta conversación incomoda de nuevo."
    mc "¿Sabes qué? Me encantaría pasar la noche contigo."
    show yuri 3cf zorder 2 at t11
    y "¿Enserio?"
    mc "¿Estás sorprendida por qué quiero pasar el rato contigo?"
    y 4ca "No. E-es solo que..."
    y 4cb "A algunas personas no les gustaría pasar el rato conmigo..."
    "Pongo mi brazo alrededor de Yuri y caminamos adentro."
    show yuri zorder 1 at thide
    hide yuri
    mc "Bueno Yuri..."
    mc "No soy de esos {i}algunos{/i}."

    scene bg yuri_house_interior_night
    with wipeleft_scene

    "Caminamos a la sala y aprecio el ambiente tranquilo."
    #
    mc "Tienes un bonito sofa, ¿Te importa si me siento?"
    show yuri 3cg zorder 2 at t11
    y "Erm pues..."
    y 3ch "Estás algo sudoroso."
    "..."
    mc "Está bien..."
    mc "Entonces, ¿Dónde podria relajar las piernas?"
    y 3cf "Podria ser en la cocina."
    mc "Supongo que podemos descansar un rato y no sé..."
    mc "Leer o algo."
    y 3cd "Eso suena increíble."
    show yuri zorder 1 at thide
    hide yuri
    "Me dirijo a la cocina y me siento en una de las sillas que estan en la mesa."
    "Al percatarme veo que hay sillas que sobran."
    mc "¿No te sientes sola?"
    show yuri 3cs zorder 2 at t11
    y "Algunas veces, pero contigo aveces se siente mejor."
    "Siento que la sangre se sube a mi cara."
    mc "En serio me gustaria quedarme más tiempo."
    mc "Pero no traje ropa para ducharme."
    y 3cq "Podrias...yo...quieres..."
    y 3ch "Creo que no seria buena idea."
    "Intento adivinar lo que queria decir."
    mc "¿Algo como prestarme tu ropa?"
    show yuri 3co zorder 2 at t11
    "Se ve que entendi lo que decia y mira hacia otro lado."
    "Mi rostro se pone caliente de nuevo."
    mc "Seee...Creo que tienes razón mejor cambiemos de tema."
    mc "¿Tu no te vas a bañar?"
    y 3cq "Uhh creo que tienes razon, disculpame, mi casa es tu casa."
    "Yuri sube las escaleras sin antes darme una calida sonrisa."
    "Supongo que podria ver su sala por un rato."
    "Paseo cerca de un estante y veo un retrato de sus padres y ella cuando era niña."
    "Incluso que los años pasaron sigue teniendo esa mirada inocente que tenia de pequeña."
    "Si hubiera estado mientras ella estaba teniendo esos problemas problablemente se abriria mejor."
    "Pero tambien tengo que abrirme con ella."
    mc "Tengo que hacerlo por tí."
    "Caliento una tetera para hacer un té para los dos."
    stop music fadeout 2.0
    scene bg yuri_house_interior_night
    with wipeleft_scene
    play music t107

    "Después de un rato yuri vuelve con otro cambio de ropa."
    show yuri 3nc zorder 2 at t11
    y "Ufufu."
    y "Espero que no haya tardado demasiado."
    mc "No es nada, te podria esperar cien años si es necesario."
    show yuri 3nu zorder 2 at t11
    "Hago que Yuri se sonroja un poco."
    "Buena esa [player]"
    "Sostengo una bandeja con la tetera y dos tazas pequeñas."
    mc "Pense que podíamos sentarnos con el té mientras escuchamos la lluvia."
    "Yuri todavia no se había dado cuenta que estaba lloviendo afuera."
    y "Oh, claro. Es una muy buena idea."
    y 1nb "¿Te importaría si subimos? Mi habitación tiene una ventana grande."
    mc "Claro, ¿Por qué no?"

    scene bg yuri_bedroom_night
    with wipeleft_scene

    "Una vez en su habitación, tomo asiento en su cama."
    show yuri 3nu zorder 2 at t11
    "Yuri sirve el té y me alcanza mi taza."
    mc "Gracias."
    "Yuri agarra un libro."
    y 3nb "Te importaría si nosotros lo...terminamos?"
    "Insolación Infinita."
    "El libro con el que Yuri y yo hemos compartido estos ultimos meses."
    "Un libro con una historia retorcida de pérdida que nos ha unido, y ahora estamos en el ultimo capítulo."
    mc "Claro."
    show yuri 3nu
    "Estoy listo."
    show yuri zorder 2 at s11
    "Con las tazas de té en mano, tomamos nuestra posición habitual de lectura."
    "Sin embargo, nuestros cuerpos estan más juntos."
    "Por un rato nos quedamos en silencio bebiendo, leyendo, y escuchando la lluvia."
    "Estamos en las ultimas lineas del libro."

    $ fixedsay = True
    window hide
    with Pause(1)
    window show
    with Pause(1)
    $ nvl_enable = True
    mcnvl "Me siento en la esquina de esta celda."
    mcnvl "No se que es peor si soy honesta."
    mcnvl "Estar rodeada de cuatro paredes de concreto, o el hecho de que estoy sola."
    mcnvl "Sí solo hay una cosa que los humanos comparten; es el miedo a estar solo."
    mcnvl "Algunas personas aceptan la muerte..."
    mcnvl "Algunas personas se asustan por los espacios pequeños, las arañas, o la oscuridad."
    nvl clear
    mcnvl "Pero la soledad..."
    mcnvl "No hay nada más horrible que eso."
    mcnvl "Porque cuando estás solo, no tienes a nadie para ayudarte a calmar ese miedo."
    nvl clear
    mcnvl "Miró a través de la pequeña ventana en lo alto de la celda."
    mcnvl "El sakura..."
    mcnvl "Esta brillando."
    mcnvl "Debe ser primavera entonces."
    mcnvl "Eso significa que estoy aqui desde..."
    mcnvl "..."
    mcnvl "No estoy segura de cuanto."
    mcnvl "¿Cómo puedes medir el tiempo si ni siquiera puedes ver el sol?"
    nvl clear
    mcnvl "Observo mi brazo vendado."
    mcnvl "Me he visto a mi misma entrar en la locura, salir, y después volver a entrar en ella."
    mcnvl "Es como un ciclo."
    mcnvl "He estado tanto tiempo aqui que puedo saber cuando empezaré a perder mi mente."
    mcnvl "Incluso mis alucinaciones no quieren hablarme más."
    nvl clear
    mcnvl "\"¡Boom, boom, boom!\""
    mcnvl "Se escucha un golpe mounstroso al otro lado de mi puerta."
    mcnvl "Gateo al centro de la habitación y lo enfrento."
    mcnvl "¡Los golpes son más altos y profundos!"
    mcnvl "¡Cerca y más cerca!"
    mcnvl "Pero se detienen..."
    nvl clear
    mcnvl "Permanezco en el centro de la habitación, mí corazón late fuertemente."
    mcnvl "El aire es denso."
    mcnvl "No me atrevo a hacer un sonido porque temo romper el frágil silencio."
    mcnvl "Mi visión se centra en la puerta de acero que me ha mantenido encerrada."
    mcnvl "El sonido de un metal raspandose suena y llena la habitación."
    mcnvl "Apago mis oídos instintivamente, pero mis ojos nunca se apartan de la puerta."
    mcnvl "Cierro mí respiración."
    mcnvl "Y la puerta se abre crujiendo."
    nvl clear
    window hide
    $ nvl_enable = False
    with Pause(0.5)
    window auto
    $ fixedsay = False
    ###ahi te dejo algo de chamba con las expresiones y las escenas xdddd
    mc "¿Espera qué?"
    mc "¿Eso es todo?"
    "Miro a Yuri."
    y 3nt "Supongo que tendremos que esperar que la continuación salga."
    "Dejo soltar un suspiro."
    mc "Lo suficientemente justo."
    "Pongo el libro en la mesita de noche."
    mc "Lo he disfrutado."
    y 3ns "¿En serio?"
    mc "Sí."
    mc "Gracias por compartir este libro conmigo."
    show yuri 3nu
    "Yuri se ruboriza mientras intenta esconder su sonrisa."
    "Mientras, continuamos escuchando las gotas de lluvia cayendo."
    show yuri 3nl
    "Una vez que el té se acabo, Yuri suelta un bostezo."
    mc "¿Cansada?"
    y 3nm "Ujumm."
    "Nos deslizamos uno al lado del otro mientras escuchamos el mundo exterior."
    "La melodica sinfonía de las gotas cayendo en el techo son relajantes."
    y "¿[player]?"
    mc "¿Sí?"
    y 3nh "Tal vez esta es una pregunta extraña, pero..."
    y "¿Por qué tus padres nunca están en casa?"
    mc "Ehhhh..."
    y 3nn "Oh, ¡Lo siento! Eso es muy personal yo--"
    mc "No, no, esta bien."
    show yuri 3nt
    mc "Pienso que es importante que lo sepas."
    "Pongo mi brazo alrededor de ella y me acerco más."

    scene black
    with dissolve_scene_full

    show yuri zorder 1 at thide
    hide yuri
    show y_cg8-a at cgfade
    with dissolve_scene_half
    show rain as rain1 at move_diag(0)
    show rain2 as rain2 at move_diag(0.3)
    show rain3 as rain3 at move_diag(0.6)
    show rain4 as rain4 at move_diag(0.9)
    $ persistent.cg_viewed[3] = True


    "El sonido de la lluvia continua haciendo eco en la habitación."
    "Puedo sentir nuestros latidos sincronizados al ritmo de la lluvia cayendo en el techo."
    mc "Cuando era un niño, tal vez diez o once, mis padres fueron golpeados por un problema financiero."
    mc "Fue cuando era realmente joven, asi que no recuerdo lo específico de ello."
    mc "Sin embargo, recuerdo que mis padres me sentaron, y me dijieron que se estaban separando."
    mc "Me hicieron elegir con quien quería vivir de los dos."
    mc "Se qué se ve que es mucho para un niño, pero ellos querían estar seguros de lo que era mejor para mí."
    mc "Al final, decidí quedarme con mi padre y pues mi madre se fue."
    y "Lo siento..."
    mc "Está bien."
    mc "Fue hace mucho tiempo."
    mc "Después de que mi mamá se fue ella consiguió un trabajo en una gran compañía banquera y se mudo."
    mc "Sin embargo, tuve la suerte de que mis padres fueran civilizados, y ambos aún aceptan cuidarme."
    y "Tienes la suerte de tener a dos padres que se preocupan por ti."
    mc "Eso es lo que pienso de ello."
    mc "Eventualmente el negocio de mi padre decayó, y de nuevo fuimos golpeados por un problema financiero."
    mc "Después de eso el se encuentra ahora en servicio militar."

    show y_cg8-b at cgfade
    show rain as rain1 zorder 3 at move_diag(0)
    show rain2 as rain2 zorder 3 at move_diag(0.3)
    show rain3 as rain3 zorder 3 at move_diag(0.6)
    show rain4 as rain4 zorder 3 at move_diag(0.9)
    $ persistent.cg_viewed[4] = True

    y "¿El te dejó?"
    mc "Basicamente."
    mc "Después de la caida del negocio, no podía darse el lujo de criarme, y con mi madre en otra parte del mundo tampoco podía estar allí para mí."
    mc "Así que la unica forma de que mi padre ganase dinero era meterse al servicio militar."
    mc "Le dan cheques, la mayoría de los cuales van a la casa por facturas y cosas."
    mc "Y con el dinero que mi madre me da puedo comprar comida y otros productos de nesesidad."
    mc "No es mucho, pero es suficiente para sobrevivir sin luchar."
    mc "Bueno...fisicamente estoy bien, pero a veces me siento algo solo."
    mc "Estar meses en casa viendo como pasa el tiempo..."
    hide y_cg8-b
    "Yuri me mira profundamente."
    "Sus ojos brillan."
    "Ella mueve su mano y pasa su pulgar por mi mejilla."
    "Solo ahora me doy cuenta que estaba llorando suavemente todo este tiempo."
    "Yuri me abraza y entierra su cabeza en mi pecho."
    y "Gracias."
    mc "¿Por qué?"
    y "Por contarme tu historia."
    "Me relajo un poco."
    "Pongo mi mano arriba de Yuri y empiezo a dar suaves palmaditas en su cabeza."
    "Su suave respiración empieza a calmar mis nervios."
    "La lluvia sigue persistente pero eso ya no me da importancia."

    scene black
    with fade

    "Me levanto y me recuesto en la esquina de la ventana."
    "Eso fue algo duro de decir."
    "Yuri me mira timidamente mientras sigue sentada."
    y "¿[player], puedes prometerme algo?"
    mc "¿Qué es?"
    y "Tan pronto como la secuela del libro salga, {i}La Guía del Sakura{/i}, ¿Podremos leerla juntos?"
    "Permanezco en silencio por un momento."
    mc "Pensé que eso ya estaba bastante implícito."
    y "Bueno...no quería asumir nada."
    mc "Bastante justo."
    "Observo su hermoso cabello largo combinar con sus ojos."
    mc "Okay. Te prometo que en cuanto el libro salga, lo leeremos juntos."
    "Yuri no dice nada en respuesta. En cambio, solo se acerca y me abraza suavemente."
    mc "Yo te amo, Yuri."
    "Allí esta esa palabra de nuevo."
    "Una palabra a la cual no puedo entender su significado."
    "Pero igualmente la digo."
    "Porque realmente es la unica palabra que no puedo sacar de mi mente."
    "Yuri me acompaña hacia la puerta y me presta su paraguas."
    "Su suave voz me despide combinado con el sonido del viento humedo y el chapotear de las gotas."
    "Giro viendo por ultima vez sus ojos violetas."
    "Y lo unico que me acompaña es el perfume impregnado en su paraguas."

    stop music fadeout 3.0
    scene black
    with dissolve_scene_full
    pause 1.0





    jump chapter10