A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

A_union_B = A.union(B)
print("A union B:", A_union_B)

A_intersection_B = A.intersection(B)
print("A intersection B:", A_intersection_B)

is_A_subset_B = A.issubset(B)
print("Is A subset of B:", is_A_subset_B)

are_A_B_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets:", are_A_B_disjoint)

A.update(B)
print("A after joining with B:", A)

B.update(A)
print("B after joining with A:", B)

A_symmetric_difference_B = A.symmetric_difference(B)
print("Symmetric difference between A and B:", A_symmetric_difference_B)

del A
del B
