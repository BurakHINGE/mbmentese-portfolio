import os
import re

DOMAIN = "https://mburakmentese.dev"

def get_canonical_url(filepath):
    # Convert local path to canonical URL path
    # e.g., ./index.html -> https://mburakmentese.dev/
    # e.g., ./blog.html -> https://mburakmentese.dev/blog
    # e.g., ./blog/mac-adresi-ve-arp/index.html -> https://mburakmentese.dev/blog/mac-adresi-ve-arp
    clean_path = filepath.replace('./', '').replace('index.html', '')
    if clean_path.endswith('.html'):
        clean_path = clean_path[:-5]
    if clean_path.endswith('/'):
        clean_path = clean_path[:-1]
    
    if clean_path == "":
        return DOMAIN
    else:
        return f"{DOMAIN}/{clean_path}"

def generate_schema(filepath, url):
    if filepath in ['./index.html', './hakkimda.html']:
        return """
    <!-- YENİ EKLENDİ: SEO Schema Markup (Person) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Mehmet Burak Menteşe",
      "url": "https://mburakmentese.dev",
      "jobTitle": "Computer Engineering Student & Developer",
      "alumniOf": "Marmara University",
      "sameAs": [
        "https://github.com/BurakHINGE",
        "https://www.linkedin.com/in/mehmetburakmentese/",
        "https://medium.com/@burakmentese16"
      ]
    }
    </script>"""
    elif 'blog/' in filepath or 'projeler/' in filepath:
        # Extract title from h1 if possible, otherwise generic
        return f"""
    <!-- YENİ EKLENDİ: SEO Schema Markup (Article/Project) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "author": {{
        "@type": "Person",
        "name": "Mehmet Burak Menteşe"
      }},
      "url": "{url}"
    }}
    </script>"""
    return ""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    url = get_canonical_url(filepath)

    # 1. Add Canonical Tag
    if '<link rel="canonical"' not in content:
        canonical_tag = f'\n    <!-- YENİ EKLENDİ: Canonical URL -->\n    <link rel="canonical" href="{url}" />'
        # Insert before </head>
        content = content.replace('</head>', f'{canonical_tag}\n</head>')

    # 2. Add Schema Markup
    if 'application/ld+json' not in content:
        schema_tag = generate_schema(filepath, url)
        content = content.replace('</head>', f'{schema_tag}\n</head>')

    # 3. Merge duplicated Heading tags (h1, h2, h3) for TR/EN translations
    # Pattern looks for <hX class="... content-tr">TEXT_TR</hX> \s* <hX class="... content-en" style="display:none;">TEXT_EN</hX>
    # Note: 'style="display:none;"' might be 'style="display: none;"'
    
    # H1
    h1_pattern = re.compile(r'<h1([^>]*)class="([^"]*?)content-tr([^"]*)"([^>]*)>(.*?)</h1>\s*<h1([^>]*)class="([^"]*?)content-en([^"]*)"[^>]*display:\s*none;?[^>]*>(.*?)</h1>', re.IGNORECASE | re.DOTALL)
    
    def h1_repl(m):
        # We merge them into a single H1, applying the classes of the first (minus content-tr) to the H1,
        # and putting content-tr/en on spans inside.
        classes_before = m.group(2).strip()
        classes_after = m.group(3).strip()
        h1_classes = f"{classes_before} {classes_after}".strip()
        
        tr_text = m.group(5).strip()
        en_text = m.group(9).strip()
        
        return f'<h1 class="{h1_classes}">\n    <span class="content-tr">{tr_text}</span>\n    <span class="content-en" style="display:none;">{en_text}</span>\n</h1>'

    content = h1_pattern.sub(h1_repl, content)

    # H2
    h2_pattern = re.compile(r'<h2([^>]*)class="([^"]*?)content-tr([^"]*)"([^>]*)>(.*?)</h2>\s*<h2([^>]*)class="([^"]*?)content-en([^"]*)"[^>]*display:\s*none;?[^>]*>(.*?)</h2>', re.IGNORECASE | re.DOTALL)
    def h2_repl(m):
        classes_before = m.group(2).strip()
        classes_after = m.group(3).strip()
        h2_classes = f"{classes_before} {classes_after}".strip()
        tr_text = m.group(5).strip()
        en_text = m.group(9).strip()
        
        class_attr = f' class="{h2_classes}"' if h2_classes else ''
        return f'<h2{class_attr}>\n    <span class="content-tr">{tr_text}</span>\n    <span class="content-en" style="display:none;">{en_text}</span>\n</h2>'

    content = h2_pattern.sub(h2_repl, content)
    
    # H3
    h3_pattern = re.compile(r'<h3([^>]*)class="([^"]*?)content-tr([^"]*)"([^>]*)>(.*?)</h3>\s*<h3([^>]*)class="([^"]*?)content-en([^"]*)"[^>]*display:\s*none;?[^>]*>(.*?)</h3>', re.IGNORECASE | re.DOTALL)
    def h3_repl(m):
        classes_before = m.group(2).strip()
        classes_after = m.group(3).strip()
        h3_classes = f"{classes_before} {classes_after}".strip()
        tr_text = m.group(5).strip()
        en_text = m.group(9).strip()
        
        class_attr = f' class="{h3_classes}"' if h3_classes else ''
        return f'<h3{class_attr}>\n    <span class="content-tr">{tr_text}</span>\n    <span class="content-en" style="display:none;">{en_text}</span>\n</h3>'

    content = h3_pattern.sub(h3_repl, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


# Find all HTML files
import glob
html_files = glob.glob('./**/*.html', recursive=True)

for file in html_files:
    process_file(file)

print("HTML files processed for Canonical, Schema, and Heading Sync.")

# Generate XML Sitemap
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for file in html_files:
    if '404.html' in file:
        continue
    url = get_canonical_url(file)
    sitemap_content += f'''  <url>
    <loc>{url}</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n'''

sitemap_content += '</urlset>'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print("sitemap.xml generated.")

