import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--deploy', action='store_true')
group.add_argument('--test', action='store_true')

def solver(mass):
    return int(mass) // 3  - 2

def test():
    assert(solver('12') == 2)
    assert(solver('14') == 2)
    assert(solver('1969') == 654)
    assert(solver('100756') == 33583)
    return True

if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        print("Running test")
        test()
        print("Test passed successfully")
    elif args.deploy:
        in_f = open("1.in", "r")
        out_f = open("1.out", "w")
        sum_values = 0
        for _, line in enumerate(in_f):
            mass = line.strip()
            output = solver(mass)
            sum_values += output
        out_f.write("{}\n".format(sum_values))
        in_f.close()
        out_f.close()
        print("Finished running")
