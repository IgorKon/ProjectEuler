<<<<<<< HEAD
# Su Doku

# Problem 96
# Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, 
# but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. 
# The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, 
# and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.
# A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods 
# in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; 
# the example above is considered easy because it can be solved by straight forward direct deduction.
# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, 
# but all with unique solutions (the first puzzle in the file is the example above).
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 
# 483 is the 3-digit number found in the top left corner of the solution grid above.
# https://projecteuler.net/problem=96

import datetime

class SudokuPoint:
    def __init__(self, value):
        self.Value = value
        if value == 0:
            self.PossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.PossibleValues = []

def Check9Digits(sud : list) -> bool:
    if len(sud) != 9:
        return False
    sud_l = list()
    for sp in sud:
        if sp.Value == 0:
            return False
        sud_l.append(sp.Value)

    if (1 in sud_l) and (2 in sud_l) and (3 in sud_l) and \
       (4 in sud_l) and (5 in sud_l) and (6 in sud_l) and \
       (7 in sud_l) and (8 in sud_l) and (9 in sud_l):
        return True
    return False

def CheckSudoku(sudoku : list) -> bool:
    i_line = 0
    for line in sudoku:
        if not Check9Digits(line):
            return False
    return True

def MakeTransposed(sudoku : list) -> list:
    sudoku_t = list()
    for i in range(9):
        column = list()
        sudoku_t.append(column)
    for line in sudoku:
        i = 0
        for d in line:
            sudoku_t[i].append(d)
            i += 1
    return sudoku_t

def Make3by3(sudoku : list) -> list:
    sudoku3by3 = list()
    for i in range(9):
        column = list()
        sudoku3by3.append(column)
    i_start = 0
    i_count = 0
    for line in sudoku:
        j_start = 0
        for i in range(3):
            for j in range(j_start, j_start + 3):
                sudoku3by3[i_start + i].append(line[j])
            j_start += 3
        i_count += 1
        if i_count % 3 == 0:
            i_start += 3
    return sudoku3by3

def DoWeNeedToContinue(sudoku : list):
    for line in sudoku:
        for d in line:
            if d.Value == 0:
                return True
    return False

def SolveSudoku(sudoku : list):
    digit = 0
    sudoku_t = MakeTransposed(sudoku)
    sudoku3by3 = Make3by3(sudoku)
    RemoveWrongPossibleValues(sudoku)
    RemoveWrongPossibleValues(sudoku_t)
    RemoveWrongPossibleValues(sudoku3by3)
    while DoWeNeedToContinue(sudoku):
        bNeedToContinueBuySingleValue = True
        while bNeedToContinueBuySingleValue:
            bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
            if bNeedToContinueBuySingleValue:
                b1 = RemoveWrongPossibleValues(sudoku)
                b2 = RemoveWrongPossibleValues(sudoku_t)
                b3 = RemoveWrongPossibleValues(sudoku3by3)
                bNeedToContinueBuySingleValue = b1 or b2 or b3

        if MakeStepBySinglePotentioalValue(sudoku):
            RemoveWrongPossibleValues(sudoku_t)
            RemoveWrongPossibleValues(sudoku3by3)

        if MakeStepBySinglePotentioalValue(sudoku_t):
            RemoveWrongPossibleValues(sudoku)
            RemoveWrongPossibleValues(sudoku3by3)

        if MakeStepBySinglePotentioalValue(sudoku3by3):
            RemoveWrongPossibleValues(sudoku)
            RemoveWrongPossibleValues(sudoku_t)

        if RemovePossibleValuesBySegment(sudoku, sudoku3by3, False):
            bNeedToContinueBuySingleValue = True
            while bNeedToContinueBuySingleValue:
                bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
                if bNeedToContinueBuySingleValue:
                    b1 = RemoveWrongPossibleValues(sudoku)
                    b2 = RemoveWrongPossibleValues(sudoku_t)
                    b3 = RemoveWrongPossibleValues(sudoku3by3)
                    bNeedToContinueBuySingleValue = b1 or b2 or b3


        if RemovePossibleValuesBySegment(sudoku_t, sudoku3by3, True):
            bNeedToContinueBuySingleValue = True
            while bNeedToContinueBuySingleValue:
                bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
                if bNeedToContinueBuySingleValue:
                    b1 = RemoveWrongPossibleValues(sudoku)
                    b2 = RemoveWrongPossibleValues(sudoku_t)
                    b3 = RemoveWrongPossibleValues(sudoku3by3)
                    bNeedToContinueBuySingleValue = b1 or b2 or b3
        
        if RemovePossibleValuesBySegmentByException(sudoku, sudoku3by3, False):
            bNeedToContinueBuySingleValue = True
            while bNeedToContinueBuySingleValue:
                bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
                if bNeedToContinueBuySingleValue:
                    b1 = RemoveWrongPossibleValues(sudoku)
                    b2 = RemoveWrongPossibleValues(sudoku_t)
                    b3 = RemoveWrongPossibleValues(sudoku3by3)
                    bNeedToContinueBuySingleValue = b1 or b2 or b3

        if RemovePossibleValuesBySegmentByException(sudoku_t, sudoku3by3, True):
            bNeedToContinueBuySingleValue = True
            while bNeedToContinueBuySingleValue:
                bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
                if bNeedToContinueBuySingleValue:
                    b1 = RemoveWrongPossibleValues(sudoku)
                    b2 = RemoveWrongPossibleValues(sudoku_t)
                    b3 = RemoveWrongPossibleValues(sudoku3by3)
                    bNeedToContinueBuySingleValue = b1 or b2 or b3

    if CheckSudoku(sudoku) and CheckSudoku(sudoku_t) and CheckSudoku(sudoku3by3):
        digit = 100 * sudoku[0][0].Value + 10 * sudoku[0][1].Value + sudoku[0][2].Value
    else:
        print("ERROR!!!")
    return digit

