# b-*- encoding: utf-8 -*-

import csv
import unicodedata


def elimina_tildes(s):
    if not isinstance(s, unicode):
        s = s.decode('utf-8')
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

header = ['id', 'code', 'name', 'cliente_o_proveedor', 'sigla_nacion', 'cif_dni', 'codigo_divisa',
          'user_type_id/id', 'reconcile']

# creating new types
with open('../data/plan_contable/account.account.type.csv', 'w') as write_file_type:
    spamwriter = csv.writer(write_file_type, delimiter=';', quotechar='"')
    spamwriter.writerow(['id', 'name', 'type'])
    spamwriter.writerow(['tipo_clientes', 'Clientes', 'receivable'])
    spamwriter.writerow(['tipo_proveedores', 'Proveedores', 'payable'])

with open('../data/ficheros_originales/plan_contable.csv', 'r') as csvfile:
    with open('../data/plan_contable/account.account.csv', 'w') as write_file:
        spamreader = csv.reader(csvfile, delimiter=';')
        spamwriter = csv.writer(write_file, delimiter=';', quotechar='"')
        spamwriter.writerow(header)
        row_num = 0
        for row in spamreader:
            row_num += 1
            if row_num == 1:
                # omitimos la cabecera
                continue
            cliente_o_proveedor = row[2].strip()
            if cliente_o_proveedor == 'Cliente':
                tipo_cuenta = 'tipo_clientes'
            elif cliente_o_proveedor == 'Proveedor':
                tipo_cuenta = 'tipo_proveedores'
            else:
                tipo_cuenta = 'l10n_es.account_type_terceros'
            row_aux = [row[0].strip(), row[0].strip(), row[1].strip(), cliente_o_proveedor,
                       row[3].strip(), row[4].strip(), row[5].strip(), tipo_cuenta, True]
            spamwriter.writerow(row_aux)
