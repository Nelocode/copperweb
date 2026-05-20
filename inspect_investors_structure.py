path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/investors.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

import re
lines = content.splitlines()

print("=== Scanning links in investors.html ===")
for idx, line in enumerate(lines):
    if "<a " in line:
        print(f"Line {idx+1}: {line.strip()[:120]}")

print("\n=== Scanning for calendar in investors.html ===")
for idx, line in enumerate(lines):
    if "calendar" in line.lower() or "event" in line.lower() or "drill" in line.lower():
        print(f"Line {idx+1}: {line.strip()[:120]}")
