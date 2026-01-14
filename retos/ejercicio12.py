import re

def parse_markdown_link(text):
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    match = re.search(pattern, text)

    if match:
        label, url = match.groups()
        return f'<a href="{url}">{label}</a>'
    return text

# Ejemplo
print(parse_markdown_link("Visita [Google](https://google.com)"))
