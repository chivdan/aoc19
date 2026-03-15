def interval(pos, direction, n):
    i, j = pos
    if direction == "U":
        return pos, (i - n, j)
    elif direction == "D":
        return pos, (i + n, j)
    elif direction == "L":
        return pos, (i, j - n)
    elif direction == "R":
        return pos, (i, j + n)
    else:
        raise RuntimeError(f"Unknown direction '{direction}'") 

def simulate(wire: list[tuple]):
    intervals = []
    pos = 0, 0
    l = 0
    for direction, n in wire:
        s, e = interval(pos, direction, n)
        intervals.append(((s, e), l))
        pos = e
        l += n
    return intervals
        
def intersect(int_l1, int_l2):
    int1, l1 = int_l1
    int2, l2 = int_l2
    (s1_i, s1_j), (e1_i, e1_j) = int1
    (s2_i, s2_j), (e2_i, e2_j) = int2

    s2_i, e2_i = sorted([s2_i, e2_i])
    s2_j, e2_j = sorted([s2_j, e2_j])
    
    for i in range(s1_i, e1_i + 1, 1 if s1_i <= e1_i else -1):
        for j in range(s1_j, e1_j + 1, 1 if s1_j <= e1_j else -1):
            if s2_i <= i <= e2_i and s2_j <= j <= e2_j:    
                return (i, j), l1 + abs(i - s1_i) + abs(j - s1_j), l2 + abs(i - s2_i) + abs(j - s2_j)
    return None, None, None
 

def solve(part1: bool):
    wires = []
    for line in open("input.txt"):
        wire = []
        for turn in line.strip().split(","):
            wire.append((turn[0], int(turn[1:])))
        wires.append(wire)

    w0 = simulate(wires[0])
    w1 = simulate(wires[1])

    distances = []
    for int0 in w0:
        for int1 in w1:
            point, l1, l2 = intersect(int0, int1)
            if point is not None:
                distances.append(sum(abs(coord) for coord in point) if part1 else l1 + l2 )

    print(sorted(distances)[1])
    


if __name__ == '__main__':
    solve(True)
    solve(False)
