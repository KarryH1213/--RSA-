#-*-coding = utf-8 -*-
#@Time : 2022-11-03 14:50
#@Author : Karry
#@File : RSA_same_modulo.py
#@Software : PyCharm
from gmpy2 import *
import binascii
with open("Frame0","r") as fp:
    d=fp.read()
with open("Frame4",'r') as f2p:
    d2=f2p.read()

def Getparameters(d,bytes):
    N=d[0:bytes]
    e=d[bytes:bytes*2]
    c=d[bytes*2:bytes*3]
    return int(N,16),int(e,16),int(c,16)

def strhex2int(e):
    return int(e,16)

def extgcd(a,b):
    if a==0:
        return (b,0,1)
    else:
        g,y,x=extgcd(b%a,a)
        return (g,x-(b//a)*y,y)
#N1=d[0:256]
#N2=int(d2[0:256],16)
#e1=d[256:512]
#e2=d2[257:512]
#c1=d[512:768]
#c2=d2[513:768]
#print(extgcd(3,5))
# N1,e1,c1=Getparameters(d,256)
# N2,e2,c2=Getparameters(d2,256)
#print(e1)
# e1=strhex2int(e1)
# e2=strhex2int(e2)
#print(extgcd(e1,e2))
#print(hex(e1))
#print(gcd(e1,e2))
#print(N1+e1+c1==d)
#print(len(d))
#print(e1)
#print(N1,N2,N1-N2)
#print(d[0:int(1024/4)+1])
#print(d2[0:int(1024/4)+1])
#print(d)
#print(type(d))
if __name__ == '__main__':
    N1, e1, c1 = Getparameters(d, 256)
    N2, e2, c2 = Getparameters(d2, 256)

    g,x,y=extgcd(e1,e2)
    if x<0:
        x=abs(x)
        c1=invert(c1,N1)
    if y<0:
        y=abs(y)
        c2=invert(c2,N1)

    M=(powmod(c1,x,N1)*powmod(c2,y,N1))%N1
    #print(powmod(3,-2,5))
    #print(hex(M))
    M=hex(M)[-16:]
    #print(M)
    plaintext=binascii.unhexlify(M).decode()
    print(plaintext)
    #print(hex(M))

#reference:https://blog.csdn.net/sinat_40845893/article/details/103336054