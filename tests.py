import unittest

from conway import Conway


class ConwayTest(unittest.TestCase):
    sut = Conway()
    live_cell = (1, 2)
    dead_cell = (1, 0)

    # def test_get_state_returns_true_for_live_cell(self):
    #     self.assertTrue(self.sut.get_cell_state(self.live_cell))
    #
    # def test_get_state_returns_false_for_dead_cell(self):
    #     self.assertFalse(self.sut.get_cell_state(self.dead_cell))

    def test_get_list_of_neighbors_top_left(self):
        expected_neighbors = [
            (0, 1, False),
            (1, 0, False),
            (1, 1, False),
        ]
        actual_neighbors = self.sut.get_list_of_neighbors((0, 0))
        self.assertEqual(expected_neighbors, actual_neighbors)

    def test_get_list_of_neighbors_center(self):
        expected_neighbors = [
            (1, 2, True),
            (2, 2, False),
            (2, 1, False),
            (2, 0, False),
            (1, 0, False),
            (0, 0, False),
            (0, 1, False),
            (0, 2, False),
        ]
        actual_neighbors = self.sut.get_list_of_neighbors((1, 1))
        self.assertEqual(len(expected_neighbors), len(actual_neighbors))
        for expected_neighbor in expected_neighbors:
            self.assertIn(expected_neighbor, actual_neighbors)

    def test_get_count_of_live_neighbors_top_left(self):
        self.assertEqual(0, self.sut.get_live_neighbor_count((0, 0)))

    def test_get_count_of_live_neighbors_center(self):
        self.assertEqual(1, self.sut.get_live_neighbor_count((1, 1)))

    def test_rule_one(self):
        self.assertFalse(self.sut.determine_cell_life((0, 0)))

    def test_life_when_4_neighbors(self):
        self.sut.grid = [
            (0, 0, False), (0, 1, False), (0, 2, False),
            (1, 0, False), (1, 1, False), (1, 2, True),
            (2, 0, False), (2, 1, True), (2, 2, True),
        ]
        t = (1, 1)
        self.assertEqual(True, self.sut.determine_cell_life(t))
        self.sut.iterate()
        expected = '   \n xx\n xx'
        self.sut.iterate()
        actual = self.sut.get_grid()
        self.assertEqual(expected, actual)

    def test_life_when_1_neighbors(self):
        self.sut.grid = [
            (0, 0, False), (0, 1, False), (0, 2, False),
            (1, 0, False), (1, 1, False), (1, 2, True),
            (2, 0, False), (2, 1, False), (2, 2, False)
        ]
        self.sut.iterate()
        t = (1, 2)
        self.assertFalse(self.sut.determine_cell_life(t))
        expected = '   \n   \n   '
        actual = self.sut.get_grid()
        self.assertEqual(expected, actual)
