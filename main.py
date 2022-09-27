from math import sqrt
import numpy
def prob(vec,n):
    norma=0
    for i in vec:
        norma+=abs(i)**2
    return ((abs(vec[n]**2)/norma))
def prob_vec(vec,vec1):
    normvec1=vec/numpy.linalg.norm(vec)
    normvec2=vec1/numpy.linalg.norm(vec1)
    prod_inter=numpy.inner()
print(prob([(-3-1j),(-2j),(1j),(2)],2))