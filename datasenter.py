from regneklynge import Regneklynge
from node import Node
from rack import Rack
class Datasenter:
    def __init__(self):
        self._regneklynger = {}

    def lesInnRegneklynge(self, filnavn):   #leser inn fra fil
        lagdNyKlynge = False    #variabel som blir true etter foerste itterasjon
        nyKlyngenavn = filnavn.strip(".txt")

        for biter in open(filnavn): #leser gjennom fil linje for linje
            bit = biter.split()
            while lagdNyKlynge == True:
                antNyeNoder = int(bit[0])   #nye noder
                minne = bit[1]              #minne på ny node
                prosessorer = bit[2]        #ant prosessorer paa ny node

                while antNyeNoder != 0:              #teller hvor mange nye noder
                    nodeX = Node(prosessorer, minne) #lager ny node
                    self._regneklynger[filnavn].settInnNode(nodeX) #legger inn node
                    antNyeNoder -= 1
                lagdNyKlynge = True
                break
            while lagdNyKlynge == False: #første bestemmer max noder per rack
                nyKlynge = Regneklynge(int(bit[0])) #lager regneklynge
                self._regneklynger[filnavn] = nyKlynge  #legger regneklynge med
                lagdNyKlynge = True                #noekkel i self._regneklynger

    def skrivUtAlleRegneklynger(self):  #info om alle regneklynger
        allInfo = []
        for klynge in self._regneklynger:
            #klynge = self._regneklynger[klynge]
            #info = self.skrivUtRegneklynge(klynge)
            allInfo.append(self.skrivUtRegneklynge(klynge))
            allInfo.append("\n")
        return ''.join(allInfo)

    def skrivUtRegneklynge(self, navn):        #printer antall racks, antall
        regneklynge = self._regneklynger[navn] #prosessorer, og noder med 32/64/
        info = ["Info om ", navn.strip(".txt").capitalize(), "\n",  #128GB minne
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
        return totaleprosessorer    # totale antallet prosessorer i datasenter

    def overGrense(self, grense):   #gjelder alle klynger
        antOverGrense = 0
        for klynge in self._regneklynger:
            klynge = self._regneklynger[klynge]
            antOverGrense += klynge.noderMedNokMinne(grense)
        return antOverGrense    #antall minne over gitt grense i hele datasenter
