import re

path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas3.html"
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove styles and scripts
html_clean = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
html_clean = re.sub(r'<script.*?>.*?</script>', '', html_clean, flags=re.DOTALL | re.IGNORECASE)

# Find all headers h1, h2, h3 and print their text and subsequent paragraphs
lines = html_clean.split('\n')
for i, line in enumerate(lines):
    if re.search(r'<h[1-3]', line, re.IGNORECASE):
        clean_header = re.sub(r'<[^>]+>', ' ', line).strip()
        if clean_header:
            print(f"\n--- Line {i}: {clean_header} ---")
            # print subsequent lines containing text
            count = 0
            for j in range(1, 40):
                if i + j < len(lines):
                    next_line = lines[i+j]
                    if re.search(r'<h[1-3]', next_line, re.IGNORECASE):
                        break
                    text = re.sub(r'<[^>]+>', ' ', next_line).strip()
                    if text:
                        print("  ", text)
                        count += 1
                        if count > 5:
                            break
