import calendar
from datetime import datetime

def print_calendar():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # Создаем календарь
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month].capitalize()

    # Выводим заголовок
    print(f"+-----------------------------+")
    print(f"|        {month_name} {year}         |")
    print(f"+----+----+----+----+----+----+----+")
    print(f"| Пн | Вт | Ср | Чт | Пт | Сб | Вс |")
    print(f"+----+----+----+----+----+----+----+")

    # Выводим дни
    for week in cal:
        week_str = "|"
        for d in week:
            if d == 0:
                week_str += "    |"
            else:
                if d == day:
                    week_str += f"[{d:2}]|"
                else:
                    week_str += f" {d:2} |"
        print(week_str)
    print(f"+----+----+----+----+----+----+----+")

print_calendar()
