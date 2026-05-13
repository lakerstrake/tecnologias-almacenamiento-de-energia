import re

file_path = 'c:/Users/USER PC/expotencia/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the aggressive hardcoded heights that were chopping off text
content = re.sub(r' h-\[350px\]', '', content)
content = re.sub(r' h-\[380px\]', '', content)
content = re.sub(r' h-\[400px\]', '', content)
content = re.sub(r' h-\[450px\]', '', content)
content = re.sub(r' h-\[480px\]', '', content)
# Also restore padding for aesthetics
content = re.sub(r'p-4', 'p-6', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored natural heights and padding")
