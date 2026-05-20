import re

path = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas2.html"
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's remove scripts and styles
html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
html = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)

# Find all headings (h1, h2, h3), tables, lists, and paragraphs in sequence
matches = re.finditer(r'<(h1|h2|h3|p|table|ul)[^>]*>(.*?)</\1>', html, re.DOTALL | re.IGNORECASE)

for m in matches:
    tag = m.group(1).lower()
    content = m.group(2)
    # clean HTML tags from inner content
    clean_text = re.sub(r'<[^>]+>', ' ', content).strip()
    clean_text = re.sub(r'\s+', ' ', clean_text)
    
    if tag in ['h1', 'h2', 'h3']:
        print(f"\n{tag.upper()}: {clean_text}")
    elif tag == 'p':
        if len(clean_text) > 2:
            print(f"  P: {clean_text[:150]}...")
    elif tag == 'table':
        print("  [TABLE]")
        # extract table rows
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', content, re.DOTALL | re.IGNORECASE)
        for r in rows[:10]:
            cols = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.DOTALL | re.IGNORECASE)
            cols_clean = [re.sub(r'<[^>]+>', ' ', c).strip() for c in cols]
            print(f"    {' | '.join(cols_clean)}")
    elif tag == 'ul':
        print("  [LIST]")
        lis = re.findall(r'<li[^>]*>(.*?)</li>', content, re.DOTALL | re.IGNORECASE)
        for li in lis[:5]:
            li_clean = re.sub(r'<[^>]+>', ' ', li).strip()
            print(f"    - {li_clean[:100]}")
