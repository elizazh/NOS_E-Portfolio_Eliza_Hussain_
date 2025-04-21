def ones_complement_sum(a, b, bit_size=16):
    result = a + b
    if result >= (1 << bit_size):
        result = (result + 1) & ((1 << bit_size) - 1)
    return result


def calculate_checksum(data, bit_size=16):
    checksum = 0
    for word in data:
        checksum = ones_complement_sum(checksum, word, bit_size)
    return ~checksum & ((1 << bit_size) - 1)


def verify_checksum(data, received_checksum, bit_size=16):
    total = 0
    for word in data:
        total = ones_complement_sum(total, word, bit_size)
    total = ones_complement_sum(total, received_checksum, bit_size)
    return total == (1 << bit_size) - 1


# Sample data (16-bit words)
data_words = [0b1101010101010101, 0b1001100110011001, 0b1111000011110000]

checksum = calculate_checksum(data_words)
print("✅ Checksum:", bin(checksum))

# Verification
if verify_checksum(data_words, checksum):
    print("✅ Data is valid (checksum passed)")
else:
    print("Data is corrupted (checksum failed)")

# Introduce error
data_words[1] ^= 1  # Flip a bit
if verify_checksum(data_words, checksum):
    print("Data is valid (checksum passed)")
else:
    print("Error detected after bit flip (checksum failed)")
