board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

answer = 1234
array1 = []
for i in range(len(board)):
    for j in range(len(board[0])):
        가로,세로 = 1,1
        cnt = 1
        if board[i][j] == 1:
            while True:
                if board[i][j] == 0 or j> len(board) -1 or i > len(board[0]) -1 :
                    break
                가로 +=1
                j += 1
            while True:
                if board[i][j] == 0 or j> len(board) -1 or i > len(board[0]) -1 :
                    break
                세로 +=1
                i += 1
            
            array1.append(가로* 세로)
                
                    
                    
    print(array1)