import re

file_path = 'c:/Users/USER PC/expotencia/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Revert section tags
content = re.sub(r'<section data-auto-animate class="w-full h-full flex flex-col justify-center px-4 md:px-12 lg:px-24 overflow-y-auto overflow-x-hidden">', r'<section data-auto-animate>', content)
content = re.sub(r'<section data-auto-animate class="text-center w-full h-full flex flex-col justify-center px-4 md:px-12 lg:px-24 overflow-y-auto overflow-x-hidden">', r'<section data-auto-animate class="text-center">', content)

# Revert specific heights that got too small for 1080p
content = re.sub(r'h-\[300px\] lg:h-\[600px\]', r'h-[600px]', content)
content = re.sub(r'h-\[300px\] lg:h-\[650px\]', r'h-[650px]', content)
content = re.sub(r'h-\[300px\] lg:h-\[550px\]', r'h-[550px]', content)
content = re.sub(r'h-\[400px\] lg:h-\[700px\]', r'h-[700px]', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML reverted sections")
