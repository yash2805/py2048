import random,copy,os,sys
n=5
w=2048
list=[]
sys.setrecursionlimit(10**8)
def input_mat_win():
    global n,w
    n = int(input("ENTER THE SIZE OF MATRIX"))
    w = int(input("ENTER WINNING NUMBER"))

def def_cus():
    global n,w,list
    c = input("DO YOU WANT DEFAULT INPUT OR CUSTOM Y/N").upper()
    if c=='Y':
        input_mat_win()
        row,col=(n,n)
        list=[[0 for i in range(col)] for j in range(row)]

    else:
        n=5
        w=2048
        row,col=(n,n)
        list=[[0 for i in range(col)] for j in range(row)]

def disp(mat):
    for i in mat:
        for j in i:
            print(j,end ="    ")
        print ("\n \n")
def chk_win(mat,w):
    for i in mat:
        for j in i:
            if j==w:
                return True
    return False
def right_shift(mat,g):
    global n
    x = g
    for i in range(n):
        for j in range(n-1):
            if mat[i][j+1]==0:
                mat[i][j+1]=mat[i][j]
                mat[i][j]=0
    if x == int(n/2):
        return mat
    else:
        return right_shift(mat,g+1)
def left_shift(mat,g):
    global n
    x = g
    for i in range(n):
        for j in range(n-1):
            if mat[i][j]==0:
                mat[i][j]=mat[i][j+1]
                mat[i][j+1]=0
    if x == int(n/2):
        return mat
    else:
        return left_shift(mat,g+1)
def up_shift(mat,g):
    global n
    x = g
    for i in range(n-1):
        for j in range(n):
            if mat[i][j]==0:
                mat[i][j]=mat[i+1][j]
                mat[i+1][j]=0
    if x == int(n/2):
        return mat
    else:
        return up_shift(mat,g+1)
        
def down_shift(mat,g):
    global n
    x = g
    for i in reversed(range(n-1)):
        for j in range(n):
            if mat[i+1][j]==0:
                mat[i+1][j]=mat[i][j]
                mat[i][j]=0
    if x == int(n/2):
        return mat
    else:
        return down_shift(mat,g+1)
def right_add(mat):
    global n
    for i in range(n):
        for j in reversed(range(0,n-1)):
            if mat[i][j+1]==mat[i][j]:
                mat[i][j+1]*=2
                mat[i][j]=0
    return(right_shift(mat,1))

def left_add(mat):
    global n
    for i in range(n):
        for j in range(n-1):
            if mat[i][j+1]==mat[i][j]:
                mat[i][j]*=2
                mat[i][j+1]=0
    return left_shift(mat,1)
def up_add(mat):
    global n
    for i in range(n-1):
        for j in range(n):
            if mat[i+1][j]==mat[i][j]:
                mat[i][j]*=2
                mat[i+1][j]=0
    return up_shift(mat,1)
def down_add(mat):
    global n
    for i in reversed(range(0,n-1)):
        for j in range(n):
            if mat[i+1][j]==mat[i][j]:
                mat[i+1][j]*=2
                mat[i][j]=0
    return down_shift(mat,1)
def rand_add(mat,n):
    x = random.randint(0,n-1)
    y = random.randint(0,n-1)
    while True:
        if mat[x][y] == 0:
            mat[x][y]=2
            break 

def chk_right(mat):
    mat1=copy.deepcopy(mat)
    mat1=right_add(right_shift(mat1,1))
    if mat1==mat:
        mat1.clear()
        return False
    else :
        mat1.clear()
        return True

def chk_left(mat):
    mat1=copy.deepcopy(mat)
    mat1=left_add(left_shift(mat1,1))
    
    if mat1==mat:
        mat1.clear()
        return False
    else :
        del mat1
        return True
def chk_up(mat):
    mat1=copy.deepcopy(mat)
    mat1=up_add(up_shift(mat1,1))
    if mat1==mat:
        mat1.clear()
        return False 
    else :
        mat1.clear()
        return True
def chk_down(mat):
    mat1=copy.deepcopy(mat)
    mat1=down_add(down_shift(mat1,1))
    if mat1==mat:
        mat1.clear()
        return False
    else:
        mat1.clear()
        return True
def chk_lost(mat):
    temp1=chk_right(mat)
    temp2=chk_left(mat)
    temp3=chk_up(mat)
    temp=chk_down(mat)
    if temp1==False and temp2==False and temp3==False and temp4==False:
        return True
    else :
        return False

def_cus()
rand_add(list,n)
disp(list)
flag=0
while True:
    mat1=copy.deepcopy(list)
    if n==1:
        if w==2:
            print("YOU HAVE WON")
            def_cus()
            rand_add(list,n)
            disp(list)
        else:
            print("YOU HAVE LOST")
            def_cus()
            rand_add(list,n)
            disp(list)
    elif n>1 :
        if chk_win(list,w):
            print("YOU HAVE WON")
            def_cus()
            rand_add(list,n)
            disp(list)
        elif chk_lost(list):
            print("YOU HAVE LOST")
            def_cus()
            rand_add(list,n)
            disp(list)
        else :
            
            if flag==0:
                c = input("\n \tENTER CHARACTER W A S D").upper()
            flag = 0    
            if c == "W":
                if chk_up(mat1)==True:
                   rand_add(up_add(up_shift(list,1)),n)
                    
                else :
                    print("INVALID MOVE")
                    c = input("\n \tENTER CHARACTER W A S D").upper()
                    flag=1
            elif c == "S":
                if chk_down(mat1)==True:
                   rand_add(down_add(down_shift(list,1)),n)
                else:
                    print("INVALID MOVE")
                    c = input("\n \tENTER CHARACTER W A S D").upper()
                    flag=1
            elif c == "A":
                if chk_left(mat1)==True:
                    rand_add(left_add(left_shift(list,1)),n)
                else :
                    print("INVALID MOVE")
                    c = input("\n \tENTER CHARACTER W A S D").upper()
                    flag=1
            elif c == "D":
                if chk_right(mat1)==True:
                    rand_add(right_add(right_shift(list,1)),n)
                else :
                    print("INVALID MOVE")
                    c = input("\n \tENTER CHARACTER W A S D").upper()
                    flag=1
            else :
                c = input("\n \t PLEASE ENTER CHARACTERS IN W A S D").upper()
                flag=1
        disp(list)
        


