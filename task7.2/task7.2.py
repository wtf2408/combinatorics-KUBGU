alph = list(map(lambda x:str(x), range(1,9)))


count = 0
file = open("task7.2.txt", "w")
word = list(map(lambda x: '', range(7))) # пустой список из 7 эл


for symbol1 in alph: # выбираем первый симовл, который будет повторяться 3 раза

    for i in range(7): # это первый индекс из 3, на котором может стоять этот символ, ему доступны 7 позиций
        
        for j in range(i+1, 7): # это второй индекс из 3, на котором может стоять этот символ, ему доступны 6 позиций

            for k in range(j+1, 7): # это третий индекс из 3, на котором может стоять этот символ, ему доступны 5 позиций

                word[i] = symbol1 # размещаем первый символ на 3 позиции
                word[j] = symbol1
                word[k] = symbol1
                alph_1 = list(filter(lambda x: x != symbol1, alph))

                for symbol2 in alph_1: # выбираем второй символ, который будет повторяться 2 раза
                    indexes_k = list(filter(lambda x: word[x] == '', range(7))) 
                    for l in indexes_k: # это первый индес из 2, на котором может стоять второй символ, ему доступны 4 позиции
                        indexes_l = list(filter(lambda x: word[x] == '', range(l+1, 7)))
                        for m in indexes_l: # это второй индес из 2, на котором может стоять второй символ, ему доступны 3 позиции
                            word[l] = symbol2 # размещаем второй символ на 2 позиции
                            word[m] = symbol2
                            
                            alph_2 = list(filter(lambda x: x != symbol2, alph_1))
                           
                            indexes_m = list(filter(lambda x: word[x] == '', range(7))) 

                            for symbol3 in alph_2: # выбираем третий символ, он не должен повторять предыдущих двух
                                alph_3 = list(filter(lambda x: x != symbol3, alph_2))
                                for symbol4 in alph_3: # выбираем третий символ, он не должен повторять предыдущие

                                    word[indexes_m[0]] = symbol3
                                    word[indexes_m[1]] = symbol4
                                    word_str = ""
                                    for char in word: word_str += char
                                    file.write(word_str+"\n")
                                    count+=1
                                    word[indexes_m[0]] = ''
                                    word[indexes_m[1]] = ''
                            word[l] = '' 
                            word[m] = ''
                word[i] = '' 
                word[j] = ''
                word[k] = ''




print(count)
file.close()