class Node:
    def __init__(self, prosessorer, minne):
        self._antallProsessorer = prosessorer
        self._minne = minne

    def __str__(self):  #str
        mld = ["antall prosessorer:",
        str(self._antallProsessorer),"\n"   #returnerer antall prosessorer
        "minne:" , str(self._minne), "\n"]  #returnerer minne
        return ' '.join(mld)

    def antProsessorer(self):   #int
        return int(self._antallProsessorer) #returnerer bare antall minne


    def nokMinne(self, minne):  #int        #returnerer 1 eller 0 istedenfor
        if minne <= int(self._minne):       #bool, fordi det er simplere
            return 1                        #aritmetikk i rack
        else:
            return 0
