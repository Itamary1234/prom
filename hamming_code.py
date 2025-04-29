from CONSTANTS import *
import reedsolo

def hamming_7_4_encode(data_bits):
    '''

    :param data_bits:
    :return: 7 bits of the message and the hamming code
    '''
    if len(data_bits) != 4:
        raise ValueError("Data must be 4 bits long.")

    # Calculate parity bits
    p1 = data_bits[0] ^ data_bits[1] ^ data_bits[3]
    p2 = data_bits[0] ^ data_bits[2] ^ data_bits[3]
    p3 = data_bits[1] ^ data_bits[2] ^ data_bits[3]

    # Return the 7-bit encoded message
    return [p1, p2, data_bits[0], p3, data_bits[1], data_bits[2], data_bits[3]]


def hamming_7_4_decode(encoded_bits):
    if len(encoded_bits) != 7:
        raise ValueError("Encoded message must be 7 bits long.")
        # Extract parity bits
    p1, p2, d1, p3, d2, d3, d4 = encoded_bits

    # Calculate syndrome
    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s3 = p3 ^ d2 ^ d3 ^ d4

    # Determine error position (if any)
    error_position = s1 * 1 + s2 * 2 + s3 * 4

    if error_position != 0:
        # print(f"Error detected at position {error_position}")
        encoded_bits[error_position - 1] ^= 1  # Correct the error

    # Extract the decoded data bits
    decoded_data = [encoded_bits[2], encoded_bits[4], encoded_bits[5], encoded_bits[6]]

    return decoded_data




def string_to_bits(input_string, round_to = 4):
    bits=[]
    for char in input_string:
        curr_bits = CHAR_TO_BINARY[char]
        for b in curr_bits:
            bits.append(b)

    while not len(bits) % round_to ==0:
        bits.append(0)
    return bits




def bits_to_string(bits, chunk_size = 4):
    string = ""
    for i in range(0, len(bits), chunk_size):
        chunk = bits[i:i + chunk_size]
        try:
            string += BINARY_TO_CHAR[tuple(chunk)]
        except:
            print('exception, chunk = '+str(chunk))
    return string

def clean_string(text: str) -> str:
    text = text.lower()
    result = ""
    for char in text:
        if char in CHAR_TO_BINARY:
            result += char
    return result


def encode_string(input_string):
    '''Encode a string into Hamming(7,4) code'''

    input_string = clean_string(input_string)


    # Convert string to bits
    bits = string_to_bits(input_string)


    # Process in 4-bit chunks
    chunks = []
    for i in range(0, len(bits), 4):
        chunk = bits[i:i + 4]
        chunks.append(hamming_7_4_encode(chunk))  # Encode each chunk

    number_of_chunks = len(chunks)
    encoded_bits = [0]*number_of_chunks*7
    for j in range(7):
        for i in range(number_of_chunks):
            encoded_bits[j * number_of_chunks + i] = chunks[i][j]

    return encoded_bits


def decode_bits(bits):
    '''Decode a Hamming(7,4) encoded message back to a string'''
    # Process in 7-bit chunks

    #this part extract the chunks from the mixed way
    number_of_chunks = len(bits) // 7
    decoded_chunks = []
    for i in range(number_of_chunks):
        decoded_chunks.append([])
        for j in range(7):
            decoded_chunks[i].append(bits[i + j * number_of_chunks])

    decoded_bits = []

    for i in range(0, len(decoded_chunks)):
        decoded_bits.extend(hamming_7_4_decode(decoded_chunks[i]))  # Decode each chunk


    # Convert decoded bits back to string
    return bits_to_string(decoded_bits)

# if __name__=='__main__':
#     sentence = "ae" #input('Enter Sentence To Send: ')
#     print(len(sentence))
#     information = encode_string(sentence)
#     print(len(information))
#     decoded_sentence = decode_bits(information)
#     print(decoded_sentence)
#
#
# def bits_to_bytes(bits):
#     return bytearray(int(''.join(map(str, bits[i:i+8])), 2) for i in range(0, len(bits), 8))
#
# def bytes_to_bits(b):
#     return [int(bit) for byte in b for bit in format(byte, '08b')]
#
#
# def reedsolo_encode_string(input_string):
#     rs = reedsolo.RSCodec(30)
#     encoded = rs.encode(input_string.encode('utf-8'))
#     return encoded
#
#
# def reedsolo_decode_bits(input_bytes):
#     rs = reedsolo.RSCodec(30)
#     return (rs.decode(input_bytes)[0]).decode('utf-8')
#
#
# def bit_list_to_ascii_string(bits):
#     if len(bits) % 8 != 0:
#         raise ValueError("Bit list length must be a multiple of 8")
#
#     chars = []
#     for i in range(0, len(bits), 8):
#         byte = bits[i:i+8]
#         byte_str = ''.join(str(b) for b in byte)
#         ascii_char = chr(int(byte_str, 2))
#         chars.append(ascii_char)
#
#     return ''.join(chars)
# def ascii_string_to_bit_list(s):
#     bits = []
#     for char in s:
#         binary_str = format(ord(char), '08b')  # Convert char to 8-bit binary string
#         bits.extend(int(bit) for bit in binary_str)
#     return bits
#
# def reed_str_to_bits(input_string):
#     bits = string_to_bits(input_string, round_to=8)
#     str = bit_list_to_ascii_string(bits)
#     encoded = reedsolo_encode_string(str)
#     return bytes_to_bits(encoded)
#
# def reed_bits_to_str(input_bits):
#     input_bytes = bits_to_bytes(input_bits)
#     decoded = reedsolo_decode_bits(input_bytes)
#     decoded_bits = ascii_string_to_bit_list(decoded)
#     return bits_to_string(decoded_bits)
#
#
# if __name__ == '__main__':
#     text = "this is my secret text"
#     bits = reed_str_to_bits(text)
#     print(bits)
#     str = reed_bits_to_str(bits)
#     print(str)