import numpy as np

from sampling import MySampling
from crossover import MyCrossover
from mutation import MyMutation
from duplicate import MyDuplicateElimination
from problemDefinition import MyProblem

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

# NSGA2 configuration
algorithm = NSGA2(pop_size=11,
                  sampling=MySampling(),
                  crossover=MyCrossover(),
                  mutation=MyMutation(),
                  eliminate_duplicates=MyDuplicateElimination())
# NSGA2 generation
res = minimize(MyProblem(),
               algorithm,
               ('n_gen', 100),
               seed=1,
               verbose=True)
# plotting
from pymoo.visualization.scatter import Scatter
Scatter().add(res.F).show()

# output result
results = res.X[np.argsort(res.F[:, 0])]
count = [np.sum([e == "a" for e in r]) for r in results[:, 0]]
print(np.column_stack([results, count]))
