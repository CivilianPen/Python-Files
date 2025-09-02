maze = [
[0,1,0,0,0,0,0],
[0,1,0,1,1,1,0],
[0,1,0,1,0,1,0],
[0,1,0,0,0,1,1],
[0,0,0,0,0,0,0],
[0,1,0,0,0,0,0],
[0,1,0,0,0,0,0],
    ]
way = [[0]*7 for i in range(7)]
way[0][0] = 1
def make_step(k,way,maze):
  for i in range(7):
    for j in range(7):
      if way[i][j] == k:
        if i>0 and way[i-1][j] == 0 and maze[i-1][j] == 0:
          way[i-1][j] = k + 1
        if j>0 and way[i][j-1] == 0 and maze[i][j-1] == 0:
          way[i][j-1] = k + 1
        if i<len(way)-1 and way[i+1][j] == 0 and maze[i+1][j] == 0:
          way[i+1][j] = k + 1
        if j<len(way[i])-1 and way[i][j+1] == 0 and maze[i][j+1] == 0:
           way[i][j+1] = k + 1
k = 0
while k <= 49:
    k += 1
    make_step(k,way,maze)
