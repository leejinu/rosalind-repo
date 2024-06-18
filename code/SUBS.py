main = input()
sub = input()

num_list = []

def equal(A,B):
    if A == B:
        return True
    else:
        return False
n = len(sub)

for i, seq in enumerate(main, 1):
    if equal(main[i-1:n+i-1], sub):
        num_list.append(i)

for n in num_list:
    print(n, end=' ')



    
