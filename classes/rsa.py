class RSA:

    def __init__(self, nPrime1, nPrime2, nPublicCoprime):
        self._p1 = nPrime1
        self._p2 = nPrime2
        self._pubCP = nPublicCoprime

        self._primeProduct = self._p1 * self._p2
        self.publicKey = (self._pubCP, self._primeProduct)

        self._eulerProduct = (self._p1 - 1) * (self._p2 - 1)
        for i in range(1, self._eulerProduct):
            res = self._pubCP * i % self._eulerProduct
            if res == 1:
                self._privCP = i
                self.privateKey = (self._privCP, self._primeProduct)
                break

    def sendPrint(self, nMessage):
        encrypted = (nMessage ** self._pubCP) % self._primeProduct
        decrypted = (encrypted ** self._privCP) % self._primeProduct
        print(f"Encrypted {nMessage}: {encrypted} - decrypted again: {decrypted}")
        decrypted = (nMessage ** self._privCP) % self._primeProduct
        encrypted = (decrypted ** self._pubCP) % self._primeProduct
        print(f"Signed {nMessage}: {decrypted} - unsigned again: {encrypted}")

    def __str__(self):
        return f"RSA ------------------------------------\n" \
               f"Prime Product: {self._p1} * {self._p2} = {self._primeProduct}\n" \
               f"Euler Product: {self._p1 - 1} * {self._p2 - 1} = {self._eulerProduct}\n" \
               f"Public Key (e, n): {self.publicKey}\n" \
               f"Private Key (d, n): {self.privateKey}"
