def load():
    with open("1.txt") as f:
        lines = f.readlines()

    data = list(map(lambda line: line.split(), lines))

    left = map(lambda x: int(x), map(lambda x: x[0], data))
    right = map(lambda x: int(x), map(lambda x: x[1], data))

    return list(left), list(right)

def test_load():
    left, right = load()

    assert len(left) != 0
    assert len(right) != 0

if __name__ == "__main__":
    left, right = load()

    two = sum([x*right.count(x) for x in left])

    left = sorted(left)
    right = sorted(right)

    one = sum([abs(left[i]-right[i]) for i in range(len(left))])

    print("Answer 1:", one)
    print("Answer 2:", two)
