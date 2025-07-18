import sys
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup

def convert_notebook_to_html(notebook_path):
    notebook = Path(notebook_path)
    if not notebook.exists():
        print(f"❌ File not found: {notebook_path}")
        return

    html_output = notebook.with_suffix('.html')
    
    # Convert .ipynb to .html
    print(f"🔄 Converting {notebook.name} to HTML...")
    subprocess.run([
        "jupyter", "nbconvert",
        "--to", "html",
        "--output", html_output.name,
        notebook.name
    ], check=True)

    # Inject dark CSS
    css_file = Path("dark-theme.css")
    if not css_file.exists():
        print("❌ dark-theme.css not found in current directory.")
        return

    with open(css_file, "r", encoding="utf-8") as f:
        dark_css = f.read()

    with open(html_output, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    style_tag = soup.new_tag("style")
    style_tag.string = dark_css
    soup.head.append(style_tag)

    with open(html_output, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"✅ Done! Dark-themed HTML saved as: {html_output}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_with_dark.py MyNotebook.ipynb")
    else:
        convert_notebook_to_html(sys.argv[1])
