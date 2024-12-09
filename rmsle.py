from pyspark.ml.evaluation import Evaluator
from math import sqrt
from operator import add
import pyspark.sql.functions as F

class RmsleEvaluator(Evaluator):

    def __init__(self,predictionCol='prediction', targetCol='label'):        
        super(RmsleEvaluator, self).__init__()
        self.predictionCol=predictionCol
        self.targetCol=targetCol
        
    def _evaluate(self, dataset, print_result=False):       
        error=self.rmsle(dataset,self.predictionCol,self.targetCol)
        if print_result:
            print ("Error: {}".format(error))
        return error
    
    def isLargerBetter(self):
        return False
    
    @staticmethod
    def rmsle(dataset,predictionCol,targetCol):
        return sqrt(dataset.select(F.avg((F.log1p(dataset[targetCol]) - F.log1p(dataset[predictionCol])) ** 2)).first()[0])

