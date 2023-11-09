from binascii import b2a_hex, a2b_hex

from Crypto.Cipher import AES


# Класс и отдельные функции, реализующие шифрование данных по алгоритму AES
class AESEncrypt:
    def __init__(self):
        self.mode = AES.MODE_CBC

    def set_key(self, key):
        self.key_len = len(key)
        if not self.key_len == 16:
            raise Exception('Limit exceed: 16 Bytes')
        self.key = key

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        count = len(text)
        add = self.key_len - (count % self.key_len)
        text = text + ('\0' * add)
        cipher_text = cryptor.encrypt(str.encode(text, 'utf-8'))
        return b2a_hex(cipher_text)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text.rstrip(b'\0'), 'utf-8')


c = AESEncrypt()


def init(key):
    c.set_key(key)
    return c


def encode(data):
    return c.encrypt(data)


def decode(data):
    return c.decrypt(data)
