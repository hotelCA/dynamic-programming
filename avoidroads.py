'''Problem Statement
    	Problem contains images. Plugin users can view them in the applet.

In the city, roads are arranged in a grid pattern. Each point on the grid represents a corner where two blocks meet. The points are connected by line segments which represent the various street blocks. Using the cartesian coordinate system, we can assign a pair of integers to each corner as shown below. 



 

You are standing at the corner with coordinates 0,0. Your destination is at corner width,height. You will return the number of distinct paths that lead to your destination. Each path must use exactly width+height blocks. In addition, the city has declared certain street blocks untraversable. These blocks may not be a part of any path. You will be given a String[] bad describing which blocks are bad. If (quotes for clarity) "a b c d" is an element of bad, it means the block from corner a,b to corner c,d is untraversable. For example, let's say
width  = 6
length = 6
bad = {"0 0 0 1","6 6 5 6"}
The picture below shows the grid, with untraversable blocks darkened in black. A sample path has been highlighted in red.



 

 
Definition
    	
Class:	AvoidRoads
Method:	numWays
Parameters:	int, int, String[]
Returns:	long
Method signature:	long numWays(int width, int height, String[] bad)
(be sure your method is public)
    
 
Constraints
-	width will be between 1 and 100 inclusive.
-	height will be between 1 and 100 inclusive.
-	bad will contain between 0 and 50 elements inclusive.
-	Each element of bad will contain between 7 and 14 characters inclusive.
-	Each element of the bad will be in the format "a b c d" where,
a,b,c,d are integers with no extra leading zeros,
a and c are between 0 and width inclusive,
b and d are between 0 and height inclusive,
and a,b is one block away from c,d.
-	The return value will be between 0 and 2^63-1 inclusive.
 
Examples
0)	
    	
6
6
{"0 0 0 1","6 6 5 6"}
Returns: 252
Example from above.
1)	
    	
1
1
{}
Returns: 2
Four blocks aranged in a square. Only 2 paths allowed.
2)	
    	
35
31
{}
Returns: 6406484391866534976
Big number.
3)	
    	
2
2
{"0 0 1 0", "1 2 2 2", "1 1 2 1"}
Returns: 0
'''

def add_to_dict(new_element, a_dict):
    a, b, c, d = [int(a_string) for a_string in new_element.split()]
    # print("a = {}, b = {}, c = {}, d = {}".format(a,b,c,d))
    # print(a + b)
    new_key = [a, b]
    new_value = [c, d]

    if a > c:
        new_key = [c, d]
        new_value = [a, b]
    elif a == c:
        if b > d:
            new_key = [c, d]
            new_value = [a, b]
        elif b == d:
            raise ValueError('Illegal element')

    if tuple(new_key) in a_dict:
        a_dict[tuple(new_key)].append(tuple(new_value))
    else:
        a_dict[tuple(new_key)] = [tuple(new_value)]


def create_dictionary(a_list):
    # Assume the list is in a form {"0 0 1 0", "1 2 2 2", "1 1 2 1"}
    # Create a dictionary with keys being the start of the path and values being an array of ends of the path since
    # Each starting point can have 2 paths.
    a_dict = {}

    for element in a_list:
        add_to_dict(element, a_dict)

    return a_dict

def is_blocked(a_key, a_value, roads_to_avoid):
    if not a_key in roads_to_avoid:
        return False
    else:
        # print("key = {}, value = {}".format(a_key, a_value))
        for value in roads_to_avoid[a_key]:
            if value == a_value:
                return True
        return False

def avoid_roads(avoid_road_list, destination):
    roads_to_avoid = create_dictionary(avoid_road_list)
    print(roads_to_avoid)
    w, h = destination
    road_map = [[0 for x in range(h + 1)] for y in range(w + 1)]
    road_map[0][0] = 1

    for i in range(w + 1):
        for j in range (h + 1):
            if i != 0 and road_map[i-1][j] != 0:
                if not is_blocked((i-1, j), (i, j),roads_to_avoid):
                    road_map[i][j] += road_map[i-1][j]
            if j != 0 and road_map[i][j-1] != 0:
                if not is_blocked((i, j-1), (i, j), roads_to_avoid):
                    road_map[i][j] += road_map[i][j-1]

    print(road_map[w][h])

destination = [19, 100]
new_list = ["7 2 7 3", "9 7 9 8", "5 3 6 3", "9 9 9 10", "8 8 8 7", "3 1 3 2", "1 4 1 3", "7 7 8 7", "7 9 7 10", "6 0 7 0", "7 5 7 4", "5 8 6 8", "2 3 2 2", "8 1 8 2", "1 3 1 2", "7 9 7 8", "0 8 1 8", "1 9 1 8", "3 8 3 9", "9 4 9 5", "5 9 6 9", "2 0 1 0", "6 0 7 0", "0 0 0 1", "1 3 1 2", "3 2 4 2", "4 9 3 9", "5 0 4 0", "2 4 2 5", "1 3 2 3", "0 4 0 5", "2 6 2 5", "3 3 2 3", "4 2 3 2", "8 8 9 8", "8 5 9 5", "7 9 7 8", "2 9 3 9", "6 0 6 1", "9 1 9 0", "4 5 4 4", "1 6 1 5", "8 4 8 5", "3 6 4 6", "1 4 1 5", "9 0 10 0", "1 2 1 3", "5 8 5 7", "5 2 6 2", "4 5 4 4"]
avoid_roads(new_list, destination)