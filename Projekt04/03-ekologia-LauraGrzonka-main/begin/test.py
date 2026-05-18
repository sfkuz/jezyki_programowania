import unittest
from World import World
from Position import Position
from Organisms.Lynx import Lynx
from Organisms.Antelope import Antelope
from Organisms.Sheep import Sheep


class TestSimulationEnvironment(unittest.TestCase):

    def setUp(self):
        self.world = World(10, 10)

    def test_lynx_creation_and_attributes(self):
        lynx = Lynx(position=Position(xPosition=5, yPosition=5), world=self.world)
        self.assertEqual(lynx.power, 6)
        self.assertEqual(lynx.initiative, 5)
        self.assertEqual(lynx.liveLength, 18)
        self.assertEqual(lynx.powerToReproduce, 14)
        self.assertEqual(lynx.sign, 'R')

    def test_antelope_fleeing_behavior(self):
        lynx = Lynx(position=Position(xPosition=2, yPosition=2), world=self.world)
        antelope = Antelope(position=Position(xPosition=3, yPosition=2), world=self.world)
        self.world.addOrganism(lynx)
        self.world.addOrganism(antelope)
        actions = antelope.move()
        move_action = actions[0]
        self.assertEqual(move_action.position.x, 5)
        self.assertEqual(move_action.position.y, 2)

    def test_antelope_attacking_behavior_when_cornered(self):
        lynx = Lynx(position=Position(xPosition=1, yPosition=0), world=self.world)
        antelope = Antelope(position=Position(xPosition=0, yPosition=0), world=self.world)
        self.world.addOrganism(lynx)
        self.world.addOrganism(antelope)
        actions = antelope.move()
        move_action = actions[0]
        self.assertEqual(move_action.position.x, 1)
        self.assertEqual(move_action.position.y, 0)

    def test_plague_activation(self):
        sheep = Sheep(position=Position(xPosition=5, yPosition=5), world=self.world)
        self.world.addOrganism(sheep)
        original_life = sheep.liveLength
        self.world.startPlague()
        self.assertEqual(sheep.liveLength, original_life // 2)
        self.assertEqual(self.world.plagueTurns, 2)

    def test_dynamic_organism_addition(self):
        sheep = Sheep(position=Position(xPosition=5, yPosition=5), world=self.world)
        success = self.world.addOrganismAtFreePosition(sheep)
        self.assertTrue(success)
        sheep2 = Sheep(position=Position(xPosition=5, yPosition=5), world=self.world)
        fail = self.world.addOrganismAtFreePosition(sheep2)
        self.assertFalse(fail)


if __name__ == '__main__':
    unittest.main()