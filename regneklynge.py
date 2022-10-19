from rack import Rack
from node import Node
class Regneklynge:
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack       #maks noder per rack
        self._rackListe = []                    #liste for rack

    def __str__(self):  #maks noder per rack og antall racks
        info = ["noder per rack:",str(self._noderPerRack), "\nantall racks",
        "regneklyngen", str(len(self._rackListe))]
        return ' '.join(info)


    def settInnNode(self, node):          #legger til en node
        if self._rackListe == []:         #sjekker om det er en rack ledig
            rack = Rack()                 #lager ny rack
            self._rackListe.append(rack)  #legger til rack i rack i self._rackListe
            self._rackListe[-1].settInn(node)  #legger til node

        elif self._rackListe[-1].getAntNoder() <  self._noderPerRack: #legger til
            self._rackListe[-1].settInn(node)    #i en eksisterende rack

        elif self._rackListe[-1].getAntNoder() == int(self._noderPerRack):
            rack = Rack()           #hvis siste rack i self._rackListe er full
            rack.settInn(node)      #lager den en ny rack og legger til node i
            self._rackListe.append(rack)    #den denne rack'en

    def antProsessorer(self):   #antall prosessorer i regneklyngen
        antallProsessorer = 0
        for rack in self._rackListe:
            prosessorerIRack = rack.antProsessorer()
            antallProsessorer += prosessorerIRack
        return antallProsessorer

    def totaleNoder(self):
        totaleNoder = 0
        for rack in self._rackListe:
            totaleNoder += rack.getAntNoder()
        return totaleNoder     #antall noder i regneklyngen

    def nodeMinneStandard(self): #antall noder med 32/64/128 gb minne
        info = []
        info = ["Noder med minst 32 GB: ", str(self.noderMedNokMinne(32)), "\n",
        "Noder med minst 64 GB: ", str(self.noderMedNokMinne(64)), "\n",
        "Noder med minst 128 GB: ",str(self.noderMedNokMinne(128))]
        return ''.join(info)

    def noderMedNokMinne(self, paakrevdMinne): #antall noder med gitt minne
            antNoderMedNokMinne = 0
            for rack in self._rackListe:
                antNoderMedNokMinne += rack.noderMedNokMinne(paakrevdMinne)
            return antNoderMedNokMinne

    def antRacks(self):         #antall racks i regneklyngen
        return len(self._rackListe)
