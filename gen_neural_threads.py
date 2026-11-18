import math

# Generate 12 radial neural threads (like Neuralink electrode threads)
threads_svg = []
for i in range(12):
    angle_deg = i * 30
    angle_rad = math.radians(angle_deg)
    # Inner point at r=62, outer point at r=73
    r_in = 62.5
    r_out = 73.5
    x1 = round(r_in * math.cos(angle_rad), 2)
    y1 = round(r_in * math.sin(angle_rad), 2)
    x2 = round(r_out * math.cos(angle_rad), 2)
    y2 = round(r_out * math.sin(angle_rad), 2)
    delay = round((i * 0.15) % 1.8, 2)
    
    # Thread line and firing synaptic node
    threads_svg.append(f'''      <!-- Synaptic Thread {i+1} ({angle_deg}°) -->
      <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#00f0ff" stroke-width="1" opacity="0.5">
        <animate attributeName="opacity" values="0.3;0.9;0.3" dur="1.8s" begin="{delay}s" repeatCount="indefinite"/>
        <animate attributeName="stroke" values="#00f0ff;#8b5cf6;#00f0ff" dur="2.4s" begin="{delay}s" repeatCount="indefinite"/>
      </line>
      <circle cx="{x2}" cy="{y2}" r="1.8" fill="#00ffcc">
        <animate attributeName="r" values="1.2;2.8;1.2" dur="1.8s" begin="{delay}s" repeatCount="indefinite"/>
        <animate attributeName="fill" values="#00ffcc;#ffffff;#8b5cf6;#00ffcc" dur="1.8s" begin="{delay}s" repeatCount="indefinite"/>
      </circle>''')

threads_str = "\n".join(threads_svg)
print("Generated", len(threads_svg), "threads")
