# Week 9 Exercises: Propositional Logic

**Course:** Introduction to Artificial Intelligence  
**Topic:** Propositional Logic - Syntax, Semantics, and CNF Conversion  
**Due:** November 5th, 2024 (Before next class)

---

## 📋 **Exercise Instructions**

- Complete all exercises below
- Show your work for all problems
- Submit via LMS (Learning Management System)
- Code exercises should be uploaded to Kaggle
- **Collaboration Policy:** You may discuss with classmates, but write solutions independently

---

## 🎯 **Part A: Syntax and Semantics (40 points)**

### **Exercise 1: Propositions and Connectives (10 points)**

**1.1** Which of the following are propositions? Explain your answer.

a) "It is raining today"  
b) "What is the capital of France?"  
c) "x + 5 = 10"  
d) "Close the window!"  
e) "All students in this class are intelligent"

**1.2** Let P = "It is sunny", Q = "It is warm", R = "We go to the beach"

Translate the following English sentences into propositional logic:

a) "If it is sunny and warm, then we go to the beach"  
b) "We go to the beach if and only if it is sunny"  
c) "It is not the case that it is sunny or warm"  
d) "Either we go to the beach or it is not sunny"

---

### **Exercise 2: Truth Tables (15 points)**

**2.1** Construct truth tables for the following formulas:

a) (P → Q) ∧ (Q → R)  
b) (P ∨ Q) → (P ∧ Q)  
c) ¬(P ∧ Q) ↔ (¬P ∨ ¬Q)

**2.2** Using truth tables, determine which of the following are:
- Tautologies (always true)
- Contradictions (always false)  
- Contingent (sometimes true, sometimes false)

a) P ∨ ¬P  
b) P ∧ ¬P  
c) (P → Q) → (¬Q → ¬P)  
d) P → (Q → P)

---

### **Exercise 3: Logical Equivalences (15 points)**

**3.1** Prove the following logical equivalences using truth tables or logical equivalences:

a) ¬(P → Q) ≡ P ∧ ¬Q  
b) P → (Q → R) ≡ (P ∧ Q) → R  
c) (P → Q) ∧ (P → R) ≡ P → (Q ∧ R)

**3.2** Simplify the following expressions using logical equivalences:

a) ¬(¬P ∨ Q) ∧ (P ∨ ¬Q)  
b) (P → Q) ∨ (Q → P)  
c) ¬(P ∧ (Q ∨ ¬P))

---

## 🎯 **Part B: CNF Conversion (40 points)**

### **Exercise 4: CNF Conversion (25 points)**

Convert the following formulas to Conjunctive Normal Form (CNF). Show all steps clearly.

**4.1** (P ∨ Q) → (P ∧ R)

**4.2** (P → Q) ↔ (¬Q → ¬P)

**4.3** ¬(P ∧ (Q → R))

**4.4** (P ∨ Q) ∧ (P → R) ∧ (Q → S)

---

### **Exercise 5: Resolution and Inference (15 points)**

**5.1** Given the following knowledge base:
- P → Q
- Q → R  
- P

Use resolution to prove R.

**5.2** Given the following knowledge base:
- P ∨ Q
- ¬P ∨ R
- ¬Q ∨ S

Use resolution to derive a new clause.

---

## 🎯 **Part C: Applications (20 points)**

### **Exercise 6: Wumpus World Logic (10 points)**

In the Wumpus World, let:
- B₁,₁ = "There is a breeze in cell (1,1)"
- P₁,₂ = "There is a pit in cell (1,2)"  
- P₂,₁ = "There is a pit in cell (2,1)"

**6.1** Express the rule "If there is a breeze in (1,1), then there is a pit in (1,2) or (2,1)" in propositional logic.

**6.2** Convert your answer from 6.1 to CNF.

**6.3** If the agent detects a breeze in (1,1) and no breeze in (1,2), what can we conclude? Use resolution to prove your answer.

---

### **Exercise 7: Medical Diagnosis System (10 points)**

Consider a simple medical diagnosis system with:
- F = "Patient has fever"
- C = "Patient has cough"  
- F = "Patient has flu"
- C = "Patient has cold"

**7.1** Express the following rules in propositional logic:
- "If patient has fever and cough, then patient has flu"
- "If patient has flu, then patient has fever"
- "Patient has either flu or cold, but not both"

**7.2** If we observe that a patient has fever and cough, what can we conclude? Use resolution to prove your answer.

---

## 💻 **Part D: Programming Exercise (Bonus: 10 points)**

### **Exercise 8: Truth Table Generator**

Write a Python function that generates truth tables for propositional logic formulas.

```python
def truth_table(formula, variables):
    """
    Generate truth table for a propositional formula
    
    Args:
        formula: String representation of the formula
        variables: List of variable names
    
    Returns:
        Dictionary with truth assignments and formula values
    """
    # Your implementation here
    pass
```

**Test your function with:**
- (P → Q) ∧ (Q → R)
- (P ∨ Q) → (P ∧ Q)

---

## 📝 **Submission Guidelines**

### **Format:**
- **Written exercises:** PDF or Word document
- **Code exercises:** Python notebook (.ipynb) or .py file
- **Show all work:** Partial credit given for correct methodology

### **Naming Convention:**
- **File name:** `LastName_FirstName_Week9_Exercises.pdf`
- **Example:** `Nguyen_Minh_Week9_Exercises.pdf`

### **Submission:**
- **LMS:** Upload written solutions
- **Kaggle:** Upload code files
- **Due date:** November 5th, 2024, before class

---

## 📚 **Resources**

### **Main Textbook:**
- **AIMA Chapter 7:** [Download PDF](http://lib.ysu.am/disciplines_bk/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf)

### **Additional Resources:**
- **CNF Conversion Guide:** Available on course website
- **Truth Table Practice:** Online tools and examples
- **Office Hours:** Dr. Trong-Nghia Nguyen - nghiant@neu.edu.vn

### **Helpful Tips:**
1. **Start with truth tables:** Build intuition for logical connectives
2. **Practice CNF conversion:** This is crucial for automated reasoning
3. **Use examples:** Connect abstract logic to real-world problems
4. **Ask questions:** Office hours available for clarification

---

## 📤 **Submission Instructions**

**Submit your solutions via one of the following methods:**

### 📄 **PDF Submission (Recommended)**
Upload your completed exercises as a PDF file to:
**https://drive.google.com/drive/folders/1y8nreGuCBV6XS27suh3Lx7vkWXud22-t?usp=sharing**

### 💻 **Code Submission (Kaggle)**
If you include any code or want to submit via Kaggle:
**https://www.kaggle.com/groups/ai66a-intro-to-ai/pending-invite/CC839838-30DA-4B84-809E-390CBD73F302**

---

**Good luck with the exercises! Remember to start early and ask questions if you need help.**
