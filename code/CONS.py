""" Consensus and Profile"""
# Findong a most liekly common ancestor

# Initialize array for DNA string 
DNA_strings = []

while 1:
    string = input("Give the sequence of DNA(exit: press enter): ")

    if string == "":
        break
    else:
        DNA_strings.append(string)
        continue


# length of DNA string
rows = len(DNA_strings)
cols = len(DNA_strings[0])

# 2D matrix for Profile
Profile = [[0]*cols for _ in range(4)]

"""
When initializing a 2D matrix in Python, be cautious of using a shallow copy method like [[0]*cols]*rows.
This method leads to all rows referencing the same object, causing unintended side effects when modifying elements.
Instead, use list comprehension to create separate objects for each row, ensuring that modifications to one element don't affect others.

Don't initialize a 2D matrix in Python like this.
Profile = [[0]*cols]*rows
"""

for sample in DNA_strings:
    for i, seq in enumerate(sample, 0):
        if seq == 'A':
            Profile[0][i]= int(Profile[0][i])+1
        elif seq == 'C':
            Profile[1][i]= int(Profile[1][i])+1
        elif seq == 'G':
            Profile[2][i]= int(Profile[2][i])+1
        elif seq == 'T':
            Profile[3][i]= int(Profile[3][i])+1


consensus = ""
for i in range(0, len(DNA_strings[0])):
    largest = 0
    pos = 0
    for j in range(0,4):
        if Profile[j][i] >= largest:
            pos = j
            largest = Profile[j][i]
        else:
            continue
    if pos == 0:
        consensus = consensus + 'A'
    elif pos == 1:
        consensus = consensus + 'C'
    elif pos == 2:
        consensus = consensus + 'G'
    elif pos == 3:
        consensus = consensus + 'T'

print(consensus)

# Print Profile
for i in range(0,4):
    if i == 0:
        print("A: ", end = '')
    elif i ==1:
        print("C: ", end = '')
    elif i ==2:
        print("G: ", end = '')
    elif i ==3:
        print("T: ", end = '')
    for j in range(0, len(Profile[0])):
        print(str(Profile[i][j])+" ", end = "")
    print()

    


            
