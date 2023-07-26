lsts = [
    [1,0,0,0,0],
    [1,0,1,0,0],
    [1,1,0,1,0],
    [1,0,1,0,0],
    [0,1,0,0,1],
    [0,0,0,1,0],
    [1,1,0,0,0]
]

def input_func():
    num = int(input())
    return num 


def process(get_num):
    counting = 0
    for i in range( len(lsts) ):
        for j in range( len(lsts[i])):
            if j == get_num:
                if lsts[i][j] == 1:
                    counting += 1

    return counting

def output_func(counting):
    print(counting)




output_func(process(input_func()))