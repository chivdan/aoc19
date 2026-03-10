def calc_fuel(mass):
    return mass//3 - 2
    
def solve(part1: bool):
    ans = 0

    for line in open("input.txt"):
        mass = int(line.strip())
        if part1:
            ans += calc_fuel(mass)
        else:
            while True:
                fuel = calc_fuel(mass)
                if fuel <= 0:
                    break
                ans += fuel
                mass = fuel

    print(ans)
        

if __name__ == '__main__':
    solve(True)
    solve(False)
