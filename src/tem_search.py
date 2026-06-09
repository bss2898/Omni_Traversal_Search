def tem_search(arr,key):

    n=len(arr)

    checked=set()

    comparisons=0

    mid=n//2

    k=0

    while True:

        indices=[]

        left=k
        right=n-1-k

        if left<n:
            indices.append(left)

        if right>=0:
            indices.append(right)

        if k==1:
            indices.append(mid)

        elif k>=2:
            indices.append(mid-(k-1))
            indices.append(mid+(k-1))

        valid=[]

        for idx in indices:
            if 0<=idx<n and idx not in checked:
                checked.add(idx)
                valid.append(idx)

        if len(valid)==0:
            break

        for idx in valid:

            comparisons+=1

            if arr[idx]==key:
                return True,comparisons

        k+=1

    return False,comparisons