def base(model,direction):
    
    if direction == 'UP':
        up(model,*get_model_position(model))
    if direction == 'DOWN':
        down(model,*get_model_position(model))
    if direction == 'RIGHT':
        right(model,*get_model_position(model))
    if direction == 'LEFT':
        left(model,*get_model_position(model))

def get_model_position(model):
    y = 0
    x = 0

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == model:
                y = i
                x = j

    return y,x    
            
def up(model,y,x):
    maps[y-1][x] = model
    maps[y][x] = '_'    
def down(model,y,x):
    maps[y+1][x] = model
    maps[y][x] = '_'    
def right(model,y,x):
    maps[y][x+1] = model
    maps[y][x] = '_'    
def left(model,y,x):
    maps[y][x-1] = model
    maps[y][x] = '_'    



maps = [
    ['_','_','_'],
    ['_','_','_'],
    ['A','T','K'],
    ['_','_','_'],
    ['_','_','_']
]


for _ in range(7):
    model, direction = input().split()
    base(model,direction)

for m in maps:
    print(*m,sep='')