# import numpy 

def getMaxElementIndexes(a, rotate):
    indices = []
    while rotate:
        a_copy = a[:]
        rotate_num = rotate.pop(0)
        for i in range(rotate_num):
            a_copy.append(a_copy.pop(0))
        max_idx = a_copy.index(max(a_copy))
        # max_idx = numpy.argmax(a_copy)
        indices.append(max_idx)
    return indices

getMaxElementIndexes([1, 2, 4, 3, 5], [0, 2])