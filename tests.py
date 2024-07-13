from unittest import TestCase

from game_state import GameState


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
