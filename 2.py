class Representative:
    def __init__(self, name, salary, establishments_visited=None):
        self.name = name
        self.salary = salary
        self.establishments_visited = establishments_visited or []
        
    def visit_establishment(self, establishment):
        self.establishments_visited.append(establishment.name)

    def __repr__(self):
        return f"Representative(name='{self.name}', salary={self.salary}, establishments_visited={self.establishments_visited})"

class Coordinator:
    def __init__(self, name, salary, region, representatives=None):
        self.name = name
        self.salary = salary
        self.region = region
        self.representatives = representatives or []
        
    def assign_representative(self, representative):
        if representative not in self.representatives:
            self.representatives.append(representative)
            
    def __repr__(self):
        return f"Coordinator(name='{self.name}', salary={self.salary}, region='{self.region}', representatives={self.representatives})"


class Establishment:
    def __init__(self, name, address, category, representatives_visited=None):
        self.name = name
        self.address = address
        self.category = category
        self.representatives_visited = representatives_visited or []
        
    def add_visit(self, representative):
        self.representatives_visited.append(representative.name)
    
    def __repr__(self):
        return f"Establishment(name='{self.name}', address='{self.address}', category='{self.category}')"



#Criando algumas instâncias de Establishment
est1 = Establishment("Restaurante do João", "Rua 1, nº 123", "Restaurante")
est2 = Establishment("Bar do Zé", "Rua 2, nº 456", "Bar")
est3 = Establishment("Cafeteria da Maria", "Rua 3, nº 789", "Cafeteria")

#Criando algumas instâncias de Representative
rep1 = Representative("João", 2000)
rep2 = Representative("Maria", 2500)
rep3 = Representative("José", 1800)

#Criando algumas instâncias de Coordinator
coord1 = Coordinator("Lucas", 3000, "Sul")
coord2 = Coordinator("Ana", 3500, "Norte")

#Atribuindo alguns representantes aos coordenadores
coord1.assign_representative(rep1)
coord1.assign_representative(rep3)
coord2.assign_representative(rep2)

#Adicionando visitas de representantes a estabelecimentos
est1.add_visit(rep1)
est1.add_visit(rep2)
est2.add_visit(rep3)
est3.add_visit(rep1)
est3.add_visit(rep2)
est3.add_visit(rep3)

#Imprimindo as informações de algumas instâncias criadas
print(rep1)
print(rep2)
print(coord1)
print(est3)