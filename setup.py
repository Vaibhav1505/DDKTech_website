import os
import re
import json

files = ['index.html', 'about.html', 'products.html', 'contact.html', 'services.html', 'portal.html']
html_dir = '.'

# 1. Extract tailwind config from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

config_match = re.search(r'tailwind\.config = (\{.*?\})\s*</script>', content, re.DOTALL)
if config_match:
    tw_config = config_match.group(1)
    
    # We need to create a valid tailwind.config.js
    # The extracted tw_config is a JS object, we need to wrap it.
    tailwind_js = f"""/** @type {{import('tailwindcss').Config}} */
export default {{
  content: [
    "./*.html",
    "./*.js"
  ],
  darkMode: "class",
  theme: {tw_config}.theme,
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries')
  ],
}}
"""
    with open('tailwind.config.js', 'w', encoding='utf-8') as f:
        f.write(tailwind_js)

# 2. Add SEO & fix Nav & CSS in all files
nav_links = {
    'Home': 'index.html',
    'Services': 'services.html',
    'Products': 'products.html',
    'About': 'about.html',
    'Contact': 'contact.html'
}

seo_data = {
    'index.html': {'title': 'DDK Technologies Studio | Premium Software & Web Development', 'desc': 'DDK Technologies Studio builds high-fidelity software, apps, and websites. We transform complex problems into elegant scalable solutions.'},
    'about.html': {'title': 'About Us | DDK Technologies Studio', 'desc': 'Learn about DDK Technologies Studio, our mission, vision, and the expert team behind our premium software solutions.'},
    'products.html': {'title': 'Our Products | DDK Technologies Studio', 'desc': 'Explore our featured in-house products like ApplySync and Twined, built with modern web architecture and AI.'},
    'contact.html': {'title': 'Contact Us | DDK Technologies Studio', 'desc': 'Get in touch with DDK Technologies Studio to scale your digital presence and build extraordinary products.'},
    'services.html': {'title': 'Our Services | DDK Technologies Studio', 'desc': 'We offer premium Web Development, App Development, Software Engineering, and Video Editing services.'},
    'portal.html': {'title': 'Corporate Portal | DDK Technologies Studio', 'desc': 'Client and employee corporate portal for DDK Technologies Studio.'},
    'software.html': {'title': 'Software Engineering | DDK Technologies Studio', 'desc': 'Enterprise-grade backend systems, custom API integrations, and scalable software solutions.'},
    'video-editing.html': {'title': 'Video Editing | DDK Technologies Studio', 'desc': 'High-fidelity post-production, motion graphics, and premium video editing services for modern brands.'}
}

def process_html(filename, content):
    # Replace CDN tailwind with local CSS
    content = re.sub(r'<script src="https://cdn\.tailwindcss\.com\?plugins=forms,container-queries"></script>', '', content)
    content = re.sub(r'<script id="tailwind-config">.*?</script>', '<link rel="stylesheet" href="./style.css">', content, flags=re.DOTALL)
    
    # Update title and add meta description
    seo = seo_data.get(filename, seo_data['index.html'])
    title_tag = f'<title>{seo["title"]}</title>\n    <meta name="description" content="{seo["desc"]}">'
    content = re.sub(r'<title>.*?</title>', title_tag, content, flags=re.DOTALL)
    
    # Add keywords
    if '<meta name="keywords"' not in content:
        content = content.replace('<head>', '<head>\n    <meta name="keywords" content="Software Development, Web Design, App Development, DDK Technologies, Tech Studio, Video Editing">')

    # Update nav links
    content = re.sub(r'href="[^"]*"([^>]*>Home<)', f'href="index.html"\\1', content)
    content = re.sub(r'href="[^"]*"([^>]*>Services<)', f'href="services.html"\\1', content)
    content = re.sub(r'href="[^"]*"([^>]*>Products<)', f'href="products.html"\\1', content)
    content = re.sub(r'href="[^"]*"([^>]*>About<)', f'href="about.html"\\1', content)
    
    # Update Contact button in Nav
    content = re.sub(r'<button([^>]*)>\s*Contact\s*</button>', r'<a href="contact.html"><button\1>Contact</button></a>', content)
    
    return content

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = process_html(file, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

# 3. Create software.html and video-editing.html based on services.html
with open('services.html', 'r', encoding='utf-8') as f:
    services_content = f.read()

# Software HTML
software_content = services_content.replace('What We Do', 'Software Engineering')
software_content = software_content.replace('Bespoke web architectures', 'We build enterprise-grade backend systems and scalable software solutions.')
software_content = process_html('software.html', software_content)
with open('software.html', 'w', encoding='utf-8') as f:
    f.write(software_content)

# Video Editing HTML
video_content = services_content.replace('What We Do', 'Premium Video Editing')
video_content = video_content.replace('Bespoke web architectures', 'High-fidelity post-production and motion graphics for modern brands.')
video_content = process_html('video-editing.html', video_content)
with open('video-editing.html', 'w', encoding='utf-8') as f:
    f.write(video_content)

print("Python script executed successfully!")
