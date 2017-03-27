'''
Problem Statement

A sequence of numbers is called a zig-zag sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a zig-zag sequence.

For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, sequence, return the length of the longest subsequence of sequence that is a zig-zag sequence. A subsequence is obtained by deleting some number of elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.


Definition

Class:	ZigZag
Method:	longestZigZag
Parameters:	int[]
Returns:	int
Method signature:	int longestZigZag(int[] sequence)
(be sure your method is public)


Constraints
-	sequence contains between 1 and 50 elements, inclusive.
-	Each element of sequence is between 1 and 1000, inclusive.

Examples
0)

{ 1, 7, 4, 9, 2, 5 }
Returns: 6
The entire sequence is a zig-zag sequence.
1)

{ 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 }
Returns: 7
There are several subsequences that achieve this length. One is 1,17,10,13,10,16,8.
2)

{ 44 }
Returns: 1
3)

{ 1, 2, 3, 4, 5, 6, 7, 8, 9 }
Returns: 2
4)

{ 70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32 }
Returns: 8
5)

{ 374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
249, 22, 176, 279, 23, 22, 617, 462, 459, 244 }
Returns: 36
'''

Series = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
Series2 = [12, 333, 700, 436, 1, 919, 959, 456, 456, 456, 1000, 193, 192, 13, 75, 818, 197, 197, 2, 777, 99, 81, 222,
           109, 1000, 19, 27, 270, 62, 189, 987, 234, 55, 2, 718, 238, 901, 901, 900, 432, 55, 606, 89, 7, 7, 23, 789,
           790, 800, 1000]
Series3 = [396, 549, 22, 819, 611, 972, 730, 638, 978, 342, 566, 514, 752, 871, 911, 172, 488, 542, 482, 974, 210, 474,
           66, 387, 1, 872, 799, 262, 567, 113, 578, 308, 813, 515, 716, 905, 434, 101, 632, 450, 74, 254, 1000, 780,
           633, 496, 513, 772, 925, 746]
Series4 = [61, 82, 126, 97, 167, 186, 119, 154, 155, 142, 153, 181, 172, 192, 223, 272, 273, 260, 280, 330, 329, 350,
           273, 324, 349, 306, 385, 375, 420, 416, 435, 457, 373, 477, 395, 487, 500, 439, 493, 537, 518, 549, 542, 500,
           524, 541, 512, 589, 549, 543]
Series5 = [10, 9, 8, 7, 6, 7, 8, 9, 10]
positive = True
count = 1
lengths = [[1, None]]


def zig_zag(series):
    for i in range(1, len(series)):
        for j in range(i - 1, -1, -1):
            if series[i] == series[j]:
                lengths.append([lengths[j][0], lengths[j][1]])
                break
            elif series[i] < series[j]:
                if lengths[j][1] == "more" or lengths[j][1] == None:
                    if len(lengths) < (i + 1):
                        lengths.append([lengths[j][0] + 1, "less"])
                    elif lengths[i][0] < lengths[j][0] + 1:
                        lengths[i][0] = lengths[j][0] + 1
                        lengths[i][1] = "less"
            else:
                if lengths[j][1] == "less" or lengths[j][1] == None:
                    if len(lengths) < (i + 1):
                        lengths.append([lengths[j][0] + 1, "more"])
                    elif lengths[i][0] < lengths[j][0] + 1:
                        lengths[i][0] = lengths[j][0] + 1
                        lengths[i][1] = "more"

    print(lengths)


zig_zag([20, 20])