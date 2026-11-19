def nax(x,c,i,j):
    try:
        if x[i][j]==1:
            x[i][j]=0
            c=c+1
            if x[i][j+1]==1:
                x[i][j+1]=0
            if x[i+1][j]==1:
                x[i+1][j]=0
            if x[i][j-1]==1:
                x[i][j-1]=0
            if x[i-1][j]==1:
                x[i-1][j]=0  
    except IndexError:
        pass
    if i<len(x):
        if j<len(x):
            nax(x,c,i,j+1)
        else:
            nax(x,c,i+1,0)
    else:
        print(c) 
n=[[1,0,0,1],
   [1,0,0,0],
   [1,0,0,0],
   [1,0,0,0]]
nax(n,c=0,i=0,j=0)