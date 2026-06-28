with open('src/components/GlobalScripts.astro', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '''      const highlightClass = c.isUser ? 'bg-brand-mint border-primary/20' : 'bg-canvas border-hairline';''',
    '''      const highlightClass = c.isUser ? 'bg-surface-dark-elevated border-brand-mint/40 shadow-[0_0_15px_rgba(164,212,197,0.2)]' : 'bg-surface-dark/50 border-hairline/10 hover:border-brand-ochre/30';'''
).replace(
    '''<div class="flex items-center justify-between p-3.5 rounded-md transition-colors border ">''',
    '''<div class="flex items-center justify-between p-4 rounded-2xl transition-all duration-300 border ">'''
).replace(
    '''<span class="w-6 text-center text-sm font-bold font-sans"></span>''',
    '''<span class="w-8 text-center text-lg font-bold font-display text-brand-ochre"></span>'''
).replace(
    '''<div class="text-caption font-bold text-ink"></div>''',
    '''<div class="text-sm font-medium text-white"></div>'''
).replace(
    '''<div class="text-[11px] text-muted font-medium"></div>''',
    '''<div class="text-[11px] text-on-dark-soft font-light tracking-wider"></div>'''
).replace(
    '''<div class="text-right font-sans text-sm font-bold text-ink">''',
    '''<div class="text-right font-display text-lg font-bold text-white">'''
).replace(
    '''<span class="text-[10px] text-muted font-normal">pts</span>''',
    '''<span class="text-[10px] text-brand-ochre font-mono tracking-widest uppercase ml-1">pts</span>'''
)

with open('src/components/GlobalScripts.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated renderLeaderboard')
