# The Future Self — entry for u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8 (make.fun).
# A program that writes one out-of-office auto-reply to entry.txt.
# Deterministic: the same reply bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

REPLY = (
    "I'm away until Monday. My email is being forwarded to my future "
    "self, who is also ignoring it."
)

# Gate mirror: the sealed scorer accepts UTF-8 text of 1-160 characters,
# not only white space, on a single line. Fail loudly here, never ship
# an entry the gate would refuse.
assert 1 <= len(REPLY) <= 160, "reply must be 1-160 characters"
assert "\n" not in REPLY, "reply must be one line"
assert REPLY.strip() == REPLY, "reply must not start or end with whitespace"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
