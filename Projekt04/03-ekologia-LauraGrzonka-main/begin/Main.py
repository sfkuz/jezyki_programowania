from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
import os
import importlib

# ZADANIE 4
if __name__ == '__main__':
    pyWorld = World(10, 10)

    pyWorld.addOrganism(Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld))
    pyWorld.addOrganism(Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld))
    pyWorld.addOrganism(Sheep(position=Position(xPosition=2, yPosition=2), world=pyWorld))

    print(pyWorld)

    while pyWorld.turn < 50:
        cmd_input = input(
            '\n[Enter] = Nastepna tura | "plague" = Plaga | "add [Nazwa] [x] [y]" = Dodaj | "q" = Wyjdz:\n').strip().split()

        if not cmd_input:
            os.system('cls' if os.name == 'nt' else 'clear')
            pyWorld.makeTurn()
            print(pyWorld)

        elif cmd_input[0].lower() == 'q':
            break

        elif cmd_input[0].lower() == 'plague':
            pyWorld.startPlague()
            print("--- PLAGA ZOSTALA AKTYWOWANA ---")
            print(pyWorld)

        elif cmd_input[0].lower() == 'add' and len(cmd_input) == 4:
            cls_name = cmd_input[1]
            try:
                x, y = int(cmd_input[2]), int(cmd_input[3])
                module = importlib.import_module(f"Organisms.{cls_name}")
                cls = getattr(module, cls_name)
                new_org = cls(position=Position(xPosition=x, yPosition=y), world=pyWorld)

                if pyWorld.addOrganismAtFreePosition(new_org):
                    print(f"Dodano {cls_name} na pozycje ({x}, {y})")
                else:
                    print("Blad: pole poza plansza lub jest zajete.")
            except Exception as e:
                print(f"Blad dodawania organizmu (Sprawdz nazwe, np. Lynx, Antelope, Sheep): {e}")
            print(pyWorld)
        else:
            print("Nieznana komenda.")