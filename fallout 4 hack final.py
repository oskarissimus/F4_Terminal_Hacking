def common_letters(password, word_to_check):
    matches = 0
    for letter_idx in range(len(password)):
        if password[letter_idx] == word_to_check[letter_idx]:
            matches += 1
    return matches

def crack_password(words):
    common_matrix = []

    for pass_idx, password in enumerate(words):
        common_matrix.append([])
        for word in words:
            common_matrix[pass_idx].append(common_letters(password,word))


    l = len(words)
    ans = {}
    ans_tmp = {}
    max_uniq = 0
    for idx1 in range(l):
        for idx2 in range(idx1+1,l):
            for idx3 in range(idx2+1,l):
                #print ("{} {} {}".format(idx1,idx2,idx3))
                tmp=[]
                matches_list=[]
                for row_idx, row in enumerate(common_matrix):
                    tmp.append( l*l*row[idx1] + l*row[idx2] + row[idx3] )
                    matches_list.append([words[row_idx], row[idx1], row[idx2], row[idx3]])
                
                #print (tmp)
                if len(set(tmp)) > max_uniq:
                    max_uniq = len(set(tmp))
                    max_uniq_matches_list = matches_list[:]
                    sol = [idx1,idx2,idx3]
                ans[idx1,idx2,idx3] = len(set(tmp))
                ans_tmp[idx1,idx2,idx3] = tmp
                if len(tmp) == len(set(tmp)):
                    print ("password cracked:")
                    print ("{} {} {}".format(words[idx1],words[idx2],words[idx3]))
                    print (matches_list)
                    return
                
    print("almost cracked:")
    print ("{} {} {}".format(words[sol[0]],words[sol[1]],words[sol[2]]))
    max_uniq_matches_list.sort(key = lambda x: x[1]*l*l+x[2]*l+x[3])
    for i in max_uniq_matches_list:
        print (i)

    #print (common_matrix[sol[0]])
    #print (common_matrix[sol[1]])
    #print (common_matrix[sol[2]])
    #print (common_matrix[4])
    #print (common_matrix[13])

words = []

while True:
    words.append(input("enter password candidate: "))
    if words[-1] == "":
        print ("computing...")
        del words[-1]
        break

crack_password(words)
e = input ("press x to exit...")
while e != "x":
    e = input ("press x to exit...")
