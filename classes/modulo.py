class Modulo:

    def __init__(self, nModulo):
        self._mod = nModulo
        self._len = len(str(self._mod))

    def table(self):
        out = []
        for i in range(1, self._mod):
            row = []
            for j in range(1, self._mod):
                row.append(j * i % self._mod)
            out.append(row)
        return out

    def inverse(self, nOf):
        for i in range(1, self._mod):
            res = nOf * i % self._mod
            if res == 1:
                return i

    def tablePrint(self):
        table = self.table()
        out = ""
        for row in table:
            column = ""
            for item in row:
                column += str(item).zfill(self._len) + " "
            out += column + "\n"

        print(f"Multiplication Table MOD {self._mod} --------------------")
        print(out)

    def inversePrint(self, nOf):
        inverse = str(self.inverse(nOf)).zfill(self._len)
        print(f"Inverse for {nOf} MOD {self._mod}: {inverse}")
