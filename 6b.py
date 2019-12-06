import argparse
import math

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--deploy', action='store_true')
group.add_argument('--test', action='store_true')

def solver(inputString, node1="YOU", node2="SAN"):
    inputString = inputString.strip()
    lines = inputString.split()

    parents = {}
    for line in lines:
        nodeA, nodeB = line.strip().split(')')
        parents[nodeB] = nodeA

    answer = math.inf

    mapNode1 = {}
    node = node1
    counter = 0
    mapNode1[node] = counter
    while node in parents:
        node = parents[node]
        counter += 1
        mapNode1[node] = counter

    node = node2
    counter = 0
    while node in parents:
        node = parents[node]
        counter += 1
        if node in mapNode1:
            answer = min(answer, counter + mapNode1[node] - 2)

    return str(answer)

def test():
    assert(solver("""
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
                  ) == "4")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        print("Running test")
        test()
        print("Test passed successfully")
    elif args.deploy:
        in_f = open("6.in", "r")
        out_f = open("6b.out", "w")

        inputs = in_f.read()
        output = solver(inputs)
        print(output)
        out_f.write("{}\n".format(output))
        in_f.close()
        out_f.close()
        print("Finished running")
