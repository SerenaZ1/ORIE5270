import numpy as	np
from scipy.optimize import fmin_bfgs
import random


def rosen(x):
    """
    Compute rosenbrock function
    :param x: variables of rosenbrock function
    :return: (int)
    """
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:1])**2.0)

def rosen_gradient(x):
    """
    Compute the gradient of rosenbrock function
    :param x: variables of rosenbrock function
    :return: np.array(length(x))
    """
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    gradient = np.zeros_like(x)
    gradient[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    gradient[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    gradient[-1] = 200*(x[-1]-x[-2]**2)
    return gradient


if __name__ == '__main__':
    opt = []
    n = 3
    for i in range(10):
      x = [random.randint(-100, 100) for j in range(n)]
      opt.append(min(fmin_bfgs(rosen, x, fprime=rosen_gradient)))
    print (min(opt))
