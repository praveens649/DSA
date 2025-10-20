def finalValueAfterOperations(operations):
    n=0
    for i in operations:
        if i in ["X++","++X"]:
            n+=1
        else:
            n-=1
    return n

print(finalValueAfterOperations(["X++","++X","--X","X++"]))