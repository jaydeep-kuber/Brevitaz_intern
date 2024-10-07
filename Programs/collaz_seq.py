# collaz seq is mathamatical uniq sqe like fibonaci 
# first we pass a nukber and we need to consider 2 rules for this seq 
    # i) n / 2 if n is even
    # ii) 3*n+1 if n is odd

def collaz_seq_itr(number):

    seq = [] # list for storing seq
    if number <= 0:
        return "Input should be a positive integer."
    elif number == 1:
        return 1
    while number != 1:
        if number % 2 == 0:
           number = number // 2
        else: number = 3 * number + 1
        seq.append(number)
    return seq

seq = [] # storing seq in rec part is like my god. jr ko puchh na to banta hai.
def collaz_seq_rec(number,seq):
    '''
    for rec approach we need to take care of termination condition first.
    then we do 2 call for this fuction with collaz 2 condition
    '''
    lst = seq
    if number == 1:
        lst.append(1)
        return lst[1:]
    else:
        if number % 2 ==0: # means number is even
            lst.append(number)
            return collaz_seq_rec(number // 2 ,lst)
        else: # means number is odd
            lst.append(number)
            return collaz_seq_rec(3 * number + 1, lst)
    
user_inp = int(input("enter a number between 1 to 20: "))
print("rec approach",collaz_seq_rec(user_inp, seq=seq))
print("itr approach",collaz_seq_itr(user_inp))