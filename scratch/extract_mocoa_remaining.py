import re

path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas4.html"
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's search for "the-coreshack" and "project-maps"
match = re.search(r'id="the-coreshack"', html, re.IGNORECASE)
if match:
    start_idx = match.start()
    # print the next 5000 characters
    print(html[start_idx:start_idx+5000])
else:
    print("Could not find the-coreshack")
