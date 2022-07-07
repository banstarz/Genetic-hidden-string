import random

class Chromosome():

    def __init__(self, 
                genes = None, 
                original = 'привет мир!', 
                mutation_probability = 0.1):
        self.genes = genes
        self.original = original
        self.fitness = None
        self.chars = ' .?!абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.mutation_probability = mutation_probability
    
    def set_random_string(self):
        self.genes = random.choices(self.chars, k = len(self.original))
        self.genes = ''.join(self.genes)
 
    def calculate_fitness_function(self):
        if self.fitness == None:
            counter = 0
            for i in range(len(self.original)):
                if self.genes[i] == self.original[i]:
                    counter+=1
            self.fitness = counter/len(self.original)
        return self.fitness

    def cross_with(self, other):
        vec = [random.choice([0, 1]) for i in range(len(self.original))]
        ParentString = [self.genes, other.genes]
        string1 = ''.join([ParentString[vec[i]][i] for i in range(len(self.original))])
        string2 = ''.join([ParentString[not vec[i]][i] for i in range(len(self.original))])
        child1 = Chromosome(string1, self.original, self.mutation_probability)
        child2 = Chromosome(string2, self.original, self.mutation_probability)
        return (child1, child2)

    def mutate(self):
        for i in range(len(self.original)):
            if random.random() < self.mutation_probability:
                char = random.choice(self.chars)
                self.genes = self.genes[0:i] + char + self.genes[i+1:]