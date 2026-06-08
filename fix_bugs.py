import os
import re
import glob

html_files = glob.glob('*.html')

def get_nav(current_page):
    def is_active(page):
        return 'text-primary font-semibold border-b-2 border-primary' if current_page == page else 'text-on-surface-variant hover:text-primary transition-colors'
        
    return f"""<nav class="fixed top-0 w-full z-50 bg-surface/70 backdrop-blur-xl border-b border-outline-variant/10 shadow-sm h-16 transition-all duration-300">
  <div class="flex justify-between items-center h-full px-4 md:px-8 max-w-7xl mx-auto">
    <!-- Logo -->
    <a href="index.html" class="flex items-baseline gap-3 select-none hover:opacity-80 transition-opacity">
      <span class="font-sans text-xl font-black tracking-tight text-on-surface uppercase">DDK</span>
      <span class="text-zinc-400 text-sm mx-0.5 select-none">/</span>
      <span class="font-sans text-[10px] font-normal tracking-[0.3em] text-zinc-500 uppercase hidden sm:block">Technologies & Co.</span>
    </a>
    
    <!-- Desktop Links -->
    <div class="hidden md:flex items-center gap-8">
      <a class="font-body-md text-body-md {is_active('index.html')}" href="index.html">Home</a>
      <a class="font-body-md text-body-md {is_active('services.html')}" href="services.html">Services</a>
      <a class="font-body-md text-body-md {is_active('products.html')}" href="products.html">Products</a>
      <a class="font-body-md text-body-md {is_active('about.html')}" href="about.html">About</a>
    </div>

    <!-- Right Actions -->
    <div class="flex items-center gap-4">
      <a href="contact.html" class="hidden sm:block"><button class="bg-primary text-on-primary px-6 py-2 rounded-xl font-body-md text-body-md hover:opacity-80 active:scale-95 transition-all">Contact</button></a>
      <button id="mobile-menu-btn" class="md:hidden p-2 text-on-surface hover:text-primary transition-colors"><span class="material-symbols-outlined text-2xl">menu</span></button>
    </div>
  </div>
</nav>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace entire <nav>...</nav>
    # Find <nav>...</nav>
    nav_pattern = re.compile(r'<nav.*?</nav>', re.DOTALL)
    new_nav = get_nav(file)
    content = nav_pattern.sub(new_nav, content)
    
    # 2. Fix index.html Hero buttons
    if file == 'index.html':
        btn_work = r'<button class="w-full md:w-auto bg-primary text-on-primary px-8 py-4 rounded-xl font-headline-sm text-body-md active:scale-95 transition-all shadow-lg shadow-primary/20">\s*Work with us\s*</button>'
        btn_work_new = r'<a href="contact.html" class="w-full md:w-auto"><button class="w-full bg-primary text-on-primary px-8 py-4 rounded-xl font-headline-sm text-body-md active:scale-95 transition-all shadow-lg shadow-primary/20">Work with us</button></a>'
        content = re.sub(btn_work, btn_work_new, content)
        
        btn_view = r'<button class="w-full md:w-auto glass-panel px-8 py-4 rounded-xl font-headline-sm text-body-md text-on-surface active:scale-95 transition-all">\s*View Products\s*</button>'
        btn_view_new = r'<a href="products.html" class="w-full md:w-auto"><button class="w-full glass-panel px-8 py-4 rounded-xl font-headline-sm text-body-md text-on-surface active:scale-95 transition-all">View Products</button></a>'
        content = re.sub(btn_view, btn_view_new, content)
        
    # 3. Fix services.html responsiveness (padding)
    if file == 'services.html':
        content = content.replace('px-margin-desktop', 'px-4 md:px-8')
        content = content.replace('px-margin-mobile', 'px-4 md:px-8')
        content = content.replace('p-10', 'p-6 md:p-10')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixes applied successfully.")
