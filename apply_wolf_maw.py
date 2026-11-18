"""
Applies the Cyber Wolf Maw (Mulut Serigala Buka-Tutup) animation to assets/namecard.svg.
"""

import re
import xml.etree.ElementTree as ET

def get_wolf_maw_elements():
    # Timing breakdown for dur="3.0s":
    # 0.0s - 0.75s: Menacing slow opening (0,0 -> 0,-24 / 0,24)
    # 0.75s - 1.4s: Hold wide open, trembling with crackling lightning arcs
    # 1.4s - 1.52s: CHOMP! Instant violent bite shut (0,-24 -> 0,3 / 0,24 -> 0,-3)
    # 1.52s - 1.75s: Shockwave explosion + recoil shudder back to 0,0
    # 1.75s - 3.0s: Clamped shut, growl idle pulse
    
    times = "0; 0.25; 0.36; 0.47; 0.51; 0.58; 1"
    upper_trans = "0,0; 0,-24; 1,-25; 0,-24; 0,3; 0,0; 0,0"
    lower_trans = "0,0; 0,24; -1,25; 0,24; 0,-3; 0,0; 0,0"
    
    behind_svg = f'''  <!-- ===== CYBER WOLF MAW: BEHIND-AVATAR BASE & SHOCKWAVES ===== -->
  <g transform="translate(110, 240)">
    <!-- Base Background for Avatar Circle -->
    <circle r="60.5" fill="#040616" stroke="#00f0ff" stroke-width="1.5" opacity="0.9"/>

    <!-- 1. BITE IMPACT SHOCKWAVES (Explodes outward on bite impact at keyTime 0.51) -->
    <g>
      <!-- Shockwave 1: Neon Cyan Plasma Burst Ring -->
      <circle cx="0" cy="0" r="50" fill="none" stroke="#00f0ff" stroke-width="3.5" opacity="0" filter="url(#neonGlow)">
        <animate attributeName="r" values="50;50;50;50;90;135;50" keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0;0;0;0;0.95;0;0" keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
        <animate attributeName="stroke" values="#ffffff;#ffffff;#ffffff;#ffffff;#00f0ff;#00f0ff;#ffffff" keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
      </circle>

      <!-- Shockwave 2: Neon Magenta / Crimson Sonic Ring -->
      <circle cx="0" cy="0" r="55" fill="none" stroke="#ff0055" stroke-width="2.5" opacity="0" filter="url(#neonGlow)">
        <animate attributeName="r" values="55;55;55;55;100;145;55" keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0;0;0;0;0.85;0;0" keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
      </circle>

      <!-- Shockwave 3: Golden Electric Core Shockwave -->
      <circle cx="0" cy="0" r="45" fill="none" stroke="#ffd700" stroke-width="2" opacity="0" filter="url(#neonGlow)">
        <animate attributeName="r" values="45;45;45;45;75;110;45" keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0;0;0;0;0.9;0;0" keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
      </circle>

      <!-- Bite Impact Center Flash -->
      <circle cx="0" cy="0" r="62" fill="none" stroke="#ffffff" stroke-width="6" opacity="0">
        <animate attributeName="opacity" values="0;0;0;0;1;0;0" keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
        <animate attributeName="stroke-width" values="6;6;6;6;1;0;0" keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
      </circle>
    </g>
  </g>'''

    foreground_svg = f'''
  <!-- ===== CYBER WOLF MAW: FOREGROUND JAWS, FANGS & HINGES (CLAMPS OVER AVATAR) ===== -->
  <g transform="translate(110, 240)">

    <!-- 2. PLASMA LIGHTNING ARCS (Crackles between fangs when mouth opens wide) -->
    <g stroke="#00f0ff" stroke-width="2" fill="none" filter="url(#neonGlow)">
      <animate attributeName="opacity" values="0;0.2;0.9;0.95;0;0;0" keyTimes="0;0.18;0.30;0.47;0.51;0.7;1" dur="3.0s" repeatCount="indefinite"/>
      <!-- Left side fang arc -->
      <path d="M -44 14 L -40 0 L -50 8 L -46 -12" stroke="#00f0ff">
        <animate attributeName="d" values="
          M -44 14 L -44 14 L -46 -12 L -46 -12;
          M -44 -4 L -38 0 L -52 8 L -46 22;
          M -44 -6 L -42 2 L -50 6 L -46 22;
          M -44 14 L -44 14 L -46 -12 L -46 -12;
          M -44 14 L -44 14 L -46 -12 L -46 -12;
          M -44 14 L -44 14 L -46 -12 L -46 -12;
          M -44 14 L -44 14 L -46 -12 L -46 -12
        " keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
      </path>
      <!-- Right side fang arc -->
      <path d="M 44 14 L 40 0 L 50 8 L 46 -12" stroke="#ff0055">
        <animate attributeName="d" values="
          M 44 14 L 44 14 L 46 -12 L 46 -12;
          M 44 -4 L 38 0 L 52 8 L 46 22;
          M 44 -6 L 42 2 L 50 6 L 46 22;
          M 44 14 L 44 14 L 46 -12 L 46 -12;
          M 44 14 L 44 14 L 46 -12 L 46 -12;
          M 44 14 L 44 14 L 46 -12 L 46 -12;
          M 44 14 L 44 14 L 46 -12 L 46 -12
        " keyTimes="{times}" dur="3.0s" repeatCount="indefinite"/>
      </path>
    </g>

    <!-- 3. MECHANICAL HINGE JOINTS (Fixed at side pivots (-70, 0) and (70, 0)) -->
    <g>
      <!-- Left Jaw Pivot Hinge -->
      <g transform="translate(-70, 0)">
        <circle cx="0" cy="0" r="10" fill="#040618" stroke="#00f0ff" stroke-width="2"/>
        <circle cx="0" cy="0" r="6" fill="#0a1535" stroke="#ff0055" stroke-width="1.2">
          <animate attributeName="stroke" values="#ff0055;#00f0ff;#ff0055" dur="1.5s" repeatCount="indefinite"/>
        </circle>
        <circle cx="0" cy="0" r="2.5" fill="#ffffff">
          <animate attributeName="fill" values="#ffffff;#00f0ff;#ffffff" dur="1.5s" repeatCount="indefinite"/>
        </circle>
        <line x1="-10" y1="0" x2="-4" y2="0" stroke="#00f0ff" stroke-width="1.5"/>
        <line x1="0" y1="-10" x2="0" y2="-4" stroke="#00f0ff" stroke-width="1.5"/>
        <line x1="0" y1="4" x2="0" y2="10" stroke="#00f0ff" stroke-width="1.5"/>
      </g>

      <!-- Right Jaw Pivot Hinge -->
      <g transform="translate(70, 0)">
        <circle cx="0" cy="0" r="10" fill="#040618" stroke="#00f0ff" stroke-width="2"/>
        <circle cx="0" cy="0" r="6" fill="#0a1535" stroke="#ff0055" stroke-width="1.2">
          <animate attributeName="stroke" values="#ff0055;#00f0ff;#ff0055" dur="1.5s" repeatCount="indefinite"/>
        </circle>
        <circle cx="0" cy="0" r="2.5" fill="#ffffff">
          <animate attributeName="fill" values="#ffffff;#00f0ff;#ffffff" dur="1.5s" repeatCount="indefinite"/>
        </circle>
        <line x1="4" y1="0" x2="10" y2="0" stroke="#00f0ff" stroke-width="1.5"/>
        <line x1="0" y1="-10" x2="0" y2="-4" stroke="#00f0ff" stroke-width="1.5"/>
        <line x1="0" y1="4" x2="0" y2="10" stroke="#00f0ff" stroke-width="1.5"/>
      </g>
    </g>

    <!-- 4. RAHANG ATAS SERIGALA (UPPER CYBER WOLF JAW & MUZZLE - OPENS UPWARDS) -->
    <g>
      <animateTransform attributeName="transform" type="translate" 
        keyTimes="{times}" 
        values="{upper_trans}" 
        dur="3.0s" repeatCount="indefinite"/>

      <!-- Mechanical Wolf Ears (Telinga Serigala Gagah di Atas Kepala) -->
      <!-- Left Wolf Ear -->
      <polygon points="-36,-64 -64,-96 -24,-72" fill="#060920" stroke="#00f0ff" stroke-width="2"/>
      <polygon points="-34,-68 -56,-90 -26,-73" fill="#ff0055" opacity="0.85">
        <animate attributeName="opacity" values="0.6;1;0.6" dur="1.5s" repeatCount="indefinite"/>
      </polygon>
      <line x1="-34" y1="-68" x2="-56" y2="-90" stroke="#ffffff" stroke-width="1.2"/>

      <!-- Right Wolf Ear -->
      <polygon points="36,-64 64,-96 24,-72" fill="#060920" stroke="#00f0ff" stroke-width="2"/>
      <polygon points="34,-68 56,-90 26,-73" fill="#ff0055" opacity="0.85">
        <animate attributeName="opacity" values="0.6;1;0.6" dur="1.5s" repeatCount="indefinite"/>
      </polygon>
      <line x1="34" y1="-68" x2="56" y2="-90" stroke="#ffffff" stroke-width="1.2"/>

      <!-- Forehead Crest & Optic Sensor -->
      <polygon points="-26,-70 0,-85 26,-70 16,-62 -16,-62" fill="#080e28" stroke="#00f0ff" stroke-width="1.5"/>
      <circle cx="0" cy="-73" r="3.5" fill="#ff0055" filter="url(#neonGlow)">
        <animate attributeName="fill" values="#ff0055;#00f0ff;#ffffff;#ff0055" dur="1.5s" repeatCount="indefinite"/>
      </circle>

      <!-- Glowing Cyber Wolf Eyes (Mata Serigala yang Menyala Ganas) -->
      <!-- Left Eye Slit -->
      <polygon points="-36,-50 -20,-45 -22,-41 -38,-45" fill="#00f0ff" filter="url(#neonGlow)">
        <animate attributeName="fill" values="#00f0ff;#ff0055;#00f0ff" dur="1.5s" repeatCount="indefinite"/>
      </polygon>
      <!-- Right Eye Slit -->
      <polygon points="36,-50 20,-45 22,-41 38,-45" fill="#00f0ff" filter="url(#neonGlow)">
        <animate attributeName="fill" values="#00f0ff;#ff0055;#00f0ff" dur="1.5s" repeatCount="indefinite"/>
      </polygon>

      <!-- Cyber Wolf Nose / Snout -->
      <polygon points="-12,-38 0,-47 12,-38 6,-32 -6,-32" fill="#050a24" stroke="#00f0ff" stroke-width="1.2"/>
      <ellipse cx="-4" cy="-35" rx="2" ry="1.2" fill="#ff0055"/>
      <ellipse cx="4" cy="-35" rx="2" ry="1.2" fill="#ff0055"/>

      <!-- Upper Skull Curved Armor Arch -->
      <path d="M -68 -6 A 70 70 0 0 1 68 -6" fill="none" stroke="#00f0ff" stroke-width="3" filter="url(#neonGlow)"/>
      <path d="M -58 -18 A 62 62 0 0 1 58 -18" fill="none" stroke="#ff0055" stroke-width="1.5" stroke-dasharray="12 4 18 6"/>

      <!-- Upper Cyber Lip Plate (Snarl Contour) -->
      <path d="M -66 -4 L -60 -14 L -44 -18 L -28 -14 L 0 -16 L 28 -14 L 44 -18 L 60 -14 L 66 -4 L 58 -4 L 46 -6 L 24 -5 L 0 -6 L -24 -5 L -46 -6 L -58 -4 Z" fill="#060a22" stroke="#00f0ff" stroke-width="1.5"/>

      <!-- ===== SHARP UPPER WOLF FANGS (TARING SERIGALA ATAS) ===== -->
      <g fill="#ffffff" stroke="#00f0ff" stroke-width="1" filter="url(#neonGlow)">
        <!-- Left Big Canine (Taring Besar Kiri Atas - Tajam Menghadap Bawah) -->
        <path d="M -50 -4 Q -46 8 -42 16 Q -37 7 -36 -4 Z" fill="#ffffff">
          <animate attributeName="fill" values="#ffffff;#00f0ff;#ffffff" dur="1.5s" repeatCount="indefinite"/>
        </path>

        <!-- Left Premolar Fang -->
        <polygon points="-34,-4 -29,6 -24,-4"/>

        <!-- Upper Incisors (Gigi Seri Tengah Atas) -->
        <polygon points="-22,-5 -17,2 -12,-5"/>
        <polygon points="-10,-5 -5,1 0,-5"/>
        <polygon points="0,-5 5,1 10,-5"/>
        <polygon points="12,-5 17,2 22,-5"/>

        <!-- Right Premolar Fang -->
        <polygon points="24,-4 29,6 34,-4"/>

        <!-- Right Big Canine (Taring Besar Kanan Atas - Tajam Menghadap Bawah) -->
        <path d="M 36 -4 Q 37 7 42 16 Q 46 8 50 -4 Z" fill="#ffffff">
          <animate attributeName="fill" values="#ffffff;#00f0ff;#ffffff" dur="1.5s" repeatCount="indefinite"/>
        </path>
      </g>

      <!-- Upper Status Badge: WOLF.JAW // APEX -->
      <g transform="translate(0, -98)">
        <rect x="-38" y="-7" width="76" height="14" rx="2" fill="#040618" stroke="#00f0ff" stroke-width="1.2">
          <animate attributeName="stroke" values="#00f0ff;#ff0055;#00f0ff" dur="1.5s" repeatCount="indefinite"/>
        </rect>
        <text x="0" y="3.5" font-family="'Courier New', monospace, Arial" font-size="7.5" font-weight="900" fill="#00f0ff" text-anchor="middle" letter-spacing="1.2">
          WOLF.JAW // APEX
          <animate attributeName="fill" values="#00f0ff;#ffffff;#ff0055;#00f0ff" dur="1.5s" repeatCount="indefinite"/>
        </text>
      </g>
    </g>

    <!-- 5. RAHANG BAWAH SERIGALA (LOWER CYBER WOLF JAW & MANDIBLE - DROPS DOWNWARDS) -->
    <g>
      <animateTransform attributeName="transform" type="translate" 
        keyTimes="{times}" 
        values="{lower_trans}" 
        dur="3.0s" repeatCount="indefinite"/>

      <!-- Lower Mandible Curved Armor Arch -->
      <path d="M -68 6 A 70 70 0 0 0 68 6" fill="none" stroke="#00f0ff" stroke-width="3" filter="url(#neonGlow)"/>
      <path d="M -58 18 A 62 62 0 0 0 58 18" fill="none" stroke="#ff0055" stroke-width="1.5" stroke-dasharray="14 5 18 6"/>

      <!-- Chin Ram Armor / Mandible Guard -->
      <polygon points="-24,64 0,84 24,64 16,56 -16,56" fill="#080e28" stroke="#00f0ff" stroke-width="1.5"/>
      <line x1="-12" y1="66" x2="12" y2="66" stroke="#ff0055" stroke-width="1.5"/>
      <line x1="-8" y1="72" x2="8" y2="72" stroke="#00f0ff" stroke-width="1.5"/>

      <!-- Lower Cyber Lip Plate -->
      <path d="M -66 4 L -60 14 L -44 18 L -28 14 L 0 16 L 28 14 L 44 18 L 60 14 L 66 4 L 58 4 L 46 6 L 24 5 L 0 6 L -24 5 L -46 6 L -58 4 Z" fill="#060a22" stroke="#00f0ff" stroke-width="1.5"/>

      <!-- ===== SHARP LOWER WOLF FANGS (TARING SERIGALA BAWAH) ===== -->
      <!-- Interlocks perfectly outside the upper canines when clamped shut! -->
      <g fill="#ffffff" stroke="#ff0055" stroke-width="1" filter="url(#neonGlow)">
        <!-- Left Interlocking Canine (Taring Bawah Kiri - Menusuk ke Atas) -->
        <path d="M -58 4 Q -54 -7 -48 -16 Q -43 -6 -41 4 Z" fill="#ffffff">
          <animate attributeName="fill" values="#ffffff;#ff0055;#ffffff" dur="1.5s" repeatCount="indefinite"/>
        </path>

        <!-- Left Premolar Fang -->
        <polygon points="-39,4 -34,-4 -29,4"/>

        <!-- Lower Incisors (Gigi Seri Tengah Bawah) -->
        <polygon points="-26,5 -21,-1 -16,5"/>
        <polygon points="-14,5 -9,-1 -4,5"/>
        <polygon points="4,5 9,-1 14,5"/>
        <polygon points="16,5 21,-1 26,5"/>

        <!-- Right Premolar Fang -->
        <polygon points="29,4 34,-4 39,4"/>

        <!-- Right Interlocking Canine (Taring Bawah Kanan - Menusuk ke Atas) -->
        <path d="M 41 4 Q 43 -6 48 -16 Q 54 -7 58 4 Z" fill="#ffffff">
          <animate attributeName="fill" values="#ffffff;#ff0055;#ffffff" dur="1.5s" repeatCount="indefinite"/>
        </path>
      </g>

      <!-- Bottom Hydraulic Status Label -->
      <g transform="translate(0, 94)">
        <text x="0" y="3" font-family="'Courier New', monospace" font-size="7" font-weight="700" fill="#a0b0d0" text-anchor="middle" letter-spacing="1.5">
          [ HYDRAULIC CLAMP // 100% ]
        </text>
      </g>
    </g>
  </g>'''

    return behind_svg, foreground_svg

