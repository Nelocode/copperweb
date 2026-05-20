import os
import re

directory = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa"
files = [f for f in os.listdir(directory) if f.endswith(".html")]

print("Files found:", files)

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Search for news patterns
    # Look for dates or headings
    # For example, let's see how many press release-like texts are in each file
    print(f"\n--- FILE: {filename} ---")
    
    # Find TSXV / OTC text
    if "TSXV" in content:
        print("Contains TSXV")
        
    # Let's search for date patterns like "May 12, 2026" or "2024", "2025", "2026"
    dates = re.findall(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}', content, re.IGNORECASE)
    print(f"Date occurrences count: {len(dates)}")
    if dates:
        print("Sample dates:", list(set(dates))[:10])
        
    # Let's search for titles of news or press releases
    # Usually in <h3> or similar tags, or inside JSON data (e.g. Next.js __NEXT_DATA__)
    next_data = re.search(r'__NEXT_DATA__.*?({.*?})', content)
    if next_data:
        print("Found __NEXT_DATA__ json structure!")
        # let's save a snippet
        json_str = next_data.group(1)
        print("Length of __NEXT_DATA__ json:", len(json_str))
        # Find some text within __NEXT_DATA__
        # Look for titles or news
        news_matches = re.findall(r'"title"\s*:\s*"([^"]+)"', json_str)
        print("Titles in __NEXT_DATA__:", len(news_matches))
        for t in news_matches[:10]:
            print("  -", t)
    else:
        # Standard search for headings
        headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', content, re.IGNORECASE)
        print(f"Headings count: {len(headings)}")
        for h in headings[:15]:
            print("  -", h.strip()[:100])
