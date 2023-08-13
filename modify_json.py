import json
import dropbox


# Initialize dropbox client
with open("model/token.json", "r") as config:
    token = json.load(config)
    dbx = dropbox.Dropbox(token["DROPBOX_TOKEN"])

dropbox_path = '/citas_datos_Andy.json'
local_data_json = 'model/data_local.json'

# Configura el archivo local JSON como una lista vacía
cita_molde = {
    "id_cita": None,
    "fecha_prog": None,
    "hora_prog": None,
    "ap_pat": None,
    "ap_mat": None,
    "nombres": None,
    "codigo": None,
    "concepto": None,
    "obs": None,
    "flag": None,
    "estado": None,
    "telefono": None,
    "correo": None,
    "fecha_reg": None,
    "hora_reg": None
}

# Guardar la lista vacía en el archivo local
with open(local_data_json, "w") as f:
    json.dump(cita_molde, f, indent=4)

# Subir el archivo JSON actualizado (ahora vacío) a Dropbox
with open(local_data_json, "rb") as f:
    dbx.files_upload(f.read(), dropbox_path,
                     mode=dropbox.files.WriteMode("overwrite"))
