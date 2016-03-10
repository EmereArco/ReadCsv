import csv


# STEP 1 - funzione che printa il csv riga per riga


def read_csv(filecsv):
    csvfile = open(filecsv, 'rb')
    csvreader = csv.reader(csvfile, delimiter=';')
    result = ''
    for row in csvreader:
        result += str(row) + '\n'
    return result


# print read_csv('ORARI.csv')


# STEP 2 - funzione che printa le sole colonne che ci interessano riga per riga


def read_csv_column(filecsv):
    csvfile = open(filecsv, 'rb')
    csvreader = csv.reader(csvfile, delimiter=';')
    result = ''
    for row in csvreader:
        codice_corsa = row[6]
        km = row[8]
        result += codice_corsa + '-' + km + '\n'
    return result


# print read_csv_column('ORARI.csv')


# STEP 3 - funzione che estrae i valori univoci di codice_corsa


def read_csv_generico(filecsv):
    csvfile = open(filecsv, 'rb')
    csvreader = csv.reader(csvfile, delimiter=';')
    return csvreader


def estrai_percorso():
    codice_corsa = []
    for row in read_csv_generico('ORARI.csv'):
        codice_corsa.append(row[6])
    return str(set(codice_corsa)) + '\n' + str(len(set(codice_corsa)))


# print estrai_percorso()
# print estrai_percorso().find('CODICE_CORSA')

# STEP 4 - funzione che associa ad ogni corsa una lista di valori di km


def estrai_corse():
    codice_corsa = []
    rownum = 0
    for row in read_csv_generico('ORARI.csv'):
        if rownum != 0:
            codice_corsa.append(row[6])
        rownum += 1
    return set(codice_corsa)


# print list(estrai_corse())
# print 'CODICE_CORSA' in estrai_corse()


def associa_km():
    percorsi_km = dict.fromkeys(estrai_corse(), str())
    rownum = 0
    for row in read_csv_generico('ORARI.csv'):
        if rownum != 0 and row[6] in percorsi_km.keys():
            percorsi_km[row[6]] += row[8]
        rownum += 1
    return percorsi_km

# for k, v in associa_km().items():
   print k, v

# STEP 5 - funzione che associa ad ogni corsa una lista di valori di orario di arrivo


def associa_orario():
    percorsi_orario = dict.fromkeys(estrai_corse(), list(str()))
    rownum = 0
    for row in read_csv_generico('ORARI.csv'):
        if rownum != 0 and row[6] in percorsi_orario.keys():
            list.insert(row[9])
        rownum += 1
    return percorsi_orario


def conv(s):
    num = s.replace(',', '.')
    km = float(num)
    return km


def estrai_percorso_km():
    percorsi_km = {}
    rownum = 0
    km_percorsi = []
    for row in read_csv('ORARI.csv'):
        if rownum == 0:
            pass
        else:
            codice_corsa = row[6]
            if codice_corsa in percorsi_km:
                percorsi_km[codice_corsa] = km_percorsi.append(conv(row[8]))
            else:
                percorsi_km[codice_corsa] = km_percorsi.append(conv(row[8]))
        rownum += 1
    return percorsi_km
