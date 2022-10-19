from node import Node
class Rack:
    def __init__(self):
        self._nodeListe = []    #liste for å oppbevare noder

    def __str__(self):
        info = []
        while self._nodeListe != []:
            for node in self._nodeListe:
                    info.append(str(node))
            break
        return ''.join(info)        #info om noder i lista


    def settInn(self, node):    #setter inn ferdig objektnode
        self._nodeListe.append(node)

    def settInnNyNode(self, antPros, minne):  #lager node ut fra argumenter
        node = Node(antPros, minne)
        self._nodeListe.append(node)

    def getAntNoder(self):  #int    #hvor mange noder i rack
        return len(self._nodeListe)

    def antProsessorer(self): #int  #hvor mange prosessorer i rack
        totaleProsessorer = 0
        for node in self._nodeListe:
            totaleProsessorer += node.antProsessorer()
        return totaleProsessorer

    def noderMedNokMinne(self, paakrevdMinne):  #int #teller hvor mange noder
        noderMedNokMinne = 0                         #som er innen for et minste
        for node in self._nodeListe:                 #krav for minne
            noderMedNokMinne += node.nokMinne(paakrevdMinne)
        return noderMedNokMinne
