import re

filepath = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas5.html"

with open(filepath, "r", encoding="utf-8") as f:
    html_content = f.read()

def clean_html(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# List of PDF links found
pdfs = [
    "https://mviwzjlrkcinutxpykvc.supabase.co/storage/v1/object/public/cms-assets/company-2/news-releases/2026-05-05-cgnt-mocoa-pea-final.pdf",
    "https://mviwzjlrkcinutxpykvc.supabase.co/storage/v1/object/public/documents/2/4001181.pdf", # Let's see which one this is
    "https://mviwzjlrkcinutxpykvc.supabase.co/storage/v1/object/public/documents/2/CGNT_2026-04-24_12-26-16.pdf",
    "https://mviwzjlrkcinutxpykvc.supabase.co/storage/v1/object/public/documents/2/CGNT_2026-04-14_06-44-53.pdf",
]

print(f"Total PDFs to inspect: {len(pdfs)}")

for idx, pdf in enumerate(pdfs):
    pos = html_content.find(pdf)
    if pos != -1:
        # Let's extract 1500 characters before the PDF link
        start = max(0, pos - 1500)
        context = html_content[start:pos + 100]
        
        # Let's find dates and titles in this context using regex
        # Date pattern
        dates = re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}', context)
        # Heading pattern
        headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', context, re.IGNORECASE)
        # Excerpt
        clean_context = clean_html(html_content[start:pos])
        
        print(f"\n=================== NEWS RELEASE {idx+1} ===================")
        print(f"PDF Link: {pdf}")
        print(f"Detected Dates: {dates}")
        print(f"Detected Headings: {headings}")
        print(f"Cleaned Text Context (last 600 chars):")
        print(clean_context[-800:])
    else:
        print(f"PDF not found in HTML: {pdf}")
