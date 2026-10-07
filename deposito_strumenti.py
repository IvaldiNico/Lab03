 import csv
from operator import attrgetter

class Strumenti:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
            self.__id_strumento = id_strumento
            self.__tipo = tipo
            self.__marca = marca
            self.__anno_acquisto = anno_acquisto
            self.__valore = valore

    def __str__(self):
        return f"{self.__id_strumento}, {self.__tipo}, {self.__marca}, {self.__anno_acquisto}, {self.__valore}"


class Prestiti:
    def __init__(self, id_prestito, data, id_strumento, cognome_allievo):
        self.__id_prestito = id_prestito
        self.__data= data
        self.__id_strumento = id_strumento
        self.__cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.__id_prestito}, {self.__data}, {self.__id_strumento}, {self.__cognome_allievo}"



class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}
        self.prestiti = {}


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, "r", encoding = "utf-8") as infile:
                reader = csv.reader(infile)

                for line in reader:
                    id_strumento = line[0]
                    tipo = line[1]
                    marca = line[2]
                    anno_acquisto= line[3]
                    valore = line[4]
                    nuovo_strumento = Strumenti(id_strumento,tipo,marca,anno_acquisto,valore)

                    self.strumenti[id_strumento] = nuovo_strumento

        except FileNotFoundError:
            print(f"File {file_path} non trovato")


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        id_strumento = "S" + str(len(self.strumenti) + 1)
        strumento_tastiera = Strumenti(id_strumento,tipo,marca,anno_acquisto,valore)

        self.strumenti[id_strumento] = strumento_tastiera

        return strumento_tastiera


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        @property
        def marca(self):
            return self.__marca

        @marca.setter
        def marca(self, marca):
            self.__marca = marca

        ordinati = sorted(self.strumenti.values(), key=attrgetter("marca"))
        return ordinati
    #TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception("non trovato")

        id_prestito = "P" + str(len(self.prestiti) + 1)

        if id_strumento not in self.prestiti:

            nuovo_prestito = Prestiti(id_prestito, data, id_strumento, cognome_allievo)
            self.prestiti[id_prestito] = nuovo_prestito
            return nuovo_prestito

        else:
            raise Exception("strumento già in prestito")



        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito in self.prestiti:
            self.prestiti.pop(id_prestito)
        else:
            raise Exception("prestito non trovato")

