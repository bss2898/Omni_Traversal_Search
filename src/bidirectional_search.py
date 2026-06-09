def bidirectional_search(arr,key):

    left=0
    right=len(arr)-1

    comparisons=0

    while left<=right:

        comparisons+=1
        if arr[left]==key:
            return True,comparisons

        if left!=right:
            comparisons+=1
            if arr[right]==key:
                return True,comparisons

        left+=1
        right-=1

    return False,comparisons