import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patches as mpatches

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Color scheme - minimal and clean
color1 = '#4A90E2'  # Blue
color2 = '#F5A623'  # Orange
color3 = '#7ED321'  # Green

# Simple boxes with minimal text

# 1. Knowledge
box1 = FancyBboxPatch((1, 5.5), 1.8, 1.2,
                      boxstyle="round,pad=0.1",
                      edgecolor=color1, linewidth=3,
                      facecolor='white')
ax.add_patch(box1)
ax.text(1.9, 6.3, 'Knowledge', fontsize=16, weight='bold', ha='center', color=color1)
ax.text(1.9, 5.9, '(Tri thức)', fontsize=11, ha='center', style='italic', color='gray')

# 2. Knowledge Base
box2 = FancyBboxPatch((3.5, 5.5), 1.8, 1.2,
                      boxstyle="round,pad=0.1",
                      edgecolor=color1, linewidth=3,
                      facecolor='white')
ax.add_patch(box2)
ax.text(4.4, 6.3, 'KB', fontsize=16, weight='bold', ha='center', color=color1)
ax.text(4.4, 5.9, '(Cơ sở tri thức)', fontsize=11, ha='center', style='italic', color='gray')

# 3. Logic (above)
box3 = FancyBboxPatch((5.1, 3.5), 1.8, 1.2,
                      boxstyle="round,pad=0.1",
                      edgecolor=color2, linewidth=3,
                      facecolor='white')
ax.add_patch(box3)
ax.text(6, 4.3, 'Logic', fontsize=16, weight='bold', ha='center', color=color2)
ax.text(6, 3.9, '(Luật)', fontsize=11, ha='center', style='italic', color='gray')

# 4. Inference (center - larger)
circle = Circle((7.5, 6.1), 0.9,
                facecolor='white',
                edgecolor=color2, linewidth=4)
ax.add_patch(circle)
ax.text(7.5, 6.3, 'Inference', fontsize=14, weight='bold', ha='center', color=color2)
ax.text(7.5, 5.9, '(Suy diễn)', fontsize=10, ha='center', style='italic', color='gray')

# 5. Action
box5 = FancyBboxPatch((9.2, 5.5), 1.8, 1.2,
                      boxstyle="round,pad=0.1",
                      edgecolor=color3, linewidth=3,
                      facecolor='white')
ax.add_patch(box5)
ax.text(10.1, 6.3, 'Action', fontsize=16, weight='bold', ha='center', color=color3)
ax.text(10.1, 5.9, '(Hành động)', fontsize=11, ha='center', style='italic', color='gray')

# Arrows showing the flow

# Knowledge → KB
arrow1 = FancyArrowPatch((2.9, 6.1), (3.4, 6.1),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=3, color=color1)
ax.add_patch(arrow1)

# KB → Inference
arrow2 = FancyArrowPatch((5.4, 6.1), (6.5, 6.1),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=3, color=color1)
ax.add_patch(arrow2)

# Logic → Inference (from below)
arrow3 = FancyArrowPatch((6.5, 4.8), (7.2, 5.3),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=3, color=color2,
                        connectionstyle="arc3,rad=0.2")
ax.add_patch(arrow3)

# Inference → Action
arrow4 = FancyArrowPatch((8.5, 6.1), (9.1, 6.1),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=3, color=color3)
ax.add_patch(arrow4)

# Add simple process numbers
numbers = [
    (1.9, 7.0, '1'),
    (4.4, 7.0, '2'),
    (6.0, 5.0, '3'),
    (7.5, 7.3, '4'),
    (10.1, 7.0, '5'),
]

for x, y, num in numbers:
    ax.text(x, y, num, fontsize=14, weight='bold', ha='center', va='center',
            bbox=dict(boxstyle='circle,pad=0.3', facecolor='white', 
                     edgecolor='black', linewidth=2))

# Minimal bottom text
ax.text(6, 2.2, 'Inference Process', 
        fontsize=18, weight='bold', ha='center', color='#333')
ax.text(6, 1.7, 'Knowledge → Representation → Reasoning → Action', 
        fontsize=13, ha='center', style='italic', color='#666')

plt.tight_layout()
plt.savefig('/Users/nguyennghia/PROJECT/Intro_to_AI/idea/Prositional logic/simple_figure.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
print("Simple figure saved as 'simple_figure.png'")
plt.show()


