import re

with open('src/components/GlobalScripts.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the logic in enderFeed that assigns colors
start_idx = content.find('let cardBgClass = \'bg-surface-card text-ink border-hairline\';')
end_idx = content.find('const hasUpvoted = upvoted.includes(issue.id);')

new_logic = '''
      let cardBgClass = 'bg-surface-dark-elevated/40 backdrop-blur-md border border-hairline/10 hover:border-brand-mint/40 transition-colors duration-300 group shadow-xl relative overflow-hidden';
      let textLight = true;
      
      let severityBadgeColor = 'text-brand-coral bg-brand-coral/10 border-brand-coral/20';
      let statusBadgeColor = 'text-brand-ochre bg-brand-ochre/10 border-brand-ochre/20 border';

      if (issue.disputed) {
        statusBadgeColor = 'bg-brand-pink/10 text-brand-pink border-brand-pink/30 border animate-pulse';
      } else if (issue.status === 'Resolved') {
        statusBadgeColor = 'bg-brand-mint/10 text-brand-mint border-brand-mint/30 border';
      }

      let disputeBtnClass = 'bg-brand-pink/10 hover:bg-brand-pink/20 text-brand-pink border border-brand-pink/30 transition-colors';

'''

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_logic + content[end_idx:]

# Also update upvote and verify buttons
content = content.replace(
'''      if (textLight) {
        // Over dark teal card
        upvoteBtnClass = hasUpvoted 
          ? 'bg-canvas/30 text-on-dark border border-canvas/25' 
          : 'bg-canvas text-ink hover:bg-surface-card';
        verifyBtnClass = 'bg-canvas/20 hover:bg-canvas/30 text-on-dark border border-canvas/25';
        resolveBtnClass = 'bg-canvas text-ink hover:bg-surface-card';
      } else {
        // Over peach, lavender, ochre, or cream card
        upvoteBtnClass = hasUpvoted 
          ? 'bg-primary text-on-primary hover:bg-primary-active' 
          : 'bg-canvas text-ink hover:bg-surface-card border border-hairline';
        verifyBtnClass = 'bg-canvas hover:bg-surface-card text-ink border border-hairline';
        resolveBtnClass = 'bg-primary text-on-primary hover:bg-primary-active';
      }''',
'''      // Dark glassmorphic buttons
      upvoteBtnClass = hasUpvoted 
        ? 'bg-brand-mint/20 text-brand-mint border-brand-mint/30 shadow-[0_0_10px_rgba(164,212,197,0.2)]' 
        : 'bg-surface-dark text-white hover:bg-surface-dark-elevated border border-hairline/20 hover:border-brand-mint/30 transition-colors';
      verifyBtnClass = 'bg-surface-dark text-white hover:bg-surface-dark-elevated border border-hairline/20 hover:border-brand-mint/30 transition-colors';
      resolveBtnClass = 'bg-brand-mint/10 text-brand-mint hover:bg-brand-mint/20 border border-brand-mint/30 transition-colors';
''')

# Update card template rendering
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

print('Updated feed cards rendering in GlobalScripts.astro')
