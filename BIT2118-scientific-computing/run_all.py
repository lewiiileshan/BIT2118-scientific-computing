"""Run every program in a folder headlessly.

Usage: python run_all.py <code_dir> <out_dir>
Saves stdout to <out_dir>/<name>.txt and each plot to <out_dir>/<name>_<n>.png
"""
import io
import os
import sys
import runpy
import contextlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

code_dir, out_dir = sys.argv[1], sys.argv[2]
os.makedirs(out_dir, exist_ok=True)

for fname in sorted(os.listdir(code_dir)):
    if not fname.endswith(".py"):
        continue
    name = fname[:-3]
    counter = {"n": 0}

    def fake_show(*args, **kwargs):
        counter["n"] += 1
        plt.gcf().savefig(os.path.join(out_dir, f"{name}_{counter['n']}.png"), dpi=130, bbox_inches="tight")
        plt.close("all")

    plt.show = fake_show
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            runpy.run_path(os.path.join(code_dir, fname), run_name="__main__")
        status = "OK"
    except Exception as e:  # keep going, report at the end
        status = f"ERROR: {type(e).__name__}: {e}"
        buf.write(status + "\n")
    with open(os.path.join(out_dir, name + ".txt"), "w") as f:
        f.write(buf.getvalue())
    print(f"{name}: {status}")
