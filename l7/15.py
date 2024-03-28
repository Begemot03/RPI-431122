class HammingEncoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits
        self.controlBits = 0
        while 2 ** self.controlBits < self.dataBits + self.controlBits + 1:
            self.controlBits += 1

    def encode(self, binary_str):
        data = list(binary_str)
        encoded_data = ['0'] * (self.dataBits + self.controlBits)

        j = 0
        for i in range(self.dataBits + self.controlBits):
            if i + 1 == 2 ** j:
                encoded_data[i] = '0'
                j += 1
            else:
                encoded_data[i] = data.pop(0)

        for i in range(self.controlBits):
            parity_bit = 0
            for j in range(2 ** i - 1, self.dataBits + self.controlBits, 2 ** (i + 1)):
                for k in range(2 ** i):
                    if j + k < self.dataBits + self.controlBits:
                        parity_bit ^= int(encoded_data[j + k])
            encoded_data[2 ** i - 1] = str(parity_bit)

        return ''.join(encoded_data)

    def decode(self, encoded_str):
        encoded_data = list(encoded_str)
        error_index = 0

        for i in range(self.controlBits):
            parity_bit = 0
            for j in range(2 ** i - 1, len(encoded_data), 2 ** (i + 1)):
                for k in range(2 ** i):
                    if j + k < len(encoded_data):
                        parity_bit ^= int(encoded_data[j + k])
            if parity_bit != 0:
                error_index += 2 ** i

        if error_index != 0:
            encoded_data[error_index - 1] = str(int(not int(encoded_data[error_index - 1])))

        decoded_data = []
        j = 0
        for i in range(len(encoded_data)):
            if i + 1 != 2 ** j:
                decoded_data.append(encoded_data[i])
            else:
                j += 1

        return ''.join(decoded_data)


# Пример использования класса HammingEncoder
hamming_encoder = HammingEncoder(4)
binary_input = "1010"
encoded_output = hamming_encoder.encode(binary_input)
print("Закодированная строка:", encoded_output)

# Имитация ошибки в переданном закодированном сообщении
encoded_input_with_error = "100101"
decoded_output = hamming_encoder.decode(encoded_input_with_error)
print("Декодированная строка:", decoded_output)