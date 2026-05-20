import os
import re

path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas4.html"
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Heading indices
headings = [
    ("Mineral Resource", r'<h2[^>]*>\s*Mineral Resource\s*</h2>'),
    ("District Exploration", r'<h2[^>]*>\s*District Exploration\s*</h2>'),
    ("Geology: Characteristics of a Giant", r'<h2[^>]*>\s*Geology:\s*Characteristics of a Giant\s*</h2>'),
    ("Content Gallery", r'<h2[^>]*>\s*Content Gallery\s*</h2>'),
    ("The Coreshack", r'<h2[^>]*>\s*The Coreshack\s*</h2>'),
    ("Project Maps", r'<h2[^>]*>\s*Project Maps\s*</h2>'),
    ("Footer", r'<footer')
]

ranges = []
for idx, (title, pattern) in enumerate(headings):
    match = re.search(pattern, html, re.IGNORECASE)
    if match:
        ranges.append((title, match.start()))

for idx in range(len(ranges) - 1):
    title = ranges[idx][0]
    start = ranges[idx][1]
    end = ranges[idx+1][1]
    
    section_html = html[start:end]
    filename = f"scratch/mocoa_{title.lower().replace(' ', '_').replace(':', '')}.html"
    with open(os.path.join("/Users/i2carvajal/Documents/Proyectos/CopperWeb", filename), "w", encoding="utf-8") as out:
        out.write(section_html)
    print(f"Saved {title} to {filename}")
