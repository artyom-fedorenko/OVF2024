
import numpy as np

def float_info(type):
    one = type(7)
    val = type(1)
    i, j = (0, 0)
    load = type(1)
    while(one + val != one):
        val /= type(2)
        i += 1
    while(load!=np.inf):
        load*=2
        j+=1
   
    print('machine eps = ', 2*val )
    print('M = ' , i-1 )
    print('power = ', np.log2(j)+1)



#def power():

def sum1(n):
    sum = 0
    for i in range(n):
        sum += (-1)**(i+1)/(i+1)
    return sum

# from small n to large

def sum2(n):
    sum = 0
    for i in range(n):
        sum += (-1)**(n-i)/(n-i)
    return sum        
#from large n to small


def sum3(n):
    s1, s2 = (0, 0)
    for i in range(n//2):
        s1 += (-1)**(2*i+1)/(2*i+1)
        s2 += (-1)**(2*i+2)/(2*i+2)
    sum = s1 + s2
    return(sum)

def sum4(n):
    s1, s2 = (0, 0)  
    for i in range(n//2):
        s1 += (-1)**(n-2*i)/(n-2*i)
        s2 += (-1)**(n-2*i-1)/(n-2*i-1)
        print((s1, s2))
    sum = s1 + s2
    return(sum)



print(sum1(1000), sum2(1000), sum3(1000), sum4(1000))

float_info(np.float32)
float_info(np.float64)

#1.0110*2**(-4)