import re
import string


class Vigenere:

    def __init__(self, sMessage, sCode, sOverrideAlphabetWith=None, makeAllUppercase=True):
        if sOverrideAlphabetWith is None:
            sOverrideAlphabetWith = string.ascii_uppercase
        self._alphbt = list(sOverrideAlphabetWith * 2)

        pattern = re.compile(r'\s+')
        self._msgStr = re.sub(pattern, '', sMessage)
        self._encStr = re.sub(pattern, '', sCode)

        self._msgLen = len(self._msgStr)
        self._encStr = self._encStr * (self._msgLen // len(self._encStr) + 1)
        self._encStr = self._encStr[:self._msgLen]

        if makeAllUppercase:
            self._msgStr = self._msgStr.upper()
            self._encStr = self._encStr.upper()

    def encrypt(self):
        out = ""
        for i in range(self._msgLen):
            textRow = self._alphbt.index(self._msgStr[i])
            viginereRow = self._alphbt.index(self._encStr[i])
            out += self._alphbt[viginereRow + textRow]
        return out

    def decrypt(self):
        out = ""
        for i in range(self._msgLen):
            textRow = self._alphbt.index(self._encStr[i])
            viginereRow = self._alphbt.index(self._msgStr[i])
            out += self._alphbt[viginereRow - textRow]
        return out

    def encryptPrint(self):
        out = self.encrypt()
        print(f"Vigenère encrypt {self._msgStr}: {out}")

    def decryptPrint(self):
        out = self.decrypt()
        print(f"Vigenère decrypt {self._msgStr}: {out}")
