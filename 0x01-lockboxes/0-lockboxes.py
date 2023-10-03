#!/usr/bin/python3
def canUnlockAll(boxes):
    #Initialize a list to keep track of visited boxes.
    visited = [False] * len(boxes)
    # Mark the first box as visited since it's already unlocked
    visited[0] = True

    #initialize a stack for for DFS and add the first box to it.
    stack = [0]

    while stack:
        current_box = stack.pop()

        #Iterate through the keys in the current box
        for key in boxes[current_box]:
            #Check if the key opens a box and if not visited
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)

    #Check if all boxes have been visited.
    return all(visited)
