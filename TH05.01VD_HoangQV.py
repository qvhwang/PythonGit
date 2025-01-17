import numpy as np

# Phần 1: Reshape Operations
print("=== Reshape Operations ===")
vector_a = np.array([5,7,2,9,10,15,2,9,2,17,28,16], dtype=np.int16)
print("Original vector:", vector_a)
print('Số phần tử của vector:', vector_a.size)
print('------------------------------------------------------')

matrix_a = vector_a.reshape(3,4)
print("Reshaped to 3x4:\n", matrix_a)
print('Số phần tử của matrix:', matrix_a.size)
print('------------------------------------------------------')

matrix_b = vector_a.reshape(2,6)
print("Reshaped to 2x6:\n", matrix_b)
print('Số phần tử của matrix:', matrix_b.size)

# Phần 2: Matrix to Vector Conversion
print("\n=== Matrix to Vector Conversion ===")
a1_2d = np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print('Matrix:\n', a1_2d)
print('-------------------------------------------------------')
print('a) ravel by row (default order=\'C\')')
print(a1_2d.ravel())
print('\nb) ravel by column (order=\'F\')')
print(a1_2d.ravel(order='F'))

# Phần 3: Split Operations
print("\n=== Split Operations ===")
x = np.arange(0,6)
print("Original array:", x)
x1, x2 = np.split(x, 2)
print("Split in half:", x1, x2)

x = np.arange(1,10)
print("\nOriginal array:", x)
x1, x2, x3 = np.split(x, [2,6])
print("Split at positions 2 and 6:", x1, x2, x3)

# Phần 4: Matrix Flip Operations
print("\n=== Matrix Flip Operations ===")
A = np.array([[1, 2, 3], [4, 5, 6]])  # Define A first
A2 = np.flip(A, 0)  # or np.flipud(A)
print('Lật ma trận theo hàng:\n', A2)

# Phần 5: Basic Operations
print("\n=== Basic Operations ===")
x = np.arange(8)
print("x =", x)
print('---------------------------------')
print("Basic arithmetic:")
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)
print("x % 2 =", x % 2)
print("x ** 3 =", x ** 3)

# Phần 6: NumPy Methods
print("\nNumPy methods:")
print("abs(-2,-1,0,1,2) =", np.abs(np.array([-2,-1,0,1,2])))
print("exp([1,2,3]) =", np.exp(np.array([1,2,3])))

# Phần 7: Rounding Operations
print("\n=== Rounding Operations ===")
arr = np.array([20.8999, 67.89899, 54.43409])
print("Original array:", arr)
print("Round to 1 decimal:", np.around(arr, 1))
print("Round to 2 decimals:", np.around(arr, 2))
print("Floor:", np.floor(arr))
print("Ceiling:", np.ceil(arr))

# Phần 8: Sorting Operations
print("\n=== Sorting Operations ===")
a = np.random.randint(1, 33, 15)
print("Original array:", a)
a_sort = np.sort(a)
b_sort = -np.sort(-a)  # Descending order
print("Ascending:", a_sort)
print("Descending:", b_sort)

# Phần 9: Search Operations
print("\n=== Search Operations ===")
x = np.array([17,2,11,1,9,15,1,3,8,1,12,13,5])
print("Original array:", x)
print("Indices where x == 1:", np.where(x == 1)[0])
print("Indices where x > 10:", np.where(x > 10)[0])
print("Indices where 5 <= x < 12:", np.where((x >= 5) & (x < 12))[0])