import re
import json

filepath = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas5.html"

with open(filepath, "r", encoding="utf-8") as f:
    html_content = f.read()

# Let's search for JSON-like strings inside the file.
# It seems there is a database of news embedded in the HTML or a JSON string.
# Let's find all chunks starting with {"id": or containing "title":
# Actually, let's look for __NEXT_DATA__ again or search for json structures.
json_matches = re.finditer(r'\{"id":\d+,"title":.*?\}(?=,\{|\]\})', html_content)
news_list = []
seen_ids = set()

for match in json_matches:
    try:
        data = json.loads(match.group(0))
        if "title" in data and "id" in data:
            if data["id"] not in seen_ids:
                seen_ids.add(data["id"])
                news_list.append(data)
    except Exception as e:
        # Maybe partial json, let's try to fix it or just parse it
        pass

# If news_list is empty, let's search using a regular expression for the json-like structure
if not news_list:
    # Let's search for the news section content in text
    print("No direct simple JSON matches found. Let's do a broader regex on the JSON array.")
    # Search for something like: [{"id":...}]
    # We can search for '"id":' and then search for brackets
    # Let's find all occurrences of: "id":
    id_indices = [m.start() for m in re.finditer(r'"id":\d+', html_content)]
    print(f"Found {len(id_indices)} occurrences of 'id':")
    # Let's print the text around the first few to see if they are in a JSON array
    for idx in id_indices[:5]:
        print(html_content[idx:idx+300])
        print("-" * 40)

# Let's write another script that parses all titles, dates, excerpts, and pdf links.
# Let's do a regex that extracts title, date, excerpt, pdf link.
# Looking at the HTML structure:
# We have items like:
# "April 8, 2026 ... Copper Giant Targets New Porphyry Centers Beyond Mocoa Resource with Third Drill Rig"
# "https://mviwzjlrkcinutxpykvc.supabase.co/storage/v1/object/public/documents/2/CGNT_2026-04-08_06-40-12.pdf"
# Let's find all PDF links in the file!
pdf_links = re.findall(r'https://[^\s"\'>]+\.pdf', html_content)
print(f"Found {len(pdf_links)} PDF links:")
for pdf in set(pdf_links):
    print("  -", pdf)

# Let's write a parser that extracts each news block from the HTML.
# A news block seems to start with a date, followed by a category or title, then description/excerpt, then PDF link.
# Let's find dates and extract text between dates.
# Let's write a python script to parse the news sequentially using HTML structure.
