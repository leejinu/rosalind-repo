def find_SCS(s,t): # SCS: Shortest common superstring
    m = len(s)
    n = len(t)

    # Initialize matrix
    mat = [[0 for x in range(0, n+1)] for y in range(0, m+1)]
    SCS = ""
    
    # Filling Matrix
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                mat[i][j] = j                
            elif j == 0:
                mat[i][j] = i
            elif s[i-1] == t[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = 1+ min(mat[i-1][j], mat[i][j-1])

    i = m
    j = n
    
    while i> 0 and j >0:
        # If current character s and t is same
        if s[i-1] == t[j-1]:
            # Put current character into shortest common supersequence(SCS)
            SCS += s[i-1]
            i -= 1
            j -= 1
            
        # If current character s and t is different
        elif mat[i-1][j] > mat[i][j-1]:
            # Put current character of t in SCS
            SCS += t[j-1]
            j -= 1
        else:
            SCS += s[i-1]
            i -= 1
    while i > 0:
        SCS += s[i-1]
        i -= 1
    while j > 0:
        SCS += t[j-1]
        j -= 1
                
    return SCS[::-1]

    
    
if __name__ == "__main__":
    
    seqs = input().split()
    s,t = seqs[0], seqs[1]

    print(find_SCS(s,t))
    
               
    
   



    
