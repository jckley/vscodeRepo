# Reads an Einstein Analytics JSON file containing Field Labels and Null Token and adds the Lables as Headers in the JSON order.
# Then adds N headerless CSV Files comprising the above mentioned fields

# EXECUTE = python EARecipeConvert2CSV.py  inputjsonfile inputcsvfile N
# (inputcsvfile = nombre del csv sin indice - sin el "_n" y sin file format extension ;
# inputjsonfile = idem sin extension,
# "N" ultimo numero de archivo a concatenar 1...N)

# VIP =
#from pathlib import Path
#input_file = Path.cwd() / 'csv_in' / in_file
#output_file = Path.cwd() /'csv_out' / out_file
# Path.cwd() te da el current directory donde estas corriendo el py


# _________________________________________________________________________________________________________________________________


import json
import re
import sys
import csv
from pathlib import Path

in_json = sys.argv[1]+'.json'
in_file = sys.argv[2]
in_nrocsvs = int(sys.argv[3])
count = 0

out_file = 'OUT_'+str(in_file)+'.csv'


input_json = Path.cwd() / 'csv_in' / in_json
output_file = Path.cwd() / 'csv_out' / out_file


# print(output_file)
# print(input_json)
# print(in_nrocsvs)


# Abre el archivo de salida
csvfile = open(output_file, 'w')

# Del archivo JSON lee los nombres de los campos
# Y los guarda en el archivo de salida
with open(input_json) as json_file:
    data = json.load(json_file)    # data es un dictionary
    # print (data)
    for p in data['objects']:
        # print(p)
        first = True
        for field in p['fields']:
            if not first:
                csvfile.write(',')
            csvfile.write(field['label'])
            print("CAMPOS = ", field['label'])
            # print(field)
            # print(field['label'])
            # print(field['name'])
            first = False
        csvfile.write('\n')


# Lee el archivo CSV linea x linea
# y los copia en el archivo de salida
for x in range(1, in_nrocsvs+1):
    aux = str(in_file)+'_'+str(x)+'.csv'
    input_file = Path.cwd() / 'csv_in' / aux
    print(input_file)
    with open(input_file) as inputcsv:
        line = inputcsv.readline()
        # print (line)              #imprimo la primera linea para verificar en la consola
        while line:
            # reemplaza null+token x null
            words = line.split(",")
            for index, word in enumerate(words):
                if 'null-' in word:
                    if '\n' in word:
                        words[index] = '\n'
                    else:
                        words[index] = ''
            line = ",".join(words)

            # escribe la linea modificada en el csvfile = open(output_file,'w')
            csvfile.write(line)
            count += 1
            line = inputcsv.readline()  # leo la siguiente linea
else:
    print("Finally finished!\n" + "Nro de registros =" + str(count))

# Cierra el archivo de salida
csvfile.close()
