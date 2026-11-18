"""
Applies the rotating Magic Circle (Lingkaran Sihir Berputar) to assets/namecard.svg.
"""

import xml.etree.ElementTree as ET

def get_magic_circle_elements():
    behind_svg = '''  <!-- ===== ARCANE MAGIC SUMMONING CIRCLE // BACKGROUND MANA AURA ===== -->
  <g transform="translate(110, 240)">
    <!-- Base dark arcane backing circle -->
    <circle r="60.5" fill="#030514" stroke="#00f0ff" stroke-width="1.5" opacity="0.95"/>
    
    <!-- Outer Mana Bloom (Pulsing Arcane Light) -->
    <circle r="72" fill="none" stroke="#00f0ff" stroke-width="8" opacity="0.25" filter="url(#neonGlow)">
      <animate attributeName="stroke" values="#00f0ff;#d946ef;#00e5ff;#a855f7;#00f0ff" dur="5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.2;0.45;0.2" dur="2.5s" repeatCount="indefinite"/>
      <animate attributeName="r" values="71;74;71" dur="2.5s" repeatCount="indefinite"/>
    </circle>

    <!-- Expanding Magic Pulse Shockwave (Periodic Arcane Wave) -->
    <circle cx="0" cy="0" r="55" fill="none" stroke="#d946ef" stroke-width="2" opacity="0" filter="url(#neonGlow)">
      <animate attributeName="r" values="55;85;110;55" keyTimes="0;0.5;0.85;1" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.8;0;0" keyTimes="0;0.5;0.85;1" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="stroke" values="#d946ef;#00f0ff;#ffffff;#d946ef" keyTimes="0;0.5;0.85;1" dur="4s" repeatCount="indefinite"/>
    </circle>
  </g>'''

    foreground_svg = '''
  <!-- ===== ARCANE MAGIC SUMMONING CIRCLE // FOREGROUND ROTATING RUNES & SACRED GEOMETRY ===== -->
  <g transform="translate(110, 240)">

    <!-- 1. OUTER CARDINAL GLYPH RING (Clockwise Rotation - 18s) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="18s" repeatCount="indefinite"/>
      
      <!-- Outer Runic Boundary Circles -->
      <circle r="78" fill="none" stroke="#00f0ff" stroke-width="1.5" opacity="0.85" filter="url(#neonGlow)"/>
      <circle r="75.5" fill="none" stroke="#d946ef" stroke-width="0.8" opacity="0.75" stroke-dasharray="6 3 12 3 4 3"/>
      <circle r="73" fill="none" stroke="#00f0ff" stroke-width="0.8" opacity="0.6"/>

      <!-- 4 Primary Cardinal Seal Nodes (North, East, South, West at 0°, 90°, 180°, 270°) -->
      <!-- North (0°) -->
      <g transform="translate(0, -78)">
        <circle cx="0" cy="0" r="3" fill="#040618" stroke="#00f0ff" stroke-width="1.2"/>
        <circle cx="0" cy="0" r="1.5" fill="#ffffff"/>
        <!-- Mystic Rune Cross -->
        <line x1="-5" y1="0" x2="5" y2="0" stroke="#00f0ff" stroke-width="0.8"/>
        <line x1="0" y1="-5" x2="0" y2="5" stroke="#00f0ff" stroke-width="0.8"/>
      </g>
      <!-- East (90°) -->
      <g transform="translate(78, 0)">
        <circle cx="0" cy="0" r="3" fill="#040618" stroke="#00f0ff" stroke-width="1.2"/>
        <circle cx="0" cy="0" r="1.5" fill="#ffffff"/>
        <line x1="-5" y1="0" x2="5" y2="0" stroke="#00f0ff" stroke-width="0.8"/>
        <line x1="0" y1="-5" x2="0" y2="5" stroke="#00f0ff" stroke-width="0.8"/>
      </g>
      <!-- South (180°) -->
      <g transform="translate(0, 78)">
        <circle cx="0" cy="0" r="3" fill="#040618" stroke="#00f0ff" stroke-width="1.2"/>
        <circle cx="0" cy="0" r="1.5" fill="#ffffff"/>
        <line x1="-5" y1="0" x2="5" y2="0" stroke="#00f0ff" stroke-width="0.8"/>
        <line x1="0" y1="-5" x2="0" y2="5" stroke="#00f0ff" stroke-width="0.8"/>
      </g>
      <!-- West (270°) -->
      <g transform="translate(-78, 0)">
        <circle cx="0" cy="0" r="3" fill="#040618" stroke="#00f0ff" stroke-width="1.2"/>
        <circle cx="0" cy="0" r="1.5" fill="#ffffff"/>
        <line x1="-5" y1="0" x2="5" y2="0" stroke="#00f0ff" stroke-width="0.8"/>
        <line x1="0" y1="-5" x2="0" y2="5" stroke="#00f0ff" stroke-width="0.8"/>
      </g>

      <!-- 4 Secondary Diagonal Nodes (45°, 135°, 225°, 315°) -->
      <circle cx="55.1" cy="-55.1" r="2" fill="#d946ef" stroke="#ffffff" stroke-width="0.8"/>
      <circle cx="55.1" cy="55.1" r="2" fill="#d946ef" stroke="#ffffff" stroke-width="0.8"/>
      <circle cx="-55.1" cy="55.1" r="2" fill="#d946ef" stroke="#ffffff" stroke-width="0.8"/>
      <circle cx="-55.1" cy="-55.1" r="2" fill="#d946ef" stroke="#ffffff" stroke-width="0.8"/>

      <!-- 12 Arcane Zodiac / Astrological Tick Marks -->
      <g stroke="#00f0ff" stroke-width="1" opacity="0.7">
        <line x1="0" y1="-73" x2="0" y2="-70"/>
        <line x1="36.5" y1="-63.2" x2="35" y2="-60.6"/>
        <line x1="63.2" y1="-36.5" x2="60.6" y2="-35"/>
        <line x1="73" y1="0" x2="70" y2="0"/>
        <line x1="63.2" y1="36.5" x2="60.6" y2="35"/>
        <line x1="36.5" y1="63.2" x2="35" y2="60.6"/>
        <line x1="0" y1="73" x2="0" y2="70"/>
        <line x1="-36.5" y1="63.2" x2="-35" y2="60.6"/>
        <line x1="-63.2" y1="36.5" x2="-60.6" y2="35"/>
        <line x1="-73" y1="0" x2="-70" y2="0"/>
        <line x1="-63.2" y1="-36.5" x2="-60.6" y2="-35"/>
        <line x1="-36.5" y1="-63.2" x2="-35" y2="-60.6"/>
      </g>
    </g>

    <!-- 2. SACRED GEOMETRY OCTAGRAM (8-Pointed Magic Star - Counter-Clockwise Rotation - 12s) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="12s" repeatCount="indefinite"/>
      
      <!-- Square 1 (Aligned with axes) -->
      <rect x="-48" y="-48" width="96" height="96" fill="none" stroke="#d946ef" stroke-width="1.2" opacity="0.8" filter="url(#neonGlow)"/>
      <!-- Square 2 (Rotated 45° to form the 8-pointed star of Solomon) -->
      <rect x="-48" y="-48" width="96" height="96" transform="rotate(45)" fill="none" stroke="#00f0ff" stroke-width="1.2" opacity="0.85" filter="url(#neonGlow)"/>

      <!-- Sacred Geometric Concentric Binding Ring -->
      <circle r="68" fill="none" stroke="#ffd700" stroke-width="0.8" opacity="0.7" stroke-dasharray="8 4 16 4"/>

      <!-- 8 Small Mystic Focus Orbs at Star Vertices -->
      <circle cx="0" cy="-67.9" r="2" fill="#ffffff" stroke="#d946ef" stroke-width="0.8"/>
      <circle cx="48" cy="-48" r="2" fill="#ffffff" stroke="#00f0ff" stroke-width="0.8"/>
      <circle cx="67.9" cy="0" r="2" fill="#ffffff" stroke="#d946ef" stroke-width="0.8"/>
      <circle cx="48" cy="48" r="2" fill="#ffffff" stroke="#00f0ff" stroke-width="0.8"/>
      <circle cx="0" cy="67.9" r="2" fill="#ffffff" stroke="#d946ef" stroke-width="0.8"/>
      <circle cx="-48" cy="48" r="2" fill="#ffffff" stroke="#00f0ff" stroke-width="0.8"/>
      <circle cx="-67.9" cy="0" r="2" fill="#ffffff" stroke="#d946ef" stroke-width="0.8"/>
      <circle cx="-48" cy="-48" r="2" fill="#ffffff" stroke="#00f0ff" stroke-width="0.8"/>
    </g>

    <!-- 3. INNER ARCANE RUNIC SCRIPT RING (Fast Clockwise Rotation - 8s) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/>
      
      <!-- Inner Runic Tracks -->
      <circle r="63.5" fill="none" stroke="#00f0ff" stroke-width="1.8" opacity="0.9" filter="url(#neonGlow)"/>
      <circle r="61" fill="none" stroke="#ffffff" stroke-width="0.8" opacity="0.85" stroke-dasharray="14 6 22 8 8 6"/>

      <!-- Floating Arcane Runes & Sigil Symbols around the inner ring (8 rune marks) -->
      <g fill="#00f0ff" stroke="#ffffff" stroke-width="0.4">
        <!-- Rune 1 (0°) -->
        <polygon points="0,-63.5 -2,-61.5 0,-59.5 2,-61.5"/>
        <!-- Rune 2 (45°) -->
        <polygon points="44.9,-44.9 43.5,-43.5 44.9,-42.1 46.3,-43.5"/>
        <!-- Rune 3 (90°) -->
        <polygon points="63.5,0 61.5,-2 59.5,0 61.5,2"/>
        <!-- Rune 4 (135°) -->
        <polygon points="44.9,44.9 43.5,46.3 44.9,47.7 46.3,46.3"/>
        <!-- Rune 5 (180°) -->
        <polygon points="0,63.5 -2,65.5 0,67.5 2,65.5"/>
        <!-- Rune 6 (225°) -->
        <polygon points="-44.9,44.9 -43.5,43.5 -44.9,42.1 -46.3,43.5"/>
        <!-- Rune 7 (270°) -->
        <polygon points="-63.5,0 -61.5,-2 -59.5,0 -61.5,2"/>
        <!-- Rune 8 (315°) -->
        <polygon points="-44.9,-44.9 -43.5,-46.3 -44.9,-47.7 -46.3,-46.3"/>
      </g>
    </g>

    <!-- 4. FLOATING MANA MOTES & MAGICAL SPARK PARTICLES (Drifting & Twinkling) -->
    <g>
      <!-- Spark 1 (Top Left) -->
      <polygon points="-58,-58 -56,-62 -54,-58 -58,-58" fill="#ffd700">
        <animate attributeName="opacity" values="0.2;1;0.2" dur="1.4s" repeatCount="indefinite"/>
        <animateTransform attributeName="transform" type="translate" values="0,0; -4,-6; 0,0" dur="2.4s" repeatCount="indefinite"/>
      </polygon>
      <!-- Spark 2 (Top Right) -->
      <polygon points="58,-58 60,-62 62,-58 58,-58" fill="#00f0ff">
        <animate attributeName="opacity" values="1;0.2;1" dur="1.7s" repeatCount="indefinite"/>
        <animateTransform attributeName="transform" type="translate" values="0,0; 4,-6; 0,0" dur="2.8s" repeatCount="indefinite"/>
      </polygon>
      <!-- Spark 3 (Bottom Left) -->
      <circle cx="-65" cy="50" r="1.5" fill="#d946ef">
        <animate attributeName="opacity" values="0.3;0.9;0.3" dur="2s" repeatCount="indefinite"/>
      </circle>
      <!-- Spark 4 (Bottom Right) -->
      <circle cx="65" cy="50" r="1.5" fill="#ffffff">
        <animate attributeName="opacity" values="0.8;0.2;0.8" dur="1.6s" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- 5. TOP ARCANE CREST BADGE: [ CIRCULUS MAGICUS // ARCANE SEAL ] -->
    <g transform="translate(0, -96)">
      <rect x="-60" y="-7" width="120" height="14" rx="2" fill="#040618" stroke="#d946ef" stroke-width="1.2">
        <animate attributeName="stroke" values="#d946ef;#00f0ff;#ffd700;#d946ef" dur="3s" repeatCount="indefinite"/>
      </rect>
      <!-- Glowing Sigil Gem -->
      <circle cx="-50" cy="0" r="2.5" fill="#00f0ff">
        <animate attributeName="fill" values="#00f0ff;#ffffff;#d946ef;#00f0ff" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="5" y="3.2" font-family="'Courier New', monospace, Arial" font-size="7" font-weight="900" fill="#00f0ff" text-anchor="middle" letter-spacing="1.2">
        CIRCULUS MAGICUS // SEAL
        <animate attributeName="fill" values="#00f0ff;#ffffff;#d946ef;#00f0ff" dur="3s" repeatCount="indefinite"/>
      </text>
    </g>

    <!-- 6. BOTTOM RUNIC STATUS PILL -->
    <g transform="translate(0, 84)">
      <rect x="-54" y="-6" width="108" height="12" rx="2" fill="#040618" stroke="#00f0ff" stroke-width="1" opacity="0.9"/>
      <text x="0" y="2.5" font-family="'Segoe UI', Arial, sans-serif" font-size="6.5" font-weight="700" fill="#e0f0ff" text-anchor="middle" letter-spacing="1.5">
        ✦ ARCANE RESONANCE: 100% ✦
      </text>
    </g>

  </g>'''

    return behind_svg, foreground_svg

def main():
    with open('assets/namecard.svg', 'r', encoding='utf-8') as f:
        svg = f.read()

    start_marker = '<!-- ===== ORBITAL DRONE BITS'
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
    
    behind_svg, foreground_svg = get_magic_circle_elements()
    
    new_section = behind_svg + '\n\n  ' + avatar_image_tag + '\n' + foreground_svg + '\n\n  '
    
    new_svg = svg[:start_pos] + new_section + svg[status_pos:]
    
    # Validate XML
    ET.fromstring(new_svg)
    print("New SVG parsed successfully! 100% Valid XML.")
    
    with open('assets/namecard.svg', 'w', encoding='utf-8') as f:
        f.write(new_svg)
    print("Successfully applied rotating Magic Circle animation to assets/namecard.svg!")

if __name__ == '__main__':
    main()
