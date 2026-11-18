"""
Applies the Honkai: Star Rail Voracity Corrosion animation to assets/namecard.svg.
"""

import xml.etree.ElementTree as ET

def get_voracity_elements():
    silhouette_d = "M -18.5 -33 L -21.5 -29 L -22.8 -22 L -23 -15 L -23.5 -5 L -24 5 L -23 14 L -16 21 L -6.5 26 L -7 31 L -20 35 L -32 42 L -44 52 L -48 58 L 0 60 L 48 58 L 44 52 L 32 42 L 20 35 L 7 31 L 6.5 26 L 16 21 L 23 14 L 24 5 L 23.5 -5 L 23 -15 L 22.8 -22 L 21.5 -29 L 18.5 -33 L 13 -25 L 7 -19 L 0 -16 L -7 -19 L -13 -25 Z"
    
    behind_svg = f'''  <!-- ===== HONKAI: STAR RAIL - VORACITY CORROSION (KOROSI VORACITY) BACKGROUND ===== -->
  <g transform="translate(110, 240)">
    <!-- Abyssal Base Circle -->
    <circle r="60.5" fill="#080004" stroke="#ff0033" stroke-width="1.5" opacity="0.9"/>

    <!-- 1. EXPANDING VORACITY CORROSION PULSES (Expanding outwards and dissolving) -->
    <g>
      <!-- Pulse 1: Blood Crimson Devour Wave -->
      <path d="{silhouette_d}" fill="none" stroke="#ff0033" stroke-width="3" opacity="0.85">
        <animateTransform attributeName="transform" type="scale" values="1; 1.15; 1.3" dur="2.2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.85; 0.35; 0" dur="2.2s" repeatCount="indefinite"/>
        <animate attributeName="stroke-width" values="3; 1.5; 0.5" dur="2.2s" repeatCount="indefinite"/>
      </path>

      <!-- Pulse 2: Burning Amber Corrosion Wave (Offset phase) -->
      <path d="{silhouette_d}" fill="none" stroke="#ff7700" stroke-width="2.5" opacity="0.85">
        <animateTransform attributeName="transform" type="scale" values="1; 1.15; 1.3" begin="1.1s" dur="2.2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.85; 0.35; 0" begin="1.1s" dur="2.2s" repeatCount="indefinite"/>
        <animate attributeName="stroke-width" values="2.5; 1.2; 0.5" begin="1.1s" dur="2.2s" repeatCount="indefinite"/>
      </path>
    </g>

    <!-- Deep Void Atmospheric Glow -->
    <circle r="58" fill="#ff0033" opacity="0.08" filter="url(#neonGlow)">
      <animate attributeName="opacity" values="0.06;0.18;0.06" dur="2.0s" repeatCount="indefinite"/>
    </circle>
  </g>'''

    foreground_svg = f'''
  <!-- ===== HONKAI: STAR RAIL - VORACITY CORROSION FOREGROUND (HUGS AVATAR SILHOUETTE) ===== -->
  <g transform="translate(110, 240)">

    <!-- 2. DEEP CORROSIVE AURA (Glow tightly following the furry wolf silhouette) -->
    <path d="{silhouette_d}" fill="none" stroke="#ff0033" stroke-width="8" opacity="0.4" filter="url(#neonGlow)">
      <animate attributeName="stroke" values="#ff0033;#ff4400;#990022;#ff0033" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="stroke-width" values="7;11;6;12;7" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.35;0.65;0.3;0.6;0.35" dur="2.4s" repeatCount="indefinite"/>
    </path>

    <!-- Secondary Hot Amber Bloom -->
    <path d="{silhouette_d}" fill="none" stroke="#ff5500" stroke-width="5" opacity="0.45" filter="url(#nitroGlow)">
      <animate attributeName="stroke" values="#ff5500;#ff0044;#ffaa00;#ff5500" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="stroke-width" values="4;8;3;7;4" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.4;0.75;0.35;0.7;0.4" dur="1.8s" repeatCount="indefinite"/>
    </path>

    <!-- 3. CRAWLING CORROSIVE ENERGY STREAMS (Slithers along the silhouette outline) -->
    <!-- Primary Crimson Stream (Clockwise flow) -->
    <path d="{silhouette_d}" fill="none" stroke="#ff0044" stroke-width="3" stroke-dasharray="24 10 36 8 16 12" stroke-linecap="round" filter="url(#neonGlow)">
      <animate attributeName="stroke-dashoffset" from="0" to="260" dur="2.6s" repeatCount="indefinite"/>
      <animate attributeName="stroke" values="#ff0044;#ff0000;#ff2200;#ff0044" dur="2.6s" repeatCount="indefinite"/>
    </path>

    <!-- Counter Hot Amber Stream (Counter-clockwise flow) -->
    <path d="{silhouette_d}" fill="none" stroke="#ffbb00" stroke-width="2" stroke-dasharray="18 14 28 10" stroke-linecap="round">
      <animate attributeName="stroke-dashoffset" from="240" to="0" dur="1.9s" repeatCount="indefinite"/>
      <animate attributeName="stroke" values="#ffbb00;#ffffff;#ff5500;#ffbb00" dur="1.9s" repeatCount="indefinite"/>
    </path>

    <!-- Razor Core Filament (White-hot sharp edge) -->
    <path d="{silhouette_d}" fill="none" stroke="#ffffff" stroke-width="1.2" opacity="0.9" stroke-dasharray="40 25 15 20">
      <animate attributeName="stroke-dashoffset" from="0" to="200" dur="3.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;1;0.5;0.95;0.7" dur="1.2s" repeatCount="indefinite"/>
    </path>

    <!-- 4. VORACITY CORROSION BARBED TEETH & THORNS (Sprouting from silhouette contour) -->
    <g fill="#ff0033" stroke="#ffffff" stroke-width="0.8" filter="url(#neonGlow)">
      <!-- Left Ear Outer Thorn -->
      <polygon points="-18.5,-33 -27,-40 -21.5,-29">
        <animate attributeName="fill" values="#ff0033;#ff6600;#ffffff;#ff0033" dur="1.5s" repeatCount="indefinite"/>
      </polygon>
      <!-- Left Ear Mid Thorn -->
      <polygon points="-22.8,-22 -30,-25 -23,-15"/>

      <!-- Right Ear Outer Thorn -->
      <polygon points="18.5,-33 27,-40 21.5,-29">
        <animate attributeName="fill" values="#ff0033;#ff6600;#ffffff;#ff0033" dur="1.5s" repeatCount="indefinite"/>
      </polygon>
      <!-- Right Ear Mid Thorn -->
      <polygon points="22.8,-22 30,-25 23,-15"/>

      <!-- Forehead Crown Horn / Spire -->
      <polygon points="-4,-17 0,-25 4,-17" fill="#ff7700">
        <animate attributeName="fill" values="#ff7700;#ffffff;#ff0044;#ff7700" dur="1.2s" repeatCount="indefinite"/>
      </polygon>

      <!-- Left Cheek Fluff Thorns -->
      <polygon points="-24,5 -33,7 -23,14">
        <animate attributeName="fill" values="#ff0033;#ffffff;#ff5500;#ff0033" dur="1.4s" repeatCount="indefinite"/>
      </polygon>
      <polygon points="-23.5,-5 -31,-6 -24,2"/>

      <!-- Right Cheek Fluff Thorns -->
      <polygon points="24,5 33,7 23,14">
        <animate attributeName="fill" values="#ff0033;#ffffff;#ff5500;#ff0033" dur="1.4s" repeatCount="indefinite"/>
      </polygon>
      <polygon points="23.5,-5 31,-6 24,2"/>

      <!-- Neck Constriction Barbs -->
      <polygon points="-6.5,26 -13,28 -7,31"/>
      <polygon points="6.5,26 13,28 7,31"/>

      <!-- Left Shoulder Corrosive Blades -->
      <polygon points="-32,42 -43,45 -44,52">
        <animate attributeName="fill" values="#ff0033;#ff5500;#ffffff;#ff0033" dur="1.6s" repeatCount="indefinite"/>
      </polygon>
      <polygon points="-20,35 -28,37 -32,42"/>

      <!-- Right Shoulder Corrosive Blades -->
      <polygon points="32,42 43,45 44,52">
        <animate attributeName="fill" values="#ff0033;#ff5500;#ffffff;#ff0033" dur="1.6s" repeatCount="indefinite"/>
      </polygon>
      <polygon points="20,35 28,37 32,42"/>
    </g>

    <!-- 5. FLOATING CORROSIVE EMBERS / ABYSSAL CINDER PARTICLES -->
    <g fill="#ff3300">
      <!-- Particle 1: Left Ear Cinder (Drifts upward) -->
      <rect x="-24" y="-36" width="3" height="3" rx="0.5">
        <animate attributeName="y" values="-36;-48;-36" dur="1.8s" repeatCount="indefinite"/>
        <animate attributeName="x" values="-24;-28;-24" dur="1.8s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.9;0.2;0.9" dur="1.8s" repeatCount="indefinite"/>
        <animate attributeName="fill" values="#ff3300;#ffbb00;#ff0033" dur="1.8s" repeatCount="indefinite"/>
      </rect>

      <!-- Particle 2: Right Ear Cinder -->
      <rect x="22" y="-36" width="3" height="3" rx="0.5">
        <animate attributeName="y" values="-36;-48;-36" dur="2.1s" repeatCount="indefinite"/>
        <animate attributeName="x" values="22;26;22" dur="2.1s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.9;0.2;0.9" dur="2.1s" repeatCount="indefinite"/>
        <animate attributeName="fill" values="#ffbb00;#ff3300;#ffffff" dur="2.1s" repeatCount="indefinite"/>
      </rect>

      <!-- Particle 3: Left Cheek Ember -->
      <rect x="-30" y="2" width="2.5" height="2.5" rx="0.5">
        <animate attributeName="y" values="2;-12;2" dur="2.4s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0;0.9;0" dur="2.4s" repeatCount="indefinite"/>
      </rect>

      <!-- Particle 4: Right Cheek Ember -->
      <rect x="28" y="2" width="2.5" height="2.5" rx="0.5">
        <animate attributeName="y" values="2;-12;2" dur="2.2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0;0.9;0" dur="2.2s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- 6. OUTER CORROSION ENERGY BOUNDARY (Enclosing perimeter) -->
    <circle r="63.5" fill="none" stroke="#ff0033" stroke-width="2" opacity="0.65" stroke-dasharray="14 6 26 8">
      <animate attributeName="stroke" values="#ff0033;#99001a;#ff5500;#ff0033" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="stroke-dashoffset" from="0" to="120" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle r="60.5" fill="none" stroke="#ff6600" stroke-width="1.2" opacity="0.8"/>

    <!-- 7. HONKAI: STAR RAIL VORACITY CORROSION UI BADGE (Top Header: [ IV VORACITY CORROSION ]) -->
    <g transform="translate(0, -78)">
      <rect x="-52" y="-7" width="104" height="14" rx="2" fill="#0c0005" stroke="#ff0033" stroke-width="1.2">
        <animate attributeName="stroke" values="#ff0033;#ff6600;#ff0033" dur="1.6s" repeatCount="indefinite"/>
      </rect>
      <!-- Level Indicator Box (Level IV) -->
      <rect x="-50" y="-5" width="18" height="10" rx="1" fill="#ff0033">
        <animate attributeName="fill" values="#ff0033;#ff4400;#ff0033" dur="1.6s" repeatCount="indefinite"/>
      </rect>
      <text x="-41" y="2.5" font-family="'Segoe UI', Arial, sans-serif" font-size="7" font-weight="900" fill="#ffffff" text-anchor="middle">
        IV
      </text>
      <!-- Label -->
      <text x="12" y="3" font-family="'Courier New', monospace, Arial" font-size="7" font-weight="900" fill="#ff4400" text-anchor="middle" letter-spacing="1">
        VORACITY CORROSION
        <animate attributeName="fill" values="#ff4400;#ffffff;#ff0033;#ff4400" dur="1.6s" repeatCount="indefinite"/>
      </text>
    </g>

    <!-- Bottom Status Pill: [ MAX HP SUPPRESSED ] -->
    <g transform="translate(0, 78)">
      <rect x="-46" y="-6" width="92" height="12" rx="2" fill="#0c0005" stroke="#ff5500" stroke-width="1" opacity="0.85"/>
      <text x="0" y="2.5" font-family="'Segoe UI', Arial, sans-serif" font-size="6.5" font-weight="700" fill="#ffaa00" text-anchor="middle" letter-spacing="1">
        [ MAX HP SUPPRESSED ]
      </text>
    </g>

  </g>'''

    return behind_svg, foreground_svg

