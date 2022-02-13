from .diffiehellman import DH


class ElGamal(DH):

    def sendPrint(self, nMessage):
        print(f"Message to encrypt: {nMessage}")
        encryptedMessageAlice = ((self.pubBob ** self.secretAlice) * nMessage) % self.mod
        encryptedMessageBob = ((self.pubAlice ** self.secretBob) * nMessage) % self.mod
        decryptedMessageAlice = encryptedMessageBob * (self.pubBob ** (self.mod - 1 - self.secretAlice)) % self.mod
        decryptedMessageBob = encryptedMessageAlice * (self.pubAlice ** (self.mod - 1 - self.secretBob)) % self.mod
        print(f"Encrypted Message Alice: {encryptedMessageAlice} - decrypted again: {decryptedMessageAlice}")
        print(f"Encrypted Message Bob: {encryptedMessageBob} - decrypted again: {decryptedMessageBob}")

    def __str__(self):
        return f"ElGamal (Generator: {self.gen}, Modulo Prime: {self.mod}): -------------\n" \
               f"Alice: Secret = {self.secretAlice}, Public = {self.pubAlice}\n" \
               f"Bob: Secret = {self.secretBob}, Public = {self.pubBob}\n" \
               f"SessionKey: {self.sessionKey}"
