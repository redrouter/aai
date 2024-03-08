elt=['w','x','y','z']
A=[0.5,0.4,0.3,0.2]
B=[0.2,0.1,0.2,1]
U=[]
print("elements=",elt)
print("set A=",A)
print("set B=",B)
for i in range(0,4):
    if A[i]>B[i]:
        U.append(A[i])
    else:
        U.append(B[i])
print("Union")
for i in range(0,3):
    print(U[i] ,"/",elt[i],end=' + ')
    for i in range(3,4):
        print(U[i] ,"/",elt[i],end=' ')
        print()
I=[]
for i in range(0,4):
    if A[i]<B[i]:
        I.append(A[i])
    else:
        I.append(B[i])
print()
print("Intersection")
for i in range(0,3):
    print(I[i] ,"/",elt[i],end=' + ')
for i in range(3,4):
        print(I[i] ,"/",elt[i],end=' ')
print()
J=[]
K=[]
C=[1,1,1,1]
print()
print("Complement of A")
for i in range(0,4):
    J.append(C[i]-A[i]) 
    output=round(J[i],2)
for i in range(0,3): 
    print(J[i] ,"/",elt[i],end=' + ') 
for i in range(3,4): 
    print(J[i] ,"/",elt[i],end=' ') 
print()
print()

print("Complement of B") 
for i in range(0,4):
    K.append(C[i]-B[i])
for i in range(0,3):
    print(K[i] ,"/",elt[i],end=' + ')
for i in range(3,4):
    print(K[i] ,"/",elt[i],end=' ')
L=[]
M=[]
print()
for i in range(0,4):
    if A[i]<K[i]:
        L.append(A[i])
    else:
        L.append(K[i])
print()
print("Difference of A/B")
for i in range(0,3):
    print(L[i] ,"/",elt[i],end=' + ')
for i in range(3,4):
    print(L[i] ,"/",elt[i],end=' ')
for i in range(0,4):
    if B[i]<J[i]:
        M.append(A[i])
    else:
        M.append(J[i])
print()
print("Difference of B/A")
for i in range(0,3):
    print(M[i] ,"/",elt[i],end=' + ')
for i in range(3,4):
    print(M[i] ,"/",elt[i],end=' ')
print()
Sum=[]
Sum1=[]
print()
print("Sum of A and B")
for i in range(0,4):
    Sum.append(A[i]+B[i])
    output=round(Sum[i],2)
    Sum1.append(output)
for i in range(0,3):
    print(Sum1[i] ,"/",elt[i],end=' + ')
for i in range(3,4):
    print(Sum1[i] ,"/",elt[i],end=' ')
print()
Prod=[]
Prod1=[]






print()




print("Product of A and B")
for i in range(0,4):
    Prod.append(A[i]*B[i])
    output=round(Prod[i],2)
    Prod1.append(output)
for i in range(0,3):
    print(Prod1[i] ,"/",elt[i],end=' + ')
for i in range(3,4):
    print(Prod1[i] ,"/",elt[i],end=' ')
