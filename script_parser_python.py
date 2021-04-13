
import io
import re
import csv

# -*- coding: utf-8 -*-

file_name = 'datos_data_engineer.tsv'
file= io.open(file_name,'r', encoding='UTF-16LE').read()

lista_file = re.findall('(([^\t]*\t[^\t]*){4}(\n|\Z))', file)

with io.open('datos_data_engineer.csv' ,'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter="|")
    for row in lista_file:
        aux_file = row[0].split('\t')
        col = len(aux_file)
        lista_final = []
        for i in range(col):
            lista_final.append(aux_file[i].replace("\n" ,"").encode("utf-8").strip())
        writer.writerow(lista_final)
        print(lista_final)
 