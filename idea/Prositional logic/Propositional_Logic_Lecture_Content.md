# Propositional Logic - Lecture Content Guide

**Course:** Introduction to Artificial Intelligence  
**Topic:** Propositional Logic (Logic Mệnh Đề)  
**Reference:** AIMA Chapters 7-8, [YouTube Tutorial](https://www.youtube.com/watch?v=ONxr7v3HaKo&t=1894s)  
**Prepared for:** Week 9 Lecture

---

## 📋 Lecture Overview

### Learning Objectives
By the end of this lecture, students should be able to:
1. Understand the syntax and semantics of propositional logic
2. Represent knowledge using logical sentences
3. Apply inference rules to derive new knowledge
4. Use truth tables and logical equivalences
5. Understand model checking and theorem proving
6. Apply resolution and CNF conversion

### Time Allocation (2-hour lecture)
- Introduction & Motivation: 15 minutes
- Syntax & Semantics: 25 minutes
- Logical Connectives & Truth Tables: 20 minutes
- Logical Equivalences: 20 minutes
- Inference Rules: 25 minutes
- Resolution & CNF: 20 minutes
- Practical Examples: 15 minutes

---

## 🎯 Part 1: Introduction to Logic in AI

### Slide 1: Title Slide
**Propositional Logic (Logic Mệnh Đề)**
- Introduction to Artificial Intelligence
- Week 9
- Dr. Trong-Nghia Nguyen

### Slide 2: Why Logic in AI?
**The Role of Logic:**
- Knowledge representation
- Reasoning and inference
- Decision making
- Verification and validation

**Real-world Applications:**
- Expert systems
- Automated reasoning
- Database query optimization
- Circuit design and verification
- Natural language understanding

### Slide 3: Knowledge-Based Agents
```
Knowledge Base (KB)
    ↓
TELL: Add new sentences
ASK: Query what is known
    ↓
Inference Engine
```

**Components:**
- **Knowledge Base:** Collection of sentences in formal language
- **Inference Engine:** Derives new sentences from existing ones
- **TELL:** Add facts to KB
- **ASK:** Query KB for conclusions

### Slide 4: From Search to Logic
**Search Problems vs. Logic:**
| Search | Logic |
|--------|-------|
| States and actions | Sentences and inference |
| Path finding | Proof finding |
| Goal state | Query satisfaction |
| Heuristics | Inference rules |

---

## 📝 Part 2: Syntax of Propositional Logic

### Slide 5: What is a Proposition?
**Definition:**
A proposition is a declarative sentence that is either TRUE or FALSE (but not both).

**Examples of Propositions:**
✅ "It is raining" (P)
✅ "2 + 2 = 4" (Q)
✅ "The student passed the exam" (R)

**Not Propositions:**
❌ "What time is it?" (question)
❌ "Close the door!" (command)
❌ "x + 1 = 5" (contains variable, not declarative)

### Slide 6: Atomic and Compound Propositions
**Atomic Propositions (Mệnh đề đơn):**
- Single propositional symbols: P, Q, R, S, ...
- Cannot be broken down further
- Examples: "It is raining", "I am hungry"

**Compound Propositions (Mệnh đề phức):**
- Formed by combining atomic propositions using logical connectives
- Examples: "It is raining AND I am hungry"

### Slide 7: Logical Connectives (Phép toán logic)
**Five Main Connectives:**

1. **Negation (NOT, Phủ định):** ¬P or ~P
2. **Conjunction (AND, Hội):** P ∧ Q
3. **Disjunction (OR, Tuyển):** P ∨ Q
4. **Implication (IF-THEN, Kéo theo):** P → Q or P ⇒ Q
5. **Biconditional (IF AND ONLY IF, Tương đương):** P ↔ Q or P ⇔ Q

### Slide 8: Syntax - BNF Grammar
**Backus-Naur Form:**
```
Sentence → AtomicSentence | ComplexSentence

AtomicSentence → True | False | P | Q | R | ...

ComplexSentence → (Sentence)
                | ¬Sentence
                | Sentence ∧ Sentence
                | Sentence ∨ Sentence
                | Sentence → Sentence
                | Sentence ↔ Sentence
```

**Operator Precedence (highest to lowest):**
1. ¬ (Negation)
2. ∧ (Conjunction)
3. ∨ (Disjunction)
4. → (Implication)
5. ↔ (Biconditional)

---

## 🔍 Part 3: Semantics of Propositional Logic

### Slide 9: Truth Values and Models
**Semantics defines:**
- Truth values: TRUE (T, 1) or FALSE (F, 0)
- How to determine truth value of any sentence

**Model:**
A model assigns truth values to all propositional symbols.

**Example:**
If we have P, Q, R, a model might be:
- m = {P: True, Q: False, R: True}

**Number of Models:**
- n propositional symbols → 2ⁿ possible models

### Slide 10: Truth Table - Negation (¬)
**NOT Operator:**

| P | ¬P |
|---|-----|
| T | F   |
| F | T   |

**Properties:**
- ¬¬P ≡ P (Double negation)
- Reverses truth value

### Slide 11: Truth Table - Conjunction (∧)
**AND Operator:**

| P | Q | P ∧ Q |
|---|---|-------|
| T | T | **T** |
| T | F | F     |
| F | T | F     |
| F | F | F     |

**Meaning:** True only when BOTH operands are true

**Example:**
- "It is raining AND I have an umbrella"

### Slide 12: Truth Table - Disjunction (∨)
**OR Operator (Inclusive):**

| P | Q | P ∨ Q |
|---|---|-------|
| T | T | **T** |
| T | F | **T** |
| F | T | **T** |
| F | F | F     |

**Meaning:** True when AT LEAST ONE operand is true

**Example:**
- "I will take the bus OR the train"

### Slide 13: Truth Table - Implication (→)
**IF-THEN Operator:**

| P | Q | P → Q |
|---|---|-------|
| T | T | **T** |
| T | F | F     |
| F | T | **T** |
| F | F | **T** |

**Meaning:**
- P is the **premise/antecedent** (giả thiết)
- Q is the **conclusion/consequent** (kết luận)
- False only when P is true and Q is false

**Important:** P → Q ≡ ¬P ∨ Q

**Example:**
- "If it rains, then the ground is wet"

### Slide 14: Understanding Implication
**Common Confusion:**
Why is "False → True" evaluated as True?

**Explanation:**
- Implication is a promise
- "If P then Q" is broken only when P is true but Q is false
- If P is false, the promise is vacuously true (không bị vi phạm)

**Example:**
- "If I win the lottery, I will buy you a car"
- If I don't win (P is false), I didn't break my promise regardless of whether I buy you a car

### Slide 15: Truth Table - Biconditional (↔)
**IF AND ONLY IF Operator:**

| P | Q | P ↔ Q |
|---|---|-------|
| T | T | **T** |
| T | F | F     |
| F | T | F     |
| F | F | **T** |

**Meaning:** True when P and Q have the SAME truth value

**Equivalence:** P ↔ Q ≡ (P → Q) ∧ (Q → P)

**Example:**
- "You pass the course if and only if you score ≥ 50"

### Slide 16: Complex Example
**Sentence:** (P ∨ Q) → (R ∧ ¬S)

**Truth Table:**
| P | Q | R | S | P∨Q | ¬S | R∧¬S | (P∨Q)→(R∧¬S) |
|---|---|---|---|-----|----|----- |--------------|
| T | T | T | T | T   | F  | F    | F            |
| T | T | T | F | T   | T  | T    | T            |
| T | F | T | T | T   | F  | F    | F            |
| ... (show 4-5 rows as example)

---

## 💡 Part 4: Logical Equivalences

### Slide 17: Logical Equivalence
**Definition:**
Two sentences α and β are logically equivalent (α ≡ β) if they have the same truth value in every model.

**Notation:** α ≡ β or α ⇔ β

### Slide 18: Important Equivalences - Part 1
**Fundamental Laws:**

1. **Double Negation:**
   - ¬(¬P) ≡ P

2. **Commutative Laws:**
   - P ∧ Q ≡ Q ∧ P
   - P ∨ Q ≡ Q ∨ P

3. **Associative Laws:**
   - (P ∧ Q) ∧ R ≡ P ∧ (Q ∧ R)
   - (P ∨ Q) ∨ R ≡ P ∨ (Q ∨ R)

4. **Distributive Laws:**
   - P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)
   - P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)

