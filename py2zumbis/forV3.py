l1 = [4, 8, 15, 16, 23, 42]
l2 = [
    47, 38, 18, 14, 29, 44, 2, 58, 25, 6, 26, 17, 24, 36, 19, 33, 7, 11, 38,
    26, 35, 39, 12, 47, 3, 12, 46, 5, 47, 8, 16, 37, 45, 52, 56, 12, 55, 42,
    10, 43, 45, 54, 22, 6, 7, 52, 38, 60, 13, 3, 51, 17, 29, 25, 21, 57, 16,
    23, 54, 4, 15, 13, 57, 53, 40, 17, 5, 33, 49, 17, 42, 39, 43, 33, 14, 36,
    5, 44, 56, 19, 28, 48, 17, 45, 38, 50, 7, 29, 15, 14, 14, 56, 58, 8, 43, 3,
    60, 6, 22, 3, 24, 54, 44, 33, 13, 51, 17, 20, 50, 53, 57, 10, 58, 22, 56,
    50, 55, 54, 24, 43, 1, 8, 14, 28, 33, 43, 17, 52, 51, 59, 39, 37, 9, 38,
    56, 1, 31, 46, 49, 46, 6, 53, 33, 36, 25, 28, 30, 33, 51, 11, 5, 25, 12,
    10, 60, 24, 37, 36, 56, 27, 42, 23, 10, 20, 6, 19, 51, 13, 60, 58, 49, 32,
    20, 34, 60, 12, 33, 52, 35, 51, 16, 2, 27, 47, 23, 53, 47, 32, 50, 54, 18,
    56, 20, 27, 43, 16, 19, 4, 25, 15, 58, 37, 59, 38, 25, 4, 18, 57, 21, 38,
    55, 43, 56, 54, 8, 60, 53, 17, 38, 4, 47, 37, 56, 38, 21, 20, 3, 5, 19, 40,
    7, 13, 22, 47, 1, 19, 46, 6, 16, 2, 6, 59, 42, 27, 1, 5, 36, 30, 10, 11,
    29, 47, 9, 39, 37, 49, 43, 41, 41, 5, 4, 52, 30, 33
]
c = 0
for w in l1:
    for ww in l2:
        # print(w, ww)
        if w == ww:
            #   print(w)
            c = c + 1
else:
    print(f'Acertou: {c}')
    print(f' Percentual: { c / len(l2) * 100 :.2f}')
