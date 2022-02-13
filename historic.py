from classes.skytale import Skytale
from classes.caesar import Caesar
from classes.vigenere import Vigenere

if __name__ == '__main__':
    Skytale("an old greek cypher").encryptPrint(8)
    Skytale("aodrecpenlgekyhr").decryptPrint(8)

    print("")

    Caesar("Caesar Cypher").encryptPrint(10)
    Caesar("mkockbmizrob").decryptPrint(10)

    print("")

    Vigenere("A secret Message", "code").encryptPrint()
    Vigenere("cghgtswqggveis", "code").decryptPrint()
