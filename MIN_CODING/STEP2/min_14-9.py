lsts = [10,50,40,20,30,40]

input_lsts = list(map(int,input().split()))

for i in range(len(input_lsts)):
    counting = 0
    for j in range(len(lsts)):
        
        if input_lsts[i] < lsts[j]:
            counting += 1 
            
    print(f'{input_lsts[i]}={counting}')
    
    