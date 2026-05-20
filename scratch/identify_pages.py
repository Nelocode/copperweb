import glob
import re

files = glob.glob("/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/*.html")
for path in sorted(files):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    
    title_text = title.group(1).strip() if title else "No title"
    h1_text = re.sub(r'<[^>]+>', ' ', h1.group(1)).strip() if h1 else "No H1"
    h1_text = h1_text.replace('\n', ' ')
    print(f"File: {path.split('/')[-1]}")
    print(f"  Title: {title_text}")
    print(f"  H1: {h1_text}")
