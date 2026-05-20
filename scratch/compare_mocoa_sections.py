import re

def extract_sections(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Remove styles and scripts
    html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    
    # Find all h2 tags
    h2_matches = list(re.finditer(r'<h2[^>]*>(.*?)</h2>', html, re.IGNORECASE | re.DOTALL))
    sections = []
    
    for idx, match in enumerate(h2_matches):
        h2_text = re.sub(r'<[^>]+>', ' ', match.group(1)).strip()
        start_pos = match.end()
        end_pos = h2_matches[idx+1].start() if idx+1 < len(h2_matches) else len(html)
        
        section_html = html[start_pos:end_pos]
        # extract paragraph text
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', section_html, re.IGNORECASE | re.DOTALL)
        paragraphs_clean = [re.sub(r'<[^>]+>', ' ', p).strip() for p in paragraphs if p.strip()]
        
        sections.append({
            'heading': h2_text,
            'paragraphs': paragraphs_clean
        })
    return sections

print("=== DOWNLOADED MOCOA PAGE SECTIONS ===")
downloaded = extract_sections("/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas4.html")
for sec in downloaded:
    print(f"\nH2: {sec['heading']}")
    for p in sec['paragraphs'][:3]:
        print(f"  - {p[:120]}...")

print("\n\n=== CURRENT MOCOA.HTML SECTIONS ===")
current = extract_sections("/Users/i2carvajal/Documents/Proyectos/CopperWeb/mocoa.html")
for sec in current:
    print(f"\nH2: {sec['heading']}")
    for p in sec['paragraphs'][:3]:
        print(f"  - {p[:120]}...")
