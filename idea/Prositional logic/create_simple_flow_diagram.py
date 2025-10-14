import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patches as mpatches

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Inference and Logic in AI', 
        fontsize=26, weight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#2C5F7C', 
                  edgecolor='black', linewidth=2, alpha=0.9),
        color='white')

# Central Circle - Inference/Reasoning
central_circle = Circle((5, 5), 1.8, 
                        facecolor='#FFD9B3', 
                        edgecolor='#D68910', 
                        linewidth=5)
ax.add_patch(central_circle)
ax.text(5, 5.5, 'Inference', fontsize=20, weight='bold', ha='center')
ax.text(5, 5.1, '(Reasoning)', fontsize=14, weight='bold', ha='center', style='italic')
ax.text(5, 4.5, 'Generate new', fontsize=11, ha='center')
ax.text(5, 4.2, 'correct statements', fontsize=11, ha='center')

# Top Box - Knowledge
knowledge_box = FancyBboxPatch((3.2, 7.2), 3.6, 1.5,
                               boxstyle="round,pad=0.2",
                               edgecolor='#2C5F7C', linewidth=4,
                               facecolor='#B3D9E6')
ax.add_patch(knowledge_box)
ax.text(5, 8.5, 'Knowledge', fontsize=18, weight='bold', ha='center')
ax.text(5, 8.0, 'Information & Facts', fontsize=12, ha='center', style='italic')
ax.text(5, 7.5, 'Represented as sentences/propositions', fontsize=10, ha='center')

# Left Box - Logic
logic_box = FancyBboxPatch((0.3, 4.0), 2.8, 2.0,
                           boxstyle="round,pad=0.2",
                           edgecolor='#D68910', linewidth=4,
                           facecolor='#FFE5CC')
ax.add_patch(logic_box)
ax.text(1.7, 5.7, 'Logic', fontsize=18, weight='bold', ha='center')
ax.text(1.7, 5.2, 'Formal Language', fontsize=12, ha='center', style='italic')
ax.text(1.7, 4.7, '• Syntax', fontsize=11, ha='center')
ax.text(1.7, 4.3, '• Semantics', fontsize=11, ha='center')

# Right Box - Knowledge Base (KB)
kb_box = FancyBboxPatch((6.9, 4.0), 2.8, 2.0,
                        boxstyle="round,pad=0.2",
                        edgecolor='#2C5F7C', linewidth=4,
                        facecolor='#E8F4F8')
ax.add_patch(kb_box)
ax.text(8.3, 5.7, 'Knowledge', fontsize=16, weight='bold', ha='center')
ax.text(8.3, 5.3, 'Base (KB)', fontsize=16, weight='bold', ha='center')
ax.text(8.3, 4.7, 'Structured', fontsize=11, ha='center', style='italic')
ax.text(8.3, 4.3, 'Representation', fontsize=11, ha='center', style='italic')

# Bottom Box - Action
action_box = FancyBboxPatch((3.0, 0.8), 4.0, 1.5,
                            boxstyle="round,pad=0.2",
                            edgecolor='#28A745', linewidth=4,
                            facecolor='#D4EDDA')
ax.add_patch(action_box)
ax.text(5, 2.0, 'Appropriate Actions', fontsize=18, weight='bold', ha='center')
ax.text(5, 1.5, 'Decisions & Behaviors', fontsize=12, ha='center', style='italic')
ax.text(5, 1.0, 'Execute • Decide • Solve', fontsize=10, ha='center')

# Arrows

# Knowledge -> Inference (from top)
arrow1 = FancyArrowPatch((5, 7.1), (5, 6.9),
                        arrowstyle='->', mutation_scale=35, 
                        linewidth=4, color='#2C5F7C')
ax.add_patch(arrow1)
ax.text(5.6, 7.0, 'Input', fontsize=12, color='#2C5F7C', weight='bold')

# Logic -> Inference (from left)
arrow2 = FancyArrowPatch((3.2, 5.0), (3.3, 5.0),
                        arrowstyle='->', mutation_scale=35, 
                        linewidth=4, color='#D68910')
