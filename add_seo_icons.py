import os
import re

# 1. Create public directory and favicon.svg
os.makedirs('public', exist_ok=True)
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#4B5563">
  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
</svg>'''

with open('public/favicon.svg', 'w', encoding='utf-8') as f:
    f.write(favicon_svg)

# 2. Add meta tags to all HTML files
files = ['index.html', 'about.html', 'products.html', 'contact.html', 'services.html', 'portal.html', 'software.html', 'video-editing.html', 'privacy-policy.html']

seo_tags = '''
    <!-- Favicon and SEO Image -->
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta property="og:image" content="/favicon.svg" />
    <meta name="twitter:image" content="/favicon.svg" />
    <meta property="og:title" content="DDK Technologies Studio" />
    <meta property="og:description" content="Premium software engineering and digital transformation." />
'''

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Insert right before </head>
        if '<link rel="icon"' not in content:
            content = content.replace('</head>', seo_tags + '</head>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)

print("SEO tags and favicon added successfully.")
