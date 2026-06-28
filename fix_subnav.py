with open('src/components/SubNav.astro', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if '<nav class="bg-surface-soft border-b border-hairline' in line:
        new_lines.append('<nav class="bg-surface-dark-elevated/60 backdrop-blur-md border-b border-hairline/10 h-[52px] flex items-center justify-between px-6 sticky top-0 z-40 select-none overflow-x-auto hide-scrollbar shadow-md">\n')
    elif 'text-body-strong hover:bg-surface-chip-translucent' in line:
        new_lines.append(line.replace('text-body-strong', 'text-on-dark-soft').replace('hover:bg-surface-chip-translucent', 'hover:bg-white/5').replace('hover:text-ink', 'hover:text-white'))
    elif 'text-primary' in line:
        new_lines.append(line.replace('text-primary', 'text-brand-mint'))
    elif 'bg-ink text-canvas' in line:
        new_lines.append(line.replace('bg-ink text-canvas', 'bg-brand-mint text-surface-dark font-bold hover:bg-brand-mint/90'))
    elif 'border-hairline text-ink' in line:
        new_lines.append(line.replace('border-hairline text-ink', 'border-hairline/20 text-white bg-surface-dark-elevated hover:bg-white/5 hover:border-brand-mint/30'))
    else:
        new_lines.append(line)

with open('src/components/SubNav.astro', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Fixed SubNav.astro')
