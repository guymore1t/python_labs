def transpose(mat: list[list[float or int]]) -> list[list]:
    if len(mat) == 0:
        return []
    
    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError
        
    res = []

    row_cnt = len(mat)
    stolb_cnt = len(mat[0])

    for stolb_index in range(stolb_cnt):
        new_row = []
        for row_index in range(row_cnt):
            new_row.append(mat[row_index][stolb_index])
        res.append(new_row)

    return res

def row_sums(mat: list[list[float or int]]) -> list[float]:

    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError
        
    res = [sum(row) for row in mat]

    return res

def col_sums(mat: list[list[float | int]]) -> list[float]:

    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError

    res = [sum(row) for row in zip(*mat)]

    return res






    
        






        



        


        
    
