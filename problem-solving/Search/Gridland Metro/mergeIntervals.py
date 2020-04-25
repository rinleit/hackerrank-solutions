# Source: https://www.geeksforgeeks.org/merging-intervals/
def mergeIntervals(arr): 
    # Sorting based on the increasing order  
    # of the start intervals 
    arr.sort(key = lambda x: x[0])
    # array to hold the merged intervals 
    m = [] 
    s, end = arr[0][0], arr[0][1]
    for i in range(len(arr)): 
        a = arr[i] 
        if a[0] > end: 
            if i != 0: 
                m.append([s, end])  
            s, end = a[0], a[1]
        else: 
            end = max(a[1], end) 
    # 'end' value gives the last point of  
    #  that particular interval 
    # 's' gives the starting point of that interval 
    # 'm' array contains the list of all merged intervals 
    if [s, end] not in m: 
        m.append([s, end])
    return m 

if __name__ == "__main__":
    arr = [[1,3], [2,6], [3,7]]
    print(mergeIntervals(arr))