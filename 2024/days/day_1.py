from pathlib import Path

year = int(Path(__file__).parent.parent.stem)
day = int(Path(__file__).stem.split('_')[1])


def run(data: list[str]) -> None:
    left_list, right_list = [], []
    for line in data:
        left, right = line.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))
    left_list.sort()
    right_list.sort()
    def part_1() -> None:
        print('Part 1')
        total_distance = 0
        for left, right in zip(left_list, right_list):
            total_distance += abs(left - right)
        print(total_distance)

    def part_2() -> None:
        print('Part 2')
        right_occurences = {}
        for right in right_list:
            if right not in right_occurences:
                right_occurences[right] = 0
            right_occurences[right] += 1
        total_scores = 0
        for left in left_list:
            if left not in right_occurences:
                continue
            total_scores += left * right_occurences[left]
        print(total_scores)
    part_1()
    part_2()


