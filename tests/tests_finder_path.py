from main import finder_path
import unittest


class TestGraph(unittest.TestCase):
    def test_get_tuple(self):
        get_tuple = finder_path.Graph.tuple(2, 3)
        self.assertEqual(get_tuple, (2, 3))

    def test_build_graph(self):
        graph = finder_path.Graph.build_graph(3, 3, [1, 2, 3, 1, 2, 3, 1, 2, 3])
        self.assertEqual(
            graph,
            {
                (0, 0): 1,
                (1, 0): 1,
                (2, 0): 1,
                (0, 1): 2,
                (1, 1): 2,
                (2, 1): 2,
                (0, 2): 3,
                (1, 2): 3,
                (2, 2): 3,
            },
        )


class TestPeaks(unittest.TestCase):
    graph = {
        (0, 0): 1,
        (1, 0): 3,
        (2, 0): 2,
        (0, 1): 1,
        (1, 1): 3,
        (2, 1): 1,
        (0, 2): 7,
        (1, 2): 2,
        (2, 2): 3,
    }

    def test_find_peak(self):
        peak = finder_path.Peaks.find_peak(self.graph)
        self.assertEqual(peak, (0, 2))


class TestBottom(unittest.TestCase):
    graph = {
        (0, 0): 1,
        (1, 0): 3,
        (2, 0): 2,
        (0, 1): 2,
        (1, 1): 3,
        (2, 1): 7,
        (0, 2): 2,
        (1, 2): 11,
        (2, 2): 3,
    }

    def test_find_bottom(self):
        bottom = finder_path.Bottom.find_bottom(self.graph)
        self.assertEqual(bottom, (0, 0))


if __name__ == "__main__":
    unittest.main()
