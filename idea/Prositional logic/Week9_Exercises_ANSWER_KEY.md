# Week 9 Exercises: ANSWER KEY (INSTRUCTOR ONLY)

**Course:** Introduction to Artificial Intelligence  
**Topic:** Propositional Logic - Syntax, Semantics, and CNF Conversion  
**⚠️ CONFIDENTIAL - DO NOT DISTRIBUTE TO STUDENTS**

---

## 🎯 **Part A: Syntax and Semantics (40 points)**

### **Exercise 1: Propositions and Connectives (10 points)**

**1.1** Which of the following are propositions? (5 points)

a) "It is raining today" ✅ **YES** - Declarative sentence, true/false  
b) "What is the capital of France?" ❌ **NO** - Question, not declarative  
c) "x + 5 = 10" ❌ **NO** - Contains variable, not a statement  
d) "Close the window!" ❌ **NO** - Command, not declarative  
e) "All students in this class are intelligent" ✅ **YES** - Declarative sentence, true/false

**1.2** Let P = "It is sunny", Q = "It is warm", R = "We go to the beach" (5 points)

a) "If it is sunny and warm, then we go to the beach" → **(P ∧ Q) → R**  
b) "We go to the beach if and only if it is sunny" → **R ⟷ P**  
c) "It is not the case that it is sunny or warm" → **¬(P ∨ Q)**  
d) "Either we go to the beach or it is not sunny" → **R ∨ ¬P**

---

### **Exercise 2: Truth Tables (15 points)**

**2.1** Construct truth tables (10 points)

a) (P → Q) ∧ (Q → R)

| P | Q | R | P→Q | Q→R | (P→Q)∧(Q→R) |
|---|---|---|-----|-----|--------------|
| T | T | T | T   | T   | T            |
| T | T | F | T   | F   | F            |
| T | F | T | F   | T   | F            |
| T | F | F | F   | T   | F            |
| F | T | T | T   | T   | T            |
| F | T | F | T   | F   | F            |
| F | F | T | T   | T   | T            |
| F | F | F | T   | T   | T            |

b) (P ∨ Q) → (P ∧ Q)

| P | Q | P∨Q | P∧Q | (P∨Q)→(P∧Q) |
|---|---|-----|-----|-------------|
| T | T | T   | T   | T           |
| T | F | T   | F   | F           |
| F | T | T   | F   | F           |
| F | F | F   | F   | T           |

c) ¬(P ∧ Q) ⟷ (¬P ∨ ¬Q)

| P | Q | P∧Q | ¬(P∧Q) | ¬P | ¬Q | ¬P∨¬Q | ¬(P∧Q)⟷(¬P∨¬Q) |
|---|---|-----|--------|----|----|-------|----------------|
| T | T | T   | F      | F  | F  | F     | T              |
| T | F | F   | T      | F  | T  | T     | T              |
| F | T | F   | T      | T  | F  | T     | T              |
| F | F | F   | T      | T  | T  | T     | T              |

**2.2** Classification (5 points)

a) P ∨ ¬P → **TAUTOLOGY** (always true)  
b) P ∧ ¬P → **CONTRADICTION** (always false)  
c) (P → Q) → (¬Q → ¬P) → **TAUTOLOGY** (contrapositive)  
d) P → (Q → P) → **TAUTOLOGY** (always true)

---

### **Exercise 3: Logical Equivalences (15 points)**

**3.1** Prove logical equivalences (10 points)

a) ¬(P → Q) ≡ P ∧ ¬Q

**Proof:**
```
¬(P → Q)
≡ ¬(¬P ∨ Q)           [Implication definition]
≡ ¬¬P ∧ ¬Q            [De Morgan's law]
≡ P ∧ ¬Q              [Double negation]
```

b) P → (Q → R) ≡ (P ∧ Q) → R

**Proof:**
```
P → (Q → R)
≡ ¬P ∨ (Q → R)        [Implication definition]
≡ ¬P ∨ (¬Q ∨ R)       [Implication definition]
≡ (¬P ∨ ¬Q) ∨ R       [Associativity]
≡ ¬(P ∧ Q) ∨ R        [De Morgan's law]
≡ (P ∧ Q) → R         [Implication definition]
```

c) (P → Q) ∧ (P → R) ≡ P → (Q ∧ R)

