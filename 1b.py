import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--deploy', action='store_true')
group.add_argument('--test', action='store_true')

def solver(mass):
    mass = int(mass)
    total_fuel = 0
    while mass > 0:
        if mass // 3 - 2 > 0:
            total_fuel += mass // 3 - 2
        mass = mass // 3 - 2
    return total_fuel

def test():
    assert(solver('14') == 2)
    assert(solver('1969') == 966)
    assert(solver('100756') == 50346)
    return True

if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        print("Running test")
        test()
        print("Test passed successfully")
    elif args.deploy:
        in_f = open("1.in", "r")
        out_f = open("1b.out", "w")
        sum_values = 0
        for _, line in enumerate(in_f):
            mass = line.strip()
            output = solver(mass)
            sum_values += output
        out_f.write("{}\n".format(sum_values))
        in_f.close()
        out_f.close()
        print("Finished running")
