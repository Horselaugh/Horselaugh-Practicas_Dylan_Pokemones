import copy
from abc import ABC, abstractmethod

class TypeCharacter(ABC):
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category

    @abstractmethod
    def create_character(self):
        pass

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.__class__.__name__}(ID: {self.id}, Nombre: {self.name}, Categoría: {self.category})"


class Entrenador(TypeCharacter):
    def __init__(self, id=None, name=None, category="Novato"):
        super().__init__(id=id, name=name, category=category)

    def create_character(self):
        print(f"Creando Entrenador: {self.name} con ID {self.id} y Categoría {self.category}")


class Pokemon(TypeCharacter):
    def __init__(self, id=None, name=None, category=None):
        super().__init__(id=id, name=name, category=category)

    def create_character(self):
        print(f"Creando Pokémon: {self.name} con ID {self.id} y Categoría {self.category}")


class RegistroCaptura: 
    def __init__(self, entrenador: Entrenador, pokemon: Pokemon):
        # Aseguramos que las instancias sean los tipos correctos
        if not isinstance(entrenador, Entrenador) or not isinstance(pokemon, Pokemon):
             raise TypeError("Ambos argumentos deben ser instancias de Entrenador y Pokemon.")
             
        self.entrenador = entrenador 
        self.pokemon = pokemon

    def describir_captura(self):
        print(f"{self.entrenador.name} (ID: {self.entrenador.id}) capturó a {self.pokemon.name} (Categoría: {self.pokemon.category})")