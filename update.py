import os
import re

files = ['index.html', 'about.html', 'products.html', 'contact.html', 'services.html', 'portal.html', 'software.html', 'video-editing.html']

# 1. Update contact info
email_old = 'hello@ddktech.co'
email_new = 'vaibhavsingh15052002@gmail.com'
email_old_caps = 'HELLO@DDKTECH.CO'
email_new_caps = 'VAIBHAVSINGH15052002@GMAIL.COM'

whatsapp_link = 'https://wa.me/7704886042'

# We'll map keywords in data-alt to real Unsplash images
images = {
    'abstract': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80',
    'code': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&q=80',
    'phone': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&q=80',
    'dashboard': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80',
    'dating': 'https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&q=80',
    'fiber': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80',
    'office': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80',
    'default': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&q=80'
}

def get_image_for_alt(alt_text):
    alt = alt_text.lower()
    if 'code' in alt or 'software' in alt: return images['code']
    if 'phone' in alt or 'mobile' in alt: return images['phone']
    if 'dashboard' in alt or 'ui' in alt: return images['dashboard']
    if 'dating' in alt or 'connection' in alt: return images['dating']
    if 'fiber' in alt or 'cable' in alt: return images['fiber']
    if 'abstract' in alt or '3d' in alt: return images['abstract']
    if 'office' in alt or 'people' in alt: return images['office']
    return images['default']

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update email
        content = content.replace(email_old, email_new)
        content = content.replace(email_old_caps, email_new_caps)
        
        # In contact.html, replace the WHATSAPP US href
        if file == 'contact.html':
            # find href="#" next to WHATSAPP US
            content = re.sub(r'href="#"([^>]*>\s*WHATSAPP US)', f'href="{whatsapp_link}"\\1', content)
        
        # Update images
        def replace_img(match):
            full_tag = match.group(0)
            alt_text = ''
            
            # Extract data-alt if present
            alt_match = re.search(r'data-alt="([^"]*)"', full_tag)
            if alt_match:
                alt_text = alt_match.group(1)
                
            new_src = get_image_for_alt(alt_text)
            
            # Replace the src attribute
            new_tag = re.sub(r'src="https://lh3\.googleusercontent\.com/[^"]*"', f'src="{new_src}"', full_tag)
            return new_tag

        content = re.sub(r'<img[^>]*src="https://lh3\.googleusercontent\.com/[^"]*"[^>]*>', replace_img, content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updates completed.")
