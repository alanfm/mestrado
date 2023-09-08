def maxVal1(searchable):
    max = searchable[0]
    for i in searchable:
        if i > max:
            max = i
    return max

def maxVal2(searchable, start, end):
    if end - start <= 1:
        return max(searchable[start], searchable[end])
    else:
        mid = round((start + end) / 2)
        max1 = maxVal2(searchable, start, mid)
        max2 = maxVal2(searchable, mid + 1, end)
        return max(max1, max2)
    
def max(fragment1, fragment2):
    if fragment1 > fragment2:
        return fragment1
    else:
        return fragment2
