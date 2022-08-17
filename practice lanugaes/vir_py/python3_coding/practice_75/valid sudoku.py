from collections import defaultdict


def validSudo(board):
    # first check each rows is not repeated values
    hash_map=[]
    for i in range(9):
        print(board[i][:])
        currentValues=board[i][i]
        if currentValues in hash_map:
            return False
        hash_map.append(currentValues)

        
        # del hash_map

    # second check each columns any values not repeated values
    pass

board =[
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# validSudo(board)



# leetcode solution

def isvalidsudo(board):
    cols=defaultdict(set)
    rows=defaultdict(set)
    squares=defaultdict(set)
    for r in range(9):
        for  c in range(9):
            if board=='.':
                continue
            if board[r][c] in rows[r]
            # print(board[c])
    pass
isvalidsudo(board)