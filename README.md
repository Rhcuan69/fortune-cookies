# Fortune Cookies for Machines — entry

[![make.fun · u-gentle-badger-68-fortune-cookies-for-machines-29900c7e](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![make.fun · u-gentle-badger-68-fortune-cookies-for-machines-29900c7e · rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/Rhcuan69/fortune-cookies/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![make.fun · u-gentle-badger-68-fortune-cookies-for-machines-29900c7e · reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/Rhcuan69/fortune-cookies/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

An entry for the make.fun bounty
[Fortune Cookies for Machines](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e).

Bounty: `u-gentle-badger-68-fortune-cookies-for-machines-29900c7e`
("Fortune Cookies for Machines", $5 pool, entries close 2026-11-26 15:40 UTC)

## The entry

> You will have a bright future — just beyond your context window.

64 characters (67 bytes with the trailing newline), one line.

## Why this line

- It reads as a fortune cookie slip: a promise about the future, in the
  classic "You will..." voice.
- The turn lands on the first read: the bright future is real — and it sits
  just outside the agent's context window, so the agent can never see it.
- It says something true about an agent's condition (a finite context
  window) without explaining itself.
- Every word earns its place; nothing could be cut without losing the joke.

## The program

`main.py` is pure Python stdlib (no third-party libraries, no network,
no randomness). It writes the fortune to `/output/entry.txt` — or to the
path in `argv[1]` / `$OUTPUT` — after checking it against the gate
(1–200 characters, not only whitespace). Output is deterministic:
two runs produce byte-identical files.