**Proof:**
```
(P → Q) ∧ (P → R)
≡ (¬P ∨ Q) ∧ (¬P ∨ R) [Implication definition]
≡ ¬P ∨ (Q ∧ R)        [Distributive law]
≡ P → (Q ∧ R)         [Implication definition]
```

**3.2** Simplify expressions (5 points)

a) ¬(¬P ∨ Q) ∧ (P ∨ ¬Q)

```
¬(¬P ∨ Q) ∧ (P ∨ ¬Q)
≡ (P ∧ ¬Q) ∧ (P ∨ ¬Q)  [De Morgan's law]
≡ P ∧ ¬Q ∧ (P ∨ ¬Q)    [Associativity]
≡ P ∧ ¬Q               [Absorption law: A ∧ (A ∨ B) ≡ A]
```

b) (P → Q) ∨ (Q → P)

```
(P → Q) ∨ (Q → P)
≡ (¬P ∨ Q) ∨ (¬Q ∨ P)  [Implication definition]
≡ ¬P ∨ Q ∨ ¬Q ∨ P      [Associativity]
≡ ¬P ∨ P ∨ Q ∨ ¬Q      [Commutativity]
≡ True ∨ True          [P ∨ ¬P ≡ True]
≡ True                 [Tautology]
```

c) ¬(P ∧ (Q ∨ ¬P))

```
¬(P ∧ (Q ∨ ¬P))
≡ ¬P ∨ ¬(Q ∨ ¬P)       [De Morgan's law]
≡ ¬P ∨ (¬Q ∧ ¬¬P)      [De Morgan's law]
≡ ¬P ∨ (¬Q ∧ P)        [Double negation]
≡ (¬P ∨ ¬Q) ∧ (¬P ∨ P) [Distributive law]
≡ (¬P ∨ ¬Q) ∧ True     [P ∨ ¬P ≡ True]
≡ ¬P ∨ ¬Q              [A ∧ True ≡ A]
≡ ¬(P ∧ Q)             [De Morgan's law]
```

---

## 🎯 **Part B: CNF Conversion (40 points)**

### **Exercise 4: CNF Conversion (25 points)**

**4.1** (P ∨ Q) → (P ∧ R) (7 points)

```
(P ∨ Q) → (P ∧ R)
≡ ¬(P ∨ Q) ∨ (P ∧ R)           [Eliminate →]
≡ (¬P ∧ ¬Q) ∨ (P ∧ R)           [De Morgan's law]
≡ ((¬P ∧ ¬Q) ∨ P) ∧ ((¬P ∧ ¬Q) ∨ R)  [Distribute ∨ over ∧]
≡ ((¬P ∨ P) ∧ (¬Q ∨ P)) ∧ ((¬P ∨ R) ∧ (¬Q ∨ R))
≡ (True ∧ (¬Q ∨ P)) ∧ ((¬P ∨ R) ∧ (¬Q ∨ R))
≡ (¬Q ∨ P) ∧ (¬P ∨ R) ∧ (¬Q ∨ R)
```

**Final CNF:** (P ∨ ¬Q) ∧ (R ∨ ¬P) ∧ (R ∨ ¬Q)

**4.2** (P → Q) ⟷ (¬Q → ¬P) (8 points)

```
(P → Q) ⟷ (¬Q → ¬P)
≡ ((P → Q) → (¬Q → ¬P)) ∧ ((¬Q → ¬P) → (P → Q))  [Eliminate ⟷]
≡ (¬(¬P ∨ Q) ∨ (¬¬Q ∨ ¬P)) ∧ (¬(¬¬Q ∨ ¬P) ∨ (¬P ∨ Q))  [Eliminate →]
≡ ((P ∧ ¬Q) ∨ (Q ∨ ¬P)) ∧ ((¬Q ∧ P) ∨ (¬P ∨ Q))  [De Morgan's and double negation]
≡ (P ∨ Q ∨ ¬P) ∧ (¬Q ∨ Q ∨ ¬P) ∧ (¬Q ∨ ¬P ∨ Q) ∧ (P ∨ ¬P ∨ Q)
≡ True ∧ True ∧ True ∧ True  [P ∨ ¬P ≡ True]
≡ True
```

**Final CNF:** True (tautology)

**4.3** ¬(P ∧ (Q → R)) (5 points)

