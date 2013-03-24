class sort:
    def __init__(self):
        pass
    def sort(self, lst):
        for i in range(0,len(lst)):
	    #import pdb;pdb.set_trace()
	    for j in range(i,len(lst)):
		if lst[i]>lst[j]:
		    temp=lst[i]
		    lst[i]=lst[j]
		    lst[j]=temp
	return lst

class search(sort):
    def __init__(self):
        pass
    def search(self, element, lst):
        #import pdb;pdb.set_trace()
        lst = sort.sort(self, lst)
	print lst
        for i in lst:
	    if element==i:
                print 'The element %d find at %d index' %(element,lst.index(i))
		break
	else:
	    print element,'is not in the list'

s=search()
s.search(8,[1,6,8,3,6,9])
        
