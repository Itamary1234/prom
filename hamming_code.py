from CONSTANTS import *


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
        print(f"Error detected at position {error_position}")
        encoded_bits[error_position - 1] ^= 1  # Correct the error

    # Extract the decoded data bits
    decoded_data = [encoded_bits[2], encoded_bits[4], encoded_bits[5], encoded_bits[6]]

    return decoded_data





def string_to_bits(input_string):
    return CHAR_TO_BINARY[input_string]

def bits_to_string(bits):
    string = ""


def encode_string(input_string):
    '''Encode a string into Hamming(7,4) code'''
    # Convert string to bits
    bits = string_to_bits(input_string)

    # Process in 4-bit chunks
    encoded_bits = []
    for i in range(0, len(bits), 4):
        chunk = bits[i:i + 4]
        encoded_bits.extend(hamming_7_4_encode(chunk))  # Encode each chunk

    return encoded_bits


def decode_string(encoded_bits):
    '''Decode a Hamming(7,4) encoded message back to a string'''
    # Process in 7-bit chunks
    decoded_bits = []
    for i in range(0, len(encoded_bits), 7):
        chunk = encoded_bits[i:i + 7]
        decoded_bits.extend(hamming_7_4_decode(chunk))  # Decode each chunk

    # Convert decoded bits back to string
    return bits_to_string(decoded_bits)


# Try it!
data = [1,1,0,1]
encoded = hamming_7_4_encode(data)
print("Encoded:", encoded)

# Introduce error
encoded[5] ^= 1
decoded = hamming_7_4_decode(encoded)
print("Decoded:", decoded)