with open('src/components/Modals.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace light mode classes with dark mode equivalents
content = content.replace('bg-canvas', 'bg-surface-dark-elevated backdrop-blur-xl')
content = content.replace('text-ink', 'text-white')
content = content.replace('border-hairline', 'border-hairline/20')
content = content.replace('text-muted', 'text-on-dark-soft')
content = content.replace('bg-surface-card', 'bg-surface-dark/50')
content = content.replace('text-primary', 'text-brand-mint')
content = content.replace('bg-primary/10', 'bg-brand-mint/10')
content = content.replace('bg-primary hover:bg-primary-active text-on-primary', 'bg-brand-mint text-surface-dark hover:bg-white hover:shadow-[0_0_15px_rgba(164,212,197,0.5)]')
content = content.replace('text-body-strong', 'font-medium')
content = content.replace('text-caption-strong', 'text-sm font-medium')
content = content.replace('text-tagline', 'text-2xl')
content = content.replace('focus:border-primary', 'focus:border-brand-mint')
content = content.replace('focus:ring-primary', 'focus:ring-brand-mint')

with open('src/components/Modals.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Modals')
