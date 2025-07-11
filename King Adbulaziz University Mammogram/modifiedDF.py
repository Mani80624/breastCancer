import csv

def read_csv(file_path):
    list_duplicate = []
    with open(file_path, 'r') as archivo_csv:
        reader_csv = csv.reader(archivo_csv)
        for row in reader_csv:
            for i in row:
                i = i.replace("BIRAD", "")
                i = i.replace(";"," ")
                i = i.replace("BC ", "BC")
                i = i + ''
                lista = i.split()
                if len(lista) >= 7:
                    del lista[6:]
                
                birads_M_L = lista.pop()
                birads_M_R = lista.pop()

                copy_list = lista[:]
                copy_list.append('L')
                copy_list.append(birads_M_L)
                lista.append('R')
                lista.append(birads_M_R)

                
                
                list_duplicate.append(lista)
                list_duplicate.append(copy_list)
    return list_duplicate

def writerCSV(nameCSV,lista_rows):
    """Write a new csv file with separation corrections"""
    with open(nameCSV, 'w', newline='', encoding='utf-8') as alias_csv:
        writer_csv = csv.writer(alias_csv, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in lista_rows:
            writer_csv.writerow(row)

    print(f'Done create {nameCSV} file!')
        


lista_duplicada = read_csv('/home/manuel/Descargas/Estudio de DB para cancer de mama/King Adbulaziz University Mammogram/BC with ultrasound.csv')

writerCSV('prueba1.csv', lista_duplicada)