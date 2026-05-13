import re

file_path = 'c:/Users/USER PC/expotencia/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Reduce heights to prevent overflow in Reveal's slide container
replacements = {
    r'h-\[600px\]': 'h-[450px]',
    r'h-\[650px\]': 'h-[500px]',
    r'h-\[700px\]': 'h-[550px]',
    r'h-\[550px\]': 'h-[400px]',
    r'mb-12': 'mb-6',
    r'mb-16': 'mb-8',
    r'gap-12': 'gap-6',
    r'gap-8': 'gap-4',
    r'p-12': 'p-6',
    r'p-10': 'p-6'
}

for old, new in replacements.items():
    content = re.sub(old, new, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Heights and margins reduced")
