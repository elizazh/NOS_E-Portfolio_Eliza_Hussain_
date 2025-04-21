import random


# Function to compute even parity bit
def compute_even_parity(data):
    return sum(data) % 2


def simulate_parity_transmission(data, error_index=None):
    parity_bit = compute_even_parity(data)
    transmitted_data = data + [parity_bit]

    print("Original Data: ", data)
    print("Computed Parity Bit (Even):", parity_bit)
    print("Transmitted Data:", transmitted_data)

    if error_index is not None:
        transmitted_data[error_index] ^= 1  # Flip bit
        print(f"\nData with an Error Introduced at index {error_index}:", transmitted_data)

    if sum(transmitted_data) % 2 == 0:
        print("No error detected (Parity Check Passed)")
    else:
        print(" Error detected (Parity Check Failed)")


data = [random.randint(0, 1) for _ in range(8)]
simulate_parity_transmission(data, error_index=3)
