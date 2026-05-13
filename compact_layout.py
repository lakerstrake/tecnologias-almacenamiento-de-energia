import re

file_path = 'c:/Users/USER PC/expotencia/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Aggressively reduce all vertical margins and paddings
replacements = {
    r'p-8': 'p-4',
    r'p-6': 'p-4',
    r'mb-12': 'mb-4',
    r'mb-8': 'mb-4',
    r'mb-6': 'mb-2',
    r'gap-12': 'gap-4',
    r'gap-8': 'gap-4',
    r'gap-6': 'gap-4',
    r'h-\[600px\]': 'h-[400px]',
    r'h-\[650px\]': 'h-[450px]',
    r'h-\[500px\]': 'h-[380px]',
    r'h-\[550px\]': 'h-[400px]',
    r'h-\[450px\]': 'h-[350px]',
    r'h-\[700px\]': 'h-[480px]',
    r'text-5xl': 'text-4xl',
    r'text-4xl': 'text-3xl'
}

for old, new in replacements.items():
    content = re.sub(old, new, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Aggressive layout compaction complete")
