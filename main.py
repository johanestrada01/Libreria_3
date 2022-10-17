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
def acc_mat_vec(mat,vec):
    fil=len(mat)
    new_vec=[0 for i in range(fil)]
    for i in range(len(mat)):
        valor=0
        for j in range(len(mat[i])):
            valor+=mat[i][j]*vec[j]
        new_vec[i]=valor
    return new_vec
def bra(vec):
    for i in range(len(vec)):
        vec[i]=vec[i].conjugate()
    return(vec)
def prod_int(vec1,vec2):
    salida=0
    for i in range(len(vec1)):
        vec1[i]=vec1[i].conjugate()
        salida+=vec1[i]*vec2[i]
    return salida
def prod_mat(mat1,mat2):
    n=len(mat1)
    m=len(mat2[0])
    prod=[[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            valor=0
            for k in range(len(mat2)):
                val1=mat2[k][j]
                val2=mat1[i][k]
                valor=val1*val2
            prod[i][j]=valor
    return prod
def observable(mat,vec):
    vec1=bra(vec)
    media=prod_int(acc_mat_vec(mat,vec),vec1)
    matriz=[[media*-1 for i in range(len(mat[0]))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            matriz[i][j]+=mat[i][j]
    matriz=prod_mat(matriz,matriz)
    var=prod_int(acc_mat_vec(matriz,vec),vec1)
    return var,media
def valores_propios(matriz):
    valores,vectores=numpy.linalg.eig(matriz)
    for i in range(len(vectores)):
        print(vectores[i],i)
    return vectores,vectores
print("ej1:")
vector=[1,0]
obs=[[0,1],[1,0]]
obs1=acc_mat_vec(obs,vector)
valores,vectores=valores_propios(obs)
print("Observacion",obs1)
print("valores:",valores)
print("vectores",vectores)
print("")
print("ej2:")
vector=[1,0]
obs=[[0,1],[1,0]]
valores,vectores=valores_propios(obs)
for i in vectores:
    print(prob_vec(i,vector))