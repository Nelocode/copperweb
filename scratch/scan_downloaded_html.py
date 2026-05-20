import os
import re

root_dir = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa"

for fname in os.listdir(root_dir):
    if fname.endswith(".html"):
        path = os.path.join(root_dir, fname)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "No Title"
        
        h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        h1s = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s]
        
        h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content, re.IGNORECASE | re.DOTALL)
        h2s = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]
        
        print(f"File: {fname}")
        print(f"  Title: {title}")
        print(f"  H1s: {h1s}")
        print(f"  H2s: {h2s[:5]}")
        print("-" * 50)
