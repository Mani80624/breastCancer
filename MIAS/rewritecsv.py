import csv

class ConverterCsvFormat:
    """self class correct Read and Write csv file with delimiter ';'"""
    def __init__(self, archivo_csv):
        """Inicialize the class"""
        self.archivo_csv = archivo_csv
        self.lista_rows = []

    def lista(self, lista_it):
        """Append new list to lista_rows"""
        for i in lista_it:
            return self.lista_rows.append(i.split())
        
    def readCVS(self):
        """Return a list of the list that representation rows"""
        self.default_values()
        with open(self.archivo_csv, 'r') as alias_csv:
            lector_csv = csv.reader(alias_csv)
            for fila in lector_csv:
                if isinstance(fila, list):
                    self.lista(fila)
        return(self.lista_rows)

    def writerCSV(self, nameCSV):
        """Write a new csv file with separation corrections"""
        self.readCVS()
        with open(nameCSV, 'w', newline='', encoding='utf-8') as alias_csv:
            writer_csv = csv.writer(alias_csv, delimiter=';',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in self.lista_rows:
                writer_csv.writerow(row)

        print(f'Done create {nameCSV} file!')

    def default_values(self):
        """Established default values"""
        self.lista_rows = []



# New instance
converterCSV = ConverterCsvFormat('MIAS.csv')
converterCSV.writerCSV('MIAS_Format_correct.csv')