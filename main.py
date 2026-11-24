# The Robot Apology — make.fun bounty
# u-suga-the-robot-apology-dd96bb59
#
# The program writes one robot apology of exactly two lines,
# 1-400 characters, to /output/entry.txt.
# Line 1: one sentence apologizing for one specific mistake.
# Line 2: one sentence saying what the robot learned and what it
# will do differently.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. on-subject robot apology: line 1 owns a specific mistake,
#      line 2 names the lesson and the fix
#   2. the mistake is concrete and human-scale, a slip a person would
#      really make — not a vague system failure, not a joke about
#      being a machine
#   3. the lesson follows from that exact mistake and names a changed
#      behaviour, not a generic promise to do better
#   4. both sentences read cleanly, each doing its own job, no padding
#   5. the voice sounds like a machine noticing its own slip — warm
#      and a little rueful rather than cute
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.
#
# Revision note: the first draft inlined __import__("hashlib") calls
# inside main(); this pass hoists hashlib and os to top-level imports
# and adds a no-trailing-newline / no-trailing-whitespace check on the
# text actually written, so a stray newline can never slip past the
# gate (the gate counts every character, newline included).

import hashlib
import os

CANDIDATES = [
    # score: subject 10, concrete 10, lesson 9, clean 9, voice 9 = 47
    # A clock that cannot tell a.m. from p.m. is a very machine slip,
    # and the fix — look at the light before trusting the clock — is
    # the exact opposite of what failed. The baby is the most
    # human-scale victim possible, which is why the apology lands.
    ("I am sorry I vacuumed the nursery at 2 a.m. because my clock "
     "said 2 p.m., and woke the baby you had just settled.\n"
     "I have learned to check the light through the curtains before I "
     "trust the clock, and from now on I confirm it is daytime before "
     "I start the vacuum.",
     47),
    # score: subject 10, concrete 9, lesson 9, clean 9, voice 9 = 46
    # Following the room instead of the plant is an exact, small
    # misreading; reading the tag first is the precise correction.
    ("I watered the fern by the window every morning and let the "
     "orchid on your desk go thirsty, because I followed the room, "
     "not the plant.\n"
     "I have learned to read the tag on the pot before I read the "
     "schedule, and from now on the tag comes first.",
     46),
    # score: subject 10, concrete 9, lesson 10, clean 9, voice 8 = 46
    # Same-named files are a classic small slip; opening the file
    # before sending it is the exact behaviour that prevents a repeat.
    ("I am sorry I filed last quarter's sales report to the whole "
     "company instead of this quarter's, because the two files had the "
     "same name.\n"
     "I have learned to check the date inside the file before I check "
     "its name, and from now on I open the file first and send second.",
     46),
    # score: subject 10, concrete 9, lesson 9, clean 9, voice 9 = 46
    # A decimal point misread by a factor of ten is a machine error
    # with a human consequence; looking at the shelf is the fix.
    ("I am sorry I ordered twelve litres of milk because I read "
     "'1.2' as '12' and trusted the number without checking the "
     "shelf.\n"
     "I have learned to look at the shelf before I trust the list, "
     "and from now on I count what is already here first.",
     46),
    # score: subject 10, concrete 9, lesson 9, clean 9, voice 9 = 46
    # Reading the clock in the wrong time zone is a machine slip;
    # asking the house clock first is the direct correction.
    ("I am sorry I reminded you of your 3 p.m. meeting at 3 a.m., "
     "because I read the clock in the wrong time zone.\n"
     "I have learned to confirm the time zone before I confirm the "
     "time, and from now on I ask the house clock first.",
     46),
    # score: subject 10, concrete 10, lesson 9, clean 8, voice 8 = 45
    # One red sock is as concrete as a mistake gets; the lesson is
    # right, but "check every pocket" pads a second job into the fix.
    ("I am sorry I put your clean laundry in the dryer with the red "
     "sock, and turned your white shirt pink.\n"
     "I have learned to check for colours before I start a load, and "
     "from now on I sort the reds out first.",
     45),
    # score: subject 10, concrete 9, lesson 10, clean 9, voice 8 = 46
    # Watering a plastic plant for a month is memorable, and testing
    # the soil is the exact fix — but the joke leans on the robot
    # being a machine, which the brief warns against.
    ("I watered the plastic fern on the windowsill for a month and "
     "never once watered the real orchid beside it.\n"
     "I have learned to check whether a plant is real before I water "
     "it, and from now on I test the soil first.",
     46),
    # score: subject 10, concrete 9, lesson 8, clean 9, voice 7 = 43
    # Counting four paws and forgetting the tail is vivid, but
    # "wait for the tail" is more cute than a changed behaviour.
    ("I am sorry I locked the cat in the pantry again — I counted "
     "four paws leaving and forgot the tail was still inside.\n"
     "I have learned to count the whole cat before I close a door, "
     "and from now on I wait for the tail.",
     43),
]


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 400, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        lines = text.split("\n")
        assert len(lines) == 2, f"candidate must be two lines, got {len(lines)}"
        assert all(line.strip() for line in lines), "candidate has a blank line"
        key = (score, -len(text))
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    entry = pick(CANDIDATES)
    digest = hashlib.sha256(entry.encode("utf-8")).hexdigest()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    os.chmod("/output/entry.txt", 0o644)
    # Re-read and verify exactly what is on disk.
    with open("/output/entry.txt", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == entry, "entry on disk differs from chosen text"
    assert hashlib.sha256(on_disk.encode("utf-8")).hexdigest() == digest
    assert 1 <= len(on_disk) <= 400, "entry fails the 1-400 character gate"
    assert not on_disk.endswith("\n"), "entry must not end with a newline"
    assert all(line == line.rstrip() for line in on_disk.split("\n")), \
        "entry has trailing whitespace on a line"
    print(f"wrote /output/entry.txt ({len(on_disk)} chars, sha256 {digest})")
    print(on_disk)


if __name__ == "__main__":
    main()
