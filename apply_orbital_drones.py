"""
Applies the Orbital Drone Bits (Satellite Defense Array) avatar border animation to assets/namecard.svg.
"""

import xml.etree.ElementTree as ET

def get_orbital_drone_elements():
    times = "0; 0.27; 0.54; 0.8; 1"
    
    # Drone A (Alpha - Top):
    alpha_trans = "0,-78; -8,-82; 8,-84; 4,-76; 0,-78"
    
    # Drone B (Beta - Bottom-Left):
    beta_trans = "-70,42; -75,36; -66,48; -68,40; -70,42"
    
    # Drone C (Gamma - Bottom-Right):
    gamma_trans = "72,36; 66,44; 76,40; 70,34; 72,36"
    
    # Triangulation Polygon Points:
    tri_points = (
        "0,-78 -70,42 72,36; "
        "-8,-82 -75,36 66,44; "
        "8,-84 -66,48 76,40; "
        "4,-76 -68,40 70,34; "
        "0,-78 -70,42 72,36"
    )

    behind_svg = f'''  <!-- ===== ORBITAL DRONE BITS // BACKGROUND & FORCEFIELD BASE ===== -->
  <g transform="translate(110, 240)">
    <!-- Base dark shield backing -->
    <circle r="60.5" fill="#040618" stroke="#00f0ff" stroke-width="1.5" opacity="0.9"/>

    <!-- Telemetry Range Rings (Subtle tactical HUD arcs) -->
    <circle r="64" fill="none" stroke="#00f0ff" stroke-width="1" opacity="0.4" stroke-dasharray="14 12 28 10"/>
    <circle r="66.5" fill="none" stroke="#ff0055" stroke-width="0.8" opacity="0.35" stroke-dasharray="6 20 40 15"/>

    <!-- Periodic Defense Shockwave Pulse (Expands from center outwards at t=0.54) -->
    <circle cx="0" cy="0" r="50" fill="none" stroke="#00f0ff" stroke-width="2.5" opacity="0" filter="url(#neonGlow)">
      <animate attributeName="r" values="50;50;85;115;50" keyTimes="{times}" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0;0.85;0;0" keyTimes="{times}" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="stroke" values="#00f0ff;#ffffff;#ff0055;#00f0ff;#00f0ff" keyTimes="{times}" dur="4.5s" repeatCount="indefinite"/>
    </circle>
  </g>'''

    foreground_svg = f'''
  <!-- ===== ORBITAL DRONE BITS // FOREGROUND LASER MATRIX & DRONES ===== -->
  <g transform="translate(110, 240)">

    <!-- Corner Crosshair Targeting Ticks around Avatar -->
    <g stroke="#00f0ff" stroke-width="1.5" opacity="0.75">
      <line x1="-54" y1="-54" x2="-46" y2="-54"/>
      <line x1="-54" y1="-54" x2="-54" y2="-46"/>
      <line x1="54" y1="-54" x2="46" y2="-54"/>
      <line x1="54" y1="-54" x2="54" y2="-46"/>
      <line x1="-54" y1="54" x2="-46" y2="54"/>
      <line x1="-54" y1="54" x2="-54" y2="46"/>
      <line x1="54" y1="54" x2="46" y2="54"/>
      <line x1="54" y1="54" x2="54" y2="46"/>
    </g>

    <!-- 1. TRIANGULATION LASER GRID & FORCEFIELD BARRIER (Connecting Drone Alpha, Beta & Gamma) -->
    <!-- Faint Holographic Forcefield Polygon Fill -->
    <polygon points="0,-78 -70,42 72,36" fill="#00f0ff" opacity="0.08" filter="url(#neonGlow)">
      <animate attributeName="points" values="{tri_points}" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.08;0.14;0.06;0.12;0.08" dur="2.2s" repeatCount="indefinite"/>
    </polygon>

    <!-- Primary Neon Cyan Laser Beam Triangulation Lines -->
    <polygon points="0,-78 -70,42 72,36" fill="none" stroke="#00f0ff" stroke-width="1.8" filter="url(#neonGlow)">
      <animate attributeName="points" values="{tri_points}" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="stroke" values="#00f0ff;#00ffff;#80f0ff;#00f0ff" dur="3s" repeatCount="indefinite"/>
    </polygon>

    <!-- Secondary Pulsing Neon Magenta Laser Particle Stream -->
    <polygon points="0,-78 -70,42 72,36" fill="none" stroke="#ff0055" stroke-width="1.2" stroke-dasharray="16 10 24 8" stroke-linecap="round">
      <animate attributeName="points" values="{tri_points}" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="stroke-dashoffset" from="0" to="180" dur="2.4s" repeatCount="indefinite"/>
    </polygon>

    <!-- Core Razor-White Triangulation Laser Filament -->
    <polygon points="0,-78 -70,42 72,36" fill="none" stroke="#ffffff" stroke-width="0.8" opacity="0.9" stroke-dasharray="30 20 15 25">
      <animate attributeName="points" values="{tri_points}" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="stroke-dashoffset" from="180" to="0" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;1;0.5;0.9;0.7" dur="1.5s" repeatCount="indefinite"/>
    </polygon>

    <!-- 2. DRONE BIT ALPHA (Top Center Drone // Recon & Uplink) -->
    <g>
      <animateTransform attributeName="transform" type="translate" values="{alpha_trans}" dur="4.5s" repeatCount="indefinite"/>
      
      <!-- Plasma Jet Exhaust Flame (Pointing upwards/backward) -->
      <polygon points="-3,-5 0,-15 3,-5" fill="#00f0ff" opacity="0.85" filter="url(#neonGlow)">
        <animate attributeName="points" values="-3,-5 0,-13 3,-5; -3,-5 0,-18 3,-5; -3,-5 0,-12 3,-5" dur="0.25s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.7;1;0.6;0.9" dur="0.25s" repeatCount="indefinite"/>
      </polygon>
      <polygon points="-1.5,-5 0,-10 1.5,-5" fill="#ffffff"/>

      <!-- Twin Stabilizer Winglets -->
      <polygon points="-5,-2 -13,-6 -7,4" fill="#0a1535" stroke="#00f0ff" stroke-width="1"/>
      <polygon points="5,-2 13,-6 7,4" fill="#0a1535" stroke="#00f0ff" stroke-width="1"/>
      
      <!-- Main Drone Chassis Body (Angular Mecha Fuselage) -->
      <polygon points="-7,-4 0,-9 7,-4 5,6 -5,6" fill="#060c26" stroke="#00f0ff" stroke-width="1.4"/>
      <polygon points="-4,-2 0,-6 4,-2 3,4 -3,4" fill="#0d1b45"/>

      <!-- Glowing Core Optic Sensor Lens -->
      <circle cx="0" cy="0" r="2.5" fill="#ff0055" filter="url(#neonGlow)">
        <animate attributeName="fill" values="#ff0055;#00f0ff;#ffffff;#ff0055" dur="1.8s" repeatCount="indefinite"/>
      </circle>

      <!-- Tactical Micro Reticle Brackets -->
      <g stroke="#00f0ff" stroke-width="0.8" fill="none" opacity="0.75">
        <path d="M -10 -9 L -14 -9 L -14 7 L -10 7"/>
        <path d="M 10 -9 L 14 -9 L 14 7 L 10 7"/>
      </g>

      <!-- Drone ID Tag -->
      <text x="0" y="14" font-family="'Courier New', monospace" font-size="5.5" font-weight="900" fill="#00f0ff" text-anchor="middle" letter-spacing="0.8">
        BIT-A1
      </text>
    </g>

    <!-- 3. DRONE BIT BETA (Bottom-Left Drone // Kinetic Deflector) -->
    <g>
      <animateTransform attributeName="transform" type="translate" values="{beta_trans}" dur="4.5s" repeatCount="indefinite"/>

      <!-- Plasma Jet Exhaust Flame (Angled back-left) -->
      <polygon points="-5,1 -14,6 -2,5" fill="#00f0ff" opacity="0.85" filter="url(#neonGlow)">
        <animate attributeName="points" values="-5,1 -12,5 -2,5; -5,1 -17,8 -2,5; -5,1 -13,6 -2,5" dur="0.22s" repeatCount="indefinite"/>
      </polygon>
      <polygon points="-4,2 -9,4 -2,4" fill="#ffffff"/>

      <!-- Twin Stabilizer Winglets -->
      <polygon points="-2,-5 -6,-13 4,-7" fill="#0a1535" stroke="#00f0ff" stroke-width="1"/>
      <polygon points="-2,5 -6,13 4,7" fill="#0a1535" stroke="#00f0ff" stroke-width="1"/>

      <!-- Main Drone Chassis Body -->
      <polygon points="-4,-7 -9,0 -4,7 6,5 6,-5" fill="#060c26" stroke="#00f0ff" stroke-width="1.4"/>
      <polygon points="-2,-4 -6,0 -2,4 4,3 4,-3" fill="#0d1b45"/>

      <!-- Glowing Core Optic Sensor Lens -->
      <circle cx="0" cy="0" r="2.5" fill="#00f0ff" filter="url(#neonGlow)">
        <animate attributeName="fill" values="#00f0ff;#ffffff;#ff0055;#00f0ff" dur="1.8s" repeatCount="indefinite"/>
      </circle>

      <!-- Tactical Micro Reticle Brackets -->
      <g stroke="#00f0ff" stroke-width="0.8" fill="none" opacity="0.75">
        <path d="M -9 -10 L -9 -14 L 7 -14 L 7 -10"/>
        <path d="M -9 10 L -9 14 L 7 14 L 7 10"/>
      </g>

      <!-- Drone ID Tag -->
      <text x="-14" y="2" font-family="'Courier New', monospace" font-size="5.5" font-weight="900" fill="#00f0ff" text-anchor="middle" letter-spacing="0.8">
        BIT-B2
      </text>
    </g>

    <!-- 4. DRONE BIT GAMMA (Bottom-Right Drone // Laser Interceptor) -->
    <g>
      <animateTransform attributeName="transform" type="translate" values="{gamma_trans}" dur="4.5s" repeatCount="indefinite"/>

      <!-- Plasma Jet Exhaust Flame (Angled back-right) -->
      <polygon points="5,1 14,6 2,5" fill="#ff0055" opacity="0.85" filter="url(#neonGlow)">
        <animate attributeName="points" values="5,1 12,5 2,5; 5,1 17,8 2,5; 5,1 13,6 2,5" dur="0.24s" repeatCount="indefinite"/>
      </polygon>
      <polygon points="4,2 9,4 2,4" fill="#ffffff"/>

      <!-- Twin Stabilizer Winglets -->
      <polygon points="2,-5 6,-13 -4,-7" fill="#0a1535" stroke="#ff0055" stroke-width="1"/>
      <polygon points="2,5 6,13 -4,7" fill="#0a1535" stroke="#ff0055" stroke-width="1"/>

      <!-- Main Drone Chassis Body -->
      <polygon points="4,-7 9,0 4,7 -6,5 -6,-5" fill="#060c26" stroke="#ff0055" stroke-width="1.4"/>
      <polygon points="2,-4 6,0 2,4 -4,3 -4,-3" fill="#0d1b45"/>

      <!-- Glowing Core Optic Sensor Lens -->
      <circle cx="0" cy="0" r="2.5" fill="#ff0055" filter="url(#neonGlow)">
        <animate attributeName="fill" values="#ff0055;#00f0ff;#ffffff;#ff0055" dur="1.8s" repeatCount="indefinite"/>
      </circle>

      <!-- Tactical Micro Reticle Brackets -->
      <g stroke="#ff0055" stroke-width="0.8" fill="none" opacity="0.75">
        <path d="M 9 -10 L 9 -14 L -7 -14 L -7 -10"/>
        <path d="M 9 10 L 9 14 L -7 14 L -7 10"/>
      </g>

      <!-- Drone ID Tag -->
      <text x="14" y="2" font-family="'Courier New', monospace" font-size="5.5" font-weight="900" fill="#ff0055" text-anchor="middle" letter-spacing="0.8">
        BIT-C3
      </text>
    </g>

    <!-- 5. TOP STATUS HUD BADGE: [ ORBITAL BITS // DEFENSE ARRAY ] -->
    <g transform="translate(0, -96)">
      <rect x="-56" y="-7" width="112" height="14" rx="2" fill="#040618" stroke="#00f0ff" stroke-width="1.2">
        <animate attributeName="stroke" values="#00f0ff;#ff0055;#00f0ff" dur="2.4s" repeatCount="indefinite"/>
      </rect>
      <!-- Status Green/Cyan Blip -->
      <circle cx="-47" cy="0" r="2.5" fill="#00ff88">
        <animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/>
      </circle>
      <text x="3" y="3.2" font-family="'Courier New', monospace, Arial" font-size="7" font-weight="900" fill="#00f0ff" text-anchor="middle" letter-spacing="1">
        ORBITAL BITS // DEFENSE
        <animate attributeName="fill" values="#00f0ff;#ffffff;#ff73fa;#00f0ff" dur="2.4s" repeatCount="indefinite"/>
      </text>
    </g>

    <!-- 6. BOTTOM TELEMETRY STATUS PILL -->
    <g transform="translate(0, 84)">
      <rect x="-52" y="-6" width="104" height="12" rx="2" fill="#040618" stroke="#00f0ff" stroke-width="1" opacity="0.9"/>
      <text x="0" y="2.5" font-family="'Segoe UI', Arial, sans-serif" font-size="6.5" font-weight="700" fill="#a0f0ff" text-anchor="middle" letter-spacing="1.2">
        [ TRIANGULATION: 100% ONLINE ]
      </text>
    </g>

  </g>'''

    return behind_svg, foreground_svg

def main():
    with open('assets/namecard.svg', 'r', encoding='utf-8') as f:
        svg = f.read()

    start_marker = '<!-- ===== HONKAI: STAR RAIL'
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
    
    behind_svg, foreground_svg = get_orbital_drone_elements()
    
    new_section = behind_svg + '\n\n  ' + avatar_image_tag + '\n' + foreground_svg + '\n\n  '
    
    new_svg = svg[:start_pos] + new_section + svg[status_pos:]
    
    # Validate XML
    ET.fromstring(new_svg)
    print("New SVG parsed successfully! 100% Valid XML.")
    
    with open('assets/namecard.svg', 'w', encoding='utf-8') as f:
        f.write(new_svg)
    print("Successfully applied Orbital Drone Bits animation to assets/namecard.svg!")

if __name__ == '__main__':
    main()
