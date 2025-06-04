def checkif8(x):
    if(x==0):
        return False
    else:
        while(x % 8==0):
            x=x/8
    return (x==1)
print(checkif8(8))
