# Inference Diagrams Guide

**Created:** October 13, 2025  
**For:** Introduction to AI - Propositional Logic Lecture  
**Purpose:** First slide visualization

---

## 📊 Three Diagrams Created

### 1. **inference_diagram.png** - Knowledge-Based Agent Architecture
**File:** `inference_diagram.png` (549 KB, 4170×2970 pixels)

**Best for:** 
- Detailed technical presentation
- Advanced students
- Complete system overview

**Features:**
- Shows full Knowledge-Based Agent architecture
- Numbered flow (①→②→③→④→⑤)
- Color-coded components:
  - Blue: Knowledge components
  - Orange: Logic framework
  - Green: Actions/Outputs
- Includes TELL/ASK operations
- Shows feedback loop (dotted line from Action back to KB)
- Legend explaining component types

**Content Covered:**
✓ Knowledge → Knowledge Base encoding
✓ Logic provides framework for inference
✓ Inference engine generates actions
✓ Feedback mechanism for knowledge update
✓ Complete agent cycle

---

### 2. **simple_flow_diagram.png** - Inference and Logic in AI (Circular Flow)
**File:** `simple_flow_diagram.png` (461 KB, 3570×2970 pixels)

**Best for:**
- Mid-level complexity
- Clear visual flow
- Student engagement

**Features:**
- Central circle: Inference (Reasoning) as the core process
- 5 numbered steps in circular arrangement
- Shows relationships between all components
- Side boxes explaining Logic and KB definitions
- Definition at bottom: "Inference is the process of generating..."

**Content Covered:**
✓ Knowledge at top (input)
✓ Logic (left) provides rules and representation
✓ Knowledge Base (KB) (right) provides facts
✓ Inference (center) as the processing engine
✓ Actions (bottom) as output

---

### 3. **minimal_diagram.png** - Clean Presentation Version
**File:** `minimal_diagram.png` (474 KB, 4170×2670 pixels)

**Best for:** ✨ **RECOMMENDED FOR LECTURE SLIDES**
- PowerPoint/slide presentation
- Clean, professional look
- Easy to understand at a glance
- Perfect for students taking notes

**Features:**
- Blue header bar with title
- Definition box prominently displayed
- Linear flow: Knowledge → KB → Logic → Action
- Central "Inference Engine" box showing the core process
- Two key functions of Logic highlighted (① Represent Knowledge, ② Reasoning)
- Bilingual labels (English with Vietnamese translations)
- TELL/ASK labels
- Summary box at bottom

**Content Covered:**
✓ All four main components clearly separated
✓ Inference engine as the central process
✓ Logic's dual role (representation + reasoning)
✓ Clear input/output flow
✓ Goal statement at bottom

**Vietnamese Translations Included:**
- Knowledge (Tri thức)
- Knowledge Base (Cơ sở tri thức)
- Logic (Logic)
- Action (Hành động)

---

## 🎯 Recommendation for Your Lecture

### **Use: minimal_diagram.png**

**Why:**
1. ✅ **Clean layout** - Easy to project on screen
2. ✅ **Bilingual** - English + Vietnamese terms
3. ✅ **Comprehensive** - All key concepts included
4. ✅ **Professional** - Color-coded, well-organized
5. ✅ **Student-friendly** - Clear flow with numbered steps
6. ✅ **Matches your content** - Includes all definitions you specified

---

## 📝 How to Use in Your Slide

### Slide Structure:

**Title:** Inference (Reasoning) in Artificial Intelligence

**Content:**
1. **Insert the diagram** (minimal_diagram.png)
2. **Optional bullet points below:**
   - Inference: Process of generating new correct statements from existing knowledge
   - Knowledge: Information about a domain, represented as sentences/propositions
   - Knowledge Base (KB): Structured representation in specific format
   - Logic: Language where sentences have True/False values
   - Logic's two main roles: ① Represent Knowledge, ② Enable Reasoning

