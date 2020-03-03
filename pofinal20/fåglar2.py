
# Python3 code to print subtree of all nodes  
  
# arrays for keeping position at  
# each dfs traversal for each node  
start = [None] * 100001 
endd = [None] * 100001
  
# Storing dfs order  
dfs_order = []  
adj = [[] for i in range(100001)]  
visited = [False] * 100001
  
# Recursive function for dfs traversal dfsUtil()  
def dfs(a, b):  
   
    # keep track of node visited  
    visited[a] = 1 
    b += 1
    start[a] = b  
    dfs_order.append(a)  
      
    for it in adj[a]:  
        if not visited[it]:  
            b = dfs(it, b)  
       
    endd[a] = b 
    return b 

n, c = 10, 0 
    
adj[0].append(1)  
adj[0].append(2)  
adj[0].append(3)  
adj[1].append(4)  
adj[1].append(5)  
adj[4].append(7)  
adj[4].append(8)  
adj[2].append(6)  
adj[6].append(9)  
    
# Calling dfs for node 0  
# Considering root node at 0  
dfs(0, c)  

# Print child nodes  
for j in range(start[0]+1, endd[0]+1):  
                print(dfs_order[j-1], end = " ")  
# This code is contributed by Rituraj Jain 
