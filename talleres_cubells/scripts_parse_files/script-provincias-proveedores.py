# b-*- encoding: utf-8 -*-

import csv
import unicodedata


def elimina_tildes(s):
    if not isinstance(s, unicode):
        s = s.decode('utf-8')
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


data = {}
data_paises = {}
mapa_paises = {
    'a': 'base.es',
    'alemania': 'base.de',
    'portugal': 'base.pt',
    'rusia': 'base.ru',
    'rep.eslovaca': 'base.sk',
    'francia': 'base.fr',
    'pakistan': 'base.pk',
    'espana': 'base.es',
    'italia': 'base.it',
    'belgica': 'base.be',
    'kenia': 'base.ke',
    'marruecos': 'base.ma',
    'bolivia': 'base.bo',
    'suecia': 'base.se',
    'colombia': 'base.co',
    'irlanda': 'base.ie',
    'finlandia': 'base.fi',
}

cuentas_a_ignorar = [
    400011038,
    400000096,
    400010474,
    400011001,
    400011846,
    400000923,
    400005001,
    400005002,
    400001000,
    400001860,
    40001876,
    400001962,
    400001974,
    400001977,
    400001980,
    400001995,
    400001996,
    400005004,
    400002011,
    400002173,
    430002234,
    400002265,
    400002372,
    400002437,
    400002439,
    400002440,
    400002441,
    400002442,
    400002443,
    400002446,
    400002477,
]

with open('/home/esal1/Talleres_Cubells/git_repositories/odoo/odoo/addons/base/res/res.country.state.csv',
          'r') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        data[elimina_tildes(row['name']).upper()] = 'base.%s' % (row['id'],)
        data_paises[elimina_tildes(row['name']).upper()] = 'base.%s' % (row['country_id:id'],)

header = ['id', 'sigla_nacion', 'cif_dni', 'vat', 'name', 'street', 'street2', 'actividad', 'cargo', 'nombre1',
          'comment', 'property_account_payable_id/id', 'codigo_definicion', 'codigo_condiciones', 'forma_de_pago',
          'codigo_banco', 'codigo_agencia', 'dc', 'ccc', 'iban', 'zip', 'city', 'state_id/id', 'country_id/id', 'phone',
          'telefono2', 'telefono3', 'fax', 'email', 'supplier', 'customer', 'company_type',
          'property_account_receivable_id/id']
data_keys = data.keys()

with open('../data/ficheros_originales/proveedores.csv', 'r') as csvfile:
    with open('../data/proveedores/res.partner.csv', 'w') as write_file:
        spamreader = csv.reader(csvfile, delimiter=';')
        spamwriter = csv.writer(write_file, delimiter=';',
                                quotechar='"')
        spamwriter.writerow(header)
        row_num = 0
        for row in spamreader:
            row_num += 1
            if row_num == 1:
                # omitimos la cabecera
                continue
            row_aux = row
            if row[11] and int(row[11]) in cuentas_a_ignorar:
                row_aux[11] = ''
            nombre_ciudad = elimina_tildes(row[22].decode('iso-8859-1').encode('utf8')).upper()
            nombre_pais = elimina_tildes(row[23].decode('iso-8859-1').encode('utf8')).upper()
            if nombre_ciudad:
                if nombre_ciudad in data_keys:
                    row_aux[22] = data[nombre_ciudad]
                    row_aux[23] = data_paises[nombre_ciudad]
                elif nombre_ciudad == 'STA CRUZ DE TENERIFE':
                    row_aux[22] = 'base.state_es_tf'
                    row_aux[23] = 'base.es'
                else:
                    existe = False
                    for x in data_keys:
                        if nombre_ciudad in x:
                            data[elimina_tildes(nombre_ciudad)] = data[x]
                            data_paises[elimina_tildes(nombre_ciudad)] = data[x]
                            row_aux[22] = data[x]
                            row_aux[23] = data_paises[x]
                            existe = True
                            break
                    if not existe:
                        if nombre_ciudad == 'ALEMANIA':
                            # Caso especial
                            row_aux[22] = ''
                            row_aux[23] = 'base.de'
                        else:
                            print nombre_ciudad
                            row_aux[22] = ''
            if nombre_pais and 'base' not in row[19]:
                row_aux[23] = mapa_paises[nombre_pais.lower()]

            row_aux.append('1')
            row_aux.append('0')
            row_aux.append('company')
            # account receivable
            row_aux.append(row_aux[11])
            spamwriter.writerow(row_aux)

