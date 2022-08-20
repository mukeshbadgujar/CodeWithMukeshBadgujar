import gc
import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_exists(object_id):
    for object in gc.get_objects():
        if id(object) == object_id:
            return True

    return False


class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: {hex(id(self))}, B: {hex(id(self.b))}')


class B:
    def __init__(self, a):
        self.a = a
        print(f'B: {hex(id(self))}, A: {hex(id(self.a))}')


# disable the garbage collector
gc.disable()

# Create Object
a = A()

a_id = id(a)
b_id = id(a.b)

print(ref_count(a_id))  # 2
print(ref_count(b_id))  # 1
#
print(object_exists(a_id))  # True
print(object_exists(b_id))  # True
#
#
a = None
print(ref_count(a_id))  # 1
print(ref_count(b_id))  # 1
#
print(object_exists(a_id))  # True
print(object_exists(b_id))  # True
#
# # run the garbage collector
gc.collect()
#
# # check if object exists
print(object_exists(a_id))  # False
print(object_exists(b_id))  # False
#
# # reference count
print(ref_count(a_id))  # 0
print(ref_count(b_id))  # 0
