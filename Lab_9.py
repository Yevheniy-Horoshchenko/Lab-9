import numpy as np
from math import factorial
x = [0.115,0.120,0.125,0.130,0.135,0.140]
y = [8.6572,8.2932,7.9582,7.6489,7.3623,7.0961]
h = x[1] - x[0]
x1 = 0.116
x2 = 0.141
q = (x1 - x[0])/h
q2 = (x2-x[5])
mas = []
for i in range (len(y)):
    mas.append(y[i] - y[i-1])
mas.pop (0)
print(mas)
mas_1 = []
for j in range (len(mas)):
    mas_1.append(mas[j] - mas[j-1])
mas_1.pop (0)
print(mas_1)
mas_2 = []
for g in range (len(mas_1)):
    mas_2.append(mas_1[g] - mas_1[g-1])
mas_2.pop (0)
print(mas_2)
mas_3 = []
for l in range (len(mas_2)):
    mas_3.append(mas_2[l] - mas_2[l-1])
mas_3.pop (0)
print(mas_3)
mas_4 = []
for n in range (len(mas_3)):
    mas_4.append(mas_3[n] - mas_3[n-1])
mas_4.pop (0)
print(mas_4)
s_1 = y[0]+q*mas[0]+q*(q-1)*mas_1[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*mas_2[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*mas_3[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*0/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4
print(n_1)
s_5 = y[5]+q2*mas[4]+q*(q+1)*mas_1[3]/factorial(2)
s_6 = q*(q+1)*(q+2)*mas_2[2]/factorial(3)
s_7 = q*(q+1)*(q+2)*(q+3)*mas_3[1]/factorial(4)
s_8 = q*(q+1)*(q+2)*(q+3)*(q+4)*0/factorial(5)
n_2 = s_5 + s_6 + s_7 + s_8
print(n_2)
