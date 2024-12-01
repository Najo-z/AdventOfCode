from pathlib import Path

year = int(Path(__file__).parent.parent.stem)
day = int(Path(__file__).stem.split('_')[1])


def run(data: list[str]) -> None:
    def part_1() -> None:
        print('Part 1')
        total = 0
        print(total)

    def part_2() -> None:
        print('Part 2')
        total = 0
        print(total)
    part_1()
    part_2()


