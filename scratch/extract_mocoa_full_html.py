import re

path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas4.html"
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's extract the part between '<div id="geology"' (Deposit & Scale) and the footer
# Wait, let's find the start of the sections we want.
# Mineral Resource seems to be the first one we need to add. Let's see if there is an id or heading.
# Let's find: id="mineral-resource" or similar.
# Let's search for H2 elements in the html first.
matches = list(re.finditer(r'<h2[^>]*>(.*?)</h2>', html, re.IGNORECASE))
for i, m in enumerate(matches):
    print(f"H2: {m.group(1)} at index {m.start()}")

# Let's extract from the H2 "Mineral Resource" (or similar) to the end.
# Wait, let's find the text "Mineral Resource" in the matches.
