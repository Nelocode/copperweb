from html.parser import HTMLParser

class TagBalancer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        # self-closing tags in HTML5
        self_closing = {'img', 'br', 'hr', 'meta', 'link', 'input', 'source', 'video'}
        if tag not in self_closing:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        self_closing = {'img', 'br', 'hr', 'meta', 'link', 'input', 'source', 'video'}
        if tag in self_closing:
            return
        if not self.stack:
            self.errors.append(f"Unmatched closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack.pop()
        if last_tag != tag:
            self.errors.append(f"Mismatched tag: started with <{last_tag}> at line {pos[0]}, closed with </{tag}> at line {self.getpos()[0]}")

filepath = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/corporate.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

parser = TagBalancer()
parser.feed(content)

if parser.stack:
    print("Unclosed tags remaining in stack:")
    for tag, pos in parser.stack:
        print(f"  <{tag}> started at line {pos[0]}")
else:
    print("No unclosed tags!")

if parser.errors:
    print("Mismatched / Unmatched tag errors:")
    for err in parser.errors:
        print(" ", err)
else:
    print("No tag mismatches!")
