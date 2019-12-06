import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--deploy', action='store_true')
group.add_argument('--test', action='store_true')

def solver(inputString):
    instruction_codes = inputString.strip().split(',')

    memory = {}
    for i in range(len(instruction_codes)):
        memory[i] = int(instruction_codes[i])

    outputs = ""

    idx = 0
    while True:
        instruction_code = memory[idx]
        opcode = instruction_code % 100
        if opcode == 99:
            break
        elif opcode == 1 or opcode == 2:
            if opcode == 1: operator = (lambda x,y: x+y)
            else: operator = (lambda x,y: x*y)

            if instruction_code % 1000 // 100 == 0:
                if memory[idx+1] in memory: param1 = memory[memory[idx+1]]
                else: param1 = 0
            else: param1 = memory[idx+1]

            if instruction_code % 10000 // 1000 == 0:
                if memory[idx+2] in memory: param2 = memory[memory[idx+2]]
                else: param2 = 0
            else: param2 = memory[idx+2]

            output = operator(param1, param2)
            memory[memory[idx+3]] = output
            idx += 4
        elif opcode == 3:
            memory[memory[idx+1]] = 5
            idx += 2
        elif opcode == 4:
            outputs += "{}\n".format(memory[memory[idx+1]])
            idx += 2
        elif opcode == 5 or opcode == 6:
            if instruction_code % 1000 // 100 == 0:
                if memory[idx+1] in memory: param1 = memory[memory[idx+1]]
                else: param1 = 0
            else: param1 = memory[idx+1]

            if instruction_code % 10000 // 1000 == 0:
                if memory[idx+2] in memory: param2 = memory[memory[idx+2]]
                else: param2 = 0
            else: param2 = memory[idx+2]

            if opcode == 5: operator = (lambda x: x != 0)
            else: operator = (lambda x: x == 0)

            if operator(param1):
                idx = param2
            else:
                idx += 3
        elif opcode == 7 or opcode == 8:
            if instruction_code % 1000 // 100 == 0:
                if memory[idx+1] in memory: param1 = memory[memory[idx+1]]
                else: param1 = 0
            else: param1 = memory[idx+1]

            if instruction_code % 10000 // 1000 == 0:
                if memory[idx+2] in memory: param2 = memory[memory[idx+2]]
                else: param2 = 0
            else: param2 = memory[idx+2]

            if opcode == 7: operator = (lambda x,y: x < y)
            else: operator = (lambda x,y: x == y)

            memory[memory[idx+3]] = int(operator(param1,param2))
            idx += 4

    return outputs.strip()

def test():
    assert(solver("3,0,4,0,99") == "5")
    assert(solver("1002,4,3,4,33") == "")
    assert(solver("3,9,8,9,10,9,4,9,99,-1,8") == "0")
    assert(solver("3,9,7,9,10,9,4,9,99,-1,8") == "1")
    assert(solver("3,3,1108,-1,8,3,4,3,99") == "0")
    assert(solver("3,3,1107,-1,8,3,4,3,99") == "1")
    assert(solver("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9") == "1")
    assert(solver("3,3,1105,-1,9,1101,0,0,12,4,12,99,1") == "1")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        print("Running test")
        test()
        print("Test passed successfully")
    elif args.deploy:
        in_f = open("5.in", "r")
        out_f = open("5.out", "w")

        inputs = in_f.read()
        output = solver(inputs)
        print(output)
        out_f.write("{}\n".format(output))
        in_f.close()
        out_f.close()
        print("Finished running")
