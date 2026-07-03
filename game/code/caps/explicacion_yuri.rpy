## explicacion_yuri.rpy
## Este archivo contiene las declaraciones de las imágenes y el diálogo tutorial explicativo.

# 1. DECLARACIÓN DE IMÁGENES
# En Ren'Py, declaramos las imágenes usando la palabra clave 'image'.
# El formato '.webp' es ideal porque está súper optimizado, pesa poco y soporta transparencias impecables.
# Usamos 'yuri_parraga' como la primera palabra de la etiqueta (el tag), de esta forma
# Ren'Py sabe que pertenecen al mismo personaje y reemplazará la expresión automáticamente al mostrar otra.

image yuri_parraga enojada = "mod_assets/images/yuri/yuri_parraga_caraenojada.webp"
image yuri_parraga llorando = "mod_assets/images/yuri/yuri_parraga_carallorando.webp"
image yuri_parraga llorando_fuerte = "mod_assets/images/yuri/yuri_parraga_carallorandofuerte.webp"
image yuri_parraga pensativa = "mod_assets/images/yuri/yuri_parraga_carapensativa.webp"
image yuri_parraga triste = "mod_assets/images/yuri/yuri_parraga_caratriste.webp"

# 2. GUION DEL TUTORIAL
label explicacion_yuri2:
    
    # Configuramos el fondo del salón de clases e iniciamos con una transición de disolvencia completa
    scene bg class_day
    with dissolve_scene_full
    
    # Reproducimos una música tranquila y melódica de DDLC (t2 es 'Ohayou Sayori!')
    play music audio.t2

    "¡Bienvenido al tutorial interactivo sobre cómo usar imágenes en tu mod de DDLC!"
    
    "Hoy nos acompaña Yuri para mostrarnos cómo declarar y mostrar sprites personalizados paso a paso."

    # Mostramos a Yuri con su expresión de inicio (pensativa) usando una transición de disolverse.
    # El posicionamiento 'at t11' coloca al personaje centrado y con un tamaño estándar en DDLC.
    show yuri_parraga pensativa zorder 2 at t11
    with dissolve

    y "Hola... Es un placer saludarte de nuevo."
    
    y "Hoy te ayudaré a entender cómo funcionan las imágenes dentro del código de nuestro mod..."
    
    y "Como habrás notado, mis expresiones se encuentran en la carpeta {i}mod_assets/images/yuri/{/i} en formato {i}.webp{/i}."
    
    y "Lo primero que debes hacer es declararlas en tu código."

    # Explicación de la sintaxis usando diálogos del narrador para mayor claridad
    "Para declarar cada una de las expresiones de Yuri, usamos la palabra clave {b}image{/b} seguido del nombre del sprite y su ruta de archivo:"
    
    "Por ejemplo:\n{color=#f06}{b}image yuri_parraga enojada = \"mod_assets/images/yuri/yuri_parraga_caraenojada.webp\"{/b}{/color}"
    
    y "Al usar {b}yuri_parraga{/b} como primera palabra (el 'tag'), Ren'Py entenderá que todas son variantes del mismo personaje."
    
    y "Así, si cambias de expresión, la anterior desaparecerá automáticamente sin dejar rastros en pantalla. Permíteme hacerte una demostración..."

    # Demostración interactiva de las expresiones una a una
    
    # 1. Triste
    show yuri_parraga triste
    y "Por ejemplo, ahora he cambiado a mi expresión {b}triste{/b}."
    
    "En tu guión, solo tuviste que escribir:\n{color=#f06}{b}show yuri_parraga triste{/b}{/color}"

    # 2. Llorando
    show yuri_parraga llorando
    y "Oh... e-esta es mi expresión {b}llorando{/b}..."
    
    y "No te preocupes, no es que esté triste de verdad, ¡es solo para que veas lo fácil que es cambiar de sprite!"
    
    "El código para lograr esto es:\n{color=#f06}{b}show yuri_parraga llorando{/b}{/color}"

    # 3. Llorando Fuerte
    show yuri_parraga llorando_fuerte
    y "Y si la situación se vuelve sumamente emotiva o dramática... ¡puedes usar la versión de {b}llanto fuerte{/b}!"
    
    "Exacto. En tu guión de Ren'Py escribirías:\n{color=#f06}{b}show yuri_parraga llorando_fuerte{/b}{/color}"

    # 4. Enojada
    show yuri_parraga enojada
    y "P-pero... ¡por favor úsala solo cuando sea necesario! También tengo esta expresión {b}enojada{/b} si me haces perder la paciencia..."
    
    "Para esta cara de molestia simplemente escribes:\n{color=#f06}{b}show yuri_parraga enojada{/b}{/color}"

    # 5. Pensativa de regreso
    show yuri_parraga pensativa
    y "Uf, qué alivio volver a mi expresión {b}pensativa{/b} original..."
    
    y "Es importante notar que puedes posicionarme en diferentes lugares de la pantalla."

    "En los mods de DDLC, se usan posiciones predefinidas como {b}t11{/b} (un personaje en el centro), {b}t21{/b} y {b}t22{/b} (dos personajes), o {b}t31{/b}, {b}t32{/b}, {b}t33{/b} (tres personajes)."
    
    "También puedes usar las posiciones nativas de Ren'Py como {b}left{/b}, {b}center{/b} o {b}right{/b}:"

    # Mover a la izquierda
    show yuri_parraga pensativa at left with move
    y "Mírame, ahora me he desplazado hacia la izquierda escribiendo:\n{color=#f06}{b}show yuri_parraga pensativa at left with move{/b}{/color}"

    # Mover a la derecha
    show yuri_parraga pensativa at right with move
    y "Y ahora me muevo hacia la derecha escribiendo:\n{color=#f06}{b}show yuri_parraga pensativa at right with move{/b}{/color}"

    # Regresar al centro con efecto de entrada/transición
    show yuri_parraga pensativa at t11 with dissolve
    y "Para volver al centro de forma suave, usamos {b}at t11 with dissolve{/b}."
    
    y "Y finalmente, cuando el diálogo termina y el personaje debe retirarse, se utiliza la instrucción {b}hide{/b}."

    # Ocultar a Yuri
    hide yuri_parraga with dissolve
    "Para hacer desaparecer el personaje con una transición suave escribimos:\n{color=#f06}{b}hide yuri_parraga with dissolve{/b}{/color}"

    "¡Y eso es todo lo básico sobre el uso de imágenes en Ren'Py para DDLC!"
    
    "Ahora que dominas las bases de la declaración de imágenes (`image`), visualización (`show`), posicionamiento (`at`), transiciones (`with`) y desvanecimiento (`hide`), estás listo para crear tu propia historia."

    "Disfruta del juego."

    # Terminamos de limpiar la escena
    scene black
    with dissolve_scene_full
    
    # Detenemos la música de fondo gradualmente
    stop music fadeout 2.0

    # Saltamos al Capítulo 1 de la historia normal para continuar el juego de forma natural
    jump cap1
