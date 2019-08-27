import copy
tuple1 = [100, 1111, 88888, 4, 6, [1, 4, 6], "hello#$%"]
tuple2 = copy.deepcopy(tuple1)
tuple1[5][2] = 666
print(id(tuple1), id(tuple2))
print(tuple1, tuple2)
