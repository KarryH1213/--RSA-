#-*-coding = utf-8 -*-
#@Time : 2022-11-03 17:42
#@Author : Karry
#@File : RSA_factor_collision.py
#@Software : PyCharm
from gmpy2 import *
import binascii
with open("Frame1","r") as fp:
    d=fp.read()
with open("Frame18",'r') as f2p:
    d2=f2p.read()

def Getparameters(d,bytes):
    N=d[0:bytes]
    e=d[bytes:bytes*2]
    c=d[bytes*2:bytes*3]
    return int(N,16),int(e,16),int(c,16)

def Factor(N1,N2):
    p=int(gcd(N1,N2))
    q1=(N1//p)
    q2=(N2//p)
    return p,q1,q2

def GetFiveN(p,q):
    return int((p-1)*(q-1))

if __name__ == '__main__':

    N1, e1, c1 = Getparameters(d, 256)
    N2, e2, c2 = Getparameters(d2, 256)
    p,q1,q2=Factor(N1,N2)
    # p=int(gcd(N1,N2))
    #print(type(p))
    #q1=int(N1)/int(p)
    #print(type(q1))
    # q2=int(N2/p)
    # print(type(q1),q2)
    #print(q1*p==N1)
    FN1=GetFiveN(q1,p)
    FN2=GetFiveN(q2,p)

    d1=invert(e1,FN1)
    d2=invert(e2,FN2)
    # #print(d1,d2)
    #
    M1=powmod(c1,d1,N1)
    M2=powmod(c2,d2,N2)
    M1=hex(M1)[-16:]
    M2=hex(M2)[-16:]
    #print(hex(M1),hex(M2))
    print("frame1:"+binascii.unhexlify(M1).decode())
    print("frame1:" + binascii.unhexlify(M2).decode())
#print(FN1,FN2)