import sys
from pathlib import Path
from bs4 import BeautifulSoup

css_path = Path("styles/dark-theme.css")
with open(css_path, "r", encoding="utf-8") as css_file:
    css_content = css_file.read()

for notebook_html in Path("rendered").glob("*.html"):
    with open(notebook_html, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    style_tag = soup.new_tag("style")
    style_tag.string = css_content
    soup.head.append(style_tag)

    with open(notebook_html, "w", encoding="utf-8") as file:
        file.write(str(soup))

    print(f"✅ Applied dark theme to {notebook_html}")
