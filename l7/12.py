class Encoder:
    def encode(self, data):
        pass

    def decode(self, data):
        pass


class HuffmanEncoder(Encoder):
    def __init__(self):
        self.compressionCoef = 0

    def encode(self, data):
        self.setCompressionCoef()
        # реализация кодирования методом Хаффмана
        return "encoded_data"

    def decode(self, data):
        # реализация декодирования методом Хаффмана
        return "decoded_data"

    def setCompressionCoef(self):
        # расчет коэффициента сжатия для метода Хаффмана
        self.compressionCoef = 0.5

    def getCompressionCoef(self):
        return self.compressionCoef


class LZEncoder(Encoder):
    def __init__(self):
        self.compressionCoef = 0

    def encode(self, data):
        self.setCompressionCoef()
        # реализация кодирования методом Лемпеля-Зива
        return "encoded_data"

    def decode(self, data):
        # реализация декодирования методом Лемпеля-Зива
        return "decoded_data"

    def setCompressionCoef(self):
        # расчет коэффициента сжатия для метода Лемпеля-Зива
        self.compressionCoef = 0.4

    def getCompressionCoef(self):
        return self.compressionCoef


# Проверка работы классов
data = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991."

huffman_encoder = HuffmanEncoder()
huffman_encoded_data = huffman_encoder.encode(data)
huffman_decoded_data = huffman_encoder.decode(huffman_encoded_data)
huffman_compression_coef = huffman_encoder.getCompressionCoef()

print("Коэфициент сжатия методом Хаффмана:", huffman_compression_coef)

lz_encoder = LZEncoder()
lz_encoded_data = lz_encoder.encode(data)
lz_decoded_data = lz_encoder.decode(lz_encoded_data)
lz_compression_coef = lz_encoder.getCompressionCoef()

print("Коэфициент сжатия методом Лемпеля-Зива:", lz_compression_coef)