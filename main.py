import numpy
def prob(vec,n):
    norma=0
    for i in vec:
        norma+=abs(i)**2
    return ((abs(vec[n]**2)/norma))
def amplitud(vec1,vec):
    norm1=numpy.linalg.norm(vec)
    norm2=numpy.linalg.norm(vec1)
    for i in range(len(vec)):
        vec[i]=vec[i]*(1/norm1)
    for i in range(len(vec1)):
        vec1[i]=vec1[i]*(1/norm2)
    for i in range(len(vec)):
        vec[i]=vec[i].conjugate()
    resp=numpy.inner(vec,vec1)
    return resp
def prob_vec(vec1,vec):
    return (abs(amplitud(vec1,vec))**2)
def observable(mat,vec):
    mat2=numpy.matrix.H
    if mat2!=mat:
        raise Exception("Matriz no hermitiana")

print(amplitud([1,-1j],[1j,1]))