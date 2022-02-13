class DH:

    def __init__(self, nGenerator, nPrimeModulo):
        self.gen = nGenerator
        self.mod = nPrimeModulo

        self.secretAlice = None
        self.secretBob = None
        self.pubAlice = None
        self.pubBob = None
        self.sessionKey = None

    def alice(self, nSecret):
        self.secretAlice = nSecret

    def bob(self, nSecret):
        self.secretBob = nSecret

    def publicKeys(self):
        self.pubAlice = (self.gen ** self.secretAlice) % self.mod
        self.pubBob = (self.gen ** self.secretBob) % self.mod

    def sessionKeys(self):
        sessionAlice = (self.pubBob ** self.secretAlice) % self.mod
        sessionBob = (self.pubAlice ** self.secretBob) % self.mod
        if (sessionAlice == sessionBob):
            self.sessionKey = sessionAlice
            return self.sessionKey
        else:
            raise Exception(f"Session key calculation error: {sessionAlice} != {sessionBob}")

    def __str__(self):
        return f"Diffie Hellman (Generator: {self.gen}, Modulo Prime: {self.mod}): -------------\n" \
               f"Alice: Secret = {self.secretAlice}, Public = {self.pubAlice}\n" \
               f"Bob: Secret = {self.secretBob}, Public = {self.pubBob}\n" \
               f"SessionKey: {self.sessionKey}"
