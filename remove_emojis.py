import re

file_path = 'c:/Users/USER PC/expotencia/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for most emojis, strictly avoiding standard punctuation
emoji_pattern = re.compile(
    r'['
    r'\U0001F600-\U0001F64F'  # emoticons
    r'\U0001F300-\U0001F5FF'  # symbols & pictographs
    r'\U0001F680-\U0001F6FF'  # transport & map symbols
    r'\U0001F700-\U0001F77F'  # alchemical symbols
    r'\U0001F780-\U0001F7FF'  # Geometric Shapes Extended
    r'\U0001F800-\U0001F8FF'  # Supplemental Arrows-C
    r'\U0001F900-\U0001F9FF'  # Supplemental Symbols and Pictographs
    r'\U0001FA00-\U0001FA6F'  # Chess Symbols
    r'\U0001FA70-\U0001FAFF'  # Symbols and Pictographs Extended-A
    r'\u2600-\u26FF'          # Miscellaneous Symbols
    r'\u2705'                 # Check mark
    r'\u274C'                 # Cross mark
    r'\u23E9-\u23FA'          # Fast forward, play, pause, etc.
    r']+',
    re.UNICODE
)

content_clean = emoji_pattern.sub('', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content_clean)

