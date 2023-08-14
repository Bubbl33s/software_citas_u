import firebase_admin
from firebase_admin import credentials, db
import json

# Iniciar Firebase
cred = credentials.Certificate('model/token.json')
firebase_admin.initialize_app(
    cred, {'databaseURL': 'https://db-for-appointment-sw-default-rtdb.firebaseio.com/'})

# Función para cargar citas desde Firebase a tu JSON local


def load_appointments_db():
    ref = db.reference('citas')
    dict_from_db = ref.get()

    # Guardar en JSON local
    with open('model/data_local.json', 'w') as f:
        json.dump(dict_from_db, f)

# Función para guardar una nueva cita en Firebase


def save_appointment(new_appointment):
    ref = db.reference('citas')

    # Generar un ID único para la cita. Puedes usar otras estrategias para generar la ID.
    id_cita = ref.push().key

    # Guardar la cita en Firebase
    ref.child(id_cita).set(new_appointment)


def get_key_by_id_cita(id_cita_to_find):
    ref = db.reference('citas')
    citas = ref.get()

    for key, cita in citas.items():
        if cita['id_cita'] == id_cita_to_find:
            return key
    return None  # Si no se encuentra el id_cita


def delete_by_id_cita(id_cita_to_find):
    key = get_key_by_id_cita(id_cita_to_find)
    if key:
        ref = db.reference(f'citas/{key}')
        ref.delete()
        print(f"Cita con id_cita {id_cita_to_find} eliminada.")
    else:
        print(f"No se encontró ninguna cita con id_cita {id_cita_to_find}.")


# Cargar citas
load_appointments_db()
