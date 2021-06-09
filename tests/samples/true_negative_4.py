this_equal_13 = 1
abcdefghijklm = 2
abcdef1234567 = 3

while len(this_equal_13) < 100:
    for i in range(100):
        this_equal_13 += 1
        if i > 0:
            if i < 10:
                for j in range(i):
                    abcdefghijklm += j
                    abcdef1234567 += abcdefghijklm
                    print(abcdef1234567)
                    if i == 5:
                        print(this_equal_13)