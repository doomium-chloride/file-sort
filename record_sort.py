#documentation

#This is a variation of merge-sort

#sort is the main function
#it takes one list with sortable elements and creates a list of indecies.
#the modified merge-sort keeps track of the original index of each element
# and returns both the sorted list and the list of original indecies respectively


def ascend(length):
	out = list()
	for i in range(length):
		out.append(i)
	return out
def sort(victim):
	number = ascend(len(victim))
	return merge_sort(victim,number)
def merge(left,right,la,ra):
	result = []
	a = []
	while (len(left) > 0) and (len(right) > 0):
		if left[0] <= right[0]:
			result.append(left[0])
			left = left[1:]
			a.append(la[0])
			la = la[1:]
		else:
			result.append(right[0])
			right = right[1:]
			a.append(ra[0])
			ra = ra[1:]
	while len(left) > 0:
		result.append(left[0])
		left = left[1:]
		a.append(la[0])
		la = la[1:]
	while len(right) > 0:
		result.append(right[0])
		right = right[1:]
		a.append(ra[0])
		ra = ra[1:]
	return result,a
def merge_sort(x,a):
	if len(x) <= 1:
		return x,a
	left = []
	right = []
	la = []
	ra = []
	for i in range(len(x)):
		if i < len(x)/2:
			left.append(x[i])
			la.append(a[i])
		else:
			right.append(x[i])
			ra.append(a[i])
	left,la = merge_sort(left,la)
	right,ra = merge_sort(right,ra)
	return merge(left,right,la,ra)