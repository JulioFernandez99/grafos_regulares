
def calculo(aristas):
    m=2*aristas
    res=[]
    for i in range(1,m+1):
        div=m/i
        if div%1==0:
            res.append(div)

    res.reverse()
    cadena=""
    tam=len(res)

    for i in range(0,len(res)):
        trans=res[i]
        if i<tam-1:
            cadena+=str(trans)+" or "
        else:
            cadena+=str(trans)
    print(cadena)




calculo(25) #Ingresar el numero de aristas