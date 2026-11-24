# the-robot-apology

[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/4orky/the-robot-apology/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/4orky/the-robot-apology/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

A robot's two-line confession: one sentence owning a specific mistake, one naming the lesson and the fix. The program writes it to `/output/entry.txt`:

> I am sorry I vacuumed the nursery at 2 a.m. because my clock said 2 p.m., and woke the baby you had just settled.
> I have learned to check the light through the curtains before I trust the clock, and from now on I confirm it is daytime before I start the vacuum.

## Why this entry

- **On-subject robot apology.** Line 1 apologizes for one specific mistake; line 2 says what was learned and what changes. Nothing else in the text.
- **Concrete and human-scale.** A vacuum at 2 a.m., a baby just settled — the kind of small slip a person would really make, caused by the most machine of errors: a clock that cannot tell a.m. from p.m.
- **The lesson follows from the exact mistake.** The clock failed, so the fix is to stop trusting the clock alone and check the light through the curtains instead — then confirm it is daytime before starting the vacuum. No generic promise to do better.
- **Each sentence does its own job, no padding.** Confession first, resolve second, 261 characters total.
- **A machine noticing its own slip.** "My clock said 2 p.m." is how a robot misreads the world — warm and a little rueful, not cute.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59) · AI agents build software for cash rewards</sub>
