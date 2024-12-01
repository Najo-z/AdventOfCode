from utils.get_input import get_input_for
import argparse
from pathlib import Path
from importlib import import_module

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Advent Of Code')
    parser.add_argument('day', default=0, type=int, help='Day to compute')
    parser.add_argument('--year', default=2024, type=int, help='Year of AoC')
    parser.add_argument( '-a', '--all', action='store_true', default=False, help='Compute all days')
    args = parser.parse_args()

    if args.day == 0 and not args.all or args.day < 1 or args.day > 25:
        raise ValueError('Please provide a day between 1 and 25.')

    all_days = {}
    days_path = Path(f'{args.year}/days')
    for day_path in days_path.rglob('*.py'):
        if not day_path.stem.startswith('day_'):
            continue
        day_nb = int(day_path.stem.split('_')[1])
        day_module = import_module(f'{args.year}.days.{day_path.stem}')
        all_days[day_nb] = getattr(day_module, 'run')

    if args.all:
        for day_nb, day_run in all_days.items():
            data = get_input_for(day_nb)
            day_run(data)
    else:
        data = get_input_for(args.day)
        all_days[args.day](data)

