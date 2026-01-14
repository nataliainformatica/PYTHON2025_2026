#tema arrays y strings

def parse_markdown_list(text):
    lines = text.strip().split("\n")
    items = []

    for line in lines:
        if line.startswith("- "):
            items.append(f"<li>{line[2:]}</li>")

    return "<ul>\n" + "\n".join(items) + "\n</ul>"

#si no se puede usar split(), vamos a hacerlo manualmente

def split_manual(text, sep=" "):
    result = []
    current = ""

    for char in text:
        if char == sep:
            result.append(current)
            current = ""
        else:
            current += char

    # Agregar la última palabra
    result.append(current)
    return result


# Ejemplo
markdown = "- Apple\n- Banana\n- Cherry"
print(parse_markdown_list(markdown))
