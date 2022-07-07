import random
from chromosome import Chromosome

class GeneticAlgorithm():

    def __init__(self, 
                population_size = 200, 
                mutation_probability = 0.1, 
                max_generation = 200, 
                Elite = 15, 
                original = 'привет мир!'):
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.max_generation = max_generation
        self.original = original                
        self.population = []
        self.Elite = Elite
        self.ChildList = [0 for i in range(2*self.population_size)]
        self.weights = []
        
    def run(self):
        self.initialize_population()
        self.evaluate_fitness_for_each_chromosome_in(self.population)
        for i in range(self.max_generation):
            self.evaluate_selection_weights()
            self.CrossOver()
            self.Mutation()
            self.NextGen()
            if self.population[0].genes == self.original:
                print(self.population[0].genes)
                break
            if i % 100 == 0:
                print(self.population[0].genes)
                
    def initialize_population(self):
        self.population = [Chromosome(original = self.original, 
                                        mutation_probability = self.mutation_probability)
                           for i in range(self.population_size)]
        for i in range(self.population_size):
            self.population[i].set_random_string()
    
    def evaluate_fitness_for_each_chromosome_in(self, population):
        for i in range(len(population)):
            population[i].calculate_fitness_function()
    
    def evaluate_selection_weights(self):
        total_population_fitness = 0
        self.weights = []
        total_population_fitness = sum([chromosome.calculate_fitness_function() for chromosome in self.population])
        for chromosome in self.population:
            self.weights.append(chromosome.calculate_fitness_function()/total_population_fitness)

    def CrossOver(self):
        for i in range(self.population_size):
            parent1, parent2 = self.Selection()
            child1, child2 = parent1.cross_with(parent2)
            self.ChildList[i] = child1
            self.ChildList[i + self.population_size] = child2
            
    def Selection(self):
        parent1, parent2 = random.choices(self.population, weights = self.weights, k=2)
        return (parent1, parent2)
            
    def Mutation(self):
        for i in range(len(self.ChildList)):
            self.ChildList[i].mutate()
    
    def NextGen(self):
        sorted(self.population, key = lambda x: x.calculate_fitness_function(), reverse = True)
        sorted(self.ChildList, key = lambda x: x.calculate_fitness_function(), reverse = True)
        j=0
        for i in range(self.Elite):
            if self.population[i].calculate_fitness_function() <= self.ChildList[j].calculate_fitness_function():
                self.population[i] = self.ChildList[j]
                j+=1
        for i in range(self.Elite, self.population_size):
            self.population[i] = self.ChildList[j]
            j+=1