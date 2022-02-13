import re


class Skytale:

    def __init__(self, sMessage, makeMessageUppercase=True):
        pattern = re.compile(r'\s+')
        self._msgStr = re.sub(pattern, '', sMessage)
        if makeMessageUppercase:
            self._msgStr = self._msgStr.upper()
        self._msgList = list(self._msgStr)

    def _optimizeFor(self, nTransposition):
        nCols = len(self._msgStr) // nTransposition
        if len(self._msgStr) % nTransposition != 0:
            nCols += 1
        length = nCols * nTransposition

        optimizedString = list("_" * length)
        for pos, letter in enumerate(self._msgList):
            optimizedString[pos] = letter

        return optimizedString, nCols, length

    def encrypt(self, nTransposition):
        optimizedString, nCols, length = self._optimizeFor(nTransposition)
        out = list("_" * length)
        turn = 0
        rowCounter = 0
        for pos, letter in enumerate(out):
            if rowCounter < nCols:
                rowCounter += 1
            else:
                turn += 1
                rowCounter = 1
            marker = turn + (pos * nTransposition) % length
            out[marker] = optimizedString[pos]
        return "".join(out)

    def decrypt(self, nTransposition):
        optimizedString, nCols, length = self._optimizeFor(nTransposition)
        out = list("_" * length)
        turn = 0
        rowCounter = 0
        for pos, letter in enumerate(out):
            if rowCounter < nCols:
                rowCounter += 1
            else:
                turn += 1
                rowCounter = 1
            marker = turn + (pos * nTransposition) % length
            out[pos] = optimizedString[marker]
        return "".join(out)

    def encryptPrint(self, nTransposition):
        out = self.encrypt(nTransposition)
        print(f"Skytale encrypt {self._msgStr} ({nTransposition}): {out}")

    def decryptPrint(self, nTransposition):
        out = self.decrypt(nTransposition)
        print(f"Skytale decrypt {self._msgStr} ({nTransposition}): {out}")
