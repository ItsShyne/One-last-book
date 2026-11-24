# Autumn Whispers Yuri -- conjunto nuevo para Yuri (MPT)
#
# Uso:
#     show yuri autumn happ cm oe zorder 2 at t11
#
# Poses de cuerpo (las mismas que usa el resto de MPT):
#     ldown / lup     brazo izquierdo abajo / arriba   (1l.png / 2l.png)
#     rdown / rup     brazo derecho abajo / arriba     (1r.png / 2r.png)
#     hold_hair       torso completo, juega con un mechón de pelo (3.png)
#                     -> reemplaza los dos brazos, igual que "cross_arms" / "stab".
#
# Por defecto (sin poner nada) se muestra ldown + rdown.
# Las caras (mood, ojos, cejas, bocas, rubor, etc.) son las mismas de
# "yuri turned", así que todos los atributos que ya conoces funcionan igual.
#
# Este conjunto solo usa la vista de frente/girada ("turned"). No hay versión "shy".

init -5 python:

    # Carpeta con los cuerpos nuevos.
    autumn_path = "mod_assets/MPT/Autumn Whispers Yuri/"

    # Carpetas de las caras de Yuri (las mismas de yuri_layeredimage.rpy).
    # Se definen aquí con otro nombre para no depender del orden en que Ren'Py
    # lee los archivos.
    autumn_face_path = "mod_assets/MPT/yuri/"
    autumn_extra_path = autumn_face_path + "Extra_Assets/"