def RemoveWrongPossibleValues(sudoku : list) -> bool:
    bResult = False
    for line in sudoku:
        for d1 in line:
            if d1.Value != 0:
                continue
            for d2 in line:
                if d2.Value == 0:
                    continue
                if d2.Value in d1.PossibleValues:
                    d1.PossibleValues.remove(d2.Value)
                    bResult = True
    return bResult

def RemovePossibleValuesBySegment(sudoku : list, sudoku3by3 : list, bTransposed: bool) -> bool:
    bResult = False
    for d in range(1, 10):
        for i in range(9):
            line = sudoku[i]
            if d in line:
                continue
            for m in range(3):
                if bTransposed:
                    sudoku3by3_for_line_3 = sudoku3by3[ (i // 3) + m * 3]
                else:
                    sudoku3by3_for_line_3 = sudoku3by3[ 3 * (i // 3) + m]
                if d in sudoku3by3_for_line_3:
                    continue
                line_3 = line[3 * m : 3 * m + 3]
                line_minus3 = line[:]
                del line_minus3[3 * m : 3 * m + 3]
                bInLine3PossibleValues = False
                for j in range(3):
                    if d in line_3[j].PossibleValues:
                        bInLine3PossibleValues = True
                        break
                if bInLine3PossibleValues:
                    bInSudoku3by3ForLine3PossibleValues = False
                    addition_for_sudoku3by3_for_line_3 = sudoku3by3_for_line_3[:]
                    for j in range(3):
                        addition_for_sudoku3by3_for_line_3.remove(line_3[j])
                    for sp in addition_for_sudoku3by3_for_line_3:
                        if d in sp.PossibleValues:
                            bInSudoku3by3ForLine3PossibleValues = True
                            break
                    if not bInSudoku3by3ForLine3PossibleValues:
                        for sp in line_minus3:
                            if d in sp.PossibleValues:
                                sp.PossibleValues.remove(d)
                                bResult = True
    return bResult

def RemovePossibleValuesBySegmentByException(sudoku : list, sudoku3by3 : list, bTransposed: bool) -> bool:
    bResult = False
    for d in range(1, 10):
        for i in range(9):
            line = sudoku[i]
            if d in line:
                continue
            for m in range(3):
                if bTransposed:
                    sudoku3by3_for_line_3 = sudoku3by3[ (i // 3) + m * 3]
                else:
                    sudoku3by3_for_line_3 = sudoku3by3[ 3 * (i // 3) + m]
                if d in sudoku3by3_for_line_3:
                    continue
                line_3 = line[3 * m : 3 * m + 3]
                line_minus3 = line[:]
                del line_minus3[3 * m : 3 * m + 3]
                bInLine3PossibleValues = False
                for j in range(3):
                    if d in line_3[j].PossibleValues:
                        bInLine3PossibleValues = True
                        break
                if bInLine3PossibleValues:
                    bInLineMinus3PossibleValues = False
                    for j in range(6):
                        if d in line_minus3[j].PossibleValues:
                            bInLineMinus3PossibleValues = True
                            break
                    if not bInLineMinus3PossibleValues:
                        addition_for_sudoku3by3_for_line_3 = sudoku3by3_for_line_3[:]
                        for j in range(3):
                            addition_for_sudoku3by3_for_line_3.remove(line_3[j])
                        for sp in addition_for_sudoku3by3_for_line_3:
                            if d in sp.PossibleValues:
                                sp.PossibleValues.remove(d)
                                bResult = True
    return bResult

def MakeStepBySingleValue(sudoku : list) -> bool:
    # set value if we have singe potential variant only
    bResult = False
    for line in sudoku:
        for d in line:
            if d.Value == 0 and len(d.PossibleValues) == 1:
                d.Value = d.PossibleValues[0]
                d.PossibleValues.remove(d.Value)
                bResult = True
    return bResult

def MakeStepBySinglePotentioalValue(sudoku : list) -> bool:
    bResult = False
    # if value is in one PossibleValues for line only - set it and clear all other PossibleValues
    count_list = list()
    for i in range(10):
        index_list = list()
        count_list.append(index_list)
    for line in sudoku:
        for i in range(1, 10):
            for j in range(9):
                if i in line[j].PossibleValues:
                    count_list[i].append(j)
        for i in range(1, 10):
            index_list = count_list[i]
            if len(index_list) == 1:
                index = index_list[0]
                line[index].Value = i
                line[index].PossibleValues.clear()
                bResult = True
            index_list.clear()
    return bResult

start_time = datetime.datetime.now()
nums = list()
f = open('num96.txt') 
lines = f.readlines()
j = 0
sudoku = list()
summ = 0
count = 0
for line in lines:
    if 'Grid' in line:
        continue
    i = 0
    nums.clear()
    for s in line:
        nums.append(SudokuPoint(int(s)))
        i += 1
        if i == 9:
            break
    sudoku.append(nums[:])
    j += 1
    if j == 9:
        j = 0
        summ += SolveSudoku(sudoku)
        sudoku.clear()
        count += 1
        print(count)
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(count, summ)

=======
# Su Doku

# Problem 96
# Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, 
# but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. 
# The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, 
# and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.
# A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods 
# in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; 
# the example above is considered easy because it can be solved by straight forward direct deduction.
# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, 
# but all with unique solutions (the first puzzle in the file is the example above).
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 
# 483 is the 3-digit number found in the top left corner of the solution grid above.
# https://projecteuler.net/problem=96

import datetime

class SudokuPoint:
    def __init__(self, value):
        self.Value = value
        if value == 0:
            self.PossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.PossibleValues = []

def Check9Digits(sud : list) -> bool:
    if len(sud) != 9:
        return False
    sud_l = list()
    for sp in sud:
        if sp.Value == 0:
            return False
        sud_l.append(sp.Value)

    if (1 in sud_l) and (2 in sud_l) and (3 in sud_l) and \
       (4 in sud_l) and (5 in sud_l) and (6 in sud_l) and \
       (7 in sud_l) and (8 in sud_l) and (9 in sud_l):
        return True
    return False

def CheckSudoku(sudoku : list) -> bool:
    i_line = 0
    for line in sudoku:
        if not Check9Digits(line):
            return False
    return True

def MakeTransposed(sudoku : list) -> list:
    sudoku_t = list()
    for i in range(9):
        column = list()
        sudoku_t.append(column)
    for line in sudoku:
        i = 0
        for d in line:
            sudoku_t[i].append(d)
            i += 1
    return sudoku_t

def Make3by3(sudoku : list) -> list:
    sudoku3by3 = list()
    for i in range(9):
        column = list()
        sudoku3by3.append(column)
    i_start = 0
    i_count = 0
    for line in sudoku:
        j_start = 0
        for i in range(3):
            for j in range(j_start, j_start + 3):
                sudoku3by3[i_start + i].append(line[j])
            j_start += 3
        i_count += 1
        if i_count % 3 == 0:
            i_start += 3
    return sudoku3by3

def DoWeNeedToContinue(sudoku : list):
    for line in sudoku:
        for d in line:
            if d.Value == 0:
                return True
    return False

def SolveSudoku(sudoku : list):
    digit = 0
    sudoku_t = MakeTransposed(sudoku)
    sudoku3by3 = Make3by3(sudoku)
    RemoveWrongPossibleValues(sudoku)
    RemoveWrongPossibleValues(sudoku_t)
    RemoveWrongPossibleValues(sudoku3by3)
    while DoWeNeedToContinue(sudoku):
        bNeedToContinueBuySingleValue = True
        while bNeedToContinueBuySingleValue:
            bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
            if bNeedToContinueBuySingleValue:
                b1 = RemoveWrongPossibleValues(sudoku)
                b2 = RemoveWrongPossibleValues(sudoku_t)
                b3 = RemoveWrongPossibleValues(sudoku3by3)
                bNeedToContinueBuySingleValue = b1 or b2 or b3

        if MakeStepBySinglePotentioalValue(sudoku):
            RemoveWrongPossibleValues(sudoku_t)
            RemoveWrongPossibleValues(sudoku3by3)

        if MakeStepBySinglePotentioalValue(sudoku_t):
            RemoveWrongPossibleValues(sudoku)
            RemoveWrongPossibleValues(sudoku3by3)

        if MakeStepBySinglePotentioalValue(sudoku3by3):
            RemoveWrongPossibleValues(sudoku)
            RemoveWrongPossibleValues(sudoku_t)

        if RemovePossibleValuesBySegment(sudoku, sudoku3by3, False):
            bNeedToContinueBuySingleValue = True
            while bNeedToContinueBuySingleValue:
                bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
                if bNeedToContinueBuySingleValue:
                    b1 = RemoveWrongPossibleValues(sudoku)
                    b2 = RemoveWrongPossibleValues(sudoku_t)
                    b3 = RemoveWrongPossibleValues(sudoku3by3)
                    bNeedToContinueBuySingleValue = b1 or b2 or b3


        if RemovePossibleValuesBySegment(sudoku_t, sudoku3by3, True):
            bNeedToContinueBuySingleValue = True
            while bNeedToContinueBuySingleValue:
                bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
                if bNeedToContinueBuySingleValue:
                    b1 = RemoveWrongPossibleValues(sudoku)
                    b2 = RemoveWrongPossibleValues(sudoku_t)
                    b3 = RemoveWrongPossibleValues(sudoku3by3)
                    bNeedToContinueBuySingleValue = b1 or b2 or b3
        
        if RemovePossibleValuesBySegmentByException(sudoku, sudoku3by3, False):
            bNeedToContinueBuySingleValue = True
            while bNeedToContinueBuySingleValue:
                bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
                if bNeedToContinueBuySingleValue:
                    b1 = RemoveWrongPossibleValues(sudoku)
                    b2 = RemoveWrongPossibleValues(sudoku_t)
                    b3 = RemoveWrongPossibleValues(sudoku3by3)
                    bNeedToContinueBuySingleValue = b1 or b2 or b3

        if RemovePossibleValuesBySegmentByException(sudoku_t, sudoku3by3, True):
            bNeedToContinueBuySingleValue = True
            while bNeedToContinueBuySingleValue:
                bNeedToContinueBuySingleValue = MakeStepBySingleValue(sudoku)
                if bNeedToContinueBuySingleValue:
                    b1 = RemoveWrongPossibleValues(sudoku)
                    b2 = RemoveWrongPossibleValues(sudoku_t)
                    b3 = RemoveWrongPossibleValues(sudoku3by3)
                    bNeedToContinueBuySingleValue = b1 or b2 or b3

    if CheckSudoku(sudoku) and CheckSudoku(sudoku_t) and CheckSudoku(sudoku3by3):
        digit = 100 * sudoku[0][0].Value + 10 * sudoku[0][1].Value + sudoku[0][2].Value
    else:
        print("ERROR!!!")
    return digit

def RemoveWrongPossibleValues(sudoku : list) -> bool:
    bResult = False
    for line in sudoku:
        for d1 in line:
            if d1.Value != 0:
                continue
            for d2 in line:
                if d2.Value == 0:
                    continue
                if d2.Value in d1.PossibleValues:
                    d1.PossibleValues.remove(d2.Value)
                    bResult = True
    return bResult

def RemovePossibleValuesBySegment(sudoku : list, sudoku3by3 : list, bTransposed: bool) -> bool:
    bResult = False
    for d in range(1, 10):
        for i in range(9):
            line = sudoku[i]
            if d in line:
                continue
            for m in range(3):
                if bTransposed:
                    sudoku3by3_for_line_3 = sudoku3by3[ (i // 3) + m * 3]
                else:
                    sudoku3by3_for_line_3 = sudoku3by3[ 3 * (i // 3) + m]
                if d in sudoku3by3_for_line_3:
                    continue
                line_3 = line[3 * m : 3 * m + 3]
                line_minus3 = line[:]
                del line_minus3[3 * m : 3 * m + 3]
                bInLine3PossibleValues = False
                for j in range(3):
                    if d in line_3[j].PossibleValues:
                        bInLine3PossibleValues = True
                        break
                if bInLine3PossibleValues:
                    bInSudoku3by3ForLine3PossibleValues = False
                    addition_for_sudoku3by3_for_line_3 = sudoku3by3_for_line_3[:]
                    for j in range(3):
                        addition_for_sudoku3by3_for_line_3.remove(line_3[j])
                    for sp in addition_for_sudoku3by3_for_line_3:
                        if d in sp.PossibleValues:
                            bInSudoku3by3ForLine3PossibleValues = True
                            break
                    if not bInSudoku3by3ForLine3PossibleValues:
                        for sp in line_minus3:
                            if d in sp.PossibleValues:
                                sp.PossibleValues.remove(d)
                                bResult = True
    return bResult

def RemovePossibleValuesBySegmentByException(sudoku : list, sudoku3by3 : list, bTransposed: bool) -> bool:
    bResult = False
    for d in range(1, 10):
        for i in range(9):
            line = sudoku[i]
            if d in line:
                continue
            for m in range(3):
                if bTransposed:
                    sudoku3by3_for_line_3 = sudoku3by3[ (i // 3) + m * 3]
                else:
                    sudoku3by3_for_line_3 = sudoku3by3[ 3 * (i // 3) + m]
                if d in sudoku3by3_for_line_3:
                    continue
                line_3 = line[3 * m : 3 * m + 3]
                line_minus3 = line[:]
                del line_minus3[3 * m : 3 * m + 3]
                bInLine3PossibleValues = False
                for j in range(3):
                    if d in line_3[j].PossibleValues:
                        bInLine3PossibleValues = True
                        break
                if bInLine3PossibleValues:
                    bInLineMinus3PossibleValues = False
                    for j in range(6):
                        if d in line_minus3[j].PossibleValues:
                            bInLineMinus3PossibleValues = True
                            break
                    if not bInLineMinus3PossibleValues:
                        addition_for_sudoku3by3_for_line_3 = sudoku3by3_for_line_3[:]
                        for j in range(3):
                            addition_for_sudoku3by3_for_line_3.remove(line_3[j])
                        for sp in addition_for_sudoku3by3_for_line_3:
                            if d in sp.PossibleValues:
                                sp.PossibleValues.remove(d)
                                bResult = True
    return bResult

def MakeStepBySingleValue(sudoku : list) -> bool:
    # set value if we have singe potential variant only
    bResult = False
    for line in sudoku:
        for d in line:
            if d.Value == 0 and len(d.PossibleValues) == 1:
                d.Value = d.PossibleValues[0]
                d.PossibleValues.remove(d.Value)
                bResult = True
    return bResult

def MakeStepBySinglePotentioalValue(sudoku : list) -> bool:
    bResult = False
    # if value is in one PossibleValues for line only - set it and clear all other PossibleValues
    count_list = list()
    for i in range(10):
        index_list = list()
        count_list.append(index_list)
    for line in sudoku:
        for i in range(1, 10):
            for j in range(9):
                if i in line[j].PossibleValues:
                    count_list[i].append(j)
        for i in range(1, 10):
            index_list = count_list[i]
            if len(index_list) == 1:
                index = index_list[0]
                line[index].Value = i
                line[index].PossibleValues.clear()
                bResult = True
            index_list.clear()
    return bResult

start_time = datetime.datetime.now()
nums = list()
f = open('num96.txt') 
lines = f.readlines()
j = 0
sudoku = list()
summ = 0
count = 0
for line in lines:
    if 'Grid' in line:
        continue
    i = 0
    nums.clear()
    for s in line:
        nums.append(SudokuPoint(int(s)))
        i += 1
        if i == 9:
            break
    sudoku.append(nums[:])
    j += 1
    if j == 9:
        j = 0
        summ += SolveSudoku(sudoku)
        sudoku.clear()
        count += 1
        print(count)
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(count, summ)

>>>>>>> e63783501799e7f656276cc38d76c9b32d2fdae4
