import os

LINE = "bluffnod (n.): the smile and nod you give after asking someone to repeat themselves twice and still not catching a word."

# Mirror the sealed gate: UTF-8 text, 1-140 characters, not only white space, one line.
assert 1 <= len(LINE) <= 140 and LINE.strip() and "\n" not in LINE and "\r" not in LINE
data = LINE.encode("utf-8")
assert data.decode("utf-8") == LINE

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "wb") as f:  # binary: no newline translation
    f.write(data)
