houses = int(input())
points = []
for n in range(houses):
    points.append((int(a) for a in input().split()))

def ternarySearch(l, r, ar): 
	if (r >= l): 
		mid1 = l + (r - l) //3
		mid2 = r - (r - l) //3

        error = sum

		if (key < ar[mid1]): 

			# The key lies in between l and mid1 
			return ternarySearch(l, mid1 - 1, key, ar) 
		
		elif (key > ar[mid2]): 

			# The key lies in between mid2 and r 
			return ternarySearch(mid2 + 1, r, key, ar) 
		
		else: 

			# The key lies in between mid1 and mid2 
			return ternarySearch(mid1 + 1, 
								mid2 - 1, key, ar) 
		
	# Key not found 
	return -1

leftstart = -1000000
rightstart = 1000000