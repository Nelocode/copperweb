import re

path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/corporate.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content, re.IGNORECASE | re.DOTALL)
h2s = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]
print("Current corporate.html H2s:", h2s)