def main():
    with open('assets/namecard.svg', 'r', encoding='utf-8') as f:
        svg = f.read()

    # Find the old avatar border section
    start_marker = '<!-- ===== CYBER GLITCH'
    if start_marker not in svg:
        # Fallback search
        start_marker = 'translate(110, 240)'
    
    avatar_img_marker = '<!-- Avatar image -->'
    
    start_pos = svg.find(start_marker)
    img_pos = svg.find(avatar_img_marker)
    
    assert start_pos != -1, "Could not find start marker"
    assert img_pos != -1, "Could not find avatar image marker"
    
    # Also find end of avatar image tag
    img_end = svg.find('/>', img_pos) + 2
    
    behind_svg, foreground_svg = get_wolf_maw_elements()
    
    # Construct new section:
    # 1. Behind-avatar base & shockwaves
    # 2. Avatar image
    # 3. Foreground jaws, fangs, hinges, lightning
    
    avatar_image_tag = svg[img_pos:img_end]
    
    new_avatar_section = behind_svg + '\n\n  ' + avatar_image_tag + '\n' + foreground_svg
    
    # Replace from start_pos to img_end
    new_svg = svg[:start_pos] + new_avatar_section + svg[img_end:]
    
    # Verify XML
    ET.fromstring(new_svg)
    print("New SVG parsed successfully! 100% Valid XML.")
    
    with open('assets/namecard.svg', 'w', encoding='utf-8') as f:
        f.write(new_svg)
    print("Successfully updated assets/namecard.svg with Cyber Wolf Maw animation!")

if __name__ == '__main__':
    main()
