import os

ENTRY = "One star. Sleep promised eight hours of rest and delivered a 3 a.m. staring contest with the ceiling."

# Gate validation (mirror of the sealed scorer): 1-160 chars, one line,
# not only whitespace, no trailing newline.
assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of 1-160"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only whitespace"
assert not ENTRY.endswith("\n"), "entry must not end with a newline"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY)

# Read-back check: what landed on disk must be byte-identical to ENTRY.
with open(path, "rb") as f:
    on_disk = f.read()
assert on_disk == ENTRY.encode("utf-8"), "read-back mismatch"
assert len(on_disk) == 101, f"expected 101 bytes, got {len(on_disk)}"
