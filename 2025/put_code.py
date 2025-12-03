import os
import requests
import json
from datetime import datetime, time, timedelta
from pathlib import Path


def get_times_from_leaderboard(day: int, player_name: str = "Ryan Eaton"):
    """Fetch completion times from AoC leaderboard."""
    try:
        sess_path = Path(__file__).parent / "code" / "helpers" / "sess"
        session_cookie = sess_path.read_text().strip()

        r = requests.get(
            "https://adventofcode.com/2025/leaderboard/private/view/144198.json",
            cookies={'session': session_cookie}
        )
        data = json.loads(r.text)

        parta, delta, partb = "0:00", "0:00", "0:00"

        for key, player in data["members"].items():
            if player["name"] == player_name:
                try:
                    day_str = str(day)
                    midnight = datetime.combine(datetime.today(), time.min).timestamp()

                    # Get Part One time
                    parta_ts = player["completion_day_level"][day_str]["1"]["get_star_ts"]
                    parta = str(timedelta(seconds=parta_ts - midnight))
                    while parta[0] in ["0", ":"]:
                        parta = parta[1:]

                    # Get Part Two time and delta
                    partb_ts = player["completion_day_level"][day_str]["2"]["get_star_ts"]
                    delta = str(timedelta(seconds=partb_ts - parta_ts))
                    while delta[0] in ["0", ":"]:
                        delta = delta[1:]

                    partb = str(timedelta(seconds=partb_ts - midnight))
                    while partb[0] in ["0", ":"]:
                        partb = partb[1:]

                    return parta, delta, partb
                except:
                    pass

        return parta, delta, partb
    except Exception as e:
        print(f"Warning: Could not fetch times from leaderboard: {e}")
        return "0:00", "0:00", "0:00"


def update_readme(day: int, puzzle_name: str, part1_time: str, delta_time: str, total_time: str):
    """Update README.md with new puzzle entry."""
    readme_path = Path(__file__).parent / "README.md"

    if not readme_path.exists():
        print(f"Error: {readme_path} not found!")
        return

    content = readme_path.read_text()

    # Create new row with zero-padded day number
    day_str = f"{day:02d}"
    new_row = f"| [Day {day}: {puzzle_name}](notes/{day_str}.md) | {part1_time} | {delta_time} | {total_time} |"

    # Find the table and add the new row
    lines = content.split('\n')

    # Find where to insert (after the last table row)
    insert_idx = None
    for i, line in enumerate(lines):
        if line.startswith('|') and 'Day' in line and ':' in line:
            insert_idx = i + 1

    if insert_idx is not None:
        # Check if this day already exists
        day_pattern = f"| [Day {day}:"
        existing = False
        for i, line in enumerate(lines):
            if line.startswith(day_pattern):
                print(f"Day {day} already exists in README. Updating...")
                lines[i] = new_row
                existing = True
                break

        if not existing:
            lines.insert(insert_idx, new_row)

        # Write back
        readme_path.write_text('\n'.join(lines))
        print(f"✓ Updated README.md with Day {day}: {puzzle_name}")
    else:
        print("Error: Could not find table in README.md")


def create_note_file(day: int, puzzle_name: str, parta: str, delta: str, partb: str):
    """Create a note file with embedded code."""
    notes_dir = Path(__file__).parent / "notes"
    notes_dir.mkdir(exist_ok=True)

    day_str = f"{day:02d}"
    note_path = notes_dir / f"{day_str}.md"

    if note_path.exists():
        print(f"Note file {note_path} already exists. Skipping...")
        return

    # Read code files
    code_dir = Path(__file__).parent / "code"

    try:
        code_a = (code_dir / f"{day_str}a.py").read_text()
    except:
        code_a = "# Code not found"

    try:
        code_b = (code_dir / f"{day_str}b.py").read_text()
    except:
        code_b = "# Code not found"

    # Create note with embedded code
    prev_day = f"{day-1:02d}"
    next_day = f"{day+1:02d}"
    content = f"""# Day {day} - {puzzle_name}

> [<- Yesterday]({prev_day}.md) | [Tomorrow ->]({next_day}.md)

brief note

|      | Part One | Part Two | Total |
|------|----------|----------|-------|
| Time | {parta} | {delta} | {partb} |

## Part One
brief notes

[Code](../code/{day_str}a.py)

```python
{code_a}
```

## Part Two
brief notes

[Code](../code/{day_str}b.py)

```python
{code_b}
```"""

    note_path.write_text(content)
    print(f"✓ Created {note_path}")


def main():
    """Main entry point."""
    print("=== Advent of Code 2025 - Solution Organizer ===\n")

    # Get day number
    day_input = input("Day number (1-25): ").strip()
    day = int(day_input)

    if not 1 <= day <= 25:
        print("Error: Day must be between 1 and 25")
        return

    # Get puzzle name
    puzzle_name = input("Puzzle name: ").strip()

    # Fetch times from leaderboard
    print(f"\nFetching times from leaderboard for day {day}...")
    parta, delta, partb = get_times_from_leaderboard(day)
    print(f"Part One: {parta}, Delta: {delta}, Total: {partb}")

    # Create note file
    print("\nCreating note file...")
    create_note_file(day, puzzle_name, parta, delta, partb)

    # Update README
    print("\nUpdating README...")
    update_readme(day, puzzle_name, parta, delta, partb)

    print("\n✓ All done!")


if __name__ == "__main__":
    main()
