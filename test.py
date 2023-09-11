def check_consecutive_ones(arr, consecutive_threshold):
    ones_count = 0
    print(len(arr))
    for i in range(len(arr)):
        if arr[i] == True:
            ones_count += 1
            if ones_count >= consecutive_threshold:
                if i + 1 < len(arr) and arr[i + 1] == False:
                    return True
                # else:
                #     return False
        else:
            ones_count = 0
    
    return False

array = [False, False, True, True, True, True, False]
print(check_consecutive_ones(array, 3))