import os
from datetime import datetime

# Base URL of your website
BASE_URL = "https://busara-s.github.io"

# Directory containing your HTML files (adjust this if necessary)
SITE_DIRECTORY = "."

# Sitemap filename
SITEMAP_FILE = "sitemap.xml"

def generate_sitemap(base_url, site_directory, sitemap_file):
    urls = []
    for root, _, files in os.walk(site_directory):
        for file in files:
            if file.endswith(".html"):
                relative_path = os.path.relpath(os.path.join(root, file), site_directory)
                url = f"{base_url}/{relative_path.replace(os.sep, '/')}"
                lastmod = datetime.now().strftime("%Y-%m-%d")
                urls.append((url, lastmod))

    with open(sitemap_file, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url, lastmod in urls:
            f.write(f"  <url>\n")
            f.write(f"    <loc>{url}</loc>\n")
            f.write(f"    <lastmod>{lastmod}</lastmod>\n")
            f.write(f"  </url>\n")
        f.write('</urlset>\n')

if __name__ == "__main__":
    generate_sitemap(BASE_URL, SITE_DIRECTORY, SITEMAP_FILE)
    print(f"Sitemap generated at {SITEMAP_FILE}")
