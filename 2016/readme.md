# Ryan Eaton's Advent of Code 2016

A repository to store my solutions for [Advent of Code 2016](https://adventofcode.com/2016).

**Different from other annotated years so far, this year was done entirely asyncronously. I am starting on 2024-11-21 as practice for Advent of Code 2024. As such, times will be relative to when the puzzle was opened in my browser, as recorded by [this browser extension](https://chromewebstore.google.com/detail/advent-of-code-part-2-tim/fhmjpoppaplfhgnknpbaaklgdnnimfbn?pli=1).**

Solutions will be slightly refactored for readability before submission. In other words...

```diff
+ Refactor to remove unused code
- No logic changes allowed
- No fixing the stupid or unnecessary checks I wrote
+ Code must produce valid solutions
```

I'm going for speed. This repository is not an example of good code. It won't be pretty.

## Earnings and Emojis

This is pretty much a table of contents for my solutions and a corresponding emoji sentence for each day (some were AI generated then modified).

| Title                                                         | Part 1  | Part 2  | Total   | Points\*     | Pictogram            |
|---------------------------------------------------------------|---------|---------|---------|--------------|----------------------|
| [Day 1: No Time for a Taxicab](notes/1.md)                    | 5:43    | 3:43    | 9:26    | 189          |                      |
| [Day 2: Bathroom Security](notes/2.md)                        | 5:55    | 3:00    | 8:55    | 160          | 🔒🚽                 |
| [Day 3: Squares With Three Sides](notes/3.md)                 | 2:35    | 2:22    | 4:57    | 165          | 📏📏📏❓🟰📐          |
| [Day 4: Security Through Obscurity](notes/4.md)               | 16:16   | 7:09    | 23:25   | 32           | 🚪🔑🧮🔤➡️🎁          |
| [Day 5: How About a Nice Game of Chess?](notes/5.md)          | 5:44    | 4:21    | 10:05   | 156          | 🤬🟰0️⃣0️⃣0️⃣0️⃣0️⃣            |
| [Day 6: Signals and Noise](notes/6.md)                        | 3:57    | 0:30    | 4:27    | 95           | 🎅📡📶❌❓🔤✅⭐🎄       |
| [Day 7: Internet Protocol Version 7](notes/7.md)              | 9:38:12 | 20:53   | 9:59:05 | -            | 💻🌐🔢🔒✅🔓          |
| [Day 8: Two-Factor Authentication](notes/8.md)                | 13:48   | 1:05    | 14:53   | 128          | 🚪➡️💳➡️💻➡️🔢➡️🔓       |
| [Day 9: Explosives in Cyberspace](notes/9.md)                 | 12:34   | 1:07:06 | 1:19:40 | 16           | 🅰️🅱️✖️2️⃣🟰🅰️🅱️🅰️🅱️     |
| [Day 10: Balance Bots](notes/10.md)                           | 21:27   | 1:26    | 22:53   | 113          | 🤖🏭➡️🔢➡️🤖➡️🗑️❓🤖     |
| [Day 11: Radioisotope Thermoelectric Generators](notes/11.md) | 1:30:20 | 16:38   | 1:46:58 | 60           | ☢️⬆️🏢⛔☢️🤖🔌🚫🤯       |
| [Day 12: Leonardo's Monorail](notes/12.md)                    | 17:46   | 0:44    | 18:30   | 0            | 💻🔓⬆️🚂⛔🔑❓🔢✅       |
| [Day 13: A Maze of Twisty Little Cubicles](notes/13.md)       | 7:02    | 5:47    | 12:49   | 183          | 🏢➡️🔢➡️🧱➡️🧑‍💼➡️➡️🎯     |
| [Day 14: One-Time Pad](notes/14.md)                           | 8:50    | 7:59    | 16:49   | 185          | 🔑➡️🧂➡️🔢➡️🔽➡️🔑➡️✅     |
| [Day 15: Timing is Everything](notes/15.md)                   | 5:38    | 0:33    | 6:11    | 181          | 🎉🤖🧩🌟⏳⌛️⬇️🕳️⭕️🌀🔢   |
| [Day 16: Dragon Checksum](notes/16.md)                        | 19:11   | 36:51   | 56:02   | -            | 🐉💾🔢🔁🔄🔀🔁🔢🧮   |
| [Day 17: Two Steps Forward](notes/17.md)                      | 15:13   | 6:17    | 21:30   | 65           | 🚪🔑🔍👣🛤️🏁🏆       |
| [Day 18: Like a Rogue](notes/18.md)                           | 9:08    | 0:31    | 9:39    | 116          | 🔢➡️🔢➡️🔢🧮✅          |
| [Day 19: An Elephant Named Joseph](notes/19.md)               | 48:53   | 2:51:53 | 3:40:46 | -            | 🎁➡️🎁➡️🎁🔄❓🏆        |
| [Day 20: Firewall Rules](notes/20.md)                         | 27:07   | 3:55    | 31:02   | 0            | 🧩🎄💻🔒➡️🔢🤔🌟🌟    |
| [Day 21: Scrambled Letters and Hash](notes/21.md)             | 31:35   | 24:16   | 55:51   | 0            | 🤔🧩🔀🔄🔁🔤🔀🔄🔁🤔 |
| [Day 22: Grid Computing](notes/22.md)                         | 8:51    | 37:27   | 46:18   | -            | 🖥️💾➡️📂🧩🔀📁        |
| [Day 23: Safe Cracking](notes/23.md)                          | 15:32   | 25:30   | 41:02   | 126          | 🎉🥚🐰⚙️💻🔢🌟        |
| [Day 24: Air Duct Spelunking](notes/24.md)                    | 57:58   | 0:35    | 58:33   | 2            | 🤖🗺️🧩🕵️‍♀️💨🏁         |
| [Day 25: Clock Signal](notes/25.md)                           | 10:17   | 0:35    | 10:46   | 133          | 📡🤖⏰🎄🎁✨🎉🎉       |
|                                                               |         |         |         | 2105 / 20th! |                      |

> Referenced other solutions / hints for: 7, 16, 19, 22
>
> \* Points calculated **as if** I completed it synchronously in 2016, when fewer people were playing. When tied, I put myself last. When using a hint, I counted it as nothing, which mattered for 111 points on day 22. It's not very accurate, but it's still cool.
