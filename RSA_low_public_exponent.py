#-*-coding = utf-8 -*-
#@Time : 2022-11-05 22:17
#@Author : Karry
#@File : RSA_low_public_exponent.py
#@Software : PyCharm
from gmpy2 import *
import binascii
def Getparameters(d,bytes):
    N=d[0:bytes]
    e=d[bytes:bytes*2]
    c=d[bytes*2:bytes*3]
    return int(N,16),int(e,16),int(c,16)

if __name__ == '__main__':
    with open("Frame3", "r") as fp:#3,8,12,16,20
        d1 = fp.read()
    N1, e1, c1 = Getparameters(d1, 256)
    with open("Frame8", "r") as fp:#3,8,12,16,20
        d2 = fp.read()
    N2, e2, c2 = Getparameters(d2, 256)
    with open("Frame12", "r") as fp:#3,8,12,16,20
        d3 = fp.read()
    N3, e3, c3 = Getparameters(d3, 256)
    with open("Frame16", "r") as fp:#3,8,12,16,20
        d4 = fp.read()
    N4, e4, c4 = Getparameters(d4, 256)
    with open("Frame20", "r") as fp:#3,8,12,16,20
        d5 = fp.read()
    N5, e5, c5 = Getparameters(d5, 256)
    M=N1*N2*N3*N4*N5
    M1,M2,M3,M4,M5=M//N1,M//N2,M//N3,M//N4,M//N5
    ANS=(c1*M1*invert(M1,N1)+c2*M2*invert(M2,N2)+c3*M3*invert(M3,N3)+c4*M4*invert(M4,N4)+c5*M5*invert(M5,N5))%M
    #print(e1)
    #d1 = invert(e1, FN1)
    #i=1
    # while 1:
    Mz,D=iroot(ANS,e1)
    #     #M1 = hex(M1)
    #     #print(D)
    #     if D:
    Mz = hex(Mz)
    #print(Mz)
    Mz = Mz[-16:]
    print("frame3,8,12,16,20:" + binascii.unhexlify(Mz).decode())
    #         break
    #     #print(M1)
    #     i+=1

# referece：
# https://www.tr0y.wang/2017/11/06/CTFRSA/#数论知识