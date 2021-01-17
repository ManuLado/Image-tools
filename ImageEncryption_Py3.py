#!/usr/bin/env python
# coding: utf-8




"""
Este programa encripta o desectripta una imagen "1.png" cuadrada de nxn pixeles y la guarda como "3.png";
Autor:Gerardo Manuel Lado, ladogerardomanuel@gmail.com
Uso: *al compilar pide los parametros (e) para encriptar y (d) para desencriptar
     *debe insertar una clave numerica entera (ej: 1234)
     *debe insertar un numero (s) de iteraciones, el optimo suele ser la mitad del tamaño 
      de la imagen 
     *para desencriptar la imagen, primero renombrarla como "1.png", este proceso tarda 
       algo mas

    
"""
import cv2
import math

def read_pgm_file(file_name):
    """
        Lee un archivo de imagen .pgm

    """
    img = cv2.imread(file_name,flags=cv2.IMREAD_GRAYSCALE)

    if img is not None:
        print('img.size: ', img.size)
    else:
        print('imread({0}) -> None')

    return img

img=read_pgm_file("1.png")
size=img.shape
w,h=img.shape

newarray=[]
i=0
for x in range(w):
    temp=[]
    for y in range(h):
        temp.append(0) 
        
        pxs=img[x,y]
        newarray.append(pxs)

print ("press e (encript) or d (decript)")
process=input()
print ("----inserte clave:")
k1=int(input())
print ("----inserte s(numero de iteraciones):")
s=int(input())

if process=="e" or process=="encript":
    angle=cv2.ROTATE_90_CLOCKWISE
if process=="d" or process=="decript":
    angle=cv2.ROTATE_90_COUNTERCLOCKWISE
    s=w-s


def f(x,n):
    f=abs(int(n*math.cos(x)))      #esta funcion se cambia a gusto
    return f



def key(n):                        #esto seria algo asi como el hash de la funcion f
    
   #f da un numero flotante que admite menos de 300 cifras, depende del procesador usado
    if n<300 or n==300:
        subkey= (f(k1,10**n))

    if n>300:
        loops=0          #esto arregla el problema pero hasta 600 cifras.
        while n>300:     #si quiero mas debo repetir este pedazo de codigo
            loops+=+1
            n+=-1
        if loops<300 or loops==300:
            
            subkey=int(str(f(k1,10**n))+str(f(k1,10**loops)))
        if loops>300:
            loops2=0
            while loops>300:
                loops2+=1
                loops+=-1
            subkey=int(str(f(k1,10**n))+str(f(k1,10**loops))+str(f(k1,10**loops2)))
    return subkey

keyw= [int(d) for d in str(key(w))]

keyh= [int(d) for d in str(key(h))]

#========================================================================        
def congru(a,c): #devuelve el numero mas bajo de la congruencia lineal
    for b in range(a):
        if ((a - b)%c)== 0 and b<c:
            return (b)

      
def cycl_perm_given_index(oldarray,dimens,subindex):  #permutaciones de filas en la imagen
    array=oldarray
    
    if dimens>subindex:
        index=subindex
    if dimens<subindex or dimens==subindex:
        index= congru(subindex,dimens)
    
    array=[oldarray[i - index] for i in range(dimens)]
           
    return  array

oldpipo=newarray

#s=numero de iteraciones. Define que tan destruida va a quedar la imagen(mientra mas grande mejor)

for p in range(s):
    for step in range(h):
        newarray[w*step:(step+1)*w]= cycl_perm_given_index(oldpipo[w*step:(step+1)*w],w,keyw[step])

    print ("progress:", int(100*p/(2*s)),"%" )
progress=p

##=======================================================================================
def storePixels(name, size, pxs):          #aca guardo la imagen
    w,h=size
    outImg =np.zeros((w,h,3), np.uint8)
    
    pxIter = iter(pxs)
    for x in range(w):
        for y in range(h):
            #outImg.putpixel((x, y), pxIter.next())
            outImg[x,y]=next(pxIter)
    cv2.imwrite(name,outImg,[cv2.IMWRITE_PXM_BINARY,0])


storePixels("2.png", size, newarray)  


#aca por vagancia en lugar de permutar columnas, roto la imagen y aplico el mismo procedimiento anterior

img2=read_pgm_file("2.png")   
rotated=cv2.rotate(img2, angle)
size=rotated.shape
h, w = size

newarray=[]
i=0
for x in range(h):
    temp=[]
    for y in range(w):
        temp.append(0) 
        
        pxs=rotated[x,y]
        newarray.append(pxs)
        
oldpipo=newarray

for p in range(s):
    for step in range(w):
        newarray[h*step:(step+1)*h]= cycl_perm_given_index(oldpipo[h*step:(step+1)*h],h,keyh[step])

    print ("progress:", int(100*(progress+p)/(2*s)),"%")


storePixels("3.png", size, newarray) 



if process=="e" or process=="encript":
    print ("FINALIZED----1.png fue cifrada correctamente como 3.png")
    
if process=="d" or process=="decript":
    print ("FINALIZED----1.png fue descifrada correctamente como 3.png")

    







