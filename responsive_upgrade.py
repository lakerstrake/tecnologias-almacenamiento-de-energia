import re

file_path = 'c:/Users/USER PC/expotencia/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r'grid grid-cols-2': 'grid grid-cols-1 lg:grid-cols-2',
    r'grid md:grid-cols-3': 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3',
    r'grid grid-cols-3': 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3',
    r'w-1/2': 'w-full lg:w-1/2',
    r'w-7/12': 'w-full lg:w-7/12',
    r'w-5/12': 'w-full lg:w-5/12',
    r'flex gap-12': 'flex flex-col lg:flex-row gap-6 lg:gap-12',
    r'flex items-center gap-12': 'flex flex-col lg:flex-row items-center gap-6 lg:gap-12',
    r'h-\[600px\]': 'h-[300px] lg:h-[600px]',
    r'h-\[650px\]': 'h-[300px] lg:h-[650px]',
    r'h-\[550px\]': 'h-[300px] lg:h-[550px]',
    r'h-\[700px\]': 'h-[400px] lg:h-[700px]',
    r'text-5xl': 'text-3xl lg:text-5xl',
    r'text-6xl': 'text-4xl lg:text-6xl',
    r'text-7xl': 'text-4xl md:text-5xl lg:text-7xl',
    r'p-8': 'p-4 lg:p-8',
    r'p-6': 'p-4 lg:p-6',
    r'mb-16': 'mb-8 lg:mb-16',
    r'mb-12': 'mb-6 lg:mb-12',
    r'mb-10': 'mb-6 lg:mb-10',
    r'mb-8': 'mb-4 lg:mb-8',
    r'gap-8': 'gap-4 lg:gap-8',
    r'max-w-5xl mx-auto border-l-4': 'w-full max-w-5xl mx-auto border-l-4'
}

for old, new in replacements.items():
    content = re.sub(old, new, content)

# Inject responsive padding to sections
content = re.sub(r'<section data-auto-animate>', r'<section data-auto-animate class="w-full h-full flex flex-col justify-center px-4 md:px-12 lg:px-24 overflow-y-auto overflow-x-hidden">', content)
content = re.sub(r'<section data-auto-animate class="text-center">', r'<section data-auto-animate class="text-center w-full h-full flex flex-col justify-center px-4 md:px-12 lg:px-24 overflow-y-auto overflow-x-hidden">', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML optimized for responsiveness")
