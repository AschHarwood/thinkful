

def F(n):
    if n < 2:
        return n
    else:
    	print (n-2) + (n-1)
        return F(n-2) + F(n-1)

    

F(7)

