import unittest

from recommender import recommend


class RecommenderTests(unittest.TestCase):
    def test_known_movie_returns_recommendations(self):
        results = recommend("Avengers")
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        self.assertNotIn("Movie not found", results)

    def test_unknown_movie_returns_not_found(self):
        results = recommend("Some Unknown Movie")
        self.assertEqual(results, ["Movie not found"])


if __name__ == "__main__":
    unittest.main()
