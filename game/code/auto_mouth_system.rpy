init -1 python:
    last_speaker = None

    VALID_SPRITES = ["sayori", "yuri", "natsuki", "monika"]

    # Atributos de boca MPT
    OPEN_MOUTH_ATTRS = {"om", "ma", "md", "mo", "m_open", "m_talk", "yand_om"}
    CLOSED_MOUTH_ATTRS = {"cm", "mb", "mc", "me", "mf", "mg", "ce", "int", "stly", "jong"}
    SPECIAL_OVERLAYS = {"scream", "stab"}

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