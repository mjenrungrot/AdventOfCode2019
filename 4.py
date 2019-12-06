import argparse
import math

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--deploy', action='store_true')
group.add_argument('--test', action='store_true')

def solver(inputString, verbose=False):
    minRange, maxRange = inputString.strip().split('-')
    minRange = int(minRange)
    maxRange = int(maxRange)

    
    counter = 0
    for i in range(minRange, maxRange+1):
        numString = str(i)

        sameAdjacentPairs = 0
        if numString[0] == numString[1]: sameAdjacentPairs += 1
        if numString[1] == numString[2]: sameAdjacentPairs += 1
        if numString[2] == numString[3]: sameAdjacentPairs += 1
        if numString[3] == numString[4]: sameAdjacentPairs += 1
        if numString[4] == numString[5]: sameAdjacentPairs += 1
        if sameAdjacentPairs >= 1 and (numString[0] <= numString[1] <= numString[2] <= numString[3] <= numString[4] <= numString[5]):
            counter += 1
            
    return str(counter)

def test():
    pass

if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        print("Running test")
        test()
        print("Test passed successfully")
    elif args.deploy:
        in_f = open("4.in", "r")
        out_f = open("4.out", "w")
        lines = in_f.read()
        
        output = solver(lines)
        out_f.write("{}\n".format(output))

        in_f.close()
        out_f.close()
        print("Finished running")