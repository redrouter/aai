cardnumber=input("Enter number of Card")
cardcolor=input("Enter color of Card")
pofA = 4/52
pofB = 26/52
print("p(A)=>Probablility of drawing card with number",cardnumber,"=",round(pofA,2))
print("p(B)=>Probablility of drawing card with color ",cardcolor," =",round(pofB,2))
print("Joint Probablity of A and B=P(A) * P(B)")
pAandB= round(pofA*pofB, 2)
print("P(A and B)=",pAandB)
print("There are ",pAandB *100," % chances that of getting ",cardcolor, " card with number", cardnumber)
