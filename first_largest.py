"""
Python program to find the largest element and its location.
"""

def largest_element(a, loc=False):
    """ Return the largest element of a sequence a.
    """

    maxval= a[0]
    maxloc= 0
    for i in range(1, len(a)):
        if a[i] > maxval:
            maxval = a[i]
            maxloc =i
    if loc==True:
        return maxval, maxloc
    else:
        return maxval
     
"""    #I have no clue how to make this work or what is going on at all
def largest_el2(a, loc=False):
    maxval= a[0]
    maxloc= 0
    for (i,e) in enumerate(a):
        if e > maxval:
            maxval =e
            maxloc =i

    return maxval
"""

if  __name__ == "__main__":

    a = [1,2,3,2,1]
    print("Largest element is {} at position {}".format(*largest_element(a,True)))
    
