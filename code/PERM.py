from itertools import permutations

number = int(input("Enter the positive integer(n<=7): "))
arr = list(range(1,number+1))

permute_list = list(permutations(arr, number))

print(len(permute_list))
for permute in permute_list:
    for number in permute:
        print(number, end = ' ')
    print()

