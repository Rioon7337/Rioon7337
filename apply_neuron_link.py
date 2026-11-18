import math
import re

with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Telegram handle to @Rioon7337 (with capital 'R')
text = text.replace('Telegram: @rioon7337', 'Telegram: @Rioon7337')
text = text.replace('Tg: @rioon7337', 'Tg: @Rioon7337')

# 2. Generate 12 radial synaptic threads (Neuralink micro-electrode threads)
threads_svg = []
for i in range(12):
    angle_deg = i * 30
    angle_rad = math.radians(angle_deg)
    r_in = 62.5
    r_out = 73.5
    x1 = round(r_in * math.cos(angle_rad), 2)
    y1 = round(r_in * math.sin(angle_rad), 2)
    x2 = round(r_out * math.cos(angle_rad), 2)
    y2 = round(r_out * math.sin(angle_rad), 2)
    delay = round((i * 0.15) % 1.8, 2)
    
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

# 3. Construct the Neuralink / Neuron Link border
neuron_link_border = f'''<!-- ===== NEURALINK / NEURON LINK SYNAPSE AVATAR BORDER ===== -->
  <!-- Bio-Electric Synaptic Aura / Neural Halo -->
  <g transform="translate(110, 240)">
    <circle r="75" fill="none" stroke="#00f0ff" stroke-width="14" opacity="0.25" filter="url(#nitroOuterGlow)">
      <animate attributeName="stroke" values="#00f0ff;#8b5cf6;#06b6d4;#a855f7;#00f0ff" dur="3.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.2;0.45;0.2" dur="2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Neural Network Circuit & Synaptic Firing Rings -->
  <g transform="translate(110, 240)" filter="url(#nitroGlow)">
    <!-- 12 Radial Synaptic Threads (Neuralink Micro-electrode Threads) -->
    <g id="neuralThreads">
{threads_str}
    </g>

    <!-- Outer Neural Axon Ring (Continuous synaptic circuit pathway) -->
    <circle r="73.5" fill="none" stroke="#8b5cf6" stroke-width="0.8" opacity="0.4"/>
    
    <!-- Fast Synaptic Action Potential Pulses (Electric White & Cyan Firing Clockwise) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="2.2s" repeatCount="indefinite"/>
      <circle r="73.5" fill="none" stroke="#00f0ff" stroke-width="2.5" stroke-dasharray="24 52" stroke-linecap="round" opacity="0.95"/>
      <circle r="73.5" fill="none" stroke="#ffffff" stroke-width="2" stroke-dasharray="10 80" stroke-linecap="round" opacity="1"/>
    </g>

    <!-- Middle Neural Pathway (Counter-traveling Bio-electric Pulses in Cyan & Violet) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="3s" repeatCount="indefinite"/>
      <circle r="67.5" fill="none" stroke="#06b6d4" stroke-width="2" stroke-dasharray="35 35" stroke-linecap="round" opacity="0.85"/>
      <circle r="67.5" fill="none" stroke="#a855f7" stroke-width="1.8" stroke-dasharray="18 52" stroke-linecap="round" opacity="0.75"/>
    </g>

    <!-- High-speed Synaptic Firing Sparks (Clockwise burst) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="1.4s" repeatCount="indefinite"/>
      <circle cx="0" cy="-67.5" r="2.8" fill="#ffffff" filter="url(#neonGlow)"/>
      <circle cx="67.5" cy="0" r="2.4" fill="#00ffcc" filter="url(#neonGlow)"/>
      <circle cx="0" cy="67.5" r="2.8" fill="#ffffff" filter="url(#neonGlow)"/>
      <circle cx="-67.5" cy="0" r="2.4" fill="#00e5ff" filter="url(#neonGlow)"/>
    </g>

    <!-- Inner Bio-Chip Neural Interface Frame Ring -->
    <circle r="62.5" fill="none" stroke="#00f0ff" stroke-width="2.2" opacity="0.9"/>
    <circle r="61.5" fill="#05051a" stroke="#8b5cf6" stroke-width="1" opacity="0.8"/>
  </g>

  '''

# Replace whatever avatar border exists between the outer glow start and '<image'
start_idx = text.find('<!-- ===== ')
# Find the start of avatar border comment
start_idx = text.find('<!-- ===== CYBERNETIC SCI-FI REACTOR AVATAR BORDER ===== -->')
if start_idx == -1:
    start_idx = text.find('<!-- ===== NITRO BORDER')

end_idx = text.find('<!-- Avatar image -->')

if start_idx == -1 or end_idx == -1:
    raise ValueError(f"Could not locate avatar border markers! start: {start_idx}, end: {end_idx}")

text = text[:start_idx] + neuron_link_border + text[end_idx:]

with open(r'd:\Rioon7337\assets\namecard.svg', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS! Applied Neuron Link border and updated Telegram handle.")
