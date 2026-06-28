with open('src/pages/impact.astro', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if '<Layout title="Impact & Analytics - Pinpoint">' in line:
        new_lines.append('<Layout title="Analytics - Command Center">\n')
    elif 'bg-canvas border-b border-hairline' in line:
        new_lines.append(line.replace('bg-canvas border-b border-hairline', 'bg-surface-dark border-b border-hairline/10'))
    elif 'text-hero-display text-ink' in line:
        new_lines.append(line.replace('text-hero-display text-ink', 'text-[3.5rem] font-display font-medium text-white leading-none'))
    elif 'text-body text-lg mt-2' in line:
        new_lines.append(line.replace('text-body text-lg mt-2', 'text-on-dark-soft text-lg mt-4 font-light'))
    elif 'bg-surface-card px-3.5 py-1.5 rounded-pill border border-hairline' in line:
        new_lines.append(line.replace('text-ink text-xs font-bold tracking-wider uppercase mb-4 bg-surface-card px-3.5 py-1.5 rounded-pill border border-hairline', 'text-brand-pink text-xs font-bold tracking-widest uppercase mb-6 bg-brand-pink/10 px-4 py-1.5 rounded-full border border-brand-pink/30 shadow-[0_0_15px_rgba(255,107,90,0.2)]'))
    elif 'Pinpoint. Civic action, hand-crafted.' in line:
        new_lines.append('          Civic Resolution Analytics\n')
    elif 'text-lead text-body font-normal mb-8 max-w-2xl select-text leading-relaxed' in line:
        new_lines.append(line.replace('text-lead text-body font-normal mb-8 max-w-2xl select-text leading-relaxed', 'text-on-dark-soft text-xl font-light mb-12 max-w-2xl leading-relaxed'))
    elif 'bg-primary hover:bg-primary-active text-on-primary' in line:
        new_lines.append(line.replace('bg-primary hover:bg-primary-active text-on-primary font-sans text-button-utility font-semibold rounded-md px-6 py-3 cursor-pointer active-scale shadow-sm focus:outline-none transition-colors', 'bg-brand-mint text-surface-dark font-bold rounded-full px-8 py-3.5 hover:bg-white hover:shadow-[0_0_20px_rgba(164,212,197,0.6)] transition-all duration-300'))
    elif 'text-ink hover:bg-surface-card font-sans text-button-utility font-semibold border border-hairline rounded-md px-6 py-3 cursor-pointer active-scale transition-all flex items-center justify-center bg-transparent' in line:
        new_lines.append(line.replace('text-ink hover:bg-surface-card font-sans text-button-utility font-semibold border border-hairline rounded-md px-6 py-3 cursor-pointer active-scale transition-all flex items-center justify-center bg-transparent', 'text-white border border-hairline/20 rounded-full px-8 py-3.5 hover:border-brand-mint/40 hover:bg-surface-dark-elevated transition-all duration-300'))
    elif 'border-t border-hairline' in line:
        new_lines.append(line.replace('border-t border-hairline', 'border-t border-hairline/10'))
    elif 'text-display-md text-ink' in line:
        new_lines.append(line.replace('text-display-md text-ink', 'text-[4rem] text-white hover:text-brand-pink transition-colors duration-300'))
    elif 'text-caption text-muted font-medium' in line:
        new_lines.append(line.replace('text-caption text-muted font-medium', 'text-sm tracking-wider uppercase text-on-dark-soft font-semibold mt-2'))
    elif 'text-display-md text-primary' in line:
        new_lines.append(line.replace('text-display-md text-primary', 'text-[4rem] text-white hover:text-brand-mint transition-colors duration-300'))
    elif 'text-display-md text-brand-coral' in line:
        new_lines.append(line.replace('text-display-md text-brand-coral', 'text-[4rem] text-white hover:text-brand-coral transition-colors duration-300'))
    elif 'text-display-md text-success' in line:
        new_lines.append(line.replace('text-display-md text-success', 'text-[4rem] text-white hover:text-success transition-colors duration-300'))
    elif '🌱' in line:
        new_lines.append(line.replace('🌱 ', ''))
    else:
        new_lines.append(line)

with open('src/pages/impact.astro', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Fixed impact.astro')
