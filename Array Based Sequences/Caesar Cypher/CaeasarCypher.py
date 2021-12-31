class CaesarCypher:
    """Implementation of the Caesar Cypher Cryptography Algorithm as a python class"""

    def __init__(self, shift):
        """Shift is the number of times letters are shifted to the right"""
        encode = [None] * 26                                          # initialize the encoded list
        decode = [None] * 26                                          # initialize the decoded list

        for i in range(26):
            encode[i] = chr((i + shift) % 26 + ord('A'))
            decode[i] = chr((i - shift) % 26 + ord('A'))

        self._encoded_string = ''.join(encode)                             # string version of the lists
        self._decoded_string = ''.join(decode)                             # prevent editing of the lists

    def encrypt(self, message):
        """Return encrypted string of the message"""

        return self._transform(message, self._encoded_string)

    def decrypt(self, secret):
        """Return decrypted string of the secret"""
        return self._transform(secret, self._decoded_string)

    def _transform(self, original, reference_string):
        """Utility to transform given string to another string using given list. Returns list"""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')                                 # find index from 0 to 25
                msg[k] = reference_string[j]                               # replace this character

        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCypher(3)
    message = 'THE EAGLES HAVE LANDED'
    coded = cipher.encrypt(message)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print("Message: ", answer)
