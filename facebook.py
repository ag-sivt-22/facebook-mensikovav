from collections import deque

class Facebook:
    def __init__(self):
        self.lidi = {}
        self.hrany = []
        self.pocet = 0
        self.vzdalenosti = {}
    def pridej_uzivatel(self, jmeno):
        self.lidi[jmeno]= self.pocet
        self.pocet += 1
        self.hrany.append([])
    def pridej_znamost(self, clovek1, clovek2):
        self.hrany[self.lidi[clovek1]].append(self.lidi[clovek2])
        self.hrany[self.lidi[clovek2]].append(self.lidi[clovek1])
        self.vzdalenosti={}
    def jak_daleko(self, name1, name2):
        vrchol1, vrchol2 = self.lidi[name1], self.lidi[name2]
        if (vrchol1, vrchol2) in self.vzdalenosti:
            return self.vzdalenosti[(vrchol1,vrchol2)]
        vzdalenosti = [-1]*self.pocet
        vzdalenosti[vrchol1]=0
        fronta = deque([vrchol1])
        while fronta: 
            vrchol = fronta.popleft()
            for soused in self.hrany[vrchol]:
                if vzdalenosti[soused] ==-1:
                    vzdalenosti[soused] = vzdalenosti[vrchol]+1
                    fronta.append(soused)
                if soused == vrchol2:
                    for i in range(len(vzdalenosti)):
                        if vzdalenosti[i] != -1:
                            self.vzdalenosti[(vrchol1, i)] = vzdalenosti[i]
                            self.vzdalenosti[(i, vrchol1)] = vzdalenosti[i]
                    return vzdalenosti[vrchol2]
        for i in range(len(vzdalenosti)):
            if vzdalenosti[i] != -1:
                self.vzdalenosti[(vrchol1, i)] = vzdalenosti[i]
                self.vzdalenosti[(i, vrchol1)] = vzdalenosti[i]
            else:
                self.vzdalenosti[(vrchol1, i)] = None
                self.vzdalenosti[(i, vrchol1)] = None
        return None
# Vytvoření instance Facebooku
fb = Facebook()

# Seznam unikátních jmen
jmena = [
    "Adam", "Beata", "Cyril", "Dana", "Emil", "František", "Gabriela", "Hana", "Ivan", "Jana",
    "Karel", "Lenka", "Marek", "Nina", "Ondřej", "Petra", "Quentin", "Radka", "Stanislav", "Tereza",
    "Urbán", "Veronika", "Walter", "Xenie", "Yvona", "Zdeněk", "Alex", "Blanka", "Cecilie", "David"
]

# Vkládání známostí do Facebooku
for jmeno in jmena:
    fb.pridej_uzivatel(jmeno)
  
# Hardkodované známosti
znamosti = [
    ("Adam", "Beata"), ("Adam", "Cyril"), ("Beata", "Dana"),
    ("Cyril", "Emil"), ("Cyril", "František"), ("Dana", "Gabriela"),
    ("Emil", "Hana"), ("František", "Ivan"), ("Gabriela", "Jana"),
    ("Hana", "Karel"), ("Ivan", "Lenka"), ("Jana", "Marek"),
    ("Karel", "Nina"), ("Lenka", "Ondřej"), ("Marek", "Petra"),
    ("Nina", "Quentin"), ("Ondřej", "Radka"), ("Petra", "Stanislav"),
    ("Quentin", "Tereza"), ("Radka", "Urbán"), ("Stanislav", "Veronika"),
    ("Tereza", "Walter"), ("Urbán", "Xenie"), ("Veronika", "Yvona"),
    ("Walter", "Zdeněk"), ("Xenie", "Alex"), ("Yvona", "Blanka"),
    ("Zdeněk", "Cecilie"), ("Alex", "David"), ("Blanka", "Adam")
]

# Vkládání známostí do Facebooku
for clovek1, clovek2 in znamosti:
    fb.pridej_znamost(clovek1, clovek2)
