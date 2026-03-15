def solve(part1: bool):
    program = open("input.txt").read().strip()
    program = [int(v) for v in program.split(",")]
    
    def simulate(in1, in2):
        prog = program[:]
        prog[1] = in1
        prog[2] = in2
        for i in range(0, len(prog), 4):
            opcode = prog[i]
            p1, p2, p_out = prog[i + 1], prog[i + 2], prog[i + 3]    
                
            if opcode == 1:
                prog[p_out] = prog[p1] + prog[p2]
            elif opcode == 2:
                prog[p_out] = prog[p1] * prog[p2]
            elif opcode == 99:
                break
            else:
                raise RuntimeError(f"Unknown opcode {opcode}")

        return prog[0]

    if part1:
        print(simulate(12, 2))
    else:
        for in1 in range(100):
            for in2 in range(100):
                result = simulate(in1, in2)
                if result == 19690720:
                    print(in1 * 100 + in2)
                    break
                

if __name__ == '__main__':
    solve(True)
    solve(False)
