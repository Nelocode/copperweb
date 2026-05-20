import re

path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas3.html"
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's search for "About Copper Giant" and extract about 100 lines around it
m = re.search(r'About Copper Giant', html)
if m:
    start = max(0, m.start() - 2000)
    end = min(len(html), m.end() + 4000)
    print("EXTRACTED HTML:")
    print(html[start:end])
else:
    print("Not found")
