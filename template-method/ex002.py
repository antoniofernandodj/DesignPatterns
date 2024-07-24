from abc import ABC, abstractmethod
from typing import Iterator


class GameAI(ABC):
    # O método template define o esqueleto de um algoritmo.
    built_structures: Iterator

    def turn(self):
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    # Alguns passos podem ser implementados diretamente na classe base.
    def collect_resources(self):
        print('Collecting')
        print(self.built_structures)
        for s in self.built_structures:
            print('collecting: ', s)
            s.collect()

    # E alguns deles podem ser definidos como abstratos.
    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def build_units(self):
        pass

    # Uma classe pode ter vários métodos template.
    def attack(self):
        print('Attacking')
        enemy = self.closest_enemy()
        if enemy is None:
            self.send_scouts(self.map_center())
        else:
            self.send_warriors(enemy.position)

    @abstractmethod
    def send_scouts(self, position):
        pass

    @abstractmethod
    def send_warriors(self, position):
        pass

    @abstractmethod
    def closest_enemy(self):
        pass

    @abstractmethod
    def map_center(self):
        pass


# Classes concretas precisam implementar todas as operações abstratas da
# classe base mas não devem sobrescrever o próprio método template.
class OrcsAI(GameAI):
    def build_structures(self):
        if self.there_are_some_resources():
            # Construir fazendas, depois quartéis, depois fortaleza.
            pass

    def build_units(self):
        if self.there_are_plenty_of_resources():
            if not self.scouts:
                # Construir peão, adicionar ao grupo de batedores.
                pass
            else:
                # Construir bruto, adicionar ao grupo de guerreiros.
                pass

    def send_scouts(self, position):
        if len(self.scouts) > 0:
            # Enviar batedores para a posição.
            pass

    def send_warriors(self, position):
        if len(self.warriors) > 5:
            # Enviar guerreiros para a posição.
            pass

    def closest_enemy(self):
        # Implementar lógica para encontrar o inimigo mais próximo.
        print('Gettings closest enemy...')
        return None

    def map_center(self):
        # Implementar lógica para obter o centro do mapa.
        print('Gettings map center...')
        return (0, 0)

    def there_are_some_resources(self):
        # Implementar lógica para verificar se há recursos.
        return True

    def there_are_plenty_of_resources(self):
        # Implementar lógica para verificar se há muitos recursos.
        return True

    @property
    def built_structures(self):
        # Devolver estruturas construídas.
        return []

    @property
    def scouts(self):
        # Devolver lista de batedores.
        return []

    @property
    def warriors(self):
        # Devolver lista de guerreiros.
        return []


# Subclasses também podem sobrescrever algumas operações com uma
# implementação padrão.
class MonstersAI(GameAI):
    def collect_resources(self):
        # Monstros não coletam recursos.
        pass

    def build_structures(self):
        # Monstros não constroem estruturas.
        pass

    def build_units(self):
        # Monstros não constroem unidades.
        pass

    def send_scouts(self, position):
        # Implementação específica para monstros enviar batedores.
        pass

    def send_warriors(self, position):
        # Implementação específica para monstros enviar guerreiros.
        pass

    def closest_enemy(self):
        # Implementar lógica para encontrar o inimigo mais próximo.
        return None

    def map_center(self):
        # Implementar lógica para obter o centro do mapa.
        return (0, 0)

    @property
    def built_structures(self):
        # Monstros não constroem estruturas, então retorna uma lista vazia.
        return []

    @property
    def scouts(self):
        # Devolver lista de batedores.
        return []

    @property
    def warriors(self):
        # Devolver lista de guerreiros.
        return []


if __name__ == "__main__":
    orcs = OrcsAI()
    orcs.turn()

    monsters = MonstersAI()
    monsters.turn()
