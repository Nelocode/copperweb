import re

filepath = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas5.html"

with open(filepath, "r", encoding="utf-8") as f:
    html_content = f.read()

# Let's clean up html tags from text for easy reading
def clean_html(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Let's search for the titles and their exact surrounding texts
# We want to find dates, categories, titles, and paragraphs.
# Since it's a Next.js/Tailwind or static site, there might be recurring patterns.
# Let's look for dates like "May 12, 2026" or similar, and check what text is next to them.

# Let's find all occurrences of date patterns: e.g., "April 28, 2026", "March 18, 2026" etc.
# We can search for month names and numbers.
date_regex = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}'

# Let's find all matches
matches = list(re.finditer(date_regex, html_content))
print(f"Found {len(matches)} dates.")

for i, match in enumerate(matches):
    start = match.start()
    # Let's grab context from start to 800 characters after
    context = html_content[start:start+1000]
    cleaned = clean_html(context)
    print(f"\n--- DATE MATCH {i+1}: {match.group(0)} ---")
    print(cleaned[:400] + "...")
