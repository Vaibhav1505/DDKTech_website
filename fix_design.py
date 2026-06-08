import os
import re

files = ['index.html', 'about.html', 'products.html', 'contact.html', 'services.html', 'portal.html', 'software.html', 'video-editing.html']

giant_text_html = '''
<!-- Giant background text -->
<div class="absolute bottom-0 left-0 w-full overflow-hidden flex items-end justify-center pointer-events-none opacity-[0.03] select-none z-0 pb-12">
    <span class="font-display-lg font-black text-[18vw] leading-none text-on-surface whitespace-nowrap tracking-tighter uppercase">DDKTECH</span>
</div>
'''

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Remove the Abstract Hero Image Placeholder in index.html
        if file == 'index.html':
            content = re.sub(r'<!-- Abstract Hero Image Placeholder -->[\s\S]*?</section>', '</section>', content)

        # 2. Add giant text to footer
        # Ensure footer has relative class
        content = content.replace('<footer class="w-full py-section-gap bg-surface-container-lowest border-t border-outline-variant/20">', '<footer class="w-full py-section-gap bg-surface-container-lowest border-t border-outline-variant/20 relative overflow-hidden">')
        
        # Insert giant text right after footer opening
        if '<!-- Giant background text -->' not in content:
            content = content.replace('<footer class="w-full py-section-gap bg-surface-container-lowest border-t border-outline-variant/20 relative overflow-hidden">', '<footer class="w-full py-section-gap bg-surface-container-lowest border-t border-outline-variant/20 relative overflow-hidden">' + giant_text_html)

        # 3. Add relative z-10 to the grid to put it above the giant text
        content = content.replace('<div class="grid grid-cols-1 md:grid-cols-4', '<div class="relative z-10 grid grid-cols-1 md:grid-cols-4')
        content = content.replace('<div class="mt-section-gap pt-8 border-t', '<div class="relative z-10 mt-section-gap pt-8 border-t')
        
        # 4. Update Privacy Policy Link
        content = content.replace('href="#">Privacy Policy</a>', 'href="privacy-policy.html">Privacy Policy</a>')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

# 5. Create privacy-policy.html
import shutil
shutil.copy('about.html', 'privacy-policy.html')

with open('privacy-policy.html', 'r', encoding='utf-8') as f:
    pp_content = f.read()

# Replace main content with privacy policy placeholder
# Find <main>...</main>
main_match = re.search(r'<main[^>]*>[\s\S]*?</main>', pp_content)
if main_match:
    new_main = '''<main class="min-h-screen pt-32 pb-section-gap px-margin-mobile">
    <div class="max-w-3xl mx-auto">
        <h1 class="font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-8">Privacy Policy</h1>
        <div class="prose prose-lg text-on-surface-variant">
            <p class="mb-4">Last updated: June 2026</p>
            <h2 class="font-headline-md mt-8 mb-4">1. Introduction</h2>
            <p class="mb-4">Welcome to DDK Technologies & Co. We respect your privacy and are committed to protecting your personal data.</p>
            <h2 class="font-headline-md mt-8 mb-4">2. Data We Collect</h2>
            <p class="mb-4">We collect and process data to provide you with the best possible service.</p>
            <h2 class="font-headline-md mt-8 mb-4">3. How We Use Your Data</h2>
            <p class="mb-4">Your information is used to improve our services, communicate with you, and ensure security.</p>
        </div>
    </div>
</main>'''
    pp_content = pp_content.replace(main_match.group(0), new_main)
    # Update title
    pp_content = re.sub(r'<title>.*?</title>', '<title>Privacy Policy | DDK Technologies</title>', pp_content)

with open('privacy-policy.html', 'w', encoding='utf-8') as f:
    f.write(pp_content)

# 6. Update vite.config.js to include privacy-policy.html
with open('vite.config.js', 'r', encoding='utf-8') as f:
    vite_cfg = f.read()

if 'privacyPolicy:' not in vite_cfg:
    vite_cfg = vite_cfg.replace('portal: resolve(__dirname, \'portal.html\'),', 'portal: resolve(__dirname, \'portal.html\'),\n                privacyPolicy: resolve(__dirname, \'privacy-policy.html\'),')
    with open('vite.config.js', 'w', encoding='utf-8') as f:
        f.write(vite_cfg)

print("Design fixes applied.")
