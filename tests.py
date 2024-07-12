from unittest import TestCase

from cell import Cell
from game_state import GameState
from generation import Generation


class GameStateTests(TestCase):
    def test__field_size_to_coordinates(self):
        self.assertEqual([0], GameState.field_size_to_coordinates(1))
        self.assertEqual([-1, 0], GameState.field_size_to_coordinates(2))
        self.assertEqual([-1, 0, 1], GameState.field_size_to_coordinates(3))
        self.assertEqual([-2, -1, 0, 1], GameState.field_size_to_coordinates(4))
        self.assertEqual([-2, -1, 0, 1, 2], GameState.field_size_to_coordinates(5))
        self.assertEqual([-3, -2, -1, 0, 1, 2], GameState.field_size_to_coordinates(6))
        self.assertEqual([-3, -2, -1, 0, 1, 2, 3], GameState.field_size_to_coordinates(7))

        with self.assertRaises(AssertionError):
            GameState.field_size_to_coordinates(0)
            GameState.field_size_to_coordinates(-1)


class CellTests(TestCase):
    def test__get_neighbors(self):
        cell = Cell(0, 0)
        neighbors = cell.get_neighbors()

        # top left
        self.assertTrue(Cell(-1, -1) in neighbors)
        # top middle
        self.assertTrue(Cell(0, -1) in neighbors)
        # top right
        self.assertTrue(Cell(1, -1) in neighbors)

        # left
        self.assertTrue(Cell(-1, 0) in neighbors)
        # right
        self.assertTrue(Cell(1, 0) in neighbors)

        # bottom left
        self.assertTrue(Cell(-1, 1) in neighbors)
        # bottom middle
        self.assertTrue(Cell(0, 1) in neighbors)
        # bottom right
        self.assertTrue(Cell(1, 1) in neighbors)


class GenerationTests(TestCase):
    def test__first_gen(self):
        generation = Generation({
            Cell(-2, 0), Cell(-1, 0), Cell(0, 0), Cell(1, 0), Cell(2, 0)
        })
        next_generation = generation.calculate_next_generation()

        expected_next_generation = Generation({
            Cell(-1, -1), Cell(0, -1), Cell(1, -1),
            Cell(-1, 0), Cell(0, 0), Cell(1, 0),
            Cell(-1, 1), Cell(0, 1), Cell(1, 1)
        })
        self.assertEqual(expected_next_generation, next_generation)

    def test__second_gen(self):
        generation = Generation({
            Cell(-1, -1), Cell(0, -1), Cell(1, -1),
            Cell(-1, 0), Cell(0, 0), Cell(1, 0),
            Cell(-1, 1), Cell(0, 1), Cell(1, 1)
        })
        next_generation = generation.calculate_next_generation()

        expected_next_generation = Generation({
            Cell(0, -2),
            Cell(-1, -1), Cell(1, -1),
            Cell(-2, 0), Cell(2, 0),
            Cell(-1, 1), Cell(1, 1),
            Cell(0, 2)
        })
        self.assertEqual(expected_next_generation, next_generation)
