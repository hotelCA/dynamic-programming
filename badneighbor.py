'''
Problem Statement

The old song declares "Go ahead and hate your neighbor", and the residents of Onetinville have taken those words to heart. Every resident hates his next-door neighbors on both sides. Nobody is willing to live farther away from the town's well than his neighbors, so the town has been arranged in a big circle around the well. Unfortunately, the town's well is in disrepair and needs to be restored. You have been hired to collect donations for the Save Our Well fund.

Each of the town's residents is willing to donate a certain amount, as specified in the int[] donations, which is listed in clockwise order around the well. However, nobody is willing to contribute to a fund to which his neighbor has also contributed. Next-door neighbors are always listed consecutively in donations, except that the first and last entries in donations are also for next-door neighbors. You must calculate and return the maximum amount of donations that can be collected.


Definition

Class:	BadNeighbors
Method:	maxDonations
Parameters:	int[]
Returns:	int
Method signature:	int maxDonations(int[] donations)
(be sure your method is public)


Constraints
-	donations contains between 2 and 40 elements, inclusive.
-	Each element in donations is between 1 and 1000, inclusive.

Examples
0)

 { 10, 3, 2, 5, 7, 8 }
Returns: 19
The maximum donation is 19, achieved by 10+2+7. It would be better to take 10+5+8 except that the 10 and 8 donations are from neighbors.
1)

{ 11, 15 }
Returns: 15
2)

{ 7, 7, 7, 7, 7, 7, 7 }
Returns: 21
3)

{ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 }
Returns: 16
4)

{ 94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 }
Returns: 2926


PSEUDOCODE:

neighbors = [None]
maxAtNeighbor =[[neighbors[0], neighbors[1], neighbors[2]]]

for i-th neighbor starting at index 3 going up
    find maxAtNeighbor[i] {
        for j-th neighbor starting at i - 2 going down
            break out of loop if i-th is last index and j-th is first
            if neighbors[i] + maxAtNeighbor[j] > maxAtNeighbor[i]
                maxAtNeighbor[i] = neighbors[i] + maxAtNeighbor[j]
    }

return max value in maxAtNeighbor
'''
import copy

neighbors = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]

def bad_neighbors():
    max_at_neighbor = copy.deepcopy(neighbors)
    last_neighbor_index = len(max_at_neighbor) - 1
    first_neighbor_included = [True, False]

    for i in range(2, len(neighbors)):
        for j in range (i-2, -1, -1):
            if i == (last_neighbor_index) and j == 0:
                # No need to add the first and the last neighbors since they are actual neighbors
                #print "Break"
                break
            elif neighbors[i] + max_at_neighbor[j] > max_at_neighbor[i]:
                max_at_neighbor[i] = neighbors[i] + max_at_neighbor[j]
                first_neighbor_included.append(first_neighbor_included[j])
                #print max_at_neighbor[i]

    if len(max_at_neighbor) > 3:
        if first_neighbor_included[last_neighbor_index]:
            # If the last neighbor includes a sequence that contains the first neighbor,
            # then remove one of them (one that has smaller contribution)
            max_at_neighbor[last_neighbor_index] -= min(neighbors[0], neighbors[last_neighbor_index])

    #print max_at_neighbor
    #print first_neighbor_included

    return max(max_at_neighbor)

print "Max donation = {}".format(bad_neighbors())