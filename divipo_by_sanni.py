import galois
Rn = galois.GF(2**4)
n = 15
base = galois.Poly([1 if i in [n,0] else 0 for i in range(n+1)], field=Rn)
g = galois.Poly([1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1], field=Rn)
d = 8
a = galois.Poly([1,1,0,1,0,1,0,1,1,1,0,1,0,1], field=Rn, order="asc")

# Hamming weight of a polynomial
def weight(p):
    return sum([1 for c in p.coeffs if c != 0])

# Leading monomial of a polynomial
def leadmon(p:galois.Poly):
    m = [galois.Poly([1] + [0]*i, field=Rn) for i,\
    coef in enumerate(p.coeffs[::-1]) if coef != 0]
    return m[0]

# Division by increasing power order of x
def divipo(received: galois.Poly,generator: galois.Poly, distance:int):
    t = (distance - 1)//2
    r = received
    q = galois.Poly([0],field=Rn)
    i = 0
    while weight(r) > t and i < n:
        mg = leadmon(g)
        mr = leadmon(r)
        quot = mr // mg
        r += quot * g
        q += quot
        i += 1
    else:
        print('Maximum attempts reached without successful decoding.')
    return r, q

    
r, q = divipo(a,g,d)
print('The remainder is:',r)
q2, error = divmod(r, base)
print('The error is:',error)
word = a - error
print('The correct word is:', word)
