import json
import dropbox

# TODO: CYPHER TOKEN
token = "sl.BkA0MwyPgeHLTf2fWyKIzhlV5WMq4xoZfyHeIwp35InogvjHyqVUGCd7AJcNdUBPDR_Kk63-2SQ6dH4UunHe16O_sVApJUD3MbPWzTliRIL5OOLSnpcu7ylQAiKZVkZOE7qljQMx3lAv"
# Initialize dropbox client
dbx = dropbox.Dropbox(token)

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
    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
