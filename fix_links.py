import os
import glob
import re

def fix_links_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Navbar and Footer links
    replacements = {
        'href="index.html"': 'href="/"',
        'href="../../index.html"': 'href="/"',
        'href="hakkimda.html"': 'href="/hakkimda"',
        'href="../../hakkimda.html"': 'href="/hakkimda"',
        'href="projeler.html"': 'href="/projeler"',
        'href="../../projeler.html"': 'href="/projeler"',
        'href="blog.html"': 'href="/blog"',
        'href="../../blog.html"': 'href="/blog"',
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Project and Blog detail links
    # href="projeler/local-RAG-assistant/index.html" -> href="/projeler/local-RAG-assistant"
    # Match href="projeler/SOME_NAME/index.html"
    content = re.sub(r'href="projeler/([^/]+)/index\.html"', r'href="/projeler/\1"', content)
    
    # Match href="blog/SOME_NAME/index.html"
    content = re.sub(r'href="blog/([^/]+)/index\.html"', r'href="/blog/\1"', content)

    # What if they are linked relatively from inside another project?
    # e.g., href="../../blog/mac-adresi/index.html"
    content = re.sub(r'href="\.\./\.\./projeler/([^/]+)/index\.html"', r'href="/projeler/\1"', content)
    content = re.sub(r'href="\.\./\.\./blog/([^/]+)/index\.html"', r'href="/blog/\1"', content)

    # Let's also ensure style.css and Assets use absolute paths to prevent any nested directory issues!
    content = re.sub(r'href="style\.css', r'href="/style.css', content)
    content = re.sub(r'href="\.\./\.\./style\.css', r'href="/style.css', content)
    
    content = re.sub(r'src="\./Assets/', r'src="/Assets/', content)
    content = re.sub(r'src="Assets/', r'src="/Assets/', content)
    content = re.sub(r'src="\.\./\.\./Assets/', r'src="/Assets/', content)
    content = re.sub(r'href="\.\./\.\./Assets/', r'href="/Assets/', content)
    content = re.sub(r'href="\./Assets/', r'href="/Assets/', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

html_files = glob.glob('./**/*.html', recursive=True)
for file in html_files:
    fix_links_in_file(file)

print("All links updated successfully.")
