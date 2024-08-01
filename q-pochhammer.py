a = 0
q = 1/2
z = 0.222
#n = 1000000

def pochhammer(a,q,n):
    q_poch = 1
    for j in range(0,n):
        q_poch *= (1-a*q**j)
    return q_poch

#q-binomial theorem

def q_sum(a,q,z):
    sum_ = 0
    for i in range(0,1000):
        sum_ += pochhammer(a,q,i)/pochhammer(q,q,i)*z**i
    return sum_

def q_prod(a,q,z):
    prod = pochhammer(a*z,q,1000)/pochhammer(z,q,1000)
    return prod

print(q_sum(a,q,z), q_prod(a,q,z))
