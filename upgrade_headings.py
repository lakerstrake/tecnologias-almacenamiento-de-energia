import re

file_path = 'c:/Users/USER PC/expotencia/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add gradient-heading to h1 and h2 tags
content = re.sub(r'<h1 class="', r'<h1 class="gradient-heading ', content)
content = re.sub(r'<h2 class="', r'<h2 class="gradient-heading ', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Headings updated with premium gradient")
