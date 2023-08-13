token = "sl.BkBbCC9fQ4WINhdzkg9B4ieLXfg5KsgWUyUbguCXuJUEZIuNZYcP5Dh_FZ1RSgQ2jOOw3jsZmLhjyTCjWSbTVmaQORIU7ZpCCStH-J2r7RnRwkIFTVz-o_IZbCPA5c6HSbHzsS-zd1c1"
"https://www.dropbox.com/scl/fi/62xdntnmxqcw5w6o7qrke/citas_datos_Andy.txt?rlkey=tifveh2c8dq6p7hsmykanm41a&dl=0"

import dropbox

# Inicializar el cliente de Dropbox con tu token
dbx = dropbox.Dropbox(token)

# Ruta del archivo en Dropbox y local
dropbox_path = '/citas_datos_Andy.txt'
local_path = 'model/data_local.txt'

# Paso 1: Descargar el archivo desde Dropbox
with open(local_path, "wb") as f:
    metadata, res = dbx.files_download(path=dropbox_path)
    f.write(res.content)

# Paso 2: Agregar una línea de prueba al archivo local
with open(local_path, "w") as f:
    f.write("\nMARICÓN")

# Paso 3: Subir el archivo modificado nuevamente a Dropbox
with open(local_path, "rb") as f:
    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
