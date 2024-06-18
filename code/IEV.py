def calculate_offspring(array):
    n1 = int(array[0])*2
    n2 = int(array[1])*2
    n3 = int(array[2])*2
    n4 = int(array[3])*1.5
    n5 = int(array[4])*1
    n6 = 0
    expected_offsprings = n1+n2+n3+n4+n5+n6

    return expected_offsprings
    

strings = input("Give Six nonnegative integers: ")

array = strings.split()

print(calculate_offspring(array))


