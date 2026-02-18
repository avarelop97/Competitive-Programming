def is_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def solve() -> int:
    # weekday encoding: 0=Mon, 1=Tue, ..., 6=Sun
    weekday = 0  # 1 Jan 1900 is Monday

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Move from 1 Jan 1900 to 1 Jan 1901
    weekday = (weekday + 365) % 7  # 1900 is NOT leap (divisible by 100, not by 400)

    count = 0

    for year in range(1901, 2001):
        for month in range(12):
            if weekday == 6:  # Sunday
                count += 1

            days = month_days[month]
            if month == 1 and is_leap(year):  # February in leap year
                days = 29

            weekday = (weekday + days) % 7

    return count


if __name__ == "__main__":
    print(solve())  # 171