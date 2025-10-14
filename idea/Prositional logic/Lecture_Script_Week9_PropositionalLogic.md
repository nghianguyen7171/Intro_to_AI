# Lecture Script: Week 9 - Propositional Logic
**Course:** Introduction to Artificial Intelligence  
**Date:** October 29, 2024  
**Duration:** 2 hours  
**Slide:** 5.Propositional_Logic.pdf

---

## 🎯 **Learning Objectives**
By the end of this lecture, students should be able to:
1. Understand the syntax and semantics of propositional logic
2. Represent knowledge using logical sentences
3. Apply inference rules to derive new knowledge
4. Convert logical formulas to Conjunctive Normal Form (CNF)
5. Use resolution for automated reasoning

---

## 📋 **Lecture Outline (120 minutes)**

### **Part 1: Introduction (15 minutes)**
### **Part 2: Syntax and Semantics (35 minutes)**
### **Part 3: Inference and Resolution (40 minutes)**
### **Part 4: CNF Conversion (20 minutes)**
### **Part 5: Exercises and Q&A (10 minutes)**

---

## 🎤 **Detailed Lecture Script**

### **Part 1: Introduction (15 minutes)**

#### **Slide 1: Title Slide**
**Speaking Points:**
- "Welcome to Week 9 of our Introduction to AI course"
- "Today we'll explore Propositional Logic - the foundation of knowledge representation in AI"
- "This connects directly to our previous weeks on search, as logic allows us to represent and reason about knowledge"

#### **Slide 2-3: Why Logic in AI?**
**Speaking Points:**
- "Why do we need logic in AI? Let's think about intelligent agents"
- "An agent needs to: 1) Represent what it knows, 2) Reason about that knowledge, 3) Make decisions"
- "Logic provides a formal language for knowledge representation and reasoning"
- **Example:** "Consider a medical diagnosis system - it needs to represent symptoms, diseases, and relationships between them"

#### **Slide 4: Knowledge-Based Agents**
**Speaking Points:**
- "A knowledge-based agent has two main components:"
- "1) Knowledge Base (KB) - stores facts and rules"
- "2) Inference Engine - derives new knowledge from existing knowledge"
- **TELL operation:** "We can add new facts to the KB"
- **ASK operation:** "We can query the KB to get answers"

---

### **Part 2: Syntax and Semantics (35 minutes)**

#### **Slide 5-6: What is a Proposition?**
**Speaking Points:**
- "A proposition is a declarative sentence that is either TRUE or FALSE"
- **Examples of propositions:**
  - "It is raining" ✓
  - "2 + 2 = 4" ✓
  - "The student passed the exam" ✓
- **Not propositions:**
  - "What time is it?" ❌ (question)
  - "Close the door!" ❌ (command)
  - "x + 1 = 5" ❌ (contains variable)

#### **Slide 7-8: Syntax - Logical Connectives**
**Speaking Points:**
- "We have five main logical connectives:"
- **Negation (¬):** "NOT - reverses truth value"
- **Conjunction (∧):** "AND - true only when both are true"
- **Disjunction (∨):** "OR - true when at least one is true"
- **Implication (→):** "IF-THEN - false only when premise is true and conclusion is false"
- **Biconditional (⟷):** "IF AND ONLY IF - true when both have same truth value"

**Interactive Example:**
- "Let's work through: 'If it rains, then the ground is wet'"
- "When is this false? Only when it rains but the ground is NOT wet"

#### **Slide 9-12: Truth Tables**
**Speaking Points:**
- "Truth tables show all possible truth values for logical expressions"
- **Work through each connective:**
  - Negation: Simple reversal
  - Conjunction: Only true when both true
  - Disjunction: True unless both false
  - Implication: Tricky! False only when P=true, Q=false
  - Biconditional: True when both same value

**Class Exercise:**
- "Let's build truth table for (P ∨ Q) → R together"
- "How many rows? 2³ = 8 rows for P, Q, R"

#### **Slide 13-15: Logical Equivalences**
**Speaking Points:**
- "Two formulas are logically equivalent if they have the same truth table"
- **Key equivalences:**
  - **De Morgan's Laws:** ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
  - **Implication:** P → Q ≡ ¬P ∨ Q
  - **Contrapositive:** P → Q ≡ ¬Q → ¬P
- **Memory trick:** "Break the line, change the sign" for De Morgan's

---

### **Part 3: Inference and Resolution (40 minutes)**

#### **Slide 16-18: Logical Inference**
**Speaking Points:**
- "Inference is the process of deriving new knowledge from existing knowledge"
- **Entailment (⊨):** "KB entails α if α is true in every model where KB is true"
- **Soundness:** "If we can derive α, then KB entails α"
- **Completeness:** "If KB entails α, then we can derive α"

#### **Slide 19-21: Inference Rules**
**Speaking Points:**
- **Modus Ponens:** "If P → Q and P, then Q"
- **Modus Tollens:** "If P → Q and ¬Q, then ¬P"
- **Resolution:** "If P ∨ Q and ¬P ∨ R, then Q ∨ R"
- **Resolution is complete:** "We can derive any conclusion using only resolution"

#### **Slide 22-24: Resolution Algorithm**
**Speaking Points:**
- "Resolution is the universal inference rule"
- **Algorithm:**
  1. Convert KB and ¬α to CNF
  2. Apply resolution repeatedly
  3. If we get empty clause (⊥), then KB ⊨ α
  4. If no new clauses, then KB ⊭ α