```
¬(P ∧ (Q → R))
≡ ¬P ∨ ¬(Q → R)               [De Morgan's law]
≡ ¬P ∨ ¬(¬Q ∨ R)              [Implication definition]
≡ ¬P ∨ (Q ∧ ¬R)               [De Morgan's law and double negation]
≡ (¬P ∨ Q) ∧ (¬P ∨ ¬R)        [Distribute ∨ over ∧]
```

**Final CNF:** (Q ∨ ¬P) ∧ (¬P ∨ ¬R)

**4.4** (P ∨ Q) ∧ (P → R) ∧ (Q → S) (5 points)

```
(P ∨ Q) ∧ (P → R) ∧ (Q → S)
≡ (P ∨ Q) ∧ (¬P ∨ R) ∧ (¬Q ∨ S)  [Eliminate →]
```

**Final CNF:** (P ∨ Q) ∧ (¬P ∨ R) ∧ (¬Q ∨ S)

---

### **Exercise 5: Resolution and Inference (15 points)**

**5.1** Given: P → Q, Q → R, P. Prove R. (8 points)

**CNF Form:**
1. ¬P ∨ Q (from P → Q)
2. ¬Q ∨ R (from Q → R)  
3. P (from P)
4. ¬R (negated goal)

**Resolution Steps:**
```
5. Q      (Resolve 1,3: ¬P ∨ Q, P ⊢ Q)
6. R      (Resolve 2,5: ¬Q ∨ R, Q ⊢ R)
7. ⊥      (Resolve 4,6: ¬R, R ⊢ ⊥)
```

**Conclusion:** Contradiction found, therefore KB ⊨ R ✓

**5.2** Given: P ∨ Q, ¬P ∨ R, ¬Q ∨ S. Derive new clause. (7 points)

**Resolution Steps:**
```
1. P ∨ Q      (given)
2. ¬P ∨ R     (given)
3. ¬Q ∨ S     (given)

4. Q ∨ R      (Resolve 1,2: P ∨ Q, ¬P ∨ R ⊢ Q ∨ R)
5. R ∨ S      (Resolve 3,4: ¬Q ∨ S, Q ∨ R ⊢ R ∨ S)
```

**New clause derived:** R ∨ S

---

## 🎯 **Part C: Applications (20 points)**

### **Exercise 6: Wumpus World Logic (10 points)**

**6.1** Express the rule in propositional logic. (3 points)

**B₁,₁ → (P₁,₂ ∨ P₂,₁)**

**6.2** Convert to CNF. (4 points)

```
B₁,₁ → (P₁,₂ ∨ P₂,₁)
≡ ¬B₁,₁ ∨ (P₁,₂ ∨ P₂,₁)  [Eliminate →]
≡ ¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁    [Associativity]
```

**Final CNF:** (¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁)

**6.3** If B₁,₁ = True and ¬B₁,₂ = True, what can we conclude? (3 points)

**Given KB:**
1. ¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁ (rule)
2. B₁,₁ (observed)
3. ¬B₁,₂ (observed)

**Resolution:**
```
4. P₁,₂ ∨ P₂,₁  (Resolve 1,2: ¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁, B₁,₁ ⊢ P₁,₂ ∨ P₂,₁)
```

**Conclusion:** There must be a pit in either (1,2) or (2,1) or both.

---

### **Exercise 7: Medical Diagnosis System (10 points)**

**7.1** Express rules in propositional logic. (6 points)

- "If patient has fever and cough, then patient has flu" → **(F ∧ C) → FL**
- "If patient has flu, then patient has fever" → **FL → F**  
- "Patient has either flu or cold, but not both" → **(FL ∨ CO) ∧ ¬(FL ∧ CO)**

**7.2** If F = True and C = True, what can we conclude? (4 points)

