def printFunctions(fresh, used):
    
    while fresh:
        current = fresh.pop()
        print("Using: " + current.title())
        used.append(current)
    
