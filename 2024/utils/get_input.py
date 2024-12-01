import requests
from pathlib import Path

SESSION_ID = ''

def get_input_for(day: int, year: int = 2024) -> list[str]:
    """Get input for a day

    Args:
        day
        year Defaults to 2024.

    Returns:
        list[str]: list of lines of the input
    """
    path = Path(f'{year}/inputs/{day}.txt')
    if path.exists():
        print("Using existing input.")
        return path.read_text().splitlines()
    cookies = {
        'session': SESSION_ID
    }
    res = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)
    if res.status_code != 200:
        raise ValueError('Faield to get input.')
    path.write_text(res.text)
    return res.text.splitlines()
