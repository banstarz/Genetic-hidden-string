import random

class Chromosome():
    def __init__(self, string = None, original = 'привет мир!', threshold = 0.9):
        self.string = string
        self.original = original
        self.fitness = None
        self.chars = ' .?!абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.threshold = threshold
    
    def RandomInit(self):
        self.string = random.choices(self.chars, k = len(self.original))
        self.string = ''.join(self.string)
 
    def FitnessFunction(self):
        if self.fitness == None:
            counter = 0
            for i in range(len(self.original)):
                if self.string[i] == self.original[i]:
                    counter+=1
            self.fitness = counter/len(self.original)
        return self.fitness

    def Crossing(self, other):
        vec = [random.choice([0, 1]) for i in range(len(self.original))]
        ParentString = [self.string, other.string]
        string1 = ''.join([ParentString[vec[i]][i] for i in range(len(self.original))])
        string2 = ''.join([ParentString[not vec[i]][i] for i in range(len(self.original))])
        child1 = Chromosome(string1, self.original, self.threshold)
        child2 = Chromosome(string2, self.original, self.threshold)
        return (child1, child2)
    
    def Changeover(self):
        for i in range(len(self.original)):
            if random.random() > self.threshold:
                char = random.choice(self.chars)
                self.string = self.string[0:i] + char + self.string[i+1:]