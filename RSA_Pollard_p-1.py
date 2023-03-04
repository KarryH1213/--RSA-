#-*-coding = utf-8 -*-
#@Time : 2022-11-05 22:02
#@Author : Karry
#@File : RSA_Pollard_p-1.py
#@Software : PyCharm
from gmpy2 import *
import binascii
def Pollard(N):
    a=b=2
    while True:
        a=powmod(a,b,N)
        d=gcd(a-1,N)
        if d!=1:
            return d
        b+=1

def Getparameters(d,bytes):
    N=d[0:bytes]
    e=d[bytes:bytes*2]
    c=d[bytes*2:bytes*3]
    return int(N,16),int(e,16),int(c,16)

def GetFiveN(p,q):
    return int((p-1)*(q-1))

if __name__ == '__main__':
    with open("Frame6", "r") as fp:#2,6,19
        d = fp.read()
    N1, e1, c1 = Getparameters(d, 256)
    p=Pollard(N1)
    FN1=GetFiveN(p,N1//p)

    d1 = invert(e1, FN1)
    M1 = hex(powmod(c1, d1, N1))[-16:]
    #print(type(M1))
    #print(M1)
    print("frame2:" + binascii.unhexlify(M1).decode())

# references:
# https://blog.csdn.net/weixin_46395886/article/details/114434642
# https://www.tr0y.wang/2017/11/06/CTFRSA/#数论知识