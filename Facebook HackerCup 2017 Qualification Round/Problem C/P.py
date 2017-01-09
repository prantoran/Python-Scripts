#https://www.facebook.com/hackercup/problem/326053454264498/

fin = open('in.txt','r')

fout = open('out.txt','w')

arr = {}

for i in range(20):
    arr[i+1]= {}
    
    for j in range(20):
        arr[i+1][j+1] = {}
        
        if j == 0:
            
            for k in range(i+1):
                
                arr[i+1][j+1][k+1]=1
        else:
            
            for k in range(i+1):

                
                    
                for x in arr[i+1][j]:
                    key = k+1+x
                    if key in arr[i+1][j+1]:
                        arr[i+1][j+1][key] += arr[i+1][j][x]
                    else:
                        arr[i+1][j+1][key] = 0
                        arr[i+1][j+1][key] += arr[i+1][j][x]
                    
t = int(fin.readline())


for ca in range(t):
    H,S = map(int,fin.readline().split())
           
    lst = fin.readline().split()
   
    ansN = 0
    ansD = 1
    
    for spell in lst:
        x = 0
        y = 0
        z = 0
        neg = False
        turn = 0
        
        for c in spell:
            if c >='0' and c<='9':
                if turn == 0:
                    x = x*10 + ord(c) - ord('0')
                elif turn == 1:
                    y = y*10 + ord(c) - ord('0')
                elif turn == 2:
                    z = z*10 + ord(c) - ord('0')
            else:
                if c == '-':
                    neg = True
                turn +=1
            
        if neg == True:
            z = -z
            
        target = H - z
        curN = 0
        curD = 0
        
        for k in arr[y][x]:
            curD += arr[y][x][k]
            if k >=target:
                curN += arr[y][x][k]
        
        
        if ansN*curD < curN*ansD:
            ansN = curN
            ansD = curD
            
    ans = float(ansN)/float(ansD)
    
    fout.write("Case #%d: %.8f"%(ca+1,ans))
    fout.write('\n')
        
    