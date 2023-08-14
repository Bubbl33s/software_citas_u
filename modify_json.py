import firebase_admin
from firebase_admin import credentials, db
import json

print("Iniciando...")

print("Iniciando Firebase...")
# Iniciar Firebase
cred = credentials.Certificate('model/token.json')
firebase_admin.initialize_app(
    cred, {'databaseURL': 'https://db-for-appointment-sw-default-rtdb.firebaseio.com/'})

# Función para cargar citas desde Firebase a tu JSON local


def cargar_citas():
    ref = db.reference('citas')
    citas = ref.get()

    # Guardar en JSON local
    with open('model/data_local.json', 'w') as f:
        json.dump(citas, f)

# Función para guardar una nueva cita en Firebase


def guardar_cita(nueva_cita):
    ref = db.reference('citas')

    # Generar un ID único para la cita. Puedes usar otras estrategias para generar la ID.
    id_cita = ref.push().key

    # Guardar la cita en Firebase
    ref.child(id_cita).set(nueva_cita)


def obtener_key_por_id_cita(id_cita_buscado):
    ref = db.reference('citas')
    citas = ref.get()

    for key, cita in citas.items():
        if cita['id_cita'] == id_cita_buscado:
            return key
    return None  # Si no se encuentra el id_cita


def eliminar_cita_por_id_cita(id_cita_buscado):
    key = obtener_key_por_id_cita(id_cita_buscado)
    if key:
        ref = db.reference(f'citas/{key}')
        ref.delete()
        print(f"Cita con id_cita {id_cita_buscado} eliminada.")
    else:
        print(f"No se encontró ninguna cita con id_cita {id_cita_buscado}.")


# Ejemplo de uso:
eliminar_cita_por_id_cita("002")

# Cargar citas
cargar_citas()
