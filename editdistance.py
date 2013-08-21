#!/usr/bin/python

"""
Algorithm explanation:
This is used to calculate the edit distance between two string:
Let the strings be food and money. The entire concept is based upon changing the string food into money by either deletion / insertion / substitution of charecter
 
	" "  F  O  O  D
   " "   0   1  2  3  4   

This means that it takes 1 edit to change "" to F, 2 edits to change "" to FO

	" "  F  O  O  D
   " "   0   1  2  3  4 
   M	 1   1	2  3  4

Converting M to "" needs 1 edit for deletion. 
Converting M to F can be from 2 ways, 1) M to "" to F which is one deletion and one inserion costing 2 edits
or 2) sub M by F, costing 1 edit. So we choose the later option since its cheaper.

Converting M to FO can be done in two ways: 1) Convert M to "" to F and F to FO: 2 edits
2)sub M by F and add O(which means "" to O): 2 edits. 
Choose either. 

So on and so forth. Build the entire dynamic programming cache and return the last. edit distance. 
This is dynamic programming.


"""

def editdist(firststring, secondstring):
	cache = []
	for i in range(0,(len(firststring) + 1)):
		if i == 0:
			temp = []
			for ranger in range(0,len(secondstring) + 1):
				temp.append(ranger)
			cache.append(temp)
		else:
			temp = []
			temp.append(i)
			for j in range(1, (len(secondstring) + 1)):
				if firststring[i - 1] == secondstring[j - 1]: 
					temp.append(min(cache[i - 1][j - 1], temp[j - 1] + 1, cache[i - 1][j] + 1))
				else:
					temp.append(min(cache[i - 1][j - 1] + 1, temp[j - 1] + 1, cache[i - 1][j] + 1))
			cache.append(temp)
	return cache[-1][-1]

def main():
	firststring = raw_input("Enter the first string")
	secondstring = raw_input("Enter the second string")
	edit_distance = editdist(firststring, secondstring)
	print "Your edit distance for the string " + firststring +" and " + secondstring + " is " + str(edit_distance)
			
if __name__ == "__main__":
	main()				
		