**Given KB:**
1. (F ∧ C) → FL ≡ ¬F ∨ ¬C ∨ FL
2. FL → F ≡ ¬FL ∨ F
3. (FL ∨ CO) ∧ ¬(FL ∧ CO) ≡ (FL ∨ CO) ∧ (¬FL ∨ ¬CO)
4. F (observed)
5. C (observed)
6. ¬FL (negated goal - assume patient doesn't have flu)

**Resolution:**
```
7. ¬F ∨ ¬C ∨ FL    (from rule 1)
8. ¬FL ∨ F         (from rule 2)
9. F               (observed)
10. C              (observed)
11. ¬FL            (negated goal)

12. ¬C ∨ FL        (Resolve 7,9: ¬F ∨ ¬C ∨ FL, F ⊢ ¬C ∨ FL)
13. FL             (Resolve 10,12: C, ¬C ∨ FL ⊢ FL)
14. ⊥              (Resolve 11,13: ¬FL, FL ⊢ ⊥)
```

**Conclusion:** Contradiction found, therefore patient must have flu.

---

## 💻 **Part D: Programming Exercise (Bonus: 10 points)**

### **Exercise 8: Truth Table Generator (10 points)**

```python
import itertools

def truth_table(formula, variables):
    """
    Generate truth table for a propositional formula
    
    Args:
        formula: String representation of the formula
        variables: List of variable names
    
    Returns:
        Dictionary with truth assignments and formula values
    """
    # Parse formula and extract variables
    formula = formula.replace('→', '<=')
    formula = formula.replace('∧', 'and')
    formula = formula.replace('∨', 'or')
    formula = formula.replace('¬', 'not ')
    
    print("Truth Table for:", formula)
    print("|", " | ".join(variables), "|", "Result", "|")
    print("|" + "---|" * (len(variables) + 1))
    
    results = []
    
    for values in itertools.product([True, False], repeat=len(variables)):
        # Create environment for evaluation
        env = dict(zip(variables, values))
        
        try:
            result = eval(formula, env)
            results.append((values, result))
            
            # Format output
            row = "|".join(["T" if v else "F" for v in values])
            print(f"| {row} | {'T' if result else 'F'} |")
            
        except:
            print(f"| Error evaluating formula |")
            return None
    
    return results

# Test cases
print("=== Test 1: (P → Q) ∧ (Q → R) ===")
truth_table("(P → Q) ∧ (Q → R)", ['P', 'Q', 'R'])

print("\n=== Test 2: (P ∨ Q) → (P ∧ Q) ===")
truth_table("(P ∨ Q) → (P ∧ Q)", ['P', 'Q'])
```

**Expected Output:**
```
=== Test 1: (P → Q) ∧ (Q → R) ===
Truth Table for: (P <= Q) and (Q <= R)
| P | Q | R | Result |
|---|---|---|--------|
| T | T | T | T |
| T | T | F | F |
| T | F | T | F |
| T | F | F | F |
| F | T | T | T |
| F | T | F | F |
| F | F | T | T |
| F | F | F | T |

=== Test 2: (P ∨ Q) → (P ∧ Q) ===
Truth Table for: (P or Q) <= (P and Q)
| P | Q | Result |
|---|---|--------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |
```

---

## 📊 **Grading Rubric**

### **Part A: Syntax and Semantics (40 points)**
- **Exercise 1:** 10 points (1.1: 5 points, 1.2: 5 points)
- **Exercise 2:** 15 points (2.1: 10 points, 2.2: 5 points)  
- **Exercise 3:** 15 points (3.1: 10 points, 3.2: 5 points)

### **Part B: CNF Conversion (40 points)**
- **Exercise 4:** 25 points (4.1: 7 points, 4.2: 8 points, 4.3: 5 points, 4.4: 5 points)
- **Exercise 5:** 15 points (5.1: 8 points, 5.2: 7 points)

### **Part C: Applications (20 points)**
- **Exercise 6:** 10 points (6.1: 3 points, 6.2: 4 points, 6.3: 3 points)
- **Exercise 7:** 10 points (7.1: 6 points, 7.2: 4 points)

### **Part D: Programming (Bonus: 10 points)**
- **Exercise 8:** 10 points (correct implementation and test cases)

### **Total: 100 points + 10 bonus points**

---

## 📝 **Common Student Errors to Watch For**

1. **Implication confusion:** Students often confuse P → Q with Q → P
2. **De Morgan's mistakes:** Forgetting to change the connective (∧ to ∨, ∨ to ∧)
3. **CNF conversion errors:** Skipping steps or incorrect distribution
4. **Resolution proof mistakes:** Not properly negating the goal or missing steps
5. **Truth table errors:** Incorrect evaluation of complex formulas

---

## 🎯 **Learning Objectives Assessment**

- ✅ **Syntax/Semantics:** Can identify propositions and construct truth tables
- ✅ **Logical Equivalences:** Can apply De Morgan's laws and other equivalences  
- ✅ **CNF Conversion:** Can systematically convert any formula to CNF
- ✅ **Resolution:** Can use resolution for automated theorem proving
- ✅ **Applications:** Can apply logic to real-world problems

---

**⚠️ END OF ANSWER KEY - CONFIDENTIAL DOCUMENT**
