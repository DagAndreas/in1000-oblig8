class Datasenter:
    def __init__(self):
        self._regneklynger = {}

    def lesInnRegneklynge(self, filnavn):
        lagdNyKlynge = False
        nyKlyngenavn = filnavn.strip(".txt")
        fil = open(filnavn)

        for biter in fil:
            bit = biter.split()
            while lagdNyKlynge == True:
                antNyeNoder = int(bit[0])
                minne = bit[1]
                prosessorer = bit[2]

                while antNyeNoder != 0:
                    nodeX = Node(prosessorer, minne)
                    self._regneklynger[filnavn].settInnNode(nodeX)
                    antNyeNoder += -1
                lagdNyKlynge = True
                break
            while lagdNyKlynge == False:
                 nyKlynge = Regneklynge(int(bit[0]))
                 self._regneklynger[filnavn] = nyKlynge
                 lagdNyKlynge = True


    def skrivUtAlleRegneklynger(self):  #returnerer all info om alle regneklynger
        allInfo = []
        for klynge in self._regneklynger:
            allInfo.append(self.skrivUtRegneklynge(klynge))
            allInfo.append("\n")
        return ''.join(allInfo)

    def skrivUtRegneklynge(self, navn):
        regneklynge = self._regneklynger[navn]
        info = ["Info om ", navn.strip(".txt").capitalize(), "\n",
        "Antall racks: ", str(regneklynge.antRacks()),
        "\n","Antall prosessorer: ", str(regneklynge.antProsessorer()), "\n",
        regneklynge.nodeMinneStandard(), "\n"]
        return ''.join(info)



    def lesProsessorerIKlynger(self):   #gjelder alle klynger
        totaleprosessorer = 0
        for regner in self._regneklynger:
            klynge = self._regneklynger[regner]
            prosessorer = klynge.antProsessorer()
            totaleprosessorer += int(prosessorer)
        return totaleprosessorer

    def overGrense(self, grense):   #gjelder alle klynger
        antOverGrense = 0
        for klynge in self._regneklynger:
            klynge = self._regneklynger[klynge]
            antOverGrense += klynge.noderMedNokMinne(grense)
        return antOverGrense

class Regneklynge:
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._rackListe = []

    def __str__(self):
        return str([self._noderPerRack, len(self._rackListe)])



    def settInnNode(self, node):
        if self._rackListe == []:
            rack = Rack()
            self._rackListe.append(rack)
            self._rackListe[-1].settInn(node)

        elif self._rackListe[-1].getAntNoder() <  self._noderPerRack:
            self._rackListe[-1].settInn(node)

        elif self._rackListe[-1].getAntNoder() == int(self._noderPerRack):
            rack = Rack()
            rack.settInn(node)
            self._rackListe.append(rack)

    def antProsessorer(self):
        antallProsessorer = 0
        for rack in self._rackListe:
            prosessorerIRack = rack.antProsessorer()
            antallProsessorer += prosessorerIRack
        return antallProsessorer

    def totaleNoder(self):
        totaleNoder = 0
        for rack in self._rackListe:
            totaleNoder += rack.getAntNoder()
        return totaleNoder


    def nodeMinneStandard(self):
        info = []
        info = ["Noder med minst 32 GB: ",
        str(self.noderMedNokMinne(32)), "\n", "Noder med minst 64 GB: ",
        str(self.noderMedNokMinne(64)), "\n", "Noder med minst 128 GB: ",
        str(self.noderMedNokMinne(128))]
        return ''.join(info)

    def nodeStandardInfo(self):
        liste = []
        liste.append(self.noderMedNokMinne(32))
        liste.append(self.noderMedNokMinne(64))
        liste.append(self.noderMedNokMinne(128))
        return liste

    def noderMedNokMinne(self, paakrevdMinne):  #int
            antNoderMedNokMinne = 0
            for rack in self._rackListe:
                antNoderMedNokMinne += rack.noderMedNokMinne(paakrevdMinne)
            return antNoderMedNokMinne

    def antRacks(self):     #int
        return len(self._rackListe)

class Rack:
    def __init__(self):
        self._nodeListe = []


    def settInn(self, node):    #setter inn ferdig objektnode
        self._nodeListe.append(node)

    def settInnNyNode(self, antPros, minne):  #lager node ut fra argumenter
        node = Node(antPros, minne)
        self._nodeListe.append(node)

    def getAntNoder(self):  #int
        return len(self._nodeListe)

    def antProsessorer(self):   #int
        totaleProsessorer = 0
        for node in self._nodeListe:
            totaleProsessorer += node.antProsessorer()
        return totaleProsessorer

    def noderMedNokMinne(self, paakrevdMinne):  #int
        noderMedNokMinne = 0
        for node in self._nodeListe:
            noderMedNokMinne += node.nokMinne(paakrevdMinne)
        return noderMedNokMinne

class Node:
    def __init__(self, prosessorer, minne):
        self._antallProsessorer = prosessorer
        self._minne = minne

    def __str__(self):  #str
        mld = [self._antallProsessorer + self._minne]
        return mld

    def antProsessorer(self):   #int
        return int(self._antallProsessorer)


    def nokMinne(self, minne):  #bool
        if minne <= int(self._minne):
            return 1
        else:
            return 0
