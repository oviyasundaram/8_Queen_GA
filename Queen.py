import random
import numpy as np

class Queen_challenge():
    def random_chromosome(self):
        return [random.randint(1, 8) for _ in range(8)]

    def fitness(self,value):
        coll = 0
        row_col_coll = abs(len(value)) - abs(len(set(value)))
        coll += row_col_coll
        for i in range(len(value)):
            for j in range(i, len(value)):
                if (i != j):
                    x = abs(i - j)
                    y = abs(value[i] - value[j])
                    if (x == y):
                        coll += 1
        return 28 - coll

    def probability(self,value,fit):
        return fit / 28

    def pick(self, value, max_fit):
        valueWithmax_fit = zip(value, max_fit)
        total = sum(w for c, w in valueWithmax_fit)
        r = random.uniform(0, total)
        upto = 0
        for c, w in zip(value, max_fit):
            if upto + w >= r:
                return c
            upto += w
        assert False

    def reproduce(self,parent1, parent2):
        l = 8
        c = random.randint(0, l - 1)
        return (parent1[0:c] + parent2[c:l])

    def mutate(self,offspring):
        l = 8
        i = random.randint(0, l - 1)
        m = random.randint(1, l)
        offspring[i] = m
        return offspring

    def genetic_repeat(self,value, fit):
        mutation_probability = 0.03
        new_population = []
        max_fit= [self.probability(n, fit) for n in value]
        for i in range(len(value)):
            parent1 = self.pick(value,max_fit)
            parent2 = self.pick(value, max_fit)
            offspring = self.reproduce(parent1, parent2)
            new_parent = self.mutate(offspring)
            if random.random() < mutation_probability:
                new_parent = self.mutate(offspring)
            new_population.append(new_parent)
            if self.fitness(new_parent) == 28:
                break
        return new_population

    def run(self):
        value = self.random_chromosome()
        fit = self.fitness(value)
        max_fit = self.probability(value,fit)
        maxFitness = 28
        population = [self.random_chromosome() for _ in range(100)]
        generation = 1
        while not maxFitness in [self.fitness(chrom) for chrom in population]:
            population = self.genetic_repeat(population, fit)
            generation += 1
            chrom_out = []
        for chrom in population:
            if self.fitness(chrom) == maxFitness:
                chrom_out = chrom
                chr = ''
                for val in chrom:
                    val = val - 1
                    chr = chr + ' ' + str(val)
                self.res = chr[1:16]
                #self.result = chr[1:]
                break
if __name__ == '__main__':
    q = Queen_challenge()
    q.run()
    final_result = q.res
    print(final_result)