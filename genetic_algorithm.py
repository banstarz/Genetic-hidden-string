import random
from chromosome import Chromosome

class GeneticAlgorithm():
    def __init__(self, PopulationSize = 200, threshold = 0.9, 
        GenBound = 200, Elite = 15, original = 'привет мир!'):
        self.PopulationSize = PopulationSize
        self.threshold = threshold
        self.GenBound = GenBound
        self.original = original                
        self.Population = []
        self.Elite = Elite
        self.ChildList = [0 for i in range(2*self.PopulationSize)]
        self.GenNum = 0
        self.Weights = []
        
        
    def Process(self):
        if not self.Population:
            self.StartPopulationInit()
        self.EvalFF(self.Population)
        for i in range(self.GenBound):
            self.EvalWeights()
            self.CrossOver()
            self.Mutation()
            self.NextGen()
            self.GenNum += 1
            if self.Population[0].string == self.original:
                print(self.Population[0].string)
                break
            if i%100 == 0:
                print(self.Population[0].string)
                
    def StartPopulationInit(self):
        self.Population = [Chromosome(original = self.original, threshold = self.threshold)
                           for i in range(self.PopulationSize)]
        for i in range(self.PopulationSize):
            self.Population[i].RandomInit()
    
    def EvalFF(self, Population):
        for i in range(len(Population)):
            Population[i].FitnessFunction()
    
    def EvalWeights(self):
        PopSumFF = 0
        self.Weights = []
        PopSumFF = sum([self.Population[i].FitnessFunction() for i in range(self.PopulationSize)])
        for i in range(self.PopulationSize):
            self.Weights.append(self.Population[i].FitnessFunction()/PopSumFF)
            
    def Selection(self):
        parent1, parent2 = random.choices(self.Population, weights = self.Weights, k=2)
        return (parent1, parent2)

    def CrossOver(self):
        for i in range(self.PopulationSize):
            parent1, parent2 = self.Selection()
            child1, child2 = parent1.Crossing(parent2)
            self.ChildList[i] = child1
            self.ChildList[i + self.PopulationSize] = child2
            
    def Mutation(self):
        for i in range(len(self.ChildList)):
            self.ChildList[i].Changeover()
    
    def NextGen(self):
        sorted(self.Population, key = lambda x: x.FitnessFunction(), reverse = True)
        sorted(self.ChildList, key = lambda x: x.FitnessFunction(), reverse = True)
        j=0
        for i in range(self.Elite):
            if self.Population[i].FitnessFunction() <= self.ChildList[j].FitnessFunction():
                self.Population[i] = self.ChildList[j]
                j+=1
        for i in range(self.Elite, self.PopulationSize):
            self.Population[i] = self.ChildList[j]
            j+=1