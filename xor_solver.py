import struct

# Define the given values
value1 = INPUT_VALUE_1
value2 = INPUT_VALUE_2

# Pack the values into a binary format using little-endian notation
enc = struct.pack('<QQH', value1, value2)

# Decode the packed values to a UTF-8 string
decoded_string = enc.decode('utf-8', errors='ignore')
print(f"Decoded string: {decoded_string}")

# Print the packed values in hexadecimal format
hex_string = ''.join(['\\x' + hex(c)[2:] for c in enc])
print(f"Hexadecimal string: {hex_string}")

# Encrypt the input by XORing each byte with SELECT_XOR_VALUE
encrypted = bytes([c ^ YOUR_VALUE for c in enc[:-1]])  # Ignore the last byte for correct size
encrypted_string = ''.join([chr(c) for c in encrypted])
print(f"Encrypted string: {encrypted_string}")