def main():
    with open('assets/namecard.svg', 'r', encoding='utf-8') as f:
        svg = f.read()

    start_marker = '<!-- ===== CYBER WOLF MAW'
    if start_marker not in svg:
        start_marker = 'translate(110, 240)'
    
    avatar_img_marker = '<!-- Avatar image -->'
    status_indicator_marker = '<!-- Status indicator -->'
    
    start_pos = svg.find(start_marker)
    img_pos = svg.find(avatar_img_marker)
    status_pos = svg.find(status_indicator_marker)
    
    assert start_pos != -1, "Could not find start marker"
    assert img_pos != -1, "Could not find avatar image marker"
    assert status_pos != -1, "Could not find status indicator marker"
    
    img_end = svg.find('/>', img_pos) + 2
    avatar_image_tag = svg[img_pos:img_end]
    
    behind_svg, foreground_svg = get_voracity_elements()
    
    # Layering:
    # 1. Behind avatar base & shockwaves
    # 2. Avatar image
    # 3. Foreground silhouette-following corrosive streams, thorns, embers, and UI badges
    
    new_section = behind_svg + '\n\n  ' + avatar_image_tag + '\n' + foreground_svg + '\n\n  '
    
    new_svg = svg[:start_pos] + new_section + svg[status_pos:]
    
    # Validate XML
    ET.fromstring(new_svg)
    print("New SVG parsed successfully! 100% Valid XML.")
    
    with open('assets/namecard.svg', 'w', encoding='utf-8') as f:
        f.write(new_svg)
    print("Successfully applied Honkai: Star Rail Voracity Corrosion animation to assets/namecard.svg!")

if __name__ == '__main__':
    main()
