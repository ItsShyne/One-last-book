label cap3:
    # Definimos la animación para los párpados.
    # "dissolve_scene_full" tarda 3 segundos completos (fundido a negro +
    # pausa + fundido a la nueva escena) y Ren'Py espera a que termine ese
    # "with" ANTES de ejecutar el siguiente "show" -- por eso se veía el
    # fondo (y el negro de la propia transición) antes de que arrancara el
    # parpadeo. Con un fundido corto, el parpadeo empieza casi en el
    # segundo cero.

    stop music fadeout 2.0
    $ set_lighting(None)
    call time_skip("Unos días después") from _call_time_skip_2
    play music t112 fadein 1.5
    scene bg yuri_bedroom at enfoque_despertar
    show expression Solid("#000000") as parpados at despertar_ojos
    with Dissolve(0.3)
    $ renpy.pause(4.4, hard=True)
    "Lentamente abro mis ojos"
    "La cálida luz del sol se asoma a través de las cortinas"
    "Al principio me sorprendió cuando Yuri ofreció compartir una cama, pero pronto descubrí por qué ella no estaba nerviosa"
    "Ella no estaba mintiendo cuando dijo que tenía una cama grande"
    "Esta cosa tiene casi dos metros de ancho"
    show yuri turned casual rup lup cm ce zorder 2 at t11
    "Echo un vistazo para ver a Yuri dormir tranquilamente"
    "Durante las últimas dos semanas hemos estado tomando turnos en la casa del otro para
    leer, tomar té y demás cosas"
    "Hemos avanzado mucho el libro que leíamos juntos, estamos cerca de los últimos capítulos del libro"
    show yuri turned casual rup lup cm ce zorder 2 at thide
    hide yuri 
    "No hemos ido al Club de literatura en absoluto; de hecho estoy muy seguro de que el Club ha sido
    clausurado desde que solo están Sayori y Monika"
    "Incluso envuelto en gruesas cobijas, tengo frío"
    "Sayori amaba el Club de literatura, y probablemente ya esté clausurado"
    "Sayori"
    "¿Cómo estará Sayori?"
    show yuri turned casual me e1e b3c zorder 2 at t11
    y "[player]..."
    mc "Buenos días, ¿dormiste bien?"
    y turned casual lup rup lsur cm ce "Sí… siento que necesitaba algo así"
    "A pesar de acabar de despertar, Yuri todavía parece agotada por todo lo ocurrido."
    "Supongo que técnicamente, con la excepción de compartir una cama, nuestra relación no ha progresado más allá de ser solo amigos"
    "Aun así me alegra mucho que esté en paz… o al menos por ahora"
    y turned lsur om oe "¿Qué estás pensando?"
    mc "¿Eh?"
    y turned rdown ldown "Estabas distraído. ¿Tienes algo en mente?"
    mc "Estoy bien, solo necesito refrescarme"
    
    "Me levanto de la cama y me dirijo al baño para hacer mi rutina normal"
    show yuri zorder 2 at thide
    hide yuri  
    "Veo como Yuri sale de la habitación antes de entrar al baño"
    #escena en el baño
    scene bg yuri_bathroom
    with wipeleft_scene
    "Han sido unos días increíbles, no entiendo la imagen que veo en el espejo"
    "Unas enormes y profundas ojeras se apoderan de mi rostro."
    "Sin darle mayor importancia, me arrojé un poco de agua fría en la cara y cepillé mis dientes."
    "Estoy un poco intranquilo, el club no volvió a ser lo mismo desde el día que Monika y Yuri discutieron"
    "Me preocupa principalmente Sayori, sé que era un lugar importante para ella"
    play sound ducha fadein 0.5
    "Abro la llave para llenar la tina y tomar un baño"
    "Un baño caliente me tranquilizará un poco, seguro todo está bien"

    window hide
    #Toma el baño escena por 4 o 5 segundos mientras se baña
    $ renpy.pause(6, hard=True)
    window show
    # Si el jugador está saltando texto, para cuando llega aquí ya "escuchó"
    # de sobra el sonido de la ducha (o directamente se saltó la pausa de
    # arriba) -- se corta de inmediato en vez de seguir sonando sobre la
    # siguiente escena.
    stop sound
    "Enciendo el lavarropas y me coloco ropa cómoda que traje conmigo"
    scene bg kitchen
    with wipeleft_scene
    show yuri turned casual happ zorder 2 at t11
    "Una vez abajo, veo que Yuri ha comenzado a preparar el desayuno"
    mc "¿Qué estás haciendo?"
    show yuri turned casual rup happ om oe zorder 2 at t11
    y "Solo unos panqueques"
    mc "Huelen delicioso"
    "Le lanzo una leve sonrisa a Yuri."
    show yuri turned happ cm ce

    "Ella me envía una de vuelta y continúa cocinando."
    show yuri zorder 2 at thide
    hide yuri 
    "Tomo asiento, y me sumerjo en mis pensamientos"
    "Mi cabeza sigue sin creer lo que ha pasado en las últimas dos semanas."
    "Pasar tanto tiempo junto a Yuri, dormir en su cama, cocinar juntos"
    "Parecemos una auténtica pareja"
    "No todo ha sido perfecto, pero no puedo quejarme"
    "He tratado de hablar con Yuri sobre el elefante en la habitación"
    "Evitó el tema cada vez que intenté mencionarlo"
    "Tenemos que hablar sobre sus lesiones."
    "Yuri es muy reservada y planeé esperar a que ella se abriera a mí, pero no ha sido el caso."
    "Me he estado preparando para cuando ella lo haga, y proponer algunas ideas pero nunca pasó."
    "Contacté a un psicólogo que pueda ayudarla, y tal vez incluso prescribirle con
    medicamentos."
    show yuri turned casual rup happ zorder 2 at t11
    "Yuri llega a la mesa con dos platos de panqueques"
    "Deja un plato frente a mí, y luego toma asiento."
    y turned casual rdown happ cm ce "¿Tenías algún plan hoy, [player]?"
    "Es ahora o nunca."
    y "¿Involucraban la lectura o el té?"
    "Yuri sonríe enigmáticamente pero no comparto su momento de felicidad."
    stop music fadeout 1.5
    mc "Yuri tenemos que hablar de las heridas en tu brazo"
    show yuri turned casual lsur om oe 
    play music t200 fadein 1.5
    mc "Me preocupa que te estés haciendo daño a ti misma para lidiar con lo que sientes"
    mc "Hay maneras mucho mas sanas de lidiar con tus emociones"
    mc "Estuve investigando alternativas y técnicas para controlar el deseo de hacerlo"
    mc "Yuri, puedes salir de esto"
    show yuri turned casual n2 pani om oe zorder 2 at h11
    play sound fall
    "Yuri salta, tirando su silla al suelo."
    y turned casual n1 sad om oe "¿Por qué… por qué me harías esto?"
    "Puedo ver el miedo en sus ojos."
    show yuri turned casual sad zorder 2 at s11
    "Ella empieza a retroceder "
    "Instintivamente quiero acercarme… pero me detengo..."
    mc "oye..."
    show yuri shy casual sad om ce zorder 2 at t11
    "Ella se para frente a mí con una mirada de inmenso dolor en su rostro"
    mc "Yuri, por favor mírame."
    show yuri shy casual cm oe 
    mc "Te prometí que te ayudaría."
    mc "Y no planeo romper esa promesa."
    y shy casual om oe "[player], no creo que pueda."
    mc "No digas eso, Yuri."
    mc "Este hombre puede ser la respuesta que hemos estado buscando."
    mc "Él puede ayudarte a comprenderte a ti misma y tal vez incluso a ayudarte con tus… ya sabes."
    show yuri shy neut cm oe
    "Ella mira al suelo por lo que parece una eternidad"
    mc "Estuve investigando sobre terapia y también es una buena opción"
    mc "Encontré un consultorio cerca del centro a donde podríamos ir"
    show yuri turned casual rup lup sad cm ce zorder 2 at s11
    pause 0.5
    y "(inhalación)"
    y turned casual sad om oe "Okay"
    mc "¿Okay?"
    y "Okey, iré a ver al psicólogo"
    "Mi corazón da un salto de emoción"
    show yuri casual sad cm oe
    mc "¡Eso es genial!"
    "La abrazo con emoción, pero ella no puede hacer lo mismo"
    "La suelto"
    mc "Lo llamaré y veré cuando podemos programar una cita"
    y "..."
    "Es obvio que ella no está particularmente entusiasmada por esto."
    "He estado cerca de ella todo este tiempo y aun así me ha mantenido al margen de la mayoría de sus sentimientos."
    "No puedo imaginar cómo reaccionará teniendo que abrirse con un completo desconocido."
    "Una pequeña duda atraviesa mi mente..."
    "(¿De verdad quiere hacer esto o solo intenta tranquilizarme?)"
    y turned flus om oe "Deberíamos seguir comiendo antes de que se enfríe."
    mc "Oh... sí, claro."
    show yuri turned casual flus cm oe
    "Nos sentamos nuevamente y cada uno vuelve a su plato."
    "Levanto la vista hacia Yuri y noto un leve temblor en sus manos."
    "Las mangas de su suéter cuelgan flojamente, dejando entrever parte de sus brazos."
    "Por un instante, alcanzo a distinguir finas cicatrices alineadas sobre su piel."
    "No sé si estoy haciéndolo bien… pero no voy a dejarte sola con todo esto, Yuri."
    scene bg kitchen
    with wipeleft_scene
    show yuri turned casual n2 mj e1c b1b zorder 2 at t11
    "Yuri parece haber perdido el apetito; puedo verla simplemente jugando con sus panqueques."
    mc "Yuri, ¿estás bien? ¿No tienes hambre?"
    y turned casual sad cm oe "N-No es nada, solo me distraje..."
    "Yuri empieza a comer sus panqueques."
    "Con cada bocado parece estar forzándose a tragar; será mejor que no diga nada al respecto."
    show yuri turned casual n1 mg e1d b1c zorder 2 at t11
    stop music fadeout 2
    mc "Yuri, respecto a los planes de hoy..."
    y "¿Sí...?"
    mc "¿Qué te parece si tomamos un poco de aire después de que terminemos de desayunar?"
    y turned lsur om oe "Está bien, pero... ¿a dónde iremos?"
    mc "Podríamos ir a caminar por la plaza y visitar algunas tiendas."
    y turned happ om oe "Suena como una excelente idea."
    mc "También podríamos aprovechar para comprar comida y demás cosas para la casa."
    y turned happ om ce "Por supuesto, la despensa está un poco vacía."
    "Yuri y yo comemos tranquilamente en silencio hasta terminar nuestros platos."
    "Me levanto de la mesa"
    show yuri turned casual mg e1d b1c zorder 2 at t11
    mc "Yuri, dame tu plato."
    mc "Si necesitas prepararte para ir a la plaza, ve tranquila."
    mc "Yo lavaré los platos mientras tanto."
    y turned mla e4b b1c "Muchas gracias, [player]. No me tardo."
    "Mientras lavo los platos, escucho cómo Yuri sube las escaleras."
    scene bg living_room
    with wiperight_scene
    play music street_stroll fadein 0.5
    "Han pasado un par de minutos desde que terminé de lavar los platos."
    "Decidí no apresurar a Yuri"
    "Las chicas suelen tardar un poco en prepararse para salir, ¿no?"
    "Escucho sus pasos y veo a Yuri bajar las escaleras."
    show yuri turned casual rup lup ma e2e b1c zorder 2 at t11 
    "Mis ojos se quedan completamente hipnotizados."
    mc "Yuri, te ves... {w=1}preciosa."
    y turned n3 mk e2b b1a "[player]... n-no es para tanto."
    y turned mg e1a b1a "Creo que ya estamos listos para salir."
    y turned ldown rdown n1 mg e1a b1f "¿[player]?"
    mc "Oh, lo siento, aún sigo un poco boquiabierto al verte."
    show yuri turned casual happ om ce zorder 2 at t11 
    mc "Por supuesto, vámonos."
    #La escena cambia hasta el centro de la ciudad.
    scene bg city_street
    with wipeleft_scene
    show yuri turned casual happ om oe zorder 2 at t11
    y "[player]... ¿te molestaría entrar aquí?"
    "Miro el cartel sobre el local."
    "Es una tienda de ropa."
    mc "Sí, claro."
    "Abro la puerta y dejo pasar a Yuri primero."
    scene bg clothing_store
    with wipeleft_scene
    "Una vez dentro, busco un banco donde sentarme."
    "Nunca me gustaron demasiado las compras."
    "A menos que sea para comprar videojuegos."
    show yuri turned casual happ om oe zorder 2 at t11
    mc "¿Sabes qué estás buscando?"
    y "Oh... pensaba que podríamos simplemente mirar un poco."
    mc "¿Mirar?"
    "¿Qué tienen las mujeres con eso?"
    "¿Por qué entrarías a una tienda de ropa solo para mirar?"
    mc "Bueno... está bien."
    show yuri turned casual happ om oe zorder 2 at thide 
    hide yuri
    "Yuri comienza a revisar los estantes mientras yo permanezco sentado sin nada que hacer."
    "Miro los pósters pegados en las paredes."
    "Todos muestran modelos atractivos posando dramáticamente con ropa elegante."
    y "[player], ¿viste algo que te guste?"
    "La voz de Yuri llega desde el otro lado del estante."
    mc "Ummm…"
    "Examino rápidamente algunas prendas."
    "Mis ojos se detienen en un vestido de verano."
    "Me acerco y lo saco del perchero."
    "Es un vestido largo color magenta, de tela ligera y tirantes finos."
    "Mientras lo observo, un chico aparece detrás de mí."
    "Chico sonso" "Oye, ese es morado."
    "Chico sonso" "Es su color favorito."
    "El chico toma el vestido directamente de mis manos y se dirige a la caja para comprarlo."
    mc "Bueno... supongo que eso pasó."
    show yuri casual turned rup ma e1d b1a zorder 2 at t11
    "Camino hacia el mostrador donde Yuri recibe una bolsa del cajero."
    mc "¿Qué compraste?"
    y casual turned mb e1d b1a "Solo... algo para mí."
    "El rugido de mi estómago rompe el silencio."
    "Yuri me mira."
    mc "¿Quieres ir a comer a algún lugar?"
    y casual turned happ om ce "Por supuesto."
    "Yuri termina de pagar y sonríe suavemente mientras salimos de la tienda."
    show bg city_street
    with wipeleft_scene
    show yuri casual turned happ cm oe zorder 2 at t11
    mc "Muy bien, Yuri. ¿Dónde quieres ir a comer?"
    y casual turned happ om ce "[player], no es muy caballeroso hacer que una dama elija."
    mc "Ahhh..."
    y casual turned rup lup "Jujuju."
    y casual turned rdown ldown "Lo siento... pensé que sería divertido molestarte."
    "Yuri continúa riéndose de mí."
    "Es increíble lo cercana que se ha vuelto a mí."
    "Según todos los demás, ella suele mantenerse alejada de la gente."
    "Aunque, claro..."
    "Probablemente la mayoría no irrumpe en su casa."
    "De cualquier forma, verla reír hace que todo esto valga la pena."
    mc "Sí, sí."
    mc "Ya te divertiste suficiente."
    mc "¿No tienes un lugar o algo en específico que quieras comer?"
    y casual turned mb e1d b2a "¿Qué tal si vamos a un restaurante de ramen?"
    "La miro con curiosidad."
    mc "¿No puedes comprar ramen por menos de un euro en el supermercado?"
    y casual turned mg e1a b1c "Eso es el ramen instantáneo que compras tú..."
    y casual turned b1f "¿No me digas que nunca has probado un buen ramen auténtico?"
    mc "No puedo decir que lo haya hecho."
    y casual turned lup mh e1d b1c "¿Crees que haya algún restaurante cerca?"
    mc "Seguro encontramos uno."
    "Saco mi teléfono y comienzo a buscar restaurantes cercanos."
    "Después de unos segundos encuentro uno a pocas cuadras."
    mc "Hay uno muy cerca de aquí con muy buenas calificaciones."
    mc "Mi teléfono está por quedarse sin batería. ¿Puedes buscar la dirección en el tuyo?"
    y casual turned mg e1b b1a "Claro. ¿Cuál es?"
    mc "1273 Calle Tomorrow."
    y casual turned mla e1d b1c "Ya lo encontré."
    mc "Entonces guía el camino."
    show yuri casual turned mla e1d b1c zorder 2 at thide 
    hide yuri 
    "Caminamos juntos por las calles del centro."
    "El clima es agradable."
    "El bullicio habitual de la ciudad llena el ambiente."
    "La gente pasea de un lado a otro, probablemente disfrutando del fin de semana igual que nosotros."
    "Un hombre de mediana edad parece estar haciendo un escándalo parado en medio de la acera."
    "Lleva una camisa rosa claro con pantalones cortos a juego, cinturón negro y zapatos marrones."
    "Tiene las manos apoyadas sobre el abdomen y una sonrisa inquietante."
    "Yuri y yo pasamos rápidamente junto a él esperando que no diga nada."
    "Unos minutos después llegamos al restaurante."
    "Miro el letrero."
    "Spaghetto's Bowl."
    mc "Aquí es."
    "Mantengo la puerta abierta para Yuri y entramos."
    play music Noodle fadein 1.0
    show bg noodle_shop
    with wipeleft_scene
    mc "Hace frío aquí."
    "Tan pronto como entramos, una ráfaga de viento sopla contra mi cuerpo."
    "Este lugar definitivamente mantiene su aire acondicionado encendido."
    "Estiro mi cuello hacia adelante, más allá de la barra donde está la cocina."
    "Todos los cocineros se ciernen sobre ollas grandes que supongo que están llenas de fideos."
    "La anfitriona se acerca a nosotros."
    "Anfitriona" "Hola, ¿cuántos hoy?"
    mc "Dos por favor."
    "Anfitriona" "Justo por aquí."
    show bg noodle_shop:
        subpixel True
        linear 2.0 xalign 1.0
    "Seguimos a la anfitriona hasta una mesa y nos sentamos."
    "Anfitriona" "Su camarero estará con usted en breve."
    "Ella nos entrega los menús y se retira para sentar a los próximos clientes."
    mc "Esto es realmente agradable, Yuri."
    y "Supongo que nunca has estado en un restaurante de fideos antes, [player]."
    mc "Bueno... sí."
    "Está bastante bien por aquí."
    "Miro alrededor del lugar."
    "La iluminación tenue y la música crean el ambiente ideal para comer fideos."
    "Miro el menú."
    "Hay mucha variedad teniendo en cuenta mis puntos de vista anteriores sobre el ramen."
    mc "¿Qué vas a pedir?"
    y "Lo más probable es el Tonkatsu."
    mc "¿Te gusta la carne de cerdo?"
    y "¿Qué quieres decir?"
    mc "Uhh... solo asumí."
    "Uh oh."
    y "¿Qué, una mujer no comería carne de cerdo?"
    "No estoy seguro de si es la cocina, pero mi cara está cada vez más caliente."
    mc "No-no quise decir ninguna ofensa, yo-."
    y "Ujujuju."
    y "Eres fácil de burlar, [player]."
    "Pongo los ojos en ella."
    mc "Ok, me engañaste, muy graciosa."
    "Fue bastante divertido para ser honesto."
    "Vuelvo a leer el menú."
    mc "Creo que pediré lo mismo."
    y "Una buena elección, [player]."
    "La camarera llega a nuestra mesa"
    "Ella coloca dos vasos de agua delante de nosotros."
    "Camarera" "¿Qué les puedo ofrecer a ustedes dos?"
    mc "Una orden de Tonkatsu."
    "Ella garabatea en su libreta de notas."
    "Camarera" "¿Y para usted, señorita?"
    y "Uhhh..."
    "Yuri comienza a ponerse nerviosa."
    "Ella tiene el mismo aspecto que tenía en la cafetería."
    y "Quiero lo mismo."
    "Mis ojos se abren un poco mientras observo a Yuri."
    "La camarera, ajena a la situación, escribe las ordenes."
    y "Fiu..."
    "Camarera" "Eso será todo."
    mc "Sí."
    "Ella toma los menús y luego deja nuestra mesa."
    y "¿Está todo bien?"
    "Siento la saliva en mi garganta."
    mc "Simplemente no esperaba que ordenaras."
    "Yuri sonríe tímidamente."
    y "Bien..."
    "Supongo que cuando estoy cerca de ti me siento un poco más cómoda siendo yo misma."
    "Le doy otra sonrisa y ella me devuelve una."
    "Eso en sí mismo es una pequeña victoria."
    "La camarera regresa, tazones en mano."
    "Camarera" "Disfruten su comida."
    "Con una rápida reverencia, ella se aleja."
    mc "¿Qué de esto?"
    "Con mis palillos, señalo un tazón pequeño de mezcla roja."
    y "Es una especia que puedes poner en tu ramen."
    mc "Oh, bien."
    "Agarro el tazón pequeño y empiezo a meterlo en mi comida."
    y "¡[player], espera!"
    mc "¿Qué?"
    y "Está muy picante. Se supone que solo debes poner una pequeña cantidad."
    "Por eso viene una porción tan pequeña."
    mc "Estoy seguro de que estaré bien."
    "Después de sacar la mitad del tazón, lo puse de nuevo y revolví los fideos con mis palillos."
    "Agarro un palillo lleno de fideos y lo meto en mi boca."
    "Yuri se estremece tan pronto como los fideos entran en la boca."
    mc "No es tan mal-"
    mc "¡Oh, por Dios!"
    mc "¡Oh, mierda!"
    mc "¡Oh Dios, oh Dios!"
    "Empiezo a respirar pesadamente."
    "El humo empieza a salir de mi boca como una chimenea."
    "Me siento tan acalorado"
    "Estoy sudando a lo largo de mi frente."
    "El caldo se siente como lava fundida que se vierte por mi esófago."
    mc "¿Quién hizo esto, Satanás?"
    "Gotas de sudor caen por mi cara."
    "¿O son esas lágrimas?"
    "De cualquier manera me arde la boca."
    "Agarro el vaso de agua y lo bebo."
    "El ardor se desvanece."
    mc "¡Rayos!"
    y "¿Estás bien?"
    mc "Ve el lado positivo, mi nariz nunca ha estado tan descongestionada en años."
    y "Ujuju."
    "Compartimos unas risas y continuamos nuestras comidas."
    "Más tarde, el escenario se transporta a la entrada de la casa de Yuri"
    y "¿[player]?"
    mc "¿Sí?"
    y "Muchas gracias por la comida."
    y "Por todo, de verdad muchas gracias."
    mc "Solo era el almuerzo."
    y "No."
    "No me refiero al restaurante de fideos."
    "Me refiero a... Todo."
    "Todo lo que has hecho."
    "Realmente no he sentido que he hecho mucho"
    "Pero cuando pienso en ellos, Yuri probablemente nunca ha tenido un día en el que salga como un"
    "amigo."
    "Solo una persona que esté con ella probablemente significa todo para ella."
    mc "Está bien Yuri."
    "Como dije, los amigos se mantienen juntos."
    "Ella toma su mano y la entrelaza con la mía."
    "Es suave, pero apretada."
    y "¿Crees que todavía puedo mejorar, [player]?"
    "Simplemente le sonrío."
    "La miro fijamente a sus ojos color lavanda."
    mc "No creo que seas alguien rota."
    mc "Creo que eres alguien cansada de sentirse así."
    mc "Y quiero ayudarte mientras intentas salir de eso." 
    "Veo una lágrima deslizarse por su rostro."
    "Ella toma un momento para absorber mi declaración."
    y "Nos vemos luego, [player]."
    mc "Que tengas buena noche, Yuri."
    "Yuri se separa y entra a su casa."
    "Por un momento me quedo allí solo mientras la fresca brisa del invierno me encapsula."
    "Mis propias palabras corren repetidamente por mi mente."
    mc  "No sé cómo, pero lo superaremos."
    "Susurro para mis adentros"
    jump chequeo_ruta_semana2