### Slide 19: Important Equivalences - Part 2
**De Morgan's Laws (Luật De Morgan):**
1. ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
2. ¬(P ∨ Q) ≡ ¬P ∧ ¬Q

**Example:**
- "It is not the case that it is raining AND cold"
- ≡ "It is not raining OR it is not cold"

**Memory Trick:** "Break the line, change the sign"

### Slide 20: Implication Equivalences
**Key Equivalences for Implication:**

1. **Implication Definition:**
   - P → Q ≡ ¬P ∨ Q

2. **Contrapositive:**
   - P → Q ≡ ¬Q → ¬P

3. **Biconditional:**
   - P ↔ Q ≡ (P → Q) ∧ (Q → P)
   - P ↔ Q ≡ (P ∧ Q) ∨ (¬P ∧ ¬Q)

### Slide 21: Identity and Domination Laws
**Identity Laws:**
- P ∧ True ≡ P
- P ∨ False ≡ P

**Domination Laws:**
- P ∧ False ≡ False
- P ∨ True ≡ True

**Idempotent Laws:**
- P ∧ P ≡ P
- P ∨ P ≡ P

**Absorption Laws:**
- P ∧ (P ∨ Q) ≡ P
- P ∨ (P ∧ Q) ≡ P

---

## 🔬 Part 5: Inference and Reasoning

### Slide 22: Logical Inference
**Key Concepts:**

**Entailment (Kéo theo logic):** KB ⊨ α
- Knowledge Base KB entails sentence α
- In every model where KB is true, α is also true
- α is a logical consequence of KB

**Derivation (Suy diễn):** KB ⊢ α
- α can be derived from KB using inference rules

**Sound and Complete:**
- **Sound:** If KB ⊢ α then KB ⊨ α (derives only true things)
- **Complete:** If KB ⊨ α then KB ⊢ α (can derive everything true)

### Slide 23: Model Checking
**Algorithm:**
1. Enumerate all possible models
2. Check if α is true in all models where KB is true
3. If yes, then KB ⊨ α

**Example:**
- KB = {P → Q, P}
- Query: Does KB ⊨ Q?

| P | Q | P→Q | KB | Q |
|---|---|-----|----|---|
| T | T | T   | T  | T |
| T | F | F   | F  | - |
| F | T | T   | -  | - |
| F | F | T   | -  | - |

**Result:** In the only model where KB is true (P=T, Q=T), Q is also true. Therefore, KB ⊨ Q ✓

### Slide 24: Inference Rules - Modus Ponens
**Most Important Rule:**

**Modus Ponens (Quy tắc tách):**
```
    P → Q
    P
    ------
    Q
```

**Example:**
- "If it rains, the ground is wet"
- "It is raining"
- **Therefore:** "The ground is wet"

**Application:** Forward chaining

### Slide 25: Inference Rules - Modus Tollens
**Modus Tollens (Phản chứng):**
```
    P → Q
    ¬Q
    ------
    ¬P
```

**Example:**
- "If it rains, the ground is wet"
- "The ground is not wet"
- **Therefore:** "It did not rain"

**Contrapositive form:** Uses P → Q ≡ ¬Q → ¬P

### Slide 26: More Inference Rules
**And-Elimination (Giản lược hội):**
```
    P ∧ Q
    ------
    P
```

**And-Introduction (Tổng hợp hội):**
```
    P
    Q
    ------
    P ∧ Q
```

**Or-Introduction (Tổng hợp tuyển):**
```
    P
    ------
    P ∨ Q
```

**Double-Negation Elimination:**
```
    ¬¬P
    ------
    P
```

### Slide 27: Resolution Rule
**The Universal Inference Rule:**

**Resolution:**
```
    P ∨ Q
    ¬P ∨ R
    --------
    Q ∨ R
```

**Why Important:**
- Single rule sufficient for complete inference
- Basis for automated theorem proving
- Works with clauses in CNF

**Special Cases:**

**Unit Resolution:**
```
    P ∨ Q
    ¬P
    ------
    Q
```

**Binary Resolution:**
```
    P
    ¬P
    ------
    False (contradiction)
```

---

## 🛠️ Part 6: Normal Forms and Resolution

### Slide 28: Conjunctive Normal Form (CNF)
**Definition:**
A sentence in CNF is a conjunction of clauses, where each clause is a disjunction of literals.

**Form:** (l₁ ∨ l₂ ∨ ... ∨ lₘ) ∧ (lₙ ∨ ... ∨ lₚ) ∧ ...

**Literal:** Atomic proposition or its negation (P or ¬P)
**Clause:** Disjunction of literals

**Examples:**
- CNF: (P ∨ Q) ∧ (¬P ∨ R ∨ S) ∧ (¬Q)
- Not CNF: P ∨ (Q ∧ R)

### Slide 29: Converting to CNF
**Steps to Convert any Sentence to CNF:**

1. **Eliminate biconditionals:**
   - Replace (P ↔ Q) with (P → Q) ∧ (Q → P)

2. **Eliminate implications:**
   - Replace (P → Q) with (¬P ∨ Q)

3. **Move ¬ inward (De Morgan's):**
   - Replace ¬(P ∧ Q) with (¬P ∨ ¬Q)
   - Replace ¬(P ∨ Q) with (¬P ∧ ¬Q)
   - Replace ¬¬P with P

4. **Distribute ∨ over ∧:**
   - Replace P ∨ (Q ∧ R) with (P ∨ Q) ∧ (P ∨ R)

### Slide 30: CNF Conversion Example
**Convert:** (P → Q) ↔ (¬Q → ¬P)

**Step 1 - Eliminate ↔:**
- ((P → Q) → (¬Q → ¬P)) ∧ ((¬Q → ¬P) → (P → Q))

**Step 2 - Eliminate →:**
- (¬(¬P ∨ Q) ∨ (¬¬Q ∨ ¬P)) ∧ (¬(¬¬Q ∨ ¬P) ∨ (¬P ∨ Q))

**Step 3 - Move ¬ inward:**
- ((P ∧ ¬Q) ∨ (Q ∨ ¬P)) ∧ ((¬Q ∧ P) ∨ (¬P ∨ Q))

**Step 4 - Distribute:**
- (P ∨ Q ∨ ¬P) ∧ (¬Q ∨ Q ∨ ¬P) ∧ (¬Q ∨ ¬P ∨ Q) ∧ (P ∨ ¬P ∨ Q)

**Simplify:** True (tautology)

### Slide 31: Resolution Algorithm
**Proof by Contradiction:**

**To prove KB ⊨ α:**
1. Convert KB ∧ ¬α to CNF
2. Apply resolution rule repeatedly
3. If derive empty clause (⊥), then KB ⊨ α
4. If no new clauses can be derived, then KB ⊭ α

**Pseudocode:**
```
function PL-RESOLUTION(KB, α):
    clauses = CNF(KB ∧ ¬α)
    new = {}
    
    while True:
        for each pair of clauses C₁, C₂ in clauses:
            resolvents = RESOLVE(C₁, C₂)
            
            if ⊥ ∈ resolvents:
                return True  # Proved
            
            new = new ∪ resolvents
        
        if new ⊆ clauses:
            return False  # Cannot prove
        
        clauses = clauses ∪ new
```

### Slide 32: Resolution Example
**Given:**
- KB: {P → Q, Q → R, P}
- Prove: R

**Step 1 - Add negation of goal:**
- KB ∪ {¬R}

**Step 2 - Convert to CNF:**
- {¬P ∨ Q, ¬Q ∨ R, P, ¬R}

**Step 3 - Apply resolution:**
```
1. ¬P ∨ Q      (KB)
2. P            (KB)
3. Q            (Resolve 1,2)
4. ¬Q ∨ R       (KB)
5. R            (Resolve 3,4)
6. ¬R           (negated goal)
7. ⊥            (Resolve 5,6) ✓
```

**Conclusion:** Contradiction found, therefore KB ⊨ R

---

## 🎓 Part 7: Practical Applications

### Slide 33: Wumpus World Example
**Environment:**
- Grid world with pits and Wumpus (monster)
- Agent can perceive: Breeze (near pit), Stench (near Wumpus)
- Goal: Find gold, avoid dangers

**Knowledge Representation:**
- P₁₁: There is a pit in [1,1]
- W₁₃: There is a Wumpus in [1,3]
- B₂₁: Agent feels breeze in [2,1]

**Rules:**
- B₁₁ ↔ (P₁₂ ∨ P₂₁)
- S₁₁ ↔ (W₁₂ ∨ W₂₁)

**Inference:**
If ¬B₁₁ (no breeze), then ¬P₁₂ ∧ ¬P₂₁ (no adjacent pits)

### Slide 34: Circuit Verification
**Application in Hardware:**

**Half Adder Circuit:**
```
Inputs: A, B
Outputs: Sum, Carry

Sum = (A ∨ B) ∧ ¬(A ∧ B)  # XOR
Carry = A ∧ B
```

**Verification:**
- Prove: If A=1 and B=1, then Carry=1
- Use resolution to verify circuit properties

### Slide 35: Puzzle Solving - Sudoku
**Represent Sudoku Rules:**

**Variables:**
- P_{i,j,k}: Cell (i,j) contains number k

**Constraints:**
1. **Each cell has exactly one number:**
   - (P_{i,j,1} ∨ P_{i,j,2} ∨ ... ∨ P_{i,j,9})
   - ¬P_{i,j,k} ∨ ¬P_{i,j,l} for k ≠ l

2. **Each row has each number once:**
   - Similar constraints for rows, columns, boxes

**Solve:** Use SAT solver (resolution-based)

### Slide 36: Expert Systems
**Medical Diagnosis Example:**

**Rules:**
1. If (Fever ∧ Cough) → Flu
2. If (Fever ∧ Rash) → Measles
3. If Flu → Prescribe_Rest
4. If Measles → Prescribe_Vaccine

**Facts (from patient):**
- Fever = True
- Cough = True

**Inference:**
- Using Modus Ponens: Flu = True
- Using Modus Ponens: Prescribe_Rest = True

---

## 📊 Part 8: Limitations and Extensions

### Slide 37: Limitations of Propositional Logic
**Cannot Express:**

1. **Generalizations:**
   - "All students who study hard pass the exam"
   - Need: ∀x (Student(x) ∧ StudyHard(x) → Pass(x))

2. **Relationships:**
   - "John is taller than Mary"
   - Need: Taller(John, Mary)

3. **Object properties:**
   - "Every dog has an owner"
   - Need quantifiers and predicates

**Solution:** First-Order Logic (Next lecture)

### Slide 38: Computational Complexity
**Problems:**

**Satisfiability (SAT):**
- Is there a model that satisfies a sentence?
- NP-Complete problem
- Exponential worst-case: 2ⁿ models for n symbols

**Optimizations:**
1. DPLL algorithm (Davis-Putnam-Logemann-Loveland)
2. Conflict-driven clause learning
3. Modern SAT solvers (very efficient in practice)

**Applications:**
- Model checking
- Planning
- Scheduling
- Verification

### Slide 39: From Propositional to First-Order Logic
**Extensions Needed:**

| Propositional Logic | First-Order Logic |
|---------------------|-------------------|
| True/False values | Objects, relations |
| Propositions | Predicates |
| Connectives | Connectives + Quantifiers |
| Limited expressiveness | Rich expressiveness |

**Preview of FOL:**
- Variables: x, y, z
- Quantifiers: ∀ (for all), ∃ (there exists)
- Functions: father(John)
- Predicates: Loves(John, Mary)

---

## 🧪 Part 9: Hands-on Exercises

### Slide 40: Exercise 1 - Truth Tables
**Problem:**
Construct truth table for: (P → Q) ∧ (Q → R) → (P → R)

**Solution:**
| P | Q | R | P→Q | Q→R | P→R | (P→Q)∧(Q→R) | Result |
|---|---|---|-----|-----|-----|-------------|--------|
| T | T | T | T   | T   | T   | T           | T      |
| T | T | F | T   | F   | F   | F           | T      |
| ... (complete table)

**Conclusion:** Tautology (always true) - Transitivity of implication

### Slide 41: Exercise 2 - Logical Equivalence
**Prove:** ¬(P → Q) ≡ P ∧ ¬Q

**Solution:**
```
¬(P → Q)
≡ ¬(¬P ∨ Q)         [Implication definition]
≡ ¬¬P ∧ ¬Q          [De Morgan's law]
≡ P ∧ ¬Q            [Double negation]
```

### Slide 42: Exercise 3 - CNF Conversion
**Convert to CNF:** (P ∨ Q) → (P ∧ R)

**Solution:**
```
(P ∨ Q) → (P ∧ R)
≡ ¬(P ∨ Q) ∨ (P ∧ R)           [Eliminate →]
≡ (¬P ∧ ¬Q) ∨ (P ∧ R)           [De Morgan's]
≡ ((¬P ∧ ¬Q) ∨ P) ∧ ((¬P ∧ ¬Q) ∨ R)    [Distribute ∨]
≡ ((¬P ∨ P) ∧ (¬Q ∨ P)) ∧ ((¬P ∨ R) ∧ (¬Q ∨ R))
≡ (True ∧ (¬Q ∨ P)) ∧ ((¬P ∨ R) ∧ (¬Q ∨ R))
≡ (¬Q ∨ P) ∧ (¬P ∨ R) ∧ (¬Q ∨ R)
```

**Final CNF:** (P ∨ ¬Q) ∧ (R ∨ ¬P) ∧ (R ∨ ¬Q)

### Slide 43: Exercise 4 - Resolution Proof
**Given KB:**
1. Smoke → Fire
2. Smoke
3. Fire → Alarm

**Prove:** Alarm

**Solution in CNF:**
1. ¬Smoke ∨ Fire
2. Smoke
3. ¬Fire ∨ Alarm
4. ¬Alarm (negated goal)

**Resolution steps:**
```
5. Fire            (Resolve 1,2)
6. Alarm           (Resolve 3,5)
7. ⊥               (Resolve 4,6) ✓
```

### Slide 44: Exercise 5 - Real-World Problem
**Scenario: Course Registration**

**Facts:**
- If student has prerequisite, can enroll in course
- John has completed Programming
- Programming is prerequisite for AI
- AI is prerequisite for Machine Learning

**Questions:**
1. Can John enroll in AI? (Yes)
2. Can John enroll in Machine Learning? (No, needs AI first)

**Formalization:**
- HasPrereq(John, Programming)
- Prereq(AI, Programming)
- Prereq(ML, AI)
- ∀x,y (HasPrereq(x,y) ∧ Prereq(z,y) → CanEnroll(x,z))

*Note: This requires First-Order Logic (next lecture)*

---

## 🎯 Part 10: Summary and Key Takeaways

### Slide 45: Key Concepts Summary
**Syntax:**
- Propositions, connectives, well-formed formulas
- Precedence: ¬ > ∧ > ∨ > → > ↔

**Semantics:**
- Truth values, models, truth tables
- Logical equivalence, tautology, contradiction

**Inference:**
- Entailment (⊨), derivation (⊢)
- Inference rules: Modus Ponens, Resolution
- CNF conversion and resolution algorithm

### Slide 46: Important Equivalences Cheat Sheet
```
1. ¬¬P ≡ P
2. P → Q ≡ ¬P ∨ Q
3. P → Q ≡ ¬Q → ¬P (Contrapositive)
4. ¬(P ∧ Q) ≡ ¬P ∨ ¬Q (De Morgan's)
5. ¬(P ∨ Q) ≡ ¬P ∧ ¬Q (De Morgan's)
6. P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R) (Distribution)
7. P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R) (Distribution)
```

### Slide 47: Inference Rules Summary
```
Modus Ponens:    P→Q, P ⊢ Q
Modus Tollens:   P→Q, ¬Q ⊢ ¬P
And-Elim:        P∧Q ⊢ P
And-Intro:       P, Q ⊢ P∧Q
Or-Intro:        P ⊢ P∨Q
Resolution:      P∨Q, ¬P∨R ⊢ Q∨R
```

### Slide 48: When to Use What?
**Truth Tables:**
- Small number of propositions (≤ 5)
- Checking validity/satisfiability
- Understanding operator behavior

**Logical Equivalences:**
- Simplifying expressions
- Proving equivalences
- Converting to normal forms

**Resolution:**
- Automated theorem proving
- Large knowledge bases
- Systematic proof search

### Slide 49: Common Mistakes to Avoid
❌ **Confusing → with ↔**
- P → Q does NOT mean Q → P

❌ **Incorrect De Morgan's application**
- ¬(P ∧ Q) is ¬P ∨ ¬Q, NOT ¬P ∧ ¬Q

❌ **Affirming the consequent**
- P → Q, Q ⊬ P (Invalid!)

❌ **Denying the antecedent**
- P → Q, ¬P ⊬ ¬Q (Invalid!)

✅ **Always verify with truth tables if unsure!**

### Slide 50: Practice Recommendations
**For this week:**
1. Practice truth tables for complex formulas
2. Master CNF conversion
3. Work through resolution proofs
4. Study the Wumpus World example
5. Solve exercises in AIMA Chapter 7

**Homework Assignment:**
- Posted on LMS: [Forum Discussion](https://elearning.fda.edu.vn/mod/forum/)
- Due: Before next class
- Topics: Truth tables, equivalences, CNF, resolution

---

## 📚 Part 11: Additional Resources

### Slide 51: Recommended Study Materials
**Textbook Readings:**
- AIMA Chapter 7: Logical Agents
- AIMA Chapter 8: First-Order Logic (preview)

**Online Resources:**
- [Propositional Logic Tutorial](https://www.youtube.com/watch?v=ONxr7v3HaKo&t=1894s)
- Logic calculators and proof checkers
- Practice problem sets

**Tools:**
- Truth table generators
- CNF converters
- SAT solvers (MiniSat, Z3)

### Slide 52: Preview - Next Lecture
**First-Order Logic (FOL):**
- Objects and relations
- Predicates and functions
- Universal (∀) and existential (∃) quantifiers
- Unification and resolution in FOL
- Knowledge representation with FOL

**Why FOL?**
- More expressive than propositional logic
- Can represent complex relationships
- Foundation for knowledge representation
- Used in databases (Datalog), planning, NLP

### Slide 53: Questions?
**Discussion Topics:**
- Any confusion about truth tables?
- Difficulty with CNF conversion?
- Questions about resolution algorithm?
- Real-world applications you're curious about?

**Office Hours:**
- Dr. Trong-Nghia Nguyen: nghiant@neu.edu.vn
- Dr. Nguyen Thi Kim Ngan: ngannguyen@neu.edu.vn

**Next Class:**
- Practical exercises on Propositional Logic
- Hands-on resolution proof exercises
- Introduction to First-Order Logic

---

## 🎨 Visual Aids and Diagrams

### Recommended Visuals for Slides:

1. **Knowledge-Based Agent Architecture**
   - Flow diagram: Sensors → KB → Inference → Actions

2. **Truth Table Animations**
   - Progressive building of complex truth tables
   - Color-coding for TRUE (green) and FALSE (red)

3. **CNF Conversion Process**
   - Step-by-step tree diagram
   - Before/after comparisons

4. **Resolution Proof Tree**
   - Visual representation of resolution steps
   - Highlight contradictions

5. **Wumpus World Map**
   - Grid with symbols for pits, Wumpus, gold
   - Agent's path and inferences

6. **Logical Connectives Venn Diagrams**
   - Visual representation of AND, OR operations
   - Overlapping regions for understanding

---

## 💻 Python Code Examples

### Code Example 1: Truth Table Generator
```python
def truth_table(formula, variables):
    """Generate truth table for a propositional formula"""
    import itertools
    
    print("Truth Table for:", formula)
    print("|", " | ".join(variables), "|", formula, "|")
    print("|" + "---|" * (len(variables) + 1))
    
    for values in itertools.product([True, False], repeat=len(variables)):
        env = dict(zip(variables, values))
        result = eval(formula.replace('→', '<=').replace('∧', 'and')
                            .replace('∨', 'or').replace('¬', 'not '), env)
        row = "|".join(["T" if v else "F" for v in values])
        print(f"| {row} | {'T' if result else 'F'} |")

# Example usage
truth_table("(P and Q) or (not P and R)", ['P', 'Q', 'R'])
```

### Code Example 2: Simple Resolution Prover
```python
class Clause:
    def __init__(self, literals):
        self.literals = frozenset(literals)
    
    def resolve(self, other):
        """Resolve two clauses"""
        resolvents = []
        for lit1 in self.literals:
            for lit2 in other.literals:
                if lit1 == f"¬{lit2}" or f"¬{lit1}" == lit2:
                    # Found complementary literals
                    new_clause = (self.literals - {lit1}) | (other.literals - {lit2})
                    if len(new_clause) == 0:
                        return [Clause(set())]  # Empty clause
                    resolvents.append(Clause(new_clause))
        return resolvents

def pl_resolution(kb, query):
    """Resolution-based theorem prover"""
    clauses = kb + [negate(query)]
    
    while True:
        new = set()
        pairs = [(clauses[i], clauses[j]) 
                 for i in range(len(clauses)) 
                 for j in range(i+1, len(clauses))]
        
        for c1, c2 in pairs:
            resolvents = c1.resolve(c2)
            if Clause(set()) in resolvents:
                return True  # Proved
            new.update(resolvents)
        
        if new.issubset(clauses):
            return False  # Cannot prove
        
        clauses.extend(new)
```

---

## 🎯 Learning Assessment

### Quiz Questions (for student self-assessment):

1. **What is the truth value of (False → True)?**
   - Answer: True

2. **Simplify: ¬(P ∨ ¬Q)**
   - Answer: ¬P ∧ Q

3. **Is (P → Q) ≡ (Q → P)?**
   - Answer: No (counterexample: P=T, Q=F)

4. **Convert to CNF: (P ∧ Q) → R**
   - Answer: (¬P ∨ ¬Q ∨ R)

5. **What inference rule is this: P→Q, Q→R, therefore P→R?**
   - Answer: Hypothetical syllogism (chain rule)

---

## 📖 Bilingual Terminology Reference

### English - Vietnamese Glossary:
- Proposition = Mệnh đề
- Atomic proposition = Mệnh đề đơn
- Compound proposition = Mệnh đề phức hợp
- Negation = Phủ định
- Conjunction = Hội
- Disjunction = Tuyển
- Implication = Kéo theo
- Biconditional = Tương đương
- Premise = Tiền đề / Giả thiết
- Conclusion = Kết luận
- Inference = Suy diễn / Suy luận
- Entailment = Kéo theo logic
- Tautology = Hằng đúng
- Contradiction = Hằng sai / Mâu thuẫn
- Model = Mô hình
- Satisfiable = Thỏa mãn được
- Valid = Hợp lệ
- Sound = Đúng đắn
- Complete = Đầy đủ

---

## 🔗 References and Citations

1. Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. Chapter 7: Logical Agents.

2. YouTube Tutorial: [Propositional Logic](https://www.youtube.com/watch?v=ONxr7v3HaKo&t=1894s) - Comprehensive introduction with examples.

3. Ben-Ari, M. (2012). *Mathematical Logic for Computer Science* (3rd ed.). Springer.

4. Huth, M., & Ryan, M. (2004). *Logic in Computer Science: Modelling and Reasoning about Systems*. Cambridge University Press.

5. Smullyan, R. M. (1995). *First-Order Logic*. Dover Publications.

---

**End of Lecture Content Guide**

*This document provides comprehensive content for creating lecture slides on Propositional Logic. Adjust the depth and pacing based on your students' background and available time.*

**Prepared by:** Dr. Trong-Nghia Nguyen  
**Course:** Introduction to Artificial Intelligence  
**National Economics University**

