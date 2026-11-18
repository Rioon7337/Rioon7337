import os

# Read base64 data
with open(r'd:\Rioon7337\avatar_base64.txt', 'r') as f:
    avatar_b64 = f.read().strip()
with open(r'd:\Rioon7337\banner_base64.txt', 'r') as f:
    banner_b64 = f.read().strip()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="800" height="400">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050520"/>
      <stop offset="50%" stop-color="#0a1535"/>
      <stop offset="100%" stop-color="#0d2050"/>
    </linearGradient>

    <linearGradient id="bottomBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080828" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#0a1838" stop-opacity="0.98"/>
    </linearGradient>

    <linearGradient id="nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="50%" stop-color="#93c5fd"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>

    <linearGradient id="badgeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e40af"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>

    <linearGradient id="accentLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#60a5fa" stop-opacity="1"/>
      <stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
    </linearGradient>

    <filter id="cardGlow" x="-5%" y="-5%" width="110%" height="110%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="textGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="avatarShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000" flood-opacity="0.5"/>
    </filter>

    <clipPath id="avatarClip">
      <circle cx="110" cy="240" r="55"/>
    </clipPath>

    <clipPath id="bannerClip">
      <rect x="10" y="10" width="780" height="190" rx="14" ry="14"/>
    </clipPath>

    <clipPath id="cardClip">
      <rect x="5" y="5" width="790" height="390" rx="18" ry="18"/>
    </clipPath>
  </defs>

  <!-- Main card background -->
  <rect x="5" y="5" width="790" height="390" rx="18" ry="18" fill="url(#bgGrad)" stroke="#1a3a6a" stroke-width="2" filter="url(#cardGlow)"/>

  <!-- Banner -->
  <g clip-path="url(#bannerClip)">
    <rect x="10" y="10" width="780" height="190" fill="#0a0a1a"/>
    <image href="data:image/gif;base64,{banner_b64}" x="10" y="10" width="780" height="190" preserveAspectRatio="xMidYMid slice"/>
    <!-- Banner bottom fade -->
    <rect x="10" y="160" width="780" height="40" fill="url(#bottomBg)"/>
  </g>

  <!-- Bottom section -->
  <rect x="10" y="200" width="780" height="190" rx="0" ry="0" fill="url(#bottomBg)" clip-path="url(#cardClip)"/>

  <!-- Accent line separator -->
  <rect x="50" y="200" width="700" height="1" fill="url(#accentLine)"/>

  <!-- Avatar ring glow -->
  <circle cx="110" cy="240" r="60" fill="none" stroke="#3b82f6" stroke-width="2" opacity="0.3" filter="url(#neonGlow)"/>

  <!-- Avatar border -->
  <circle cx="110" cy="240" r="57" fill="#0d1a3e" stroke="#3b82f6" stroke-width="2.5"/>

  <!-- Avatar image -->
  <g clip-path="url(#avatarClip)" filter="url(#avatarShadow)">
    <image href="data:image/jpeg;base64,{avatar_b64}" x="55" y="185" width="110" height="110" preserveAspectRatio="xMidYMid slice"/>
  </g>

  <!-- Username -->
  <text x="185" y="235" font-family="Segoe UI, Arial, sans-serif" font-size="28" font-weight="bold" fill="url(#nameGrad)" filter="url(#textGlow)">Rioon</text>

  <!-- Tagline -->
  <text x="185" y="260" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#94a3b8">Just a Normal Furry</text>

  <!-- Decorative badges -->
  <g transform="translate(185, 275)">
    <rect x="0" y="0" width="70" height="24" rx="12" fill="url(#badgeGrad)" opacity="0.8"/>
    <text x="35" y="16" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#dbeafe" text-anchor="middle">&#x1F43E; Furry</text>

    <rect x="80" y="0" width="75" height="24" rx="12" fill="url(#badgeGrad)" opacity="0.8"/>
    <text x="117" y="16" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#dbeafe" text-anchor="middle">&#x1F4BB; Coder</text>
  </g>

  <!-- Twinkling stars -->
  <circle cx="700" cy="230" r="1.5" fill="#60a5fa" opacity="0.6">
    <animate attributeName="opacity" values="0.3;0.8;0.3" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="720" cy="250" r="1" fill="#93c5fd" opacity="0.4">
    <animate attributeName="opacity" values="0.2;0.7;0.2" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="740" cy="235" r="1.5" fill="#3b82f6" opacity="0.5">
    <animate attributeName="opacity" values="0.4;0.9;0.4" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="680" cy="260" r="1" fill="#60a5fa" opacity="0.3">
    <animate attributeName="opacity" values="0.2;0.6;0.2" dur="3.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="760" cy="270" r="1.5" fill="#93c5fd" opacity="0.5">
    <animate attributeName="opacity" values="0.3;0.8;0.3" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="660" cy="280" r="1" fill="#3b82f6" opacity="0.4">
    <animate attributeName="opacity" values="0.2;0.7;0.2" dur="4.5s" repeatCount="indefinite"/>
  </circle>

  <!-- Bottom line -->
  <rect x="100" y="370" width="600" height="0.5" fill="url(#accentLine)" opacity="0.3"/>

  <!-- Watermark -->
  <text x="750" y="385" font-family="Segoe UI, Arial, sans-serif" font-size="9" fill="#1e3a5f" text-anchor="end" opacity="0.5">github.com/Rioon</text>
</svg>'''

# Create directory
os.makedirs(r'd:\Rioon7337\Rioon\assets', exist_ok=True)

# Write SVG
with open(r'd:\Rioon7337\Rioon\assets\namecard.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

# Write README
readme = '''<p align="center">
  <img src="https://raw.githubusercontent.com/Rioon/Rioon/main/assets/namecard.svg"/>
</p>
'''
with open(r'd:\Rioon7337\Rioon\README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

svg_size = os.path.getsize(r'd:\Rioon7337\Rioon\assets\namecard.svg')
print(f'Done! SVG size: {svg_size} bytes ({svg_size/1024/1024:.1f} MB)')
