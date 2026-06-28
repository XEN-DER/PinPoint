with open('src/pages/leaderboard.astro', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if '<Layout title="Leaderboard - Pinpoint">' in line:
        new_lines.append('<Layout title="Top Citizens - Command Center">\n')
    elif 'bg-canvas border-b border-hairline' in line:
        new_lines.append(line.replace('bg-canvas border-b border-hairline', 'bg-surface-dark border-b border-hairline/10'))
    elif 'text-hero-display text-ink' in line:
        new_lines.append(line.replace('text-hero-display text-ink', 'text-[3.5rem] font-display font-medium text-white leading-none'))
    elif 'text-body text-lg mt-2' in line:
        new_lines.append(line.replace('text-body text-lg mt-2', 'text-on-dark-soft text-lg mt-4 font-light'))
    elif 'text-caption-uppercase tracking-[1.5px] font-bold mb-3 block' in line:
        new_lines.append(line.replace('text-primary text-caption-uppercase tracking-[1.5px] font-bold mb-3 block', 'text-brand-ochre text-xs tracking-widest uppercase font-bold mb-4 block'))
    elif 'text-display-md text-ink font-semibold' in line:
        new_lines.append(line.replace('text-display-md text-ink font-semibold', 'text-[2.5rem] text-white font-medium'))
    elif 'text-body-md text-muted' in line:
        new_lines.append(line.replace('text-body-md text-muted', 'text-on-dark-soft text-lg font-light'))
    elif 'bg-surface-pearl border border-hairline p-6 rounded-lg' in line:
        new_lines.append(line.replace('bg-surface-pearl border border-hairline p-6 rounded-lg', 'bg-surface-dark-elevated/40 backdrop-blur-md border border-hairline/10 p-8 rounded-3xl shadow-xl'))
    elif 'bg-primary text-white' in line:
        new_lines.append(line.replace('bg-primary text-white', 'bg-brand-ochre text-surface-dark shadow-[0_0_15px_rgba(232,185,74,0.4)]'))
    elif 'text-body-strong text-ink' in line:
        new_lines.append(line.replace('text-body-strong text-ink', 'text-xl text-white font-medium'))
    elif 'text-muted font-medium' in line:
        new_lines.append(line.replace('text-muted font-medium', 'text-on-dark-soft font-light'))
    elif 'text-lead text-primary font-bold font-sans' in line:
        new_lines.append(line.replace('text-lead text-primary font-bold font-sans', 'text-3xl text-brand-ochre font-bold font-display'))
    elif 'text-[10px] uppercase tracking-wider text-muted font-mono font-bold' in line:
        new_lines.append(line.replace('text-[10px] uppercase tracking-wider text-muted font-mono font-bold', 'text-[10px] uppercase tracking-widest text-on-dark-soft font-mono font-bold mt-1'))
    elif 'text-xs text-ink mb-1.5' in line:
        new_lines.append(line.replace('text-xs text-ink mb-1.5', 'text-sm text-white mb-2'))
    elif 'bg-surface-card rounded-full' in line:
        new_lines.append(line.replace('bg-surface-card rounded-full overflow-hidden border border-divider-soft', 'bg-surface-dark rounded-full overflow-hidden border border-hairline/10 shadow-inner'))
    elif 'bg-primary rounded-full transition-all duration-300' in line:
        new_lines.append(line.replace('bg-primary rounded-full', 'bg-gradient-to-r from-brand-ochre/50 to-brand-ochre rounded-full relative shadow-[0_0_10px_rgba(232,185,74,0.5)]'))
    elif 'text-xs font-bold text-muted uppercase tracking-wider mb-3' in line:
        new_lines.append(line.replace('text-xs font-bold text-muted uppercase tracking-wider mb-3', 'text-xs font-bold text-on-dark-soft uppercase tracking-widest mb-4'))
    elif 'bg-canvas border border-hairline px-3 py-1.5 rounded-md' in line:
        new_lines.append(line.replace('bg-canvas border border-hairline px-3 py-1.5 rounded-md', 'bg-surface-dark border border-hairline/10 px-3 py-2 rounded-lg text-white'))
    elif 'text-ink' in line and 'font-bold' in line:
        new_lines.append(line.replace('text-ink', 'text-white'))
    elif 'bg-canvas/30 border border-hairline border-dashed px-3 py-1.5 rounded-md' in line:
        new_lines.append(line.replace('bg-canvas/30 border border-hairline border-dashed px-3 py-1.5 rounded-md text-xs opacity-50 select-none', 'bg-surface-dark/50 border border-hairline/10 border-dashed px-3 py-2 rounded-lg text-xs opacity-50 select-none text-white'))
    elif 'bg-surface-pearl border border-hairline p-8 rounded-lg' in line:
        new_lines.append(line.replace('bg-surface-pearl border border-hairline p-8 rounded-lg', 'bg-surface-dark-elevated/40 backdrop-blur-md border border-hairline/10 p-8 rounded-3xl shadow-xl'))
    elif 'text-caption-uppercase text-ink font-bold mb-6 tracking-wider' in line:
        new_lines.append(line.replace('text-caption-uppercase text-ink font-bold mb-6 tracking-wider', 'text-brand-mint text-xs tracking-widest uppercase font-bold mb-6'))
    elif 'border-t border-hairline pt-4 text-xs text-muted' in line:
        new_lines.append(line.replace('border-t border-hairline pt-4 text-xs text-muted', 'border-t border-hairline/10 pt-6 text-sm text-on-dark-soft'))
    elif 'text-primary font-bold cursor-pointer hover:underline' in line:
        new_lines.append(line.replace('text-primary', 'text-brand-mint').replace('font-bold', 'font-medium'))
    elif '🕳� ' in line or '🔦' in line or '💧' in line:
        new_lines.append(line.replace('🕳� ', '🛡� ').replace('🔦', '⚡').replace('💧', '🌊'))
    else:
        new_lines.append(line)

with open('src/pages/leaderboard.astro', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Fixed leaderboard.astro')
