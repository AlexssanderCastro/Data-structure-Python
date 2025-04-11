
def inserirNum(num,array):
    print("array antes de inserir:",array)
    print("numero a ser inserido:",num)
    t=len(array)
    
    pc:int
    for i in range (t):
        if(num<array[i+1]):
            pc=i+1
            break

    
    array[t]=1
    for i in range(t-1,pc-1,-1):
        array[i+1]=array[i]

    array[pc]=num
    print("array depois de inserir:",array)


inserirNum(11,[1,2,3,4,6,10,22,33,34])
    
