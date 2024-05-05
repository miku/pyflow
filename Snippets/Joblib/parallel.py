from joblib import Parallel, delayed

from math import sqrt

result = Parallel(n_jobs=4)(delayed(sqrt)(i**2) for i in range(100))
print(result)