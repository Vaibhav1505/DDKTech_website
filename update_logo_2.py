import os
import re

files = ['index.html', 'about.html', 'products.html', 'contact.html', 'services.html', 'portal.html', 'software.html', 'video-editing.html', 'privacy-policy.html']

old_logo_nav = '''<div class="flex items-baseline gap-3 select-none">
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

old_logo_footer = '''<div class="flex items-baseline gap-3 select-none mb-6">
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

new_logo_nav = '''<div class="flex items-center gap-2 select-none group cursor-pointer">
  <span class="material-symbols-outlined text-[24px] text-zinc-600">public</span>
  <div class="flex items-center">
    <span class="font-sans text-[20px] tracking-tight text-zinc-500 font-medium">DDK Technologie</span>
    <span class="font-sans text-[20px] tracking-tight text-zinc-500 font-medium opacity-20">s</span>
    <span class="h-5 w-[1px] bg-zinc-300 ml-2 animate-[pulse_1s_ease-in-out_infinite]"></span>
  </div>
</div>'''

new_logo_footer = '''<div class="flex items-center gap-2 select-none group cursor-pointer mb-6">
  <span class="material-symbols-outlined text-[24px] text-zinc-600">public</span>
  <div class="flex items-center">
    <span class="font-sans text-[20px] tracking-tight text-zinc-500 font-medium">DDK Technologie</span>
    <span class="font-sans text-[20px] tracking-tight text-zinc-500 font-medium opacity-20">s</span>
    <span class="h-5 w-[1px] bg-zinc-300 ml-2 animate-[pulse_1s_ease-in-out_infinite]"></span>
  </div>
</div>'''

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update TopNavBar logo
        content = content.replace(old_logo_nav, new_logo_nav)
        
        # Update Footer logo
        content = content.replace(old_logo_footer, new_logo_footer)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Globe logo updated successfully.")
