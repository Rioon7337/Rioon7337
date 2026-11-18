import math

# Generate 8 orbiting Quantum Pixel Blocks (Silver Wolf's pixel cubes)
cubes_svg = []
colors = ['#ff007f', '#00f0ff', '#a855f7', '#00ff88', '#ff2a85', '#00e5ff', '#ffd700', '#00ffcc']
for i in range(8):
    angle_deg = i * 45
    color = colors[i]
    delay = round(i * 0.2, 2)
    cubes_svg.append(f'''        <!-- Quantum Pixel Cube {i+1} ({angle_deg}°) -->
        <g transform="rotate({angle_deg}) translate(0, -74)">
          <!-- Pixel block with glitch animation -->
          <rect x="-3" y="-3" width="6" height="6" rx="1" fill="{color}" stroke="#ffffff" stroke-width="0.8" filter="url(#neonGlow)">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="1.2s" begin="{delay}s" repeatCount="indefinite"/>
          </rect>
          <!-- Pixel glitch shadow / echo -->
          <rect x="-1" y="-5" width="4" height="2" fill="{color}" opacity="0.6">
            <animate attributeName="opacity" values="0;0.8;0" dur="0.8s" begin="{delay + 0.1}s" repeatCount="indefinite"/>
          </rect>
        </g>''')

cubes_str = "\n".join(cubes_svg)
print("Generated 8 Quantum Pixel cubes")
