def integerSqrt (n):
    
    z = 1

    while True:
        z += 1

        if pow(z,2) > n: # z^2 > n?
            break
    
    print z

integerSqrt(10) # biggest natural number that does not exceed n