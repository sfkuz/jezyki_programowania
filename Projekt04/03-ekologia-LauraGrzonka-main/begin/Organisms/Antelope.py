# ZADANIE 2
from .Animal import Animal
from Action import Action
from ActionEnum import ActionEnum
from Position import Position
import random


class Antelope(Animal):

    def __init__(self, antelope=None, position=None, world=None):
        super(Antelope, self).__init__(antelope, position, world)

    def clone(self):
        return Antelope(self, None, None)

    def initParams(self):
        self.power = 4
        self.initiative = 3
        self.liveLength = 11
        self.powerToReproduce = 5
        self.sign = 'A'

    def getNeighboringPosition(self):
        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

    def move(self):
        result = []
        adjacent_positions = self.world.getNeighboringPositions(self.position)
        lynx_pos = None
        lynx_org = None

        for pos in adjacent_positions:
            org = self.world.getOrganismFromPosition(pos)
            if org is not None and org.sign == 'R':
                lynx_pos = pos
                lynx_org = org
                break

        if lynx_pos:
            dx = self.position.x - lynx_pos.x
            dy = self.position.y - lynx_pos.y

            flee_pos = Position(xPosition=self.position.x + 2 * dx,
                                yPosition=self.position.y + 2 * dy)

            can_flee = False
            if self.world.positionOnBoard(flee_pos):
                if self.world.getOrganismFromPosition(flee_pos) is None:
                    can_flee = True

            if can_flee:
                result.append(Action(ActionEnum.A_MOVE, flee_pos, 0, self))
                self.lastPosition = self.position
            else:
                result.append(Action(ActionEnum.A_MOVE, lynx_pos, 0, self))
                self.lastPosition = self.position
                result.extend(lynx_org.consequences(self))
            return result

        pomPositions = self.getNeighboringPosition()
        newPosition = None

        if pomPositions:
            newPosition = random.choice(pomPositions)
            result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
            self.lastPosition = self.position
            metOrganism = self.world.getOrganismFromPosition(newPosition)
            if metOrganism is not None:
                result.extend(metOrganism.consequences(self))
        return result