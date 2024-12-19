from helpers.datagetter import aocd_data_in
import re

din, aocd_submit = aocd_data_in(split=True, numbers=False)

patterns = sorted(din[0].split(", "), key=lambda x: -len(x))
designs = din[2:]

regex = f"({'|'.join(patterns)})+"

impossible = 0
for design in designs:
    impossible += 1 if re.fullmatch(regex, design) is None else 0

aocd_submit(len(designs) - impossible)