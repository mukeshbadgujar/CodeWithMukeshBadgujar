import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


num = [1, 2, 3] # >>
num_id = id(num)
num2 = num
print(ref_count(num_id))  # 1 # 2

ranks = num
print(ref_count(num_id))  # 2 # 3

ranks = None
print(ref_count(num_id))  # 2

num = None
print(ref_count(num_id))  # 1


num2 = None
print(ref_count(num_id))