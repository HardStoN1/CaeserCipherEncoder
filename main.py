class Encoder:
    def __init__(self, depth=10):
        self.depth = depth
        self.abc = abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v','w','x','y','z']
    
    def encrypt(self, raw, key):
        raw = raw.lower()
        encrypted=""
        for c in raw:
            try:
                nc = self.abc[self.abc.index(c) + key]
                encrypted += nc
            except: 
                encrypted += c 
                pass # A number

        return encrypted
    
    def decrypt(self, encrypted):
        encrypted = encrypted.lower()
        answers = []
        decrypted = ""
        for key in range(self.depth):
            for c in encrypted:
                try:
                    nc = self.abc[self.abc.index(c) - key]
                    decrypted += nc
                except: 
                    decrypted += c 
                    pass # A number
            answers.append("[Key: {0}] {1}".format(key, decrypted))
            decrypted = ""
        
        return answers

if __name__ == "__main__":
    encoder = Encoder()
    answers = encoder.decrypt("vriw1zduh")
    print(answers)

