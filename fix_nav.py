with open('src/components/GlobalNav.astro', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<nav class=' in line:
        new_lines.append('<nav class="bg-surface-dark-elevated/80 backdrop-blur-xl border-b border-hairline/10 text-on-dark h-16 flex items-center justify-between px-6 select-none relative z-50 text-nav-link shadow-lg">\n')
    elif 'id="nav-logo"' in line:
        new_lines.append('    <a href="/" class="flex items-center gap-2.5 hover:opacity-80 active-scale" id="nav-logo">\n')
    elif 'text-ink font-display' in line:
        new_lines.append(line.replace('text-ink', 'text-white'))
    elif '<!-- Theme Toggle Button -->' in line:
        skip = True
    elif skip and '</button>' in line:
        skip = False
    elif not skip:
        # replace other light text classes
        line = line.replace('text-primary-active', 'text-brand-mint')
        line = line.replace('dark:bg-brand-mint/15', 'bg-brand-mint/15')
        line = line.replace('dark:text-brand-mint', '')
        line = line.replace('hover:text-primary', 'hover:text-brand-mint')
        new_lines.append(line)

with open('src/components/GlobalNav.astro', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Fixed GlobalNav.astro')
