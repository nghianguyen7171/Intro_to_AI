import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Create figure with white background
fig, ax = plt.subplots(1, 1, figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')

# Color scheme - professional and clean
color_main = '#1E88E5'  # Blue
color_secondary = '#FFA726'  # Orange
color_action = '#66BB6A'  # Green
color_text = '#263238'  # Dark gray

# Title
title_box = Rectangle((0, 8.2), 14, 0.7, facecolor=color_main, edgecolor='none')
ax.add_patch(title_box)
ax.text(7, 8.55, 'Inference (Reasoning) in Artificial Intelligence', 
        fontsize=24, weight='bold', ha='center', va='center', color='white')

# Main definition box
def_box = FancyBboxPatch((1, 6.8), 12, 1.0,
                         boxstyle="round,pad=0.15",
                         edgecolor=color_secondary, linewidth=3,
                         facecolor='#FFF9E6', alpha=0.9)
ax.add_patch(def_box)
ax.text(7, 7.5, 'Inference: Process of generating new correct statements', 
        fontsize=15, weight='bold', ha='center', color=color_text)
ax.text(7, 7.1, 'from previously existing correct statements/knowledge to make appropriate actions', 
        fontsize=13, ha='center', style='italic', color=color_text)

# Four main components in a flow

# 1. Knowledge
box1 = FancyBboxPatch((0.5, 4.2), 2.8, 1.8,
                      boxstyle="round,pad=0.15",
                      edgecolor=color_main, linewidth=3,
                      facecolor='#E3F2FD')
ax.add_patch(box1)
ax.text(1.9, 5.7, 'Knowledge', fontsize=16, weight='bold', ha='center', color=color_main)
ax.text(1.9, 5.3, '(Tri thức)', fontsize=12, ha='center', style='italic', color=color_text)
ax.text(1.9, 4.8, 'Information & knowledge', fontsize=10, ha='center')
ax.text(1.9, 4.5, 'about a certain field', fontsize=10, ha='center')

# 2. Knowledge Base (KB)
box2 = FancyBboxPatch((4.1, 4.2), 2.8, 1.8,
                      boxstyle="round,pad=0.15",
                      edgecolor=color_main, linewidth=3,
                      facecolor='#E3F2FD')
ax.add_patch(box2)
ax.text(5.5, 5.7, 'Knowledge Base', fontsize=16, weight='bold', ha='center', color=color_main)
ax.text(5.5, 5.3, '(Cơ sở tri thức)', fontsize=12, ha='center', style='italic', color=color_text)
ax.text(5.5, 4.8, 'Represented in specific', fontsize=10, ha='center')
ax.text(5.5, 4.5, 'form (language)', fontsize=10, ha='center')

# 3. Logic
box3 = FancyBboxPatch((7.7, 4.2), 2.8, 1.8,
                      boxstyle="round,pad=0.15",
                      edgecolor=color_secondary, linewidth=3,
                      facecolor='#FFF3E0')
ax.add_patch(box3)
ax.text(9.1, 5.7, 'Logic', fontsize=16, weight='bold', ha='center', color=color_secondary)
ax.text(9.1, 5.3, '(Logic)', fontsize=12, ha='center', style='italic', color=color_text)
ax.text(9.1, 4.9, 'Language where each', fontsize=10, ha='center')
ax.text(9.1, 4.6, 'sentence represents', fontsize=10, ha='center')
ax.text(9.1, 4.3, 'True or False value', fontsize=10, ha='center')

# 4. Action
box4 = FancyBboxPatch((11.3, 4.2), 2.8, 1.8,
                      boxstyle="round,pad=0.15",
                      edgecolor=color_action, linewidth=3,
                      facecolor='#E8F5E9')
ax.add_patch(box4)
ax.text(12.7, 5.7, 'Action', fontsize=16, weight='bold', ha='center', color=color_action)
ax.text(12.7, 5.3, '(Hành động)', fontsize=12, ha='center', style='italic', color=color_text)
ax.text(12.7, 4.8, 'Appropriate actions', fontsize=10, ha='center')
ax.text(12.7, 4.5, 'based on inference', fontsize=10, ha='center')

# Arrows connecting the boxes
arrow1 = FancyArrowPatch((3.4, 5.1), (4.0, 5.1),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=3, color=color_main)
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((7.0, 5.1), (7.6, 5.1),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=3, color=color_main)
ax.add_patch(arrow2)

arrow3 = FancyArrowPatch((10.6, 5.1), (11.2, 5.1),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=3, color=color_secondary)
ax.add_patch(arrow3)

# Central Inference Box - The main process
inference_box = FancyBboxPatch((3.5, 1.5), 7, 2.0,
                               boxstyle="round,pad=0.2",
                               edgecolor=color_secondary, linewidth=4,
                               facecolor='#FFF3E0', alpha=0.95)
ax.add_patch(inference_box)

# Add "Inference Engine" text
ax.text(7, 3.1, 'INFERENCE ENGINE', fontsize=18, weight='bold', 
        ha='center', color=color_secondary)
ax.text(7, 2.6, 'Uses Logic to Reason about Knowledge Base', fontsize=13, 
        ha='center', style='italic', color=color_text)
ax.text(7, 2.1, '→ Apply inference rules   → Derive new facts   → Make decisions', 
        fontsize=11, ha='center', color=color_text)
ax.text(7, 1.7, '→ Answer queries   → Solve problems', 
        fontsize=11, ha='center', color=color_text)

# Arrows from components to inference engine
# From KB to Inference
arrow_kb_inf = FancyArrowPatch((5.5, 4.1), (5.5, 3.6),
                               arrowstyle='->', mutation_scale=30, 
                               linewidth=3, color=color_main)
ax.add_patch(arrow_kb_inf)
ax.text(5.9, 3.85, 'Input', fontsize=11, color=color_main, weight='bold')

# From Logic to Inference
arrow_logic_inf = FancyArrowPatch((9.1, 4.1), (9.1, 3.6),
                                  arrowstyle='->', mutation_scale=30, 
                                  linewidth=3, color=color_secondary)
ax.add_patch(arrow_logic_inf)
ax.text(9.6, 3.85, 'Rules', fontsize=11, color=color_secondary, weight='bold')

# From Inference to Action
arrow_inf_action = FancyArrowPatch((10.5, 2.5), (12.0, 4.2),
                                   arrowstyle='->', mutation_scale=30, 
                                   linewidth=4, color=color_action,
                                   connectionstyle="arc3,rad=0.3")
ax.add_patch(arrow_inf_action)
ax.text(11.5, 3.3, 'Output', fontsize=12, color=color_action, weight='bold')

# Two key functions of Logic - in boxes
logic_function1 = FancyBboxPatch((0.5, 2.5), 2.5, 0.6,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=color_secondary, linewidth=2,
                                 facecolor='white', alpha=0.9)
ax.add_patch(logic_function1)
ax.text(1.75, 2.8, '① Represent Knowledge', fontsize=11, weight='bold', 
        ha='center', color=color_secondary)

logic_function2 = FancyBboxPatch((0.5, 1.6), 2.5, 0.6,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=color_secondary, linewidth=2,
                                 facecolor='white', alpha=0.9)
ax.add_patch(logic_function2)
ax.text(1.75, 1.9, '② Reasoning/Inference', fontsize=11, weight='bold', 
        ha='center', color=color_secondary)

# Connecting arrows from logic functions
arrow_func1 = FancyArrowPatch((3.1, 2.8), (3.4, 2.8),
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2, color=color_secondary, linestyle='--')
ax.add_patch(arrow_func1)

arrow_func2 = FancyArrowPatch((3.1, 1.9), (3.4, 1.9),
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2, color=color_secondary, linestyle='--')
ax.add_patch(arrow_func2)

# Bottom summary box
summary_box = FancyBboxPatch((1.5, 0.2), 11, 0.8,
                             boxstyle="round,pad=0.15",
                             edgecolor='gray', linewidth=2,
                             facecolor='#FFFDE7', alpha=0.9)
ax.add_patch(summary_box)
ax.text(7, 0.75, 'Goal: Use formal logic and knowledge to automatically derive new conclusions', 
        fontsize=13, weight='bold', ha='center', color=color_text)
ax.text(7, 0.4, 'and make intelligent decisions', 
        fontsize=13, weight='bold', ha='center', color=color_text)

# Add TELL/ASK labels
tell_box = FancyBboxPatch((4.8, 3.8), 0.6, 0.25,
                          boxstyle="round,pad=0.05",
                          edgecolor='black', linewidth=1,
                          facecolor='lightyellow')
ax.add_patch(tell_box)
ax.text(5.1, 3.925, 'TELL', fontsize=9, ha='center', weight='bold')

ask_box = FancyBboxPatch((11.2, 3.2), 0.6, 0.25,
                         boxstyle="round,pad=0.05",
                         edgecolor='black', linewidth=1,
                         facecolor='lightgreen')
ax.add_patch(ask_box)
ax.text(11.5, 3.325, 'ASK', fontsize=9, ha='center', weight='bold')

plt.tight_layout()
plt.savefig('/Users/nguyennghia/PROJECT/Intro_to_AI/idea/Prositional logic/minimal_diagram.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
print("Minimal diagram saved as 'minimal_diagram.png'")
plt.show()


