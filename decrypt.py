from common import *
class Decryptor:

    def __init__(self, message, key):
        self.original_key = key
        self.original_message = message
        self.decrypt_message = self.decrypt(self.original_key)

    def decrypt(self, ct_hex):
        r = whitening(ct_hex, self.original_key)
        for i in range(15, -1, -1):
            r = self.round_function(r, i)

        p = [r[2], r[3], r[0], r[1]]
        p_hex = ""
        for pi in p:
            p_hex += format(pi, "04x")

        p = whitening(p_hex, self.original_key)
        p_str = ""
        for pi in p:
            p_str += format(pi, "04x")
        return p_str


    

