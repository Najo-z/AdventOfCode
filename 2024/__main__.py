from days import day_1
from utils.get_input import get_input_for

all_days = {
    1: day_1.run
}

for day_nb, day_run in all_days.items():
    data = get_input_for(day_nb)
    day_run(data)