layeredimage yuri autumn:

    # Una sola textura en vez de varias capas (evita problemas de alpha en fades).
    at renpy.partial(Flatten, drawable_resolution=False)

    always autumn_face_path + "yuri_turned_facebase.png"

    # Atributos para la lógica de autofocus.
    group af_logic multiple:
        attribute afm null
        attribute afz null


    group mood:
        attribute neut default null # neutral
        attribute angr null # angry
        attribute anno null # annoyed
        attribute cry null  # crying
        attribute curi null # curious
        attribute dist null # distant
        attribute doub null # doubtful
        attribute flus null # flustered
        attribute happ null # happy
        attribute laug null # laughing
        attribute lsur null # surprised (lightly)
        attribute nerv null # nervous
        attribute pani null # panicked
        attribute pout null # pouting
        attribute sad null  # sad
        attribute sedu null # seductive
        attribute shoc null # shocked
        attribute vang null # VERY angry
        attribute vsur null # surprised (very)
        attribute worr null # worried
        attribute yand null # yandere


    group blush:
        attribute nobl default null # Normal Blush.
        attribute awkw null # Awkward.
        attribute blus null # Blushing.
        attribute blaw null # Blushing AND Awkward.
        attribute empty null # No blush at all, just Empty.


    ### Cuerpo -- brazo izquierdo (se dibuja debajo del derecho)
    #--------------------------------------------------------------------------------------
    group left:
        attribute ldown default:
            autumn_path + "1l.png"
        attribute lup if_any(["rup"]):
            autumn_path + "2l.png"

        # "hold_hair" ya trae el torso completo (definido en el grupo "right"),
        # así que aquí se anula el brazo izquierdo por defecto.
        attribute hold_hair:
            null


    ### Cuerpo -- brazo derecho
    #--------------------------------------------------------------------------------------
    group right:
        attribute rdown default:
            autumn_path + "1r.png"
        attribute rup:
            autumn_path + "2r.png"

        attribute hold_hair:
            autumn_path + "3.png"


    # Segundo grupo "left": si el brazo derecho está abajo, el izquierdo en alto
    # tiene que dibujarse por encima del derecho.
    group left:
        attribute lup if_not(["rup", "hold_hair"]):
            autumn_path + "2l.png"


    group nose:

        attribute nose default if_any(["nobl"]):
            autumn_face_path + "yuri_turned_nose_n1.png"
        attribute nose default if_any(["awkw"]):
            autumn_face_path + "yuri_turned_nose_n2.png"
        attribute nose default if_any(["blus"]):
            autumn_face_path + "yuri_turned_nose_n3.png"
        attribute nose default if_any(["blaw"]):
            autumn_face_path + "yuri_turned_nose_n4.png"
        attribute nose default if_any(["empty"]):
            null

        attribute n1:
            autumn_face_path + "yuri_turned_nose_n1.png"
        attribute n2:
            autumn_face_path + "yuri_turned_nose_n2.png"
        attribute n3:
            autumn_face_path + "yuri_turned_nose_n3.png"
        attribute n4:
            autumn_face_path + "yuri_turned_nose_n4.png"


    group mouth:

        # Bocas cerradas por defecto
        attribute cm default if_any(["happ","laug"]):
            autumn_face_path + "yuri_turned_mouth_ma.png"
        attribute cm default if_any(["neut","lsur","worr"]):
            autumn_face_path + "yuri_turned_mouth_md.png"
        attribute cm default if_any(["sedu"]):
            autumn_face_path + "yuri_turned_mouth_me.png"
        attribute cm default if_any(["dist","pout","curi"]):
            autumn_face_path + "yuri_turned_mouth_mf.png"
        attribute cm default if_any(["shoc"]):
            autumn_face_path + "yuri_turned_mouth_mg.png"
        attribute cm default if_any(["anno","vsur","sad","angr","cry","doub"]):
            autumn_face_path + "yuri_turned_mouth_mj.png"
        attribute cm default if_any(["nerv","flus"]):
            autumn_face_path + "yuri_turned_mouth_mk.png"
        attribute cm default if_any(["vang","pani"]):
            autumn_face_path + "yuri_turned_mouth_mm.png"
        attribute cm default if_any(["yand"]):
            autumn_face_path + "yuri_turned_mouth_mo.png"

        # Bocas abiertas
        attribute om if_any(["happ", "laug"]):
            autumn_face_path + "yuri_turned_mouth_mb.png"
        attribute om if_any(["nerv","yand"]):
            autumn_face_path + "yuri_turned_mouth_mc.png"
        attribute om if_any(["worr","pout"]):
            autumn_face_path + "yuri_turned_mouth_me.png"
        attribute om if_any(["sedu"]):
            autumn_face_path + "yuri_turned_mouth_mf.png"
        attribute om if_any(["dist","lsur","angr","cry"]):
            autumn_face_path + "yuri_turned_mouth_mg.png"
        attribute om if_any(["neut","anno","vsur","curi"]):
            autumn_face_path + "yuri_turned_mouth_mh.png"
        attribute om if_any(["flus","doub"]):
            autumn_face_path + "yuri_turned_mouth_mi.png"
        attribute om if_any(["sad"]):
            autumn_face_path + "yuri_turned_mouth_mk.png"
        attribute om if_any(["vang","shoc","pani"]):
            autumn_face_path + "yuri_turned_mouth_ml.png"

        ### Todas las bocas - etiquetas cortas
        attribute ma:
            autumn_face_path + "yuri_turned_mouth_ma.png"
        attribute mb:
            autumn_face_path + "yuri_turned_mouth_mb.png"
        attribute mc:
            autumn_face_path + "yuri_turned_mouth_mc.png"
        attribute md:
            autumn_face_path + "yuri_turned_mouth_md.png"
        attribute me:
            autumn_face_path + "yuri_turned_mouth_me.png"
        attribute mf:
            autumn_face_path + "yuri_turned_mouth_mf.png"
        attribute mg:
            autumn_face_path + "yuri_turned_mouth_mg.png"
        attribute mh:
            autumn_face_path + "yuri_turned_mouth_mh.png"
        attribute mi:
            autumn_face_path + "yuri_turned_mouth_mi.png"
        attribute mj:
            autumn_face_path + "yuri_turned_mouth_mj.png"
        attribute mk:
            autumn_face_path + "yuri_turned_mouth_mk.png"
        attribute ml:
            autumn_face_path + "yuri_turned_mouth_ml.png"
        attribute mm:
            autumn_face_path + "yuri_turned_mouth_mm.png"
        attribute mn:
            autumn_face_path + "yuri_turned_mouth_mn.png"
        attribute mo:
            autumn_face_path + "yuri_turned_mouth_mo.png"
        attribute mp:
            autumn_face_path + "yuri_turned_mouth_mp.png"
        attribute mq:
            autumn_face_path + "yuri_turned_mouth_mq.png"
        attribute mr:
            autumn_face_path + "yuri_turned_mouth_mr.png"

        # Bocas "legacy" y extras de LayeredRedux
        attribute mla:
            autumn_extra_path + "yuri_turned_mouth_mla.png"
        attribute mlb:
            autumn_extra_path + "yuri_turned_mouth_mlb.png"
        attribute mlc:
            autumn_extra_path + "yuri_turned_mouth_mlc.png"
        attribute ms:
            autumn_extra_path + "yuri_turned_mouth_ms.png"
        attribute mt:
            autumn_extra_path + "yuri_turned_mouth_mt.png"
        attribute mu:
            autumn_extra_path + "yuri_turned_mouth_mu.png"
        attribute mv:
            autumn_extra_path + "yuri_turned_mouth_mv.png"
        attribute mw:
            autumn_extra_path + "yuri_turned_mouth_mw.png"


    group eyes if_not(["s_scream", "s_dark", "s_yandere"]):

        # Ojos abiertos por defecto
        attribute oe default if_any(["neut","sedu"]):
            autumn_face_path + "yuri_turned_eyes_e1a.png"
        attribute oe default if_any(["dist","worr"]):
            autumn_face_path + "yuri_turned_eyes_e1b.png"
        attribute oe default if_any(["happ","angr","pout","curi"]):
            autumn_face_path + "yuri_turned_eyes_e1d.png"
        attribute oe default if_any(["cry"]):
            autumn_face_path + "yuri_turned_eyes_e1h.png"
        attribute oe default if_any(["lsur","vang"]):
            autumn_face_path + "yuri_turned_eyes_e2a.png"
        attribute oe default if_any(["anno","flus","laug","sad"]):
            autumn_face_path + "yuri_turned_eyes_e2b.png"
        attribute oe default if_any(["nerv","doub"]):
            autumn_face_path + "yuri_turned_eyes_e2c.png"
        attribute oe default if_any(["shoc","pani","vsur"]):
            autumn_face_path + "yuri_turned_eyes_e2d.png"
        attribute oe default if_any(["yand"]):
            autumn_face_path + "yuri_turned_eyes_e3a.png"

        # Ojos cerrados por defecto
        attribute ce if_any(["dist","anno","vang","flus","lsur","shoc","vsur","worr","sad","angr","nerv","curi","doub"]):
            autumn_face_path + "yuri_turned_eyes_e4a.png"
        attribute ce if_any(["neut","happ","yand","pani","laug","sedu","pout"]):
            autumn_face_path + "yuri_turned_eyes_e4b.png"
        attribute ce if_any(["cry"]):
            autumn_face_path + "yuri_turned_eyes_e4e.png"

        ### Todos los ojos - etiquetas cortas
        attribute e1a:
            autumn_face_path + "yuri_turned_eyes_e1a.png"
        attribute e1b:
            autumn_face_path + "yuri_turned_eyes_e1b.png"
        attribute e1c:
            autumn_face_path + "yuri_turned_eyes_e1c.png"
        attribute e1d:
            autumn_face_path + "yuri_turned_eyes_e1d.png"
        attribute e1e:
            autumn_face_path + "yuri_turned_eyes_e1e.png"
        attribute e1f:
            autumn_face_path + "yuri_turned_eyes_e1f.png"
        attribute e1g:
            autumn_face_path + "yuri_turned_eyes_e1g.png"
        attribute e1h:
            autumn_face_path + "yuri_turned_eyes_e1h.png"
        attribute e2a:
            autumn_face_path + "yuri_turned_eyes_e2a.png"
        attribute e2b:
            autumn_face_path + "yuri_turned_eyes_e2b.png"
        attribute e2c:
            autumn_face_path + "yuri_turned_eyes_e2c.png"
        attribute e2d:
            autumn_face_path + "yuri_turned_eyes_e2d.png"
        attribute e3a:
            autumn_face_path + "yuri_turned_eyes_e3a.png"
        attribute e3b:
            autumn_face_path + "yuri_turned_eyes_e3b.png"
        attribute e4a:
            autumn_face_path + "yuri_turned_eyes_e4a.png"
        attribute e4b:
            autumn_face_path + "yuri_turned_eyes_e4b.png"
        attribute e4c:
            autumn_face_path + "yuri_turned_eyes_e4c.png"
        attribute e4d:
            autumn_face_path + "yuri_turned_eyes_e4d.png"
        attribute e4e:
            autumn_face_path + "yuri_turned_eyes_e4e.png"
        attribute e0a:
            autumn_face_path + "yuri_turned_eyes_e0a.png"
        attribute e0b:
            autumn_face_path + "yuri_turned_eyes_e0b.png"
        attribute ela:
            autumn_face_path + "yuri_turned_eyes_ela.png"
        attribute elb:
            autumn_face_path + "yuri_turned_eyes_elb.png"

        # Ojos extra de LayeredRedux
        attribute e2e:
            autumn_extra_path + "yuri_turned_eyes_e2e.png"
        attribute e3c:
            autumn_extra_path + "yuri_turned_eyes_e3c.png"
        attribute e4f:
            autumn_extra_path + "yuri_turned_eyes_e4f.png"
        attribute e4g:
            autumn_extra_path + "yuri_turned_eyes_e4g.png"
        attribute e4h:
            autumn_extra_path + "yuri_turned_eyes_e4h.png"
        attribute e0c:
            autumn_extra_path + "yuri_turned_eyes_e0c.png"
        attribute e0d:
            autumn_extra_path + "yuri_turned_eyes_e0d.png"
        attribute e0e:
            autumn_extra_path + "yuri_turned_eyes_e0e.png"
        attribute e0f:
            autumn_extra_path + "yuri_turned_eyes_e0f.png"
        attribute e0g:
            autumn_extra_path + "yuri_turned_eyes_e0g.png"
        attribute e0h:
            autumn_extra_path + "yuri_turned_eyes_e0h.png"
        attribute esilly1:
            autumn_extra_path + "yuri_turned_eyes_silly1.png"
        attribute esilly2:
            autumn_extra_path + "yuri_turned_eyes_silly2.png"
        attribute estar1a:
            autumn_extra_path + "yuri_turned_eyes_star1a.png"
        attribute estar1b:
            autumn_extra_path + "yuri_turned_eyes_star1b.png"
        attribute estar2a:
            autumn_extra_path + "yuri_turned_eyes_star2a.png"
        attribute estar2b:
            autumn_extra_path + "yuri_turned_eyes_star2b.png"
        attribute estar3a:
            autumn_extra_path + "yuri_turned_eyes_star3a.png"
        attribute estar3b:
            autumn_extra_path + "yuri_turned_eyes_star3b.png"


    group eyebrows if_not(["s_scream", "s_dark", "s_yandere"]):

        # Cejas por defecto
        attribute brow default if_any(["happ","neut"]):
            autumn_face_path + "yuri_turned_eyebrows_b2a.png"
        attribute brow default if_any(["flus","lsur","laug"]):
            autumn_face_path + "yuri_turned_eyebrows_b1b.png"
        attribute brow default if_any(["dist","sedu"]):
            autumn_face_path + "yuri_turned_eyebrows_b3c.png"
        attribute brow default if_any(["anno", "pout"]):
            autumn_face_path + "yuri_turned_eyebrows_b1d.png"
        attribute brow default if_any(["vang","angr"]):
            autumn_face_path + "yuri_turned_eyebrows_b1e.png"
        attribute brow default if_any(["curi","doub"]):
            autumn_face_path + "yuri_turned_eyebrows_b1f.png"
        attribute brow default if_any(["worr","sad","nerv","cry"]):
            autumn_face_path + "yuri_turned_eyebrows_b2b.png"
        attribute brow default if_any(["yand","shoc","vsur","pani"]):
            autumn_face_path + "yuri_turned_eyebrows_b2c.png"

        ### Todas las cejas - etiquetas cortas
        # (algunas se excluyen con los ojos grandes, igual que en "yuri turned")
        attribute b1a:
            autumn_face_path + "yuri_turned_eyebrows_b1a.png"
        attribute b1b:
            autumn_face_path + "yuri_turned_eyebrows_b1b.png"
        attribute b1c if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            autumn_face_path + "yuri_turned_eyebrows_b1c.png"
        attribute b1d if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            autumn_face_path + "yuri_turned_eyebrows_b1d.png"
        attribute b1e if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            autumn_face_path + "yuri_turned_eyebrows_b1e.png"
        attribute b1f:
            autumn_face_path + "yuri_turned_eyebrows_b1f.png"
        attribute b2a:
            autumn_face_path + "yuri_turned_eyebrows_b2a.png"
        attribute b2b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            autumn_face_path + "yuri_turned_eyebrows_b2b.png"
        attribute b2c:
            autumn_face_path + "yuri_turned_eyebrows_b2c.png"
        attribute b3a if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            autumn_face_path + "yuri_turned_eyebrows_b3a.png"
        attribute b3b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            autumn_face_path + "yuri_turned_eyebrows_b3b.png"
        attribute b3c:
            autumn_face_path + "yuri_turned_eyebrows_b3c.png"

        # Estas cejas sí se permiten en moods "problemáticos" si los ojos están cerrados.
        attribute b1c if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            autumn_face_path + "yuri_turned_eyebrows_b1c.png"
        attribute b1d if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            autumn_face_path + "yuri_turned_eyebrows_b1d.png"
        attribute b1e if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            autumn_face_path + "yuri_turned_eyebrows_b1e.png"
        attribute b2b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            autumn_face_path + "yuri_turned_eyebrows_b2b.png"
        attribute b3a if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            autumn_face_path + "yuri_turned_eyebrows_b3a.png"
        attribute b3b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            autumn_face_path + "yuri_turned_eyebrows_b3b.png"


    # Este grupo va al final a propósito: se dibuja encima de toda la cara.
    group special:
        attribute s_scream:
            autumn_face_path + "yuri_turned_special_scream.png"
        attribute s_dark:
            autumn_extra_path + "yuri_turned_special_dark.png"
        attribute s_yandere:
            autumn_extra_path + "yuri_turned_special_yandere.png"


    group decor:
        attribute blood_mark:
            autumn_extra_path + "yuri_turned_bloodmark.png"

    group sweat:
        attribute sweat1:
            autumn_extra_path + "yuri_turned_sweat.png"
        attribute sweat2:
            autumn_extra_path + "yuri_turned_sweat2.png"

    group eyebags:
        attribute eyebags:
            autumn_extra_path + "yuri_turned_eyebags.png"

    group tears:
        attribute tears1:
            autumn_extra_path + "yuri_turned_tears.png"
        attribute tears2:
            autumn_extra_path + "yuri_turned_sobbing.png"
