#!/usr/bin/env python3
import sys
from datetime import date
from os import path


REMINDER_FILE = path.expanduser('~/.config/.remind')


def parse_line(line):
    l = line.split(" ")
    date = l[0]
    reminder = " ".join(l[1:])

    date_components = date.split("-")

    return ([int(elem) for elem in date_components], reminder)


def fits(matcher, today):
    return (
        # yearly
        (len(matcher) == 2 and today.day == matcher[0]
                           and today.month == matcher[1])
        or
        # one time
        (len(matcher) == 3 and today.day == matcher[0]
                           and today.month == matcher[1]
                           and today.year == matcher[2])
    )


def remind():
    today = date.today()

    with open(REMINDER_FILE) as f:
        for line in f:
            date_components, reminder = parse_line(line)
            if fits(date_components, today):
                print(reminder, end='')


def add_reminder(date, elem):
    with open(REMINDER_FILE, 'a+') as f:
        f.write('{} {}\n'.format(date, elem))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        remind()
    elif len(sys.argv) == 2:
        print("You can either call remind without arguments or with two arguments.")
    else:
        add_reminder(sys.argv[1], " ".join(sys.argv[2:]))
