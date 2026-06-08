import os
import re

files = ['index.html', 'about.html', 'products.html', 'contact.html', 'services.html', 'portal.html', 'software.html', 'video-editing.html', 'privacy-policy.html']

logo_html_nav = '''<div class="flex items-baseline gap-3 select-none">
  <!-- Core Monospace/Grotesque Wordmark -->
  <span class="font-sans text-xl font-black tracking-tight text-on-surface uppercase">
    DDK
  </span>
  
  <!-- Single Technical Splitter -->
  <span class="text-zinc-400 text-sm mx-0.5 select-none">/</span>
  
  <!-- Minimal Subtext Descriptor -->
  <span class="font-sans text-[10px] font-normal tracking-[0.3em] text-zinc-500 uppercase">
    Technologies & Co.
  </span>
</div>'''

logo_html_footer = '''<div class="flex items-baseline gap-3 select-none mb-6">
  <!-- Core Monospace/Grotesque Wordmark -->
  <span class="font-sans text-xl font-black tracking-tight text-on-surface uppercase">
    DDK
  </span>
  
  <!-- Single Technical Splitter -->
  <span class="text-zinc-400 text-sm mx-0.5 select-none">/</span>
  
  <!-- Minimal Subtext Descriptor -->
  <span class="font-sans text-[10px] font-normal tracking-[0.3em] text-zinc-500 uppercase">
    Technologies & Co.
  </span>
</div>'''

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update TopNavBar logo
        content = content.replace('<div class="font-display-lg text-headline-sm font-bold text-on-surface">DDK Technologies &amp; Co.</div>', logo_html_nav)
        
        # Update Footer logo
        content = content.replace('<div class="font-display-lg text-headline-sm font-bold text-on-surface mb-6">DDK Technologies &amp; Co.</div>', logo_html_footer)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Logo updated successfully.")
