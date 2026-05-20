import re

path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas.html"
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Remove scripts and styles
html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
html = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)

matches = re.finditer(r'<(h1|h2|h3|h4|p|table|ul)[^>]*>(.*?)</\1>', html, re.DOTALL | re.IGNORECASE)

for m in matches:
    tag = m.group(1).lower()
    content = m.group(2)
    clean_text = re.sub(r'<[^>]+>', ' ', content).strip()
    clean_text = re.sub(r'\s+', ' ', clean_text)
    
    if tag in ['h1', 'h2', 'h3', 'h4']:
        print(f"\n{tag.upper()}: {clean_text}")
    elif tag == 'p':
        if len(clean_text) > 2:
            print(f"  P: {clean_text[:180]}...")
