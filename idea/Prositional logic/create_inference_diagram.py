import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as patches

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define colors
color_knowledge = '#E8F4F8'  # Light blue
color_kb = '#B3D9E6'  # Medium blue
color_logic = '#FFE5CC'  # Light orange
color_inference = '#FFD9B3'  # Medium orange
color_action = '#D4EDDA'  # Light green

# Title
ax.text(5, 9.5, 'Knowledge-Based Agent Architecture', 
        fontsize=24, weight='bold', ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.8))

# 1. Knowledge Box (Top Left)
knowledge_box = FancyBboxPatch((0.5, 6.5), 2.5, 2,
                               boxstyle="round,pad=0.15",
                               edgecolor='#2C5F7C', linewidth=3,
                               facecolor=color_knowledge)
ax.add_patch(knowledge_box)
ax.text(1.75, 8.2, 'Knowledge', fontsize=16, weight='bold', ha='center')
ax.text(1.75, 7.7, 'Information & Facts', fontsize=11, ha='center', style='italic')
ax.text(1.75, 7.3, '• Domain information', fontsize=9, ha='center')
ax.text(1.75, 7.0, '• Facts & Rules', fontsize=9, ha='center')
ax.text(1.75, 6.7, '• Sentences/Propositions', fontsize=9, ha='center')

# 2. Knowledge Base (KB) Box (Middle Left)
kb_box = FancyBboxPatch((0.5, 4.0), 2.5, 2,
                        boxstyle="round,pad=0.15",
                        edgecolor='#2C5F7C', linewidth=3,
                        facecolor=color_kb)
ax.add_patch(kb_box)
ax.text(1.75, 5.7, 'Knowledge Base', fontsize=16, weight='bold', ha='center')
ax.text(1.75, 5.3, '(KB)', fontsize=14, weight='bold', ha='center', style='italic')
ax.text(1.75, 4.8, 'Structured representation', fontsize=10, ha='center', style='italic')
ax.text(1.75, 4.4, '• Knowledge language', fontsize=9, ha='center')
ax.text(1.75, 4.1, '• Specific format', fontsize=9, ha='center')

# 3. Logic Box (Top Right)
logic_box = FancyBboxPatch((4.0, 6.5), 2.5, 2,
                           boxstyle="round,pad=0.15",
                           edgecolor='#D68910', linewidth=3,
                           facecolor=color_logic)
ax.add_patch(logic_box)
ax.text(5.25, 8.2, 'Logic', fontsize=16, weight='bold', ha='center')
ax.text(5.25, 7.7, 'Formal Language', fontsize=11, ha='center', style='italic')
ax.text(5.25, 7.2, '• Syntax (form)', fontsize=9, ha='center')
ax.text(5.25, 6.9, '• Semantics (meaning)', fontsize=9, ha='center')
ax.text(5.25, 6.6, '• True/False values', fontsize=9, ha='center')

# 4. Inference (Reasoning) Box (Center)
inference_box = FancyBboxPatch((3.5, 3.5), 3.5, 2.5,
                               boxstyle="round,pad=0.15",
                               edgecolor='#D68910', linewidth=4,
                               facecolor=color_inference)
ax.add_patch(inference_box)
ax.text(5.25, 5.7, 'Inference (Reasoning)', fontsize=16, weight='bold', ha='center')
ax.text(5.25, 5.2, 'Generate new correct statements', fontsize=11, ha='center', style='italic')
ax.text(5.25, 4.7, 'from existing knowledge', fontsize=11, ha='center', style='italic')
ax.text(5.25, 4.2, '• Deduction', fontsize=9, ha='center')
ax.text(5.25, 3.9, '• Inference Rules', fontsize=9, ha='center')
ax.text(5.25, 3.6, '• Logical Derivation', fontsize=9, ha='center')

# 5. Action Box (Bottom)
action_box = FancyBboxPatch((3.0, 0.5), 4.5, 1.8,
                            boxstyle="round,pad=0.15",
                            edgecolor='#28A745', linewidth=3,
                            facecolor=color_action)
ax.add_patch(action_box)
ax.text(5.25, 2.0, 'Appropriate Actions', fontsize=16, weight='bold', ha='center')
ax.text(5.25, 1.6, 'Decisions & Behaviors', fontsize=11, ha='center', style='italic')
ax.text(5.25, 1.1, '• Execute plans  • Make decisions  • Solve problems', 
        fontsize=9, ha='center')
ax.text(5.25, 0.7, '• Respond to queries  • Control systems', 
        fontsize=9, ha='center')

# Arrows showing relationships

