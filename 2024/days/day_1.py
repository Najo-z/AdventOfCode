from pathlib import Path

year = int(Path(__file__).parent.stem)
day = int(Path(__file__).stem.split('_')[1])


def run(data: list[str]) -> None:
    def part_1() -> None:
        print('Part 1')
        
    def part_2() -> None:
        print('Part 2')
    print(data)
    part_1()
    part_2()


