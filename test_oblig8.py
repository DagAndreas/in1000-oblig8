from datasenter import Datasenter
from regneklynge import Regneklynge
from rack import Rack
from node import Node

def hovedprogram():
    print("tester Node")
    node1 = Node(2,16)
    node2 = Node(1,100)

    assert(node1.antProsessorer() == 2)
    assert(node2.antProsessorer() == 1)
    assert(node1.antProsessorer() != 16)

    assert(node1.nokMinne(8) == True)       #true
    assert(not node1.nokMinne(32) == True)  #true
    assert(node2.nokMinne(100) == True)     #true
    assert(not node2.nokMinne(101) == True) #true

    print("printer node1:")
    print(str(node1))
    print("printer node2")
    print(str(node2))


    print("tester Rack")
    rack1 = Rack()
    rack1.settInn(node1)
    rack1.settInn(node2)
    assert(rack1.getAntNoder() == 2)         #tester metoder i Rack-klassen
    assert(rack1.antProsessorer() == 3)
    assert(rack1.noderMedNokMinne(16) == 2)
    assert(not rack1.noderMedNokMinne(100) == 2)
    print("printer info om rack1")
    print(rack1)
    print()



    print("tester Regneklynge")
    regneklynge1 = Regneklynge(2)           #lager ny regneklynge
    regneklynge1.settInnNode(node1)         #tester metoden "settInnNode"
    regneklynge1.settInnNode(node2)
    assert(regneklynge1.antProsessorer() == 3)
    assert(not regneklynge1.antProsessorer() == 2)
    assert(regneklynge1.totaleNoder() == 2)

    node3 = Node(2,8)                       #lager ny node
    regneklynge1.settInnNode(node3)
    assert(regneklynge1.totaleNoder() == 3) #tester om totaleNoder oppdateres
    print(regneklynge1.nodeMinneStandard())
    assert(regneklynge1.noderMedNokMinne(16) == 2)
    assert(regneklynge1.noderMedNokMinne(4) == 3)
    assert(regneklynge1.noderMedNokMinne(256) == 0)
    assert(regneklynge1.antRacks() == 2)
    print(str(regneklynge1))
    print()



    print("tester Datasenter")
    datasenter = Datasenter()
    datasenter.lesInnRegneklynge("abel.txt")
    assert(datasenter.overGrense(32)==666)
    assert(datasenter.overGrense(64)==666)
    assert(datasenter.overGrense(128)==16)
    assert(not datasenter.overGrense(18) == 16)
    assert(datasenter.lesProsessorerIKlynger() == 682)
    print("tester informasjon om abel.txt")
    print(datasenter.skrivUtRegneklynge("abel.txt"))

    print()
    datasenter.lesInnRegneklynge("saga.txt")
    print(datasenter.skrivUtAlleRegneklynger())

hovedprogram()
