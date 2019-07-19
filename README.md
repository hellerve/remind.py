# remind.py

A simple tool to set reminders for myself. I use it to remind myself of birthdays and
other appointments. It’s not fancy, but it gets the job done better than anything else.

## Installation

Installing the tool is as simple as calling `make install`. You should then be able to
call `remind`.

Uninstalling it can be done via `make uninstall`.

## Usage

There are only two modes of operation for `remind`.

If it’s called without any arguments, it looks up the reminders for today. This is what I
put at the end of my `zshrc` so that I get these reminders whenever I open a terminal.

The other mode calls it with two or more arguments. The first one is the date on which the
reminder should happen. It can either be of the form `DD-MM`—which is a yearly reminder,
for birthdays and the like—, or of the form `DD-MM-YYYY`—which is a once-off reminder. The
other arguments are the message of the reminder.

<hr/>

Have fun!
