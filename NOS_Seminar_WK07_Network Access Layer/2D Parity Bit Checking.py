import numpy as np


def compute_parity(mat):
    return np.sum(mat, axis=1) % 2, np.sum(mat, axis=0) % 2


# 4x4 matrix
data = np.array([
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
])
print("Original Data:\n", data)

# Computing original parity
row_par, col_par = compute_parity(data)
print("Row Parity:", row_par)
print("Column Parity:", col_par)

# Inject error
data_err = data.copy()
data_err[2, 1] ^= 1
print("\nData with error at (2, 1):\n", data_err)

# Recalculate
new_row_par, new_col_par = compute_parity(data_err)
print("New Row Parity:", new_row_par)
print("New Column Parity:", new_col_par)

# Error detection
err_row = np.where(new_row_par != row_par)[0]
err_col = np.where(new_col_par != col_par)[0]

if err_row.size == 1 and err_col.size == 1:
    err_pos = (err_row[0], err_col[0])
    print(f"\n Error detected at: {err_pos}")
    data_err[err_pos] ^= 1  # Correct the error
    print("Corrected Data:\n", data_err)
else:
    print("No single-bit error detected or multiple errors occurred.")
