import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--deploy', action='store_true')
group.add_argument('--test', action='store_true')

def solver(nums):
    nums = dict(enumerate(list(map(int, nums.split(',')))))
    nums[1] = 12
    nums[2] = 2

    curr = 0
    while curr < len(nums):
        if nums[curr] == 1:
            if 0 <= nums[curr+1] < len(nums): arg1 = nums[nums[curr+1]]
            else: arg1 = 0
            if 0 <= nums[curr+2] < len(nums): arg2 = nums[nums[curr+2]]
            else: arg2 = 0
            arg3 = nums[curr+3]
            if 0 <= arg3 < len(nums): nums[arg3] = arg1 + arg2
            curr += 4
        elif nums[curr] == 2:
            if 0 <= nums[curr+1] < len(nums): arg1 = nums[nums[curr+1]]
            else: arg1 = 0
            if 0 <= nums[curr+2] < len(nums): arg2 = nums[nums[curr+2]]
            else: arg2 = 0
            arg3 = nums[curr+3]
            if 0 <= arg3 < len(nums): nums[arg3] = arg1 * arg2
            curr += 4
        elif nums[curr] == 99:
            break

    return nums[0]

def test():
    assert(solver('1,0,0,0,99') == 2)
    assert(solver('2,3,0,3,99') == 2)
    return True

if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        print("Running test")
        test()
        print("Test passed successfully")
    elif args.deploy:
        in_f = open("2.in", "r")
        out_f = open("2.out", "w")
        sum_values = 0
        for _, line in enumerate(in_f):
            mass = line.strip()
            output = solver(mass)
            sum_values += output
        out_f.write("{}\n".format(sum_values))
        in_f.close()
        out_f.close()
        print("Finished running")
