
m,n = map(int,input().split())
flat = []
for i in range(m):
    s = list(map(str,input().split()))
    flat.append(s)
  
for i in range(m):
    for j in range(n):
        if flat[i][j] == 'O':
            flat[i][j] = 0
        elif flat[i][j] == 'W':
            flat[i][j] = 1
        elif flat[i][j] == 'H':
            human_xy = [j,i]
            flat[i][j] = 0
        elif flat[i][j] == 'M':
            mouse_xy = [j,i]
            flat[i][j] = 0
        else:
            finish = [j,i]
            flat[i][j] = 0
   
def make_step(k,way,maze):
  for i in range(m):
    for j in range(n):
      if way[i][j] == k:
        if i>0 and way[i-1][j] == 0 and maze[i-1][j] == 0:
          way[i-1][j] = k + 1
        if j>0 and way[i][j-1] == 0 and maze[i][j-1] == 0:
          way[i][j-1] = k + 1
        if i<len(way)-1 and way[i+1][j] == 0 and maze[i+1][j] == 0:
          way[i+1][j] = k + 1
        if j<len(way[i])-1 and way[i][j+1] == 0 and maze[i][j+1] == 0:
           way[i][j+1] = k + 1

def Human_path(flat,finish,human_xy):
    human_plate = []
    for i in range(len(flat)):
        human_plate.append([])
        for j in range(len(flat[i])):
            human_plate[-1].append(0)
    human_plate[human_xy[1]][human_xy[0]] = 1
    k = 0
    while k <= m*n:
        k += 1
        make_step(k,human_plate,flat)
    return(human_plate[finish[1]][finish[0]])
    
mouse_result = 10**10+1
was = []
def Mouse_path(finish,mouse_xy,flat_mouse,plate_mouse):
    k = 0
    while k <= m*n:
        k += 1
        make_step(k,plate_mouse,flat_mouse)
    return plate_mouse[finish[1]][finish[0]]
    
for y in range(m):
    for x in range(n):
        mouse_plate = []  
        for i in range(len(flat)):
            mouse_plate.append([])
            for j in range(len(flat[i])):
                mouse_plate[-1].append(0)
        mouse_plate[mouse_xy[1]][mouse_xy[0]] = 1
        flat_for_mouse = []
        for j in range(len(flat)):
            flat_for_mouse.append(flat[j])
        if flat_for_mouse[y][x] == 1 and [x,y] not in was:
            flat_for_mouse[y][x] = 0
            was.append([x,y])
            
            if mouse_result > Mouse_path(finish,mouse_xy,flat_for_mouse,mouse_plate) and Mouse_path(finish,mouse_xy,flat_for_mouse,mouse_plate) != 0:
                mouse_result = Mouse_path(finish,mouse_xy,flat_for_mouse,mouse_plate)

            flat_for_mouse[y][x] = 1

if (Human_path(flat,finish,human_xy)-1)//2 + (Human_path(flat,finish,human_xy)-1)%2 != 0:
    human_result = (Human_path(flat,finish,human_xy))//2
else:
    human_result = 10**10
human_final_result = (human_result)

if (mouse_result) != 0:
    mouse_final_result = ((mouse_result)-1)
else:
    mouse_final_result = 10**10+1

if human_final_result > mouse_final_result:
    print("MOUSE")
elif human_final_result < mouse_final_result:
    print("HUMAN")
else:
    print("DRAW")
