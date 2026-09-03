init -1 python:
    last_speaker = None

    VALID_SPRITES = ["sayori", "yuri", "natsuki", "monika"]

    # Atributos de boca MPT
    # NOTA: "ce"/"oe" son ojos (cerrados/abiertos), no boca -- nunca deben
    # entrar aquí. Antes "ce" estaba incluido por error y is_mouth_attribute()
    # lo trataba como boca, así que cada vez que el sistema auto-boca actuaba
    # sobre un personaje con ojos cerrados (p. ej. "happ cm ce"), se lo quitaba
    # de clean_attrs y los ojos volvían a abrirse solos ("oe", el default del
    # grupo eyes) justo cuando el personaje debía seguir con ojos cerrados.
    OPEN_MOUTH_ATTRS = {"om", "ma", "md", "mo", "m_open", "m_talk", "yand_om"}
    CLOSED_MOUTH_ATTRS = {"cm", "mb", "mc", "me", "mf", "mg"}
    # "scream" no existe como atributo -- el real es "s_scream", así que esta
    # comprobación nunca protegía nada. Según el propio MPT de Yuri (comentario
    # junto a sus atributos "Special"), "s_scream" y "s_dark" SÍ permiten
    # cambiar la boca (no hace falta protegerlos); el único que no debe tocarse
    # es "s_yandere", que antes faltaba aquí por completo.
    SPECIAL_OVERLAYS = {"stab", "s_yandere"}

    def is_mpt_sprite(char_tag):
        """Determina si el sprite activo en pantalla usa MPT o el modelo base."""
        attrs = renpy.get_attributes(char_tag) or ()
        # Si tiene atributos en formato texto de MPT como 'turned', 'forward', 'happ', 'om'
        for a in attrs:
            if a in ["turned", "forward", "tap", "cross", "shy", "lean", "om", "cm"]:
                return True
        return False

    def is_mouth_attribute(attr):
        """Identifica atributos de boca MPT."""
        if attr in OPEN_MOUTH_ATTRS or attr in CLOSED_MOUTH_ATTRS:
            return True
        if attr.startswith("m") or "_m" in attr or "mouth" in attr:
            return True
        return False

    def has_specific_mouth(attrs):
        """
        True si el personaje ya tiene puesta una boca ESPECÍFICA a mano
        (p. ej. "mk" para una mueca de dolor), en vez de la genérica "om"/"cm"
        que pone el propio sistema automático. En ese caso el sistema no debe
        tocar nada: se respeta la elección manual del guion mientras dure esa
        línea, en vez de sobrescribirla apenas el personaje habla.
        """
        for a in attrs:
            if is_mouth_attribute(a) and a not in ("om", "cm"):
                return True
        return False


    def auto_mouth_callback(character_tag, event, **kwargs):
        global last_speaker

        if event == "begin":
            # 1. Si habla un personaje sin sprite visual (MC, Dr, Narrador), cerramos la boca de la chica previa
            if character_tag not in VALID_SPRITES:
                if last_speaker in VALID_SPRITES:
                    close_character_mouth(last_speaker)
                    last_speaker = None
                return

            # 2. Si cambia la chica activa, cerramos la boca de la anterior
            if last_speaker and last_speaker != character_tag and last_speaker in VALID_SPRITES:
                close_character_mouth(last_speaker)

            # 3. Guardar chica activa y abrir su boca
            last_speaker = character_tag
            open_character_mouth(character_tag)


    def open_character_mouth(char_tag):
        if char_tag not in VALID_SPRITES or not renpy.showing(char_tag):
            return

        attrs = list(renpy.get_attributes(char_tag) or [])

        if any(overlay in attrs for overlay in SPECIAL_OVERLAYS):
            return

        if has_specific_mouth(attrs):
            return

        # SINTAXIS MPT
        if is_mpt_sprite(char_tag):
            clean_attrs = [a for a in attrs if not is_mouth_attribute(a)]
            clean_attrs.append("om")
            renpy.show(f"{char_tag} " + " ".join(clean_attrs))

        # SINTAXIS DDLC BASE (ejemplo: '1a', '2c', '4m')
        else:
            # En el modelo base, la boca la controla el comando Say o la sintaxis nativa de DDLC
            # Simplemente dejamos que Ren'Py mantenga el sprite base tal como está sin chocar
            pass


    def close_character_mouth(char_tag):
        if char_tag not in VALID_SPRITES or not renpy.showing(char_tag):
            return

        attrs = list(renpy.get_attributes(char_tag) or [])

        if any(overlay in attrs for overlay in SPECIAL_OVERLAYS):
            return

        if has_specific_mouth(attrs):
            return

        # SINTAXIS MPT
        if is_mpt_sprite(char_tag):
            clean_attrs = [a for a in attrs if not is_mouth_attribute(a)]
            clean_attrs.append("cm")
            renpy.show(f"{char_tag} " + " ".join(clean_attrs))

        # SINTAXIS DDLC BASE
        else:
            pass

    # Guardado seguro compatible con pickle
    mouth_cb = renpy.curry(auto_mouth_callback)