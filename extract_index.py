import sys

with open('temp_index_copy.txt', 'r', encoding='utf-16') as f:
    lines = f.readlines()

# We want the imports and the Hero section.
# Hero section ends right before <section id="analytics-section">

out = []
for line in lines:
    if '<section id="analytics-section"' in line:
        break
    out.append(line)

# Add our new dynamic dashboard grid linking to the new pages
dashboard_html = """
  <section class="max-w-6xl mx-auto px-6 py-12">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 animate-slide-up-fade stagger-2">
      <a href="/feed" class="bg-surface-card hover:bg-surface-strong border border-hairline rounded-lg p-6 flex flex-col gap-3 transition-transform active-scale group cursor-pointer block">
        <div class="w-12 h-12 bg-primary text-on-primary rounded-full flex items-center justify-center text-xl shadow-sm group-hover:scale-110 transition-transform">??</div>
        <h3 class="text-lead font-bold text-ink">Active Issues</h3>
        <p class="text-caption text-muted">Browse, verify, and resolve issues reported in your neighborhood.</p>
      </a>
      
      <a href="/hotspots" class="bg-surface-card hover:bg-surface-strong border border-hairline rounded-lg p-6 flex flex-col gap-3 transition-transform active-scale group cursor-pointer block">
        <div class="w-12 h-12 bg-primary text-on-primary rounded-full flex items-center justify-center text-xl shadow-sm group-hover:scale-110 transition-transform">???</div>
        <h3 class="text-lead font-bold text-ink">Hotspots Map</h3>
        <p class="text-caption text-muted">Visualize problem areas and neighborhood clusters in real-time.</p>
      </a>

      <a href="/impact" class="bg-surface-card hover:bg-surface-strong border border-hairline rounded-lg p-6 flex flex-col gap-3 transition-transform active-scale group cursor-pointer block">
        <div class="w-12 h-12 bg-primary text-on-primary rounded-full flex items-center justify-center text-xl shadow-sm group-hover:scale-110 transition-transform">??</div>
        <h3 class="text-lead font-bold text-ink">Impact Analytics</h3>
        <p class="text-caption text-muted">See the real-time difference we are making in the community.</p>
      </a>

      <a href="/leaderboard" class="bg-surface-card hover:bg-surface-strong border border-hairline rounded-lg p-6 flex flex-col gap-3 transition-transform active-scale group cursor-pointer block">
        <div class="w-12 h-12 bg-primary text-on-primary rounded-full flex items-center justify-center text-xl shadow-sm group-hover:scale-110 transition-transform">??</div>
        <h3 class="text-lead font-bold text-ink">Leaderboard</h3>
        <p class="text-caption text-muted">Earn points and rank up by reporting and verifying issues.</p>
      </a>
    </div>
  </section>
"""
out.append(dashboard_html)
out.append('</Layout>\n')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.writelines(out)

print("Rebuilt index.astro")
