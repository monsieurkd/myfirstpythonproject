def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ' , '')
   
    if len(my_word) != len(other_word):
        return False
    revealed = []
    for i in range(len(my_word)) :
        for o in range(len(other_word)):
           
            if my_word[i] != '_' and i == o:
                revealed.append(my_word[i])
    

            
    for i in range(len(my_word)) :
        for o in range(len(other_word)):
            
            if my_word[i] == '_' and i == o:
                
                if other_word[o] in revealed:
                    return False
            
    for i in range(len(my_word)) :
        for o in range(len(other_word)):            

            if i == o and my_word[i] != '_' and my_word[i] != other_word[o]:
                return False
            
    return True


print(match_with_gaps('tel_ ph_ _ e', 'telephone'))