alph = list(map(lambda x:str(x), range(1,9))) # исходный алфавит

file = open("task7.1.txt", "w")
count = 0
for i in alph:
    alph_i = list(filter(lambda x: x != i, alph)) # алфавит из всех символов alph кроме i
    for j in alph_i:
        alph_j = list(filter(lambda x: x != j, alph_i)) # алфавит из всех символов alph_i кроме j или всех символов alph коме i, j
        for k in alph_j:
            alph_k = list(filter(lambda x: x != k, alph_j)) # анолонично alph / i, j, k
            for l in alph_k:
                alph_l = list(filter(lambda x: x != l, alph_k)) # alph / i, j, k, l
                for m in alph_l:
                    word = i + j + k + l + m
                    count+=1
                    file.write(word+"\n")

file.write(str(count))
file.close()