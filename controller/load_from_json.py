import json


def get_appointments_list():
    appointments_list = []

    with open('model/data_local.json', 'r') as j:
        local_db = json.load(j)

        # Single appointment
        for sngl_apmnt in local_db.values():
            aux_list = [sngl_apmnt["id_cita"], sngl_apmnt["concepto"], sngl_apmnt["fecha_prog"],
                        sngl_apmnt["hora_prog"], sngl_apmnt["ap_pat"], sngl_apmnt["ap_mat"], sngl_apmnt["nombres"],
                        sngl_apmnt["codigo"], sngl_apmnt["flag"], sngl_apmnt["estado"]]

            appointments_list.append(aux_list)

    return appointments_list
