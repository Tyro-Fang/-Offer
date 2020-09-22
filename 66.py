visited=[]
def HaveRoute(matrix,route):
    global visited
    if matrix==None or route==None:
        return False
    if len(matrix)<1 or len(matrix[0])<1:
        return False
    rows=len(matrix)
    cols=len(matrix[0])
    for i in range(rows*cols):
        visited.append(False)
    for i in range(rows):
        for j in range(cols):
            res=HaveRoutePerBegin(matrix,i,j,route,rows,cols)
            if res==True:
                return True
    return False


def HaveRoutePerBegin(matrix,row,col,route,rows,cols):
    global visited
    if route=='':
        return True
    if  visited[row*col+col]==True or row<0 or col<0:
        return False
    visited[row*col+col]=True
    hasRoute=False
    if row<rows and col<cols and matrix[row][col]==route[0]:
        hasRoute=HaveRoutePerBegin(matrix,row+1,col,route[1:],rows,cols) or HaveRoutePerBegin(matrix,row,col+1,route[1:],rows,cols) or HaveRoutePerBegin(matrix,row-1,col,route[1:],rows,cols) or HaveRoutePerBegin(matrix,row,col-1,route[1:],rows,cols)
    visited[row*col+col]=False
    return hasRoute



a=[['a','b','c','e'],['s','f','c','s'],['a','d','e','e']]
b='abcb'
print(HaveRoute(a,b))