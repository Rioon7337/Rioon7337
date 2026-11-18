import math

# Dottore's signature orbiting surgical scalpel / acoustic resonance needles
# Let's create 6 floating mechanical needles orbiting at r=73
needles_svg = []
for i in range(6):
    angle_deg = i * 60
    angle_rad = math.radians(angle_deg)
    # Each needle points inwards/tangentially
    needles_svg.append(f'''        <!-- Dottore Floating Blade / Syringe Drone {i+1} ({angle_deg}°) -->
        <g transform="rotate({angle_deg}) translate(0, -73)">
          <!-- Sharp mechanical scalpel / needle -->
          <polygon points="0,-10 3.5,2 0,6 -3.5,2" fill="#0c1829" stroke="#00f0ff" stroke-width="1.2" filter="url(#neonGlow)">
            <animate attributeName="stroke" values="#00f0ff;#a855f7;#00ffcc;#00f0ff" dur="3s" begin="{i*0.5}s" repeatCount="indefinite"/>
          </polygon>
          <!-- Glowing energy core in the needle -->
          <circle cx="0" cy="0" r="1.5" fill="#ffffff" filter="url(#neonGlow)"/>
          <!-- Cryo energy spike tip -->
          <line x1="0" y1="-10" x2="0" y2="-14" stroke="#00f0ff" stroke-width="1.5" stroke-linecap="round">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" begin="{i*0.3}s" repeatCount="indefinite"/>
          </line>
        </g>''')

needles_str = "\n".join(needles_svg)
print("Generated 6 Dottore floating blades")
