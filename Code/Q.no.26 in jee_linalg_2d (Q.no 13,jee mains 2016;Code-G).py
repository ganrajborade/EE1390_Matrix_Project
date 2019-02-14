import numpy as np
import matplotlib.pyplot as plt

#Finding the point P
A = np.linalg.inv(np.array([[1,-1],[7,-1]]))
B = np.array([-1,5])
P = np.matmul(A,B)
print("The coordinates of P in the matrix form is : ",P)
#Midpoint=M   
M = np.array([-1,-2])
#Finding the point R
R = 2*M - P

#Finding the point of intersection of PQ and QS

def dir_vec(AB):
    return np.matmul(AB,dvec)
def norm_vec(AB):
    return np.matmul(omat,np.matmul(AB,dvec))

PR = np.vstack((P,R)).T
dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])
m1 = dir_vec(PR)
m2 = np.array([7,-1])
X = np.vstack((m1,m2))
p = np.zeros(2)
p[0] = m1[0]*M[0] + m1[1]*M[1]
p[1] = m2[0]*P[0] + m2[1]*P[1]
Q = np.matmul(np.linalg.inv(X),p)
print("The coordinates of Q in the matrix form is : ",Q)

print("The coordinates of R in the matrix form is : ",R)

#Finding the point of intersection of PS and SR
MQ = np.vstack((M,Q)).T
n1 = norm_vec(MQ)
n2 = np.array([1,-1])
Y = np.vstack((n1,n2))
q = np.zeros(2)
q[0] = n1[0]*M[0] + n1[1]*M[1]
q[1] = n2[0]*P[0] + n2[1]*P[1]
S = np.matmul(np.linalg.inv(Y),q)
print("The coordinates of S in the matrix form is : ",S)


#Drawing the diagram:

len = 10
lam_1 = np.linspace(0,1,len)

x_PQ = np.zeros((2,10))
x_QR = np.zeros((2,10))
x_RS = np.zeros((2,10))
x_SP = np.zeros((2,10))
x_RP = np.zeros((2,10))
x_SQ = np.zeros((2,10))
for i in range(len):
    temp1 = P + lam_1[i]*(Q-P)
    x_PQ[:,i] = temp1.T
    temp2 = Q + lam_1[i]*(R-Q)
    x_QR[:,i] = temp2.T
    temp3 = R + lam_1[i]*(S-R)
    x_RS[:,i] = temp3.T
    temp4 = S + lam_1[i]*(P-S)
    x_SP[:,i] = temp4.T
    temp5 = P + lam_1[i]*(R-P)
    x_RP[:,i] = temp5.T
    temp6 = S + lam_1[i]*(Q-S)
    x_SQ[:,i] = temp6.T
    
    
plt.plot(x_PQ[0,:],x_PQ[1,:],label = '$PQ:[ 7 -1]x - 5 = 0$')
plt.plot(x_QR[0,:],x_QR[1,:],label = '$QR:[1 -1]x - 3 = 0$')
plt.plot(x_RS[0,:],x_RS[1,:],label = '$RS:[7 -1]x + 15 = 0$')
plt.plot(x_SP[0,:],x_SP[1,:],label = '$SP:[1 -1]x + 1 = 0$')
plt.plot(x_RP[0,:],x_RP[1,:],label = '$RP$')
plt.plot(x_SQ[0,:],x_SQ[1,:],label = '$SQ$')


plt.plot(P[0],P[1],'o')
plt.plot(Q[0],Q[1],'o')
plt.plot(R[0],R[1],'o')
plt.plot(S[0],S[1],'o')
plt.plot(M[0],M[1],'o')



plt.text(P[0]*(1+0.1),P[1]*(1-0.1),'P(1,2)')

plt.text(Q[0]*(1+0.1),Q[1]*(1),'Q(0.334,-2.667)')

plt.text(R[0]*(1-0.1),R[1]*(1),'R(-3,-6)')

plt.text(S[0]*(1+0.1),S[1]*(1-0.1),'S(-2.334,-1.334)')

plt.text(M[0]*(1+0.1),M[1]*(1-0.1),'M(-1,-2)')

plt.axis('equal')

plt.legend(loc ='best')

plt.xlim(-8,12)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()

plt.show()
