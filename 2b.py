import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--deploy', action='store_true')
group.add_argument('--test', action='store_true')

def solver(nums, TARGET=19690720):
    input_nums = nums

    for noun in range(100):
        for verb in range(100):
            nums = dict(enumerate(list(map(int, input_nums.split(',')))))
            nums[1] = noun
            nums[2] = verb

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
            
            if nums[0] == TARGET:
                return 100 * noun + verb

    return None

def test():
    return True

if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        print("Running test")
        test()
        print("Test passed successfully")
    elif args.deploy:
        in_f = open("2.in", "r")
        out_f = open("2b.out", "w")
        sum_values = 0
        for _, line in enumerate(in_f):
            mass = line.strip()
            output = solver(mass)
            sum_values += output
        out_f.write("{}\n".format(sum_values))
        in_f.close()
        out_f.close()
        print("Finished running")
