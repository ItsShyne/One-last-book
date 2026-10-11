# Chats del teléfono (Better EMR Phone) que se usan en el cap. 2.
# Las claves de los personajes son: "mc", "y" (Yuri), "s", "m", "n" y "x" (el número desconocido).

init python:
    import datetime

    # Fija la fecha, la hora y la batería que muestra el teléfono para que coincidan con la historia
    # (si no, mostraría la hora y la batería reales de la computadora del jugador).
    # La historia ocurre en octubre de 2026: jueves 1 (casa de Yuri), viernes 2 y sábado 3 (la salida).
    def phone_hora(dia, hora, minuto, bateria=70, mes=10, anio=2026):
        phone.system.date = datetime.datetime(anio, mes, dia, hora, minuto)
        phone.system.battery_level = bateria
        phone.system.wifi = True
        phone.system.locked = True

    # Los chats y personajes del teléfono se guardan dentro de la partida. Si el nombre del
    # contacto cambia en el código, una partida guardada antes seguiría mostrando el nombre viejo;
    # al cargar, esto lo actualiza.
    def phone_refrescar_nombres():
        for var in ("chat_desconocido", "pc_desconocido"):
            obj = getattr(renpy.store, var, None)
            if obj is not None:
                obj.name = "Desconocido"

    config.after_load_callbacks.append(phone_refrescar_nombres)

# Número desconocido que le escribe a MC.
# prioridad 10 para que se cree despues de phone.character._characters (que usa prioridad 0)
default 10 pc_desconocido = phone.character.Character("Desconocido", phone.asset("default_icon.png"), "x", 28, "#555555")

init phone register:
    define "Desconocido":
        add "mc" add "x"
        icon phone.asset("default_icon.png")
        as chat_desconocido key "desconocido"

init phone register:
    define "Yuri":
        add "mc" add "y"
        icon phone.asset("yuri_icon.png")
        as chat_yuri key "yuri"
