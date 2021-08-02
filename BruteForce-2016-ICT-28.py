import itertools

DNA = ["eebdabadaedebabebddebabeeaddbaebbaddbeebebdbdedaabebabdedbbb",
       "adbaebddbdbaeabbbdabeeabaedbaeaeeddeaaeebdaaaeaaaedebeadaaee",
       "aaaedbbadbdeaeeebebbbebbedbddebebddeeaaedadddebdabdbabaadaed",

       ]


t = 3
n = 60
l = 8



def score(DNA, s):
    Arr = ['a', 'e', 'd', 'b']
    arr = []
    k = 0
    for d in DNA:
        tempArr = []
        for w in d[s[k]:s[k] + l]:
            tempArr.append(w)

        k += 1
        arr.append(tempArr)
    i = 0
    mat = []

    i1 = 0
    while i1 < len(Arr):
        j1 = 0
        arr1 = []
        while j1 < l:
            arr1.append(0)
            j1 += 1
        mat.append(arr1)
        i1 += 1
    while i < len(Arr):
        j = 0
        while j < l:
            k = 0
            while k < t:
                if Arr[i] == arr[k][j]:
                    mat[i][j] += 1
                k += 1
            j += 1
        i += 1

        x = 0
        sum = 0
        while x < l:
            y = 0
            max = 0
            while y < len(mat):
                if mat[y][x] > max:
                    max = mat[y][x]
                y += 1
            sum += max
            x += 1
    return sum



def BruteForce(DNA, t, n, l):
    data = itertools.product(range(n - l), repeat=t)
    bestScore = 0
    bestMotif = []
    for s in data:
        sco = score(DNA, s)
        if sco > bestScore:
            bestMotif = s
            bestScore = sco

    print("Best Score is: ", bestScore)
    print("Best Motif is: ", bestMotif)

    return bestMotif


BruteForce(DNA, t, n, l)

"""
>>> 
=========== RESTART: C:/Users/dell/Desktop/BruteForce-2016-ICT-28.py ===========
Best Score is:  21
Best Motif is:  (1, 4, 45)
>>> 
"""
