# conways game of life
import time,copy,random
numOfColEle = 60 #60 col width
numOfRow = 20 #20 row height

# create a list of list for cell. simple create a grid

'''
col = 6
row = 2
interpret as 2 lsts with 6 ele
nextcell=[ 
            [e1 e2 e3 e4 e5 e6],
            [e1 e2 e3 e4 e5 e6]            
        ]
'''

nextCell=[] # use chat gpt to take a look how this list look like in each itration
for x in range(numOfColEle):
    column = []
    for y in range(numOfRow):
        if random.randint(0,1) == 0:
            column.append('#') # alive cell
        else: column.append(' ') # deth cell
    nextCell.append(column)

while True:
    print("\n\n next step \n\n")
    currentCells= copy.deepcopy(nextCell) 
    # copy.deepcopy() to make a complete, independent copy, not just a reference to the same list. 
    # Print currentCells on the screen:
    for y in range(numOfRow):
        for x in range(numOfColEle):
            print(currentCells[x][y], end="")
        print()
    # Calculate the next step's cells based on current step's cells:
    for x in range(numOfColEle):
        for y in range(numOfRow):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % numOfColEle # col
            rightCoord = (x + 1) % numOfColEle # col
            upCoord = (y - 1) % numOfRow # row
            dwnCoord = (y + 1) % numOfRow # row

             # Count number of living neighbors:
            '''
            lft-up      up      right-up
            lft         --#--    right
            lft-dwn     dwn     right-dwn
            '''

            numOfNeighbr = 0
            if currentCells[leftCoord][upCoord] == '#': #- cross: lft-up
                numOfNeighbr += 1

            if currentCells[x][upCoord] == '#': #- top : up
                numOfNeighbr += 1

            if currentCells[rightCoord][upCoord] == '#': #- cross: right-up
                numOfNeighbr += 1

            if currentCells[leftCoord][y] == '#': #- side: lft
                numOfNeighbr += 1

            if currentCells[rightCoord][y] == '#': #- side: right
                numOfNeighbr += 1

            if currentCells[leftCoord][dwnCoord] == '#': #- cross: lft-dwn 
                numOfNeighbr += 1

            if currentCells[x][dwnCoord] == '#': #- down: den
                numOfNeighbr += 1

            if currentCells[rightCoord][dwnCoord] == '#': #- crpss: right-dwn
                numOfNeighbr += 1

            # Set cell based on Conway's Game of Life rules:
            '''
            # 1. Any live cell with fewer than two live neighbors dies, as if by under 
            # 2. Any live cell with two or three live neighbors lives on to the next generation 
            # 3. Any live cell with more than three live neighbors dies, as if by over 
            # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if 
            # by reproduction
            ''' 
            if currentCells[x][y] == '#' and (numOfNeighbr in [2,3]):
                 # Living cells with 2 or 3 neighbors stay alive:
                nextCell[x][y] = '#'
            elif currentCells[x][y] == ' ' and numOfNeighbr == 3:
                # Dead cells with 3 neighbors become alive:
                nextCell[x][y] = '#'
            else:
                # All other cells die:
                nextCell[x][y] = ' '
    time.sleep(2)