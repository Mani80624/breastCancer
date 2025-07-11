import csv

class ConverterCsvFormat:
    def __init__(this, archivo_csv):
        this.archivo_csv = archivo_csv
        this.lista_rows = []

    def lista(this, lista_it):
        for i in lista_it:
            return this.lista_rows.append(i.split())
        
    def readCVS(this):
        this.default_values()
        with open(this.archivo_csv, 'r') as alias_csv:
            lector_csv = csv.reader(alias_csv)
            for fila in lector_csv:
                if isinstance(fila, list):
                    this.lista(fila)
        return(this.lista_rows)

    def writerCSV(this, nameCSV):
        this.readCVS()
        with open(nameCSV, 'w', newline='', encoding='utf-8') as alias_csv:
            writer_csv = csv.writer(alias_csv, delimiter=';',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in this.lista_rows:
                writer_csv.writerow(row)

    def default_values(this):
        this.lista_rows = []



# new instance
convert_file = ConverterCsvFormat("MIAS.csv")
convert_file.writerCSV('MIAS_Format_correct.csv')