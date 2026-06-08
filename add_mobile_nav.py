import os
import re
import glob

html_files = glob.glob('*.html')

drawer_html = """
<!-- Mobile Drawer -->
<div id="mobile-overlay" class="fixed inset-0 z-[90] bg-black/50 opacity-0 pointer-events-none transition-opacity duration-300 md:hidden"></div>
<div id="mobile-drawer" class="fixed inset-y-0 right-0 z-[100] w-64 bg-surface shadow-2xl transform translate-x-full transition-transform duration-300 md:hidden flex flex-col p-6 border-l border-outline-variant/20">
  <div class="flex justify-end mb-8">
    <button id="close-menu-btn" class="p-2 text-on-surface hover:text-primary transition-colors"><span class="material-symbols-outlined text-2xl">close</span></button>
  </div>
  <a class="font-headline-sm text-headline-sm mb-6 text-on-surface hover:text-primary transition-colors" href="index.html">Home</a>
  <a class="font-headline-sm text-headline-sm mb-6 text-on-surface hover:text-primary transition-colors" href="services.html">Services</a>
  <a class="font-headline-sm text-headline-sm mb-6 text-on-surface hover:text-primary transition-colors" href="products.html">Products</a>
  <a class="font-headline-sm text-headline-sm mb-6 text-on-surface hover:text-primary transition-colors" href="about.html">About</a>
  <a class="font-headline-sm text-headline-sm mt-auto text-on-surface hover:text-primary transition-colors" href="contact.html">Contact</a>
</div>
<script>
  const menuBtn = document.getElementById('mobile-menu-btn');
  const closeBtn = document.getElementById('close-menu-btn');
  const drawer = document.getElementById('mobile-drawer');
  const overlay = document.getElementById('mobile-overlay');

  function toggleMenu() {
    if (!drawer || !overlay) return;
    const isOpen = !drawer.classList.contains('translate-x-full');
    if (isOpen) {
      drawer.classList.add('translate-x-full');
      overlay.classList.add('opacity-0', 'pointer-events-none');
      overlay.classList.remove('opacity-100', 'pointer-events-auto');
    } else {
      drawer.classList.remove('translate-x-full');
      overlay.classList.remove('opacity-0', 'pointer-events-none');
      overlay.classList.add('opacity-100', 'pointer-events-auto');
    }
  }

  menuBtn?.addEventListener('click', toggleMenu);
  closeBtn?.addEventListener('click', toggleMenu);
  overlay?.addEventListener('click', toggleMenu);
</script>
</body>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add hamburger menu to navbar
    # Look for the Contact button anchor and wrap it
    if 'id="mobile-menu-btn"' not in content:
        pattern = r'(<a href="contact\.html">\s*<button[^>]*>Contact</button>\s*</a>)'
        replacement = r'<div class="flex items-center gap-2">\n\1\n<button id="mobile-menu-btn" class="md:hidden p-2 text-on-surface hover:text-primary transition-colors"><span class="material-symbols-outlined text-2xl">menu</span></button>\n</div>'
        content = re.sub(pattern, replacement, content)
        
    # 2. Add drawer and scripts before </body>
    if 'id="mobile-drawer"' not in content:
        content = content.replace('</body>', drawer_html)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Mobile drawer added to all HTML files successfully.")