# Knowledge -> KB
arrow1 = FancyArrowPatch((1.75, 6.4), (1.75, 6.1),
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=3, color='#2C5F7C',
                        connectionstyle="arc3,rad=0")
ax.add_patch(arrow1)
ax.text(2.3, 6.25, 'Encode', fontsize=10, color='#2C5F7C', weight='bold')

# KB -> Inference
arrow2 = FancyArrowPatch((3.1, 5.0), (3.4, 5.0),
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=3, color='#2C5F7C',
                        connectionstyle="arc3,rad=0")
ax.add_patch(arrow2)
ax.text(3.25, 5.3, 'Input', fontsize=10, color='#2C5F7C', weight='bold')

# Logic -> Inference (provides framework)
arrow3 = FancyArrowPatch((5.25, 6.4), (5.25, 6.1),
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=3, color='#D68910',
                        connectionstyle="arc3,rad=0")
ax.add_patch(arrow3)
ax.text(6.0, 6.25, 'Framework', fontsize=10, color='#D68910', weight='bold')

# Inference -> Action
arrow4 = FancyArrowPatch((5.25, 3.4), (5.25, 2.4),
                        arrowstyle='->', mutation_scale=35, 
                        linewidth=4, color='#28A745',
                        connectionstyle="arc3,rad=0")
ax.add_patch(arrow4)
ax.text(6.0, 2.9, 'Generate', fontsize=11, color='#28A745', weight='bold')

# Feedback loop: Action -> KB (dotted line)
arrow5 = FancyArrowPatch((3.0, 1.4), (1.0, 4.0),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=2, color='gray', linestyle='--',
                        connectionstyle="arc3,rad=0.3")
ax.add_patch(arrow5)
ax.text(1.0, 2.5, 'Update\nKnowledge', fontsize=9, color='gray', 
        style='italic', ha='center')

# Add side annotations

# Left side: TELL/ASK
tell_ask_box = FancyBboxPatch((0.1, 4.5), 0.3, 1.0,
                              boxstyle="round,pad=0.02",
                              edgecolor='black', linewidth=1,
                              facecolor='lightyellow')
ax.add_patch(tell_ask_box)
ax.text(0.05, 5.3, 'TELL', fontsize=8, rotation=90, ha='center', weight='bold')
ax.text(0.05, 4.8, 'ASK', fontsize=8, rotation=90, ha='center', weight='bold')

# Right side: Process flow
ax.text(7.8, 8.0, 'Logic provides:', fontsize=11, weight='bold', ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.7))
ax.text(7.8, 7.6, '1. Representation', fontsize=9, ha='left')
ax.text(7.8, 7.3, '2. Inference rules', fontsize=9, ha='left')
ax.text(7.8, 7.0, '3. Semantics', fontsize=9, ha='left')

# Bottom annotation
ax.text(5, 0.1, 'Goal: Use knowledge and reasoning to make intelligent decisions',
        fontsize=12, ha='center', style='italic', weight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', alpha=0.8))

# Add legend
legend_elements = [
    mpatches.Patch(facecolor=color_knowledge, edgecolor='#2C5F7C', linewidth=2, label='Knowledge Components'),
    mpatches.Patch(facecolor=color_logic, edgecolor='#D68910', linewidth=2, label='Logic Framework'),
    mpatches.Patch(facecolor=color_action, edgecolor='#28A745', linewidth=2, label='Actions/Outputs'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=10, 
          framealpha=0.9, title='Component Types', title_fontsize=11)

# Add main process flow numbers
ax.text(1.0, 8.8, '①', fontsize=20, weight='bold', ha='center', 
        bbox=dict(boxstyle='circle', facecolor='white', edgecolor='black', linewidth=2))
ax.text(1.0, 5.8, '②', fontsize=20, weight='bold', ha='center',
        bbox=dict(boxstyle='circle', facecolor='white', edgecolor='black', linewidth=2))
ax.text(5.25, 8.8, '③', fontsize=20, weight='bold', ha='center',
        bbox=dict(boxstyle='circle', facecolor='white', edgecolor='black', linewidth=2))
ax.text(7.5, 4.5, '④', fontsize=20, weight='bold', ha='center',
        bbox=dict(boxstyle='circle', facecolor='white', edgecolor='black', linewidth=2))
ax.text(5.25, 2.8, '⑤', fontsize=20, weight='bold', ha='center',
        bbox=dict(boxstyle='circle', facecolor='white', edgecolor='black', linewidth=2))

plt.tight_layout()
plt.savefig('/Users/nguyennghia/PROJECT/Intro_to_AI/idea/Prositional logic/inference_diagram.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
print("Diagram saved as 'inference_diagram.png'")
plt.show()


