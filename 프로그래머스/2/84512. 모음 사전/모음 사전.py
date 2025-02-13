def solution(word):
    arr_word = ['A', "E", "I", "O", "U"]

    alphabet_dict={}

    temp = 0



    for i in arr_word:
        temp += 1
        alphabet_dict[i] = temp
        for j in arr_word:
            temp += 1
            alphabet_dict[i+j] = temp    
            for k in arr_word:
                temp += 1
                alphabet_dict[i+j+k] = temp
                for l in arr_word:
                    temp += 1
                    alphabet_dict[i+j+k+l] = temp
                    for m in arr_word:
                        temp += 1
                        alphabet_dict[i+j+k+l+m] = temp

    answer = alphabet_dict[word]
    return answer