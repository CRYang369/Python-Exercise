'''
A 2d grid map of m rows and n colunms is initiallly filled with water.We may perform 
an addland operation which turns the water at position (row,col) into a land.
Given a list of postions to operate,count the number of islands after each addland operation.
An island is surouded by water and is formed by connecting adjacent lands horizontally or 
vertically.You may assume all four edges of the grid are all surrouded by water.
Union-find structure.Parent stores the parent island,self if not attached to any other
land.Number of unique neighbour islands are counted by ascending to ultimate parents,
updating links to grandparents to compress paths and speed futer lookups.All connected 
neighbours are combined by union.
Time O(k log*k) where log * is iterated logrithm and k is number of positions
Space O(k)


'''


class Solution:  

    def numIsland(self,m,n,position):
       # islands=[[0]*n for _ in range(m)]
       count=[0]
       roots={}   #key is (r,c) value is parent(r,c)          
       for i,j in position:
           if (i,j) in roots:
               count.append(count[-1])
               continue
           nbors=set()
           for nbor in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
               if nbor in roots:
                   island=roots[nbor]
                   while island!=roots[island]:
                       roots[island]=roots[roots[island]]
                       island=roots[island]
                   nbors.add(island)
           if not nbors:
               roots[(i,j)]=(i,j)
               count.append(count[-1]+1)
           else:
               this_island=nbors.pop()
               for nbor in nbors:
                   roots[nbor]=this_island
               roots[(i,j)]=this_island
               if count[-1]==1:
                   count.append(1)    
               else:
                   count.append(count[-1]-len(nbors))
       return count[1:]

if __name__=="__main__":
    
    position=[[0,0],[0,1],[1,2],[2,1]]
    s=Solution()
    print(s.numIsland(3,3,position))       