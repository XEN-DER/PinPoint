with open('src/pages/feed.astro', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if '<Layout title="Active Issues - Pinpoint">' in line:
        new_lines.append('<Layout title="Active Issues - Command Center">\n')
    elif 'bg-surface-card border-b border-hairline' in line:
        new_lines.append(line.replace('bg-surface-card border-b border-hairline', 'bg-surface-dark border-b border-hairline/10'))
    elif 'text-hero-display text-ink' in line:
        new_lines.append(line.replace('text-hero-display text-ink', 'text-[3.5rem] font-display font-medium text-white leading-none'))
    elif 'text-body text-lg mt-2' in line:
        new_lines.append(line.replace('text-body text-lg mt-2', 'text-on-dark-soft text-lg mt-4 font-light'))
    elif 'text-caption-uppercase text-muted' in line:
        new_lines.append(line.replace('text-caption-uppercase text-muted', 'text-xs text-brand-mint tracking-[2px] uppercase'))
    elif 'text-display-lg text-ink font-semibold' in line:
        new_lines.append(line.replace('text-display-lg text-ink font-semibold', 'text-[2.5rem] text-white font-medium'))
    elif 'text-body-md text-muted' in line:
        new_lines.append(line.replace('text-body-md text-muted', 'text-on-dark-soft text-lg font-light'))
    elif 'bg-canvas border border-hairline p-5 rounded-md' in line:
        new_lines.append(line.replace('bg-canvas border border-hairline p-5 rounded-md', 'bg-surface-dark-elevated/40 backdrop-blur-md border border-hairline/10 p-5 rounded-2xl shadow-xl'))
    elif 'bg-canvas border border-hairline rounded-pill' in line:
        new_lines.append(line.replace('bg-canvas border border-hairline', 'bg-surface-dark border-hairline/20 text-white').replace('placeholder-muted', 'placeholder-on-dark-soft/50'))
    elif 'text-caption text-ink font-semibold' in line:
        new_lines.append(line.replace('text-caption text-ink font-semibold', 'text-sm text-white font-medium bg-surface-dark'))
    elif 'bg-canvas border border-hairline p-12' in line:
        new_lines.append(line.replace('bg-canvas border border-hairline p-12', 'bg-surface-dark-elevated/20 border border-hairline/10 p-12'))
    elif 'text-body-strong text-ink' in line:
        new_lines.append(line.replace('text-body-strong text-ink', 'text-xl text-white font-medium'))
    else:
        new_lines.append(line)

with open('src/pages/feed.astro', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Fixed feed.astro')
