#HOLA CAMBIO REALIZADO
def suma(a,b):
    try:
        op1=int(a)
        op2=int(b)
        return op1+op2
    except:
        return None
def resta(a,b):
    try:
        op1=int(a)
        op2=int(b)
        return op1-op2
    except:
        return None
def multiplicacion(a,b):
    try:
        op1=int(a)
        op2=int(b)
        return op1*op2
    except:
        return None
def division(a,b):
    try:
        op1=int(a)
        op2=int(b)
        if op2==0:
            return None
        return op1/op2
    except:
        return None
r=suma('ghetr5',4)
r1=suma('75',4)
print(r,r1)