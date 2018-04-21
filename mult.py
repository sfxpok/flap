def mult(z,i,n):

    while True:

        z = z*i
        i += 1

        if z*i <= n:
            break

mult(1,2,4)