ax.add_patch(arrow2)
ax.text(3.0, 5.5, 'Rules', fontsize=12, color='#D68910', weight='bold', rotation=0)

# KB -> Inference (from right)
arrow3 = FancyArrowPatch((6.8, 5.0), (6.7, 5.0),
                        arrowstyle='->', mutation_scale=35, 
                        linewidth=4, color='#2C5F7C')
ax.add_patch(arrow3)
ax.text(7.2, 5.5, 'Facts', fontsize=12, color='#2C5F7C', weight='bold')

# Inference -> Action (to bottom)
arrow4 = FancyArrowPatch((5, 3.1), (5, 2.4),
                        arrowstyle='->', mutation_scale=40, 
                        linewidth=5, color='#28A745')
ax.add_patch(arrow4)
ax.text(5.8, 2.7, 'Output', fontsize=13, color='#28A745', weight='bold')

# Additional relationship arrows

# Knowledge -> KB (encoding)
arrow5 = FancyArrowPatch((6.5, 7.8), (8.0, 6.1),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=3, color='#2C5F7C',
                        connectionstyle="arc3,rad=0.3")
ax.add_patch(arrow5)
ax.text(7.5, 7.0, 'Encode', fontsize=10, color='#2C5F7C', 
        weight='bold', style='italic')

# Logic -> Knowledge (representation)
arrow6 = FancyArrowPatch((2.5, 6.2), (3.8, 7.3),
                        arrowstyle='->', mutation_scale=25, 
                        linewidth=3, color='#D68910',
                        connectionstyle="arc3,rad=-0.3")
ax.add_patch(arrow6)
ax.text(2.5, 6.8, 'Represent', fontsize=10, color='#D68910', 
        weight='bold', style='italic')

# Add numbered process flow
process_numbers = [
    (5, 8.9, '1', 'Collect Knowledge'),
    (1.7, 6.3, '2', 'Define Logic'),
    (8.3, 6.3, '3', 'Build KB'),
    (5, 5, '4', 'Infer'),
    (5, 2.6, '5', 'Act'),
]

for x, y, num, label in process_numbers:
    if num == '4':  # Central inference - larger
        ax.text(x-0.1, y, num, fontsize=24, weight='bold', ha='center', va='center',
                bbox=dict(boxstyle='circle', facecolor='white', 
                         edgecolor='black', linewidth=3))
    else:
        ax.text(x, y, num, fontsize=18, weight='bold', ha='center', va='center',
                bbox=dict(boxstyle='circle', facecolor='yellow', 
                         edgecolor='black', linewidth=2))

# Add key concepts in boxes
concepts = [
    (1.0, 2.5, 'Logic =\nLanguage\nwith\nTrue/False\nvalues', '#FFE5CC'),
    (9.0, 2.5, 'KB =\nStructured\nknowledge\nin specific\nformat', '#E8F4F8'),
]

for x, y, text, color in concepts:
    concept_box = FancyBboxPatch((x-0.6, y-0.5), 1.2, 1.0,
                                 boxstyle="round,pad=0.1",
                                 edgecolor='black', linewidth=2,
                                 facecolor=color, alpha=0.7)
    ax.add_patch(concept_box)
    ax.text(x, y, text, fontsize=8, ha='center', va='center', weight='bold')

# Add the main definition box
definition_text = (
    "Inference is the process of generating new correct statements\n"
    "from previously existing knowledge to make appropriate actions"
)
ax.text(5, 0.2, definition_text, fontsize=11, ha='center', 
        style='italic', weight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', 
                  edgecolor='#D68910', linewidth=2, alpha=0.9))

plt.tight_layout()
plt.savefig('/Users/nguyennghia/PROJECT/Intro_to_AI/idea/Prositional logic/simple_flow_diagram.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
print("Simple flow diagram saved as 'simple_flow_diagram.png'")
plt.show()


