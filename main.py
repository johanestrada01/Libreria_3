from math import sqrt
import numpy
def prob(vec,n):
    norma=0
    for i in vec:
        norma+=abs(i)**2
    return ((abs(vec[n]**2)/norma))
def prob_vec(vec,vec1):
    norm1=numpy.linalg.norm(vec)
    norm2=numpy.linalg.norm(vec1)
    for i in range(len(vec)):
        vec[i]=vec[i]*(1/norm1)
    for i in range(len(vec1)):
        vec1[i]=vec1[i]*(1/norm2)
    vec1=numpy.matrix.getH(vec)

    print(norm1)
prob_vec([1+2j,2+2j],[1+1j,1])

print(prob([(-3-1j),(-2j),(1j),(2)],2))