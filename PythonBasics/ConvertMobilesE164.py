import sys
import csv
input_file = sys.argv[1]
output_file = str(input_file) + '_OUT' + '.csv'

reader = csv.reader(open(input_file + '.csv', "r"), delimiter=',', quotechar='"')
writer = csv.writer(open(output_file, "w"), quoting=csv.QUOTE_NONE, escapechar='\\')

writer.writerows(reader)

# Ejemplo
# python3 DQuotesV2.py Vota_JMU_DED