**Example:** "Let's work through a simple resolution proof"

---

### **Part 4: CNF Conversion (20 minutes)**

#### **Slide 25-28: CNF Conversion Steps**
**Speaking Points:**
- "CNF = Conjunctive Normal Form = conjunction of disjunctions"
- **Four steps:**
  1. **Eliminate biconditionals:** α ⟷ β becomes (α → β) ∧ (β → α)
  2. **Eliminate implications:** α → β becomes ¬α ∨ β
  3. **Move negation inward:** Use De Morgan's laws
  4. **Distribute ∨ over ∧:** α ∨ (β ∧ γ) becomes (α ∨ β) ∧ (α ∨ γ)

**Worked Example:**
- "Let's convert B₁,₁ ⟷ (P₁,₂ ∨ P₂,₁) to CNF step by step"
- **Step 1:** (B₁,₁ → (P₁,₂ ∨ P₂,₁)) ∧ ((P₁,₂ ∨ P₂,₁) → B₁,₁)
- **Step 2:** (¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ (¬(P₁,₂ ∨ P₂,₁) ∨ B₁,₁)
- **Step 3:** (¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ ((¬P₁,₂ ∧ ¬P₂,₁) ∨ B₁,₁)
- **Step 4:** (¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ (¬P₁,₂ ∨ B₁,₁) ∧ (¬P₂,₁ ∨ B₁,₁)

#### **Slide 29-30: Why CNF?**
**Speaking Points:**
- "Why convert to CNF?"
- **Resolution works with CNF:** "Single universal inference rule"
- **Automated reasoning:** "Computers can systematically find proofs"
- **SAT solvers:** "Modern algorithms optimized for CNF"
- **Scalability:** "Handles large knowledge bases efficiently"

---

### **Part 5: Exercises and Q&A (10 minutes)**

#### **Exercise 1: Truth Tables**
- "Construct truth table for (P → Q) ∧ (Q → R) → (P → R)"
- "What do you notice? This is a tautology!"

#### **Exercise 2: Logical Equivalence**
- "Prove: ¬(P → Q) ≡ P ∧ ¬Q"
- "Use truth tables or logical equivalences"

#### **Exercise 3: CNF Conversion**
- "Convert (P ∨ Q) → (P ∧ R) to CNF"
- "Show all steps"

#### **Q&A Session**
- Address student questions
- Connect to previous weeks (search algorithms)
- Preview next week (First-Order Logic)

---

## 🎯 **Key Teaching Points**

### **Emphasize:**
1. **Real-world applications:** Medical diagnosis, expert systems, planning
2. **Connection to search:** Logic provides knowledge representation for intelligent agents
3. **Practical skills:** Students can now represent and reason about knowledge
4. **Computational thinking:** Systematic approaches to problem-solving

### **Common Misconceptions:**
1. **Implication confusion:** "If P then Q" is not the same as "If Q then P"
2. **De Morgan's laws:** Students often forget to change the connective
3. **CNF purpose:** Why we need to convert to CNF for automated reasoning

### **Interactive Elements:**
1. **Truth table construction:** Do together as class
2. **CNF conversion:** Step-by-step with student participation
3. **Resolution examples:** Work through simple proofs
4. **Real examples:** Use Wumpus World or medical diagnosis

---

## 📚 **Resources for Students**

### **Main Textbook:**
- **AIMA Chapter 7:** [PDF Link](http://lib.ysu.am/disciplines_bk/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf)
- **Focus on:** Sections 7.1-7.5 (Syntax, Semantics, Inference, Resolution)

### **Additional Reading:**
- **CNF Conversion Guide:** Created in `idea/Prositional logic/CNF_Conversion_Method_English.md`
- **Lecture Content:** Comprehensive guide in `Propositional_Logic_Lecture_Content.md`

### **Practice Exercises:**
- **Homework 5:** Logic and Neural Networks (Due: November 12th)
- **Online exercises:** Will be posted on course website

---

## 🎤 **Speaking Tips**

### **Engagement Techniques:**
1. **Start with examples:** "Imagine you're a doctor diagnosing a patient..."
2. **Use visual aids:** Truth tables, CNF conversion steps
3. **Interactive questions:** "What do you think happens when..."
4. **Real-world connections:** Connect to previous weeks, preview future topics

### **Pacing:**
- **Don't rush truth tables:** Students need time to understand
- **Emphasize CNF conversion:** This is crucial for automated reasoning
- **Save time for exercises:** Students learn by doing

### **Assessment:**
- **Check understanding:** Ask students to explain back to you
- **Common errors:** Watch for implication and De Morgan's mistakes
- **Encourage questions:** Logic can be confusing, questions are welcome

---

## 📝 **Post-Lecture Notes**

### **Follow-up Actions:**
1. **Post exercises** on course website
2. **Create practice problems** for next week
3. **Prepare FOL introduction** for Week 10
4. **Update course materials** with any clarifications

### **Student Support:**
- **Office hours:** Available for CNF conversion help
- **Online resources:** Additional practice problems
- **Peer study groups:** Encourage collaboration on exercises

---

**End of Lecture Script**

*This script provides a comprehensive guide for delivering the Week 9 Propositional Logic lecture. Adjust timing and examples based on student responses and class dynamics.*
