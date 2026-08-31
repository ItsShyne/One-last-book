init -1 python:
    # Sistema de iluminacion ambiental para los sprites de personajes.
    # Se combina con el oscurecido de auto2focus (ver auto2focus_ren.py,
    # CharacterDim.__call__) multiplicando las matrices de color, asi que
    # un personaje que habla/no habla sigue teniendo esa diferencia de
    # brillo SOBRE el tinte de iluminacion actual.
    #
    # AUTOMATICO: se detecta el tinte a partir del nombre del fondo actual
    # ("bg" es el tag que usan todos los fondos del mod). Por convencion,
    # sin sufijo = de dia, y el resto sigue el sufijo del archivo:
    #   _night / _evening / _nolight -> noche
    #   _rainy / _stormy / _cloudy   -> lluvia
    #   _aft / _afternoon            -> tarde
    #   (cualquier otro caso)        -> dia
    # No hace falta tocar el guion para que esto funcione: cambia solo con
    # el "scene bg ..."/"show bg ..." que ya está puesto en cada escena.
    #
    # Si en algun momento se necesita forzar un tinte puntual (por ejemplo,
    # una escena de dia que por guion debería sentirse "de noche"), se
    # puede usar manualmente:
    #     $ set_lighting("noche")   # fuerza el preset
    #     $ set_lighting(None)      # vuelve a detectarlo automático

    lighting_presets = {
        "dia":    IdentityMatrix(),
        "tarde":  TintMatrix("#ffd9a0") * BrightnessMatrix(-0.03),
        "noche":  TintMatrix("#8fa8d9") * BrightnessMatrix(-0.04),
        "lluvia": SaturationMatrix(0.6) * TintMatrix("#a9b8c9") * BrightnessMatrix(-0.08),
    }

    def detect_lighting_from_bg_name(name):
        name = (name or "").lower()
        if "night" in name or "evening" in name or "nolight" in name:
            return "noche"
        if "rainy" in name or "stormy" in name or "cloudy" in name:
            return "lluvia"
        if "aft" in name or "afternoon" in name:
            return "tarde"
        return "dia"

    # Nombre del tinte que se esta mostrando ahora mismo. Solo se actualiza
    # cuando NO hay una transicion en curso en la capa "master" (dissolve,
    # wipe, etc) -- asi el cambio se aplica recien cuando el fondo nuevo ya
    # terminó de reproducirse, nunca antes ni a mitad de la animación.
    _lighting_active_name = "dia"

    def _master_layer_transitioning():
        try:
            return bool(renpy.game.interface.transition.get("master"))
        except Exception:
            return False

    def get_current_lighting_matrix():
        global _lighting_active_name

        if current_lighting_override is not None:
            requested = current_lighting_override
        else:
            attrs = renpy.get_attributes("bg") or ()
            requested = detect_lighting_from_bg_name(attrs[0] if attrs else "")

        if not _master_layer_transitioning():
            _lighting_active_name = requested

        return lighting_presets.get(_lighting_active_name, IdentityMatrix())

    def set_lighting(name):
        if name is not None and name not in lighting_presets:
            raise Exception(
                "set_lighting: '%s' no es un preset valido. Presets disponibles: %s"
                % (name, ", ".join(lighting_presets.keys()))
            )
        store.current_lighting_override = name

default current_lighting_override = None
