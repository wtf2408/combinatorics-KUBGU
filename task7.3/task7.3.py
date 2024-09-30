alph = list(map(lambda x: str(x), range(1, 9)))
count = 0

file = open('task7_3.txt', 'w')

def entersThree(word, elem):
    count = 0
    for symbol in word:
        if symbol == elem: count += 1
    if count == 3: return True
    else: return False

for i in alph:
    for j in alph:
        for k in alph:
            for l in alph:
                for m in alph:
                    for n in alph:
                        word = i+j+k+l+m+n
                        if entersThree(word, "2"):
                            file.write(word+"\n")
                            count += 1
file.write(str(count))
file.close()
