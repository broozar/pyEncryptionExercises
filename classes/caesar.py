import re
import string


class Caesar:

    def __init__(self, sMessage, sOverrideAlphabetWith=None, makeMessageUppercase=True):
        pattern = re.compile(r'\s+')
        self._msgStr = re.sub(pattern, '', sMessage)
        if makeMessageUppercase:
            self._msgStr = self._msgStr.upper()

        if sOverrideAlphabetWith is None:
            sOverrideAlphabetWith = string.ascii_uppercase
        self._alphbt = list(sOverrideAlphabetWith)
        self._lenAlphbt = len(self._alphbt)

    def encrypt(self, nTransposition):
        out = ""
        for letter in self._msgStr:
            out += self._alphbt[(self._alphbt.index(letter) + nTransposition) % self._lenAlphbt]
        return out

    def decrypt(self, nTransposition):
        out = ""
        for letter in self._msgStr:
            out += self._alphbt[(self._alphbt.index(letter) - nTransposition) % self._lenAlphbt]
        return out

    def encryptPrint(self, nTransposition):
        out = self.encrypt(nTransposition)
        print(f"Caesar encrypt {self._msgStr} ({nTransposition}): {out}")

    def decryptPrint(self, nTransposition):
        out = self.decrypt(nTransposition)
        print(f"Caesar decrypt {self._msgStr} ({nTransposition}): {out}")
