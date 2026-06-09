def linear_search(arr,key):
    comparisons=0

    for i in range(len(arr)):
        comparisons+=1

        if arr[i]==key:
            return True,comparisons

    return False,comparisons
