# define a function which will take list as a argument and this function
# will return a reversed list


# examples
# [1,2,3,4]   ---> [4,3,2,1]
# ['word1' , 'word2']  ---. ['word2' , 'word1']


def reverse_list(l):
    l.reverse()
    return l

    
numbers = [1,2,3,4]
print(reverse_list(numbers))