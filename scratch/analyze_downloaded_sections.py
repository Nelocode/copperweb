import re

path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas4.html"
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's search for the H2 headers
headers = [
    ("Mineral Resource", r'<h2[^>]*>\s*Mineral Resource\s*</h2>'),
    ("District Exploration", r'<h2[^>]*>\s*District Exploration\s*</h2>'),
    ("Geology: Characteristics of a Giant", r'<h2[^>]*>\s*Geology:\s*Characteristics of a Giant\s*</h2>'),
    ("Content Gallery", r'<h2[^>]*>\s*Content Gallery\s*</h2>')
]

for title, pattern in headers:
    match = re.search(pattern, html, re.IGNORECASE)
    if match:
        start_idx = match.start()
        # Find next h2
        next_h2 = re.search(r'<h2', html[match.end():], re.IGNORECASE)
        if next_h2:
            end_idx = match.end() + next_h2.start()
        else:
            end_idx = len(html)
        print(f"\n==================================================")
        print(f"SECTION: {title}")
        print(f"==================================================")
        content_block = html[start_idx:end_idx]
        print(content_block[:1500])
        if len(content_block) > 1500:
            print("... [TRUNCATED] ...")
            print(content_block[-800:])
    else:
        print(f"Could not find section: {title}")
