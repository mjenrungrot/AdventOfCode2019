import argparse
import math

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--deploy', action='store_true')
group.add_argument('--test', action='store_true')

def solver(inputString, verbose=False):
    def move(point, event):
        if event[0] == "R":
            return (point[0], point[1] + int(event[1:]))
        elif event[0] == "L":
            return (point[0], point[1] - int(event[1:]))
        elif event[0] == "U":
            return (point[0] + int(event[1:]), point[1])
        elif event[0] == "D":
            return (point[0] - int(event[1:]), point[1])

    def findIntersection(point1_1, point1_2, point2_1, point2_2):
        if point1_1[0] == point1_2[0] and point2_1[0] == point2_2[0]:
            return None
        elif point1_1[0] == point1_2[0] and point2_1[1] == point2_2[1]:
            row = point1_1[0]
            col = point2_1[1]
            if ((point2_1[0] <= row <= point2_2[0]) or (point2_2[0] <= row <= point2_1[0])) and \
               ((point1_1[1] <= col <= point1_2[1]) or (point1_2[1] <= col <= point1_1[1])):
               return (row,col)
            
        elif point1_1[1] == point1_2[1] and point2_1[0] == point2_2[0]:
            row = point2_1[0]
            col = point1_1[1]
            if ((point1_1[0] <= row <= point1_2[0]) or (point1_2[0] <= row <= point1_1[0])) and \
               ((point2_1[1] <= col <= point2_2[1]) or (point2_2[1] <= col <= point2_1[1])):
               return (row,col)

        elif point1_1[1] == point1_2[1] and point2_1[1] == point2_2[1]:
            return None

    def abs(x):
        if(x < 0): return -x
        else: return x

    def hamming(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    firstPath, secondPath = inputString.strip().split('\n')
    firstPath = firstPath.split(',')
    secondPath = secondPath.split(',')

    minDist = math.inf
    prevPoint1 = (0,0)
    sumDist1 = 0
    for segment1 in range(len(firstPath)):
        currPoint1 = move(prevPoint1, firstPath[segment1])
        prevPoint2 = (0,0)
        sumDist2 = 0
        for segment2 in range(len(secondPath)):
            currPoint2 = move(prevPoint2, secondPath[segment2])
            
            intersection = findIntersection(prevPoint1, currPoint1, prevPoint2, currPoint2)
            if verbose: print("{}[{}-{}] {}[{}-{}] intersection={}".format(segment1, prevPoint1, currPoint1, segment2, prevPoint2, currPoint2, intersection))
            if intersection is None: 
                pass
            elif segment1 == 0 and segment2 == 0: 
                pass
            else:
                dist1 = hamming(prevPoint1, intersection)
                dist2 = hamming(prevPoint2, intersection)
                minDist = min(minDist, dist1 + sumDist1 + dist2 + sumDist2)

            sumDist2 += hamming(prevPoint2, currPoint2)
            prevPoint2 = currPoint2

        sumDist1 += hamming(prevPoint1, currPoint1)
        prevPoint1 = currPoint1

    return str(minDist)

def test():
    assert(solver("""R8,U5,L5,D3
U7,R6,D4,L4
""") == "30")
    assert(solver("""R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
""") == "610")
    assert(solver("""R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
""") == "410")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        print("Running test")
        test()
        print("Test passed successfully")
    elif args.deploy:
        in_f = open("3.in", "r")
        out_f = open("3b.out", "w")
        lines = in_f.read()
        
        output = solver(lines)
        out_f.write("{}\n".format(output))

        in_f.close()
        out_f.close()
        print("Finished running")