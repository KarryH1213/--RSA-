#-*-coding = utf-8 -*-
#@Time : 2022-11-03 18:45
#@Author : Karry
#@File : RSA_Fermat_factor.py
#@Software : PyCharm
from gmpy2 import *
import binascii
with open("Frame10","r") as fp:
    d=fp.read()

def Getparameters(d,bytes):
    N=d[0:bytes]
    e=d[bytes:bytes*2]
    c=d[bytes*2:bytes*3]
    return int(N,16),int(e,16),int(c,16)

def Fermat_factor(N):
    a=iroot(N,2)[0]+1
    while a<N:
        b=a*a-N
        if is_square(b):
            b=isqrt(b)
            break

        else:
            a=a+1
    return (a+b),abs(a-b)

def GetFiveN(p,q):
    return int((p-1)*(q-1))
if __name__ == '__main__':
    N1,e1,c1=Getparameters(d,256)
    p,q=Fermat_factor(N1)
    FN1=GetFiveN(p,q)

    d1=invert(e1,FN1)
    M1=hex(powmod(c1,d1,N1))[-16:]
    print("frame10:"+binascii.unhexlify(M1).decode())
    #print(p,q)
    #print(p*q==N1)

# references:
# https://blog.csdn.net/weixin_49267515/article/details/122391473
# https://blog.csdn.net/weixin_52111404/article/details/126984120
# https://www.tr0y.wang/2017/11/06/CTFRSA/#数论知识