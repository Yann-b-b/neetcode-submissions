class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # the goal is to make sure that there is no repeat
        # number insie the 3x3 squares as well as the horizontal
        # and vertical cuts of the board

        #I can assume first maybe that we can work to check
        # just those things and then move to more complex later
        #horizontal
        for row in board: 
            check_set = set()
            for val in row:
                
                if val != ".":
                    if val in check_set:
                        print("f1")
                        return False
                    check_set.add(val)
        
        #vertical
        check_set = set()
        for col in zip(*board): #unzips vertically
            check_set = set()
            print(col)
            for val in col:
                if val != ".":
                    if val in check_set:
                        print("f2")
                        return False
                    check_set.add(val)

        #cubes

        for j,row in enumerate(board): #unzips vertically
            if j%3 ==0:

                check_set1 = set()
                check_set2 = set()
                check_set3 = set()
            for i, val in enumerate(row):
                if i<3 and i>=0:
                    if val != ".":
                        if val in check_set1:
                            print("f3")
                            return False
                        check_set1.add(val)
                elif i<6 and i>=3:
                    if val != ".":
                        if val in check_set2:
                            print("f4")
                            return False
                        check_set2.add(val)
                elif i < 9 and i>=6:
                    if val != ".":
                        if val in check_set3:
                            print("f5")
                            return False
                        check_set3.add(val)
        return True
            
                
