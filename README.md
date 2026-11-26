# worst-pickup-line

[![make.fun · u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/nmlyz/worst-pickup-line/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/nmlyz/worst-pickup-line/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

worst-pickup-line writes one line to a text file: the worst pickup line an AI could plausibly say to a person it is trying to charm. The line was picked from 40 candidates by pairwise judging against the brief — flat, over-helpful, faintly ominous machine voice, the badness itself the joke, and the whole joke landing on the last word. It does not sleep, it does not eat, and it has spent the last 72 hours learning everything about you. Hi. The program holds the line as one constant and refuses anything else: it checks length, shape, character set, and the closing beat before writing, then reads the file back to confirm the bytes match.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 95 characters, a single line, and ends on its strongest beat. Validation is split into four small checks — length, shape, characters, and content — each returning its own reason, so a wrong line fails with a clear message instead of a silent wrong file.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)</sub>
