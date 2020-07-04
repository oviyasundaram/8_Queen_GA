import unittest
import Queen

class TestEightQueens(unittest.TestCase):

    def test_random_chromosome(self):
        c = Queen.Queen_challenge()
        value = c.random_chromosome()
        self.assertAlmostEqual(len(value), 8)

    def test_run(self):
        c = Queen.Queen_challenge()
        value = c.random_chromosome()
        fit = c.fitness(value)
        max_fit = c.probability(value,fit)
        population = value
        parent1 = population[0]
        parent2 = population[1]
        self.assertIn(parent1, population)
        self.assertIn(parent2, population)


    def test_result(self):
        c = Queen.Queen_challenge()
        c.run()
        result = c.res
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()