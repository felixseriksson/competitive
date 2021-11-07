r, c, l = [int(x) for x in input().split()]

# Base node of segment tree. 
ini_seg = [[ 0 for x in range(1000)] for y in range(1000)]

# final 2d-segment tree. 
fin_seg = [[ 0 for x in range(1000)] for y in range(1000)]

# # Rectangular matrix.
# rect= [[ 1, 2, 3, 4 ],
#        [ 5, 6, 7, 8 ],
#        [ 1, 7, 5, 9 ],
#        [ 3, 0, 6, 2 ]]

rect = [[int(x) for x in input().split()] for _ in range(r)]

  
# # size of x coordinate.
# size = 4
size = c

'''
* A recursive function that constructs 
* Inital Segment Tree for array rect[][] = { }. 
* 'pos' is index of current node in segment  
* tree seg[]. 'strip' is the enumeration  
* for the y-axis. 
'''
def segment(low, high, pos, strip): 
    if (high == low) : 
        ini_seg[strip][pos] = rect[strip][low] 
    else : 
        mid = (low + high) // 2
        segment(low, mid, 2 * pos, strip) 
        segment(mid + 1, high, 2 * pos + 1, strip) 
        ini_seg[strip][pos] = (ini_seg[strip][2 * pos] + ini_seg[strip][2 * pos + 1])

# A recursive function that constructs  
# Final Segment Tree for array ini_seg[][] = { }. 
def finalSegment(low, high, pos): 
    if (high == low) : 
        for i in range(1, 2 * size): 
            fin_seg[pos][i] = ini_seg[low][i] 
    else : 
        mid = (low + high) // 2
        finalSegment(low, mid, 2 * pos) 
        finalSegment(mid + 1, high, 2 * pos + 1) 
        for i in range( 1, 2 * size): 
            fin_seg[pos][i] = (fin_seg[2 * pos][i] + fin_seg[2 * pos + 1][i]) 
'''  
* Return sum of elements in range  
* from index x1 to x2 . It uses the  
* final_seg[][] array created using  
* finalsegment() function. 'pos' is  
* index of current node in segment  
* tree fin_seg[][]. 
'''

def minfinalQuery(pos, start, end, x1, x2, node): 
    if (x2 < start or end < x1) : 
        return 0
    if (x1 <= start and end <= x2) : 
        return fin_seg[node][pos] 
    mid = (start + end) // 2
    p1 = minfinalQuery(2 * pos, start, mid, x1, x2, node) 
    p2 = minfinalQuery(2 * pos + 1, mid + 1, end, x1, x2, node) 
    return min(p1, p2)

'''  
* This function calls the finalQuery function 
* for elements in range from index x1 to x2 . 
* This function queries the yth coordinate. 
'''
def minquery(pos, start, end, y1, y2, x1, x2): 
    if (y2 < start or end < y1) : 
        return 0
    if (y1 <= start and end <= y2) : 
        return (minfinalQuery(1, 1, c-1, x1, x2, pos)) 
    mid = (start + end) // 2
    p1 = minquery(2 * pos, start, mid, y1, y2, x1, x2) 
    p2 = minquery(2 * pos + 1, mid + 1, end, y1, y2, x1, x2) 
    return min(p1, p2)

pos = 1
low = 0
high = c-1

# Call the ini_segment() to create the 
# inital segment tree on x- coordinate 
for strip in range(c): 
    segment(low, high, 1, strip) 
# Call the final function to built  
# the 2d segment tree. 
finalSegment(low, high, 1) 
''' 
Query: 
* To request the query for sub-rectangle  
* y1, y2=(2, 3) x1, x2=(2, 3) 
* update the value of index (3, 3)=100; 
* To request the query for sub-rectangle  
* y1, y2=(2, 3) x1, x2=(2, 3) 
'''
print( "The min of the submatrix (y1, y2)->(2, 3), ", 
       "(x1, x2)->(2, 3) is ", minquery(1, 0, c, 2, 2, 1, 1))