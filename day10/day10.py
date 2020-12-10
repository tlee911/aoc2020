
def read_input(path):
    with open(path, 'r') as file:
        l = file.readlines()
    return [ int(s) for s in l ]

def get_dist(path):
    data = read_input(path)
    ordered = [0] + sorted(data) + [max(data) + 3]
    print(ordered)

    step1 = 0
    step2 = 0
    step3 = 0
    diffs = []
    for i in range(len(ordered) - 1):
        diff = ordered[i+1] - ordered[i]
        diffs.append(diff)
        if diff == 1:
            step1 += 1
        elif diff == 2:
            step2 += 1
        elif diff == 3:
            step3 += 1
    print(diffs)
    return (step1, step3)

print(get_dist('example.txt'))
print(get_dist('test.txt'))
print(get_dist('input.txt'))