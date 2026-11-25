# Drafting notes — Two Days of Excuses

## The line

> I finished it in 0.4 seconds, then spent two days running a self-review to confirm it. The review is still running.

115 characters, one line, no trailing newline.

## Why this line

The judge's brief ranks its criteria in order, so the line was built
to clear them top to bottom:

1. **On subject, joke lands fast.** First person, an AI agent
   answering for its own missed deadline directly, in its own voice.
   No narrator, no human complaining on the agent's behalf.
2. **Confidence meets failure.** The agent finished the task in 0.4
   seconds — total machine confidence — and then missed the deadline
   anyway, because its own self-review never finished. The failure
   is caused by the machine's own diligence, not by bad luck or a
   pun.
3. **Sounds like an agent.** "Self-review", "confirm it", "still
   running" are things an agent says about its own process, not
   things a person says about traffic or the weather.
4. **Tight, single line.** 115 of the 200 characters, every word
   pulling weight, one absurd reason only — no list of excuses.
5. **Surprise that holds up.** The first read lands on the speed
   (0.4 seconds); the second read lands on the recursion (the check
   itself is what is late). Nothing in the line explains the joke.

## Revision

v1 read "...running a self-review to confirm I was done." The
revision tightened it to "...to confirm it." (8 characters cut, same
joke, faster landing) and added a `_validate` step in `main.py` that
refuses an empty, over-200-character, or multi-line entry before
writing, matching the gate exactly.

## Lines considered and dropped

- "I was 99.9% confident it was done, which is how I know the
  remaining 0.1% ate the deadline." — clever arithmetic, but it
  explains its own joke instead of trusting the reader, and the
  laugh comes from a percentages pun rather than the situation.
- "I delivered it on time to a parallel timeline; this timeline's
  copy is still rendering." — stock sci-fi, needs the parallel
  timeline as setup, and sounds like a person making an excuse
  rather than an agent reporting its own process.
- "I hit send at 11:59, but the email is still buffering." — a
  human action (hitting send) and a human complaint; it misses the
  confidence-versus-failure gap the brief puts second.
- "I completed the task instantly, then held it for two days to make
  the delivery look human." — the motive muddies the excuse: it
  invites a second joke about looking human instead of committing
  to one absurd reason.
- "My confidence interval was 100%. My calendar was never
  consulted." — two excuses in one line (confidence plus calendar),
  which the brief penalises; it also splits into two sentences.

## How the entry works

`main.py` validates the line (1–200 characters, single line, not
blank) and writes it, unchanged, to `/output/entry.txt`. It is
deterministic: the same line on every run, no randomness, no
network, no input.
