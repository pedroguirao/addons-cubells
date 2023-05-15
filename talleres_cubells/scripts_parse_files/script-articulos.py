# b-*- encoding: utf-8 -*-

import csv
import unicodedata


def elimina_tildes(s):
    if not isinstance(s, unicode):
        s = s.decode('utf-8')
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

header = ['codigo_empresa', 'default_code', 'name', 'description_purchase', 'description_sale',
          'standard_price', 'descuento_compras', 'fecha_precio']

with open('../data/ficheros_originales/articulos.csv', 'r') as csvfile:
    with open('../data/articulos/product.template.csv', 'w') as write_file:
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
            row_aux[5] = row_aux[5].replace(',', '.')
            row_aux[6] = row_aux[6].replace(',', '.')
            list_fecha = row_aux[7].split('/')
            if row_aux[7]:
                row_aux[7] = '%(year)s-%(month)s-%(day)s' % ({'year': list_fecha[2],
                                                              'month': list_fecha[1],
                                                              'day': list_fecha[0]})
            spamwriter.writerow(row_aux)
