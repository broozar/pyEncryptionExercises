from classes.diffiehellman import DH
from classes.elgamal import ElGamal
from classes.rsa import RSA

if __name__ == '__main__':
    dh = DH(3, 7)
    dh.alice(5)
    dh.bob(3)
    dh.publicKeys()
    dh.sessionKeys()
    print(dh)

    print("")

    eg = ElGamal(7, 23)
    eg.alice(6)
    eg.bob(13)
    eg.publicKeys()
    eg.sessionKeys()
    print(eg)
    eg.sendPrint(17)

    print("")

    rsa = RSA(17, 31, 13)
    print(rsa)
    rsa.sendPrint(456)
