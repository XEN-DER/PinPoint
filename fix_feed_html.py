with open('src/components/GlobalScripts.astro', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'class="font-bold text-lg mb-1.5 line-clamp-1 group-hover:text-primary transition-colors"',
    'class="font-display font-medium text-xl text-white mb-2 line-clamp-1 group-hover:text-brand-mint transition-colors"'
).replace(
    'class="text-sm opacity-90 leading-snug mb-4 line-clamp-2"',
    'class="text-sm text-on-dark-soft font-light leading-relaxed mb-5 line-clamp-2"'
).replace(
    'class="font-semibold text-[13px] opacity-80 flex items-center gap-1.5 truncate"',
    'class="font-light text-sm text-on-dark-soft flex items-center gap-2 truncate"'
).replace(
    'class="text-[12px] font-mono tracking-tighter opacity-60 flex items-center gap-1"',
    'class="text-[12px] font-mono tracking-widest text-on-dark-soft/50 flex items-center gap-1 uppercase"'
).replace(
    'px-2.5 py-0.5 rounded text-[11px] font-bold tracking-wide flex items-center gap-1',
    'px-3 py-1 rounded-full text-[10px] font-bold tracking-widest uppercase flex items-center gap-1.5'
)

with open('src/components/GlobalScripts.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated html generation')