**Speaking Points:**
- Start with Knowledge at top left
- Explain how it's encoded into KB
- Show Logic provides the framework
- Central Inference Engine combines KB + Logic
- Output: Appropriate Actions
- Emphasize the TELL (input) and ASK (query) operations

---

## 🔄 Alternative Uses

### For Different Contexts:

**inference_diagram.png:**
- Use for: Research presentations, technical workshops
- Audience: Graduate students, researchers
- Advantage: Shows complete feedback loop

**simple_flow_diagram.png:**
- Use for: Interactive lectures, tutorials
- Audience: Undergraduate students, beginners
- Advantage: Circular flow emphasizes iterative process

**minimal_diagram.png:**
- Use for: Main lectures, conference talks, online courses
- Audience: All levels
- Advantage: Best readability on projector

---

## 🎨 Customization

All diagrams are generated using Python (matplotlib). To customize:

### Scripts Available:
1. `create_inference_diagram.py` - Full architecture diagram
2. `create_simple_flow_diagram.py` - Circular flow diagram
3. `create_minimal_diagram.py` - Clean presentation diagram

### Easy Modifications:
- **Colors:** Change color_main, color_secondary, color_action variables
- **Text:** Edit any text strings in the scripts
- **Size:** Modify figsize parameter
- **Resolution:** Change dpi value (currently 300)
- **Layout:** Adjust box positions (x, y coordinates)

### To regenerate:
```bash
python create_minimal_diagram.py
```

---

## 📚 Integration with Lecture Content

### These diagrams visualize concepts from:

**Your Propositional Logic Lecture:**
- Week 9: Propositional Logic – Syntax, Semantics, and Inference
- Reference: AIMA Chapters 7-8
- YouTube Tutorial: https://www.youtube.com/watch?v=ONxr7v3HaKo&t=1894s

### Next Slides Should Cover:
1. Introduction slide (✅ Use these diagrams)
2. What is Propositional Logic?
3. Syntax and Semantics
4. Truth Tables
5. Logical Connectives
6. Inference Rules
7. ... (see Propositional_Logic_Lecture_Content.md)

---

## 💡 Teaching Tips

### When Presenting These Diagrams:

1. **Start Simple:**
   - Point to each component one by one
   - Don't overwhelm students with all information at once

2. **Use Examples:**
   - Knowledge: "It is raining"
   - KB: Store as proposition P
   - Logic: P → Q (if raining, then ground is wet)
   - Inference: Derive Q (ground is wet)
   - Action: Take umbrella

3. **Interactive:**
   - Ask students to identify each component
   - Have them trace the flow
   - Quiz: "What happens at the Inference Engine?"

4. **Connect to Real World:**
   - Expert systems (medical diagnosis)
   - Game AI (chess, go)
   - Automated reasoning
   - Database query optimization

---

## 📂 File Organization

```
/idea/Prositional logic/
├── inference_diagram.png          (Detailed architecture)
├── simple_flow_diagram.png        (Circular flow)
├── minimal_diagram.png            (Presentation-ready) ⭐
├── create_inference_diagram.py    (Generator script)
├── create_simple_flow_diagram.py  (Generator script)
├── create_minimal_diagram.py      (Generator script)
├── Propositional_Logic_Lecture_Content.md  (Full lecture guide)
└── Diagrams_Guide.md              (This file)
```

---

## ✨ Summary

**Quick Decision Guide:**

| Need | Use This Diagram |
|------|------------------|
| Main lecture slide | **minimal_diagram.png** ⭐ |
| Technical workshop | inference_diagram.png |
| Interactive tutorial | simple_flow_diagram.png |
| Online course | minimal_diagram.png |
| Research presentation | inference_diagram.png |

**All diagrams:**
- ✅ High resolution (300 DPI)
- ✅ PNG format (transparent background support)
- ✅ Professional quality
- ✅ Ready to insert into PowerPoint/Google Slides/Keynote
- ✅ Include all key concepts you specified

---

**Created by:** Dr. Trong-Nghia Nguyen  
**Course:** Introduction to Artificial Intelligence  
**Institution:** National Economics University  
**Date:** October 13, 2025


