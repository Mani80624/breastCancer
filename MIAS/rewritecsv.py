import csv

class ConverterCsvFormat:
    """This class correct Read and Write csv file with delimiter ';'"""
    def __init__(this, archivo_csv):
        """Inicialize the class"""
        this.archivo_csv = archivo_csv
        this.lista_rows = []

    def lista(this, lista_it):
        """Append new list to lista_rows"""
        for i in lista_it:
            return this.lista_rows.append(i.split())
        
    def readCVS(this):
        """Return a list of the list that representation rows"""
        this.default_values()
        with open(this.archivo_csv, 'r') as alias_csv:
            lector_csv = csv.reader(alias_csv)
            for fila in lector_csv:
                if isinstance(fila, list):
                    this.lista(fila)
        return(this.lista_rows)

    def writerCSV(this, nameCSV):
        """Write a new csv file with separation corrections"""
        this.readCVS()
        with open(nameCSV, 'w', newline='', encoding='utf-8') as alias_csv:
            writer_csv = csv.writer(alias_csv, delimiter=';',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in this.lista_rows:
                writer_csv.writerow(row)

        print(f'Done create {nameCSV} file!')

    def default_values(this):
        """Established default values"""
        this.lista_rows = []



# New instance
converterCSV = ConverterCsvFormat('MIAS.csv')
converterCSV.writerCSV('MIAS_Format_correct.csv')