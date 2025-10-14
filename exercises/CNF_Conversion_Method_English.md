# Converting Propositional Logic to Conjunctive Normal Form (CNF)

## Step-by-Step Method

### **Initial Expression:**
```
B₁,₁ ⟷ (P₁,₂ ∨ P₂,₁)
```

---

### **Step 1: Eliminate Biconditional (⟷)**
**Rule:** Replace α ⟷ β with (α → β) ∧ (β → α)

**Result:**
```
(B₁,₁ → (P₁,₂ ∨ P₂,₁)) ∧ ((P₁,₂ ∨ P₂,₁) → B₁,₁)
```

---

### **Step 2: Eliminate Implication (→)**
**Rule:** Replace α → β with ¬α ∨ β

**Result:**
```
(¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ (¬(P₁,₂ ∨ P₂,₁) ∨ B₁,₁)
```

---

### **Step 3: Move Negation Inward**
**Rule:** Use De Morgan's laws and double negation
- ¬(α ∨ β) = ¬α ∧ ¬β
- ¬(α ∧ β) = ¬α ∨ ¬β
- ¬¬α = α

**Result:**
```
(¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ ((¬P₁,₂ ∧ ¬P₂,₁) ∨ B₁,₁)
```

---

### **Step 4: Apply Distributive Law**
**Rule:** Distribute ∨ over ∧
- α ∨ (β ∧ γ) = (α ∨ β) ∧ (α ∨ γ)

**Result:**
```
(¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ (¬P₁,₂ ∨ B₁,₁) ∧ (¬P₂,₁ ∨ B₁,₁)
```

---

## **Final CNF Form:**
```
(¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ (¬P₁,₂ ∨ B₁,₁) ∧ (¬P₂,₁ ∨ B₁,₁)
```

---

## **General Algorithm for CNF Conversion:**

### **Step 1:** Eliminate Biconditionals
- Replace α ⟷ β with (α → β) ∧ (β → α)

### **Step 2:** Eliminate Implications  
- Replace α → β with ¬α ∨ β

### **Step 3:** Move Negation Inward
- Apply De Morgan's laws:
  - ¬(α ∨ β) = ¬α ∧ ¬β
  - ¬(α ∧ β) = ¬α ∨ ¬β
- Apply double negation: ¬¬α = α

### **Step 4:** Distribute ∨ over ∧
- Apply: α ∨ (β ∧ γ) = (α ∨ β) ∧ (α ∨ γ)

---

## **Example for Slides:**

### **CNF Conversion Algorithm**

**Input:** B₁,₁ ⟷ (P₁,₂ ∨ P₂,₁)

**Step 1:** Eliminate ⟷
```
(B₁,₁ → (P₁,₂ ∨ P₂,₁)) ∧ ((P₁,₂ ∨ P₂,₁) → B₁,₁)
```

**Step 2:** Eliminate →
```
(¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ (¬(P₁,₂ ∨ P₂,₁) ∨ B₁,₁)
```

**Step 3:** Move ¬ inward
```
(¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ ((¬P₁,₂ ∧ ¬P₂,₁) ∨ B₁,₁)
```

**Step 4:** Distribute ∨ over ∧
```
(¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ (¬P₁,₂ ∨ B₁,₁) ∧ (¬P₂,₁ ∨ B₁,₁)
```

**Output:** CNF form with 3 clauses

---

## **Key Rules Summary:**

| Original | Replace With |
|----------|--------------|
| α ⟷ β | (α → β) ∧ (β → α) |
| α → β | ¬α ∨ β |
| ¬(α ∨ β) | ¬α ∧ ¬β |
| ¬(α ∧ β) | ¬α ∨ ¬β |
| ¬¬α | α |
| α ∨ (β ∧ γ) | (α ∨ β) ∧ (α ∨ γ) |

---

## **For Slide Presentation:**

### **Converting to CNF - 4 Steps**

1. **Eliminate Biconditionals** (⟷)
   - Replace with implications

2. **Eliminate Implications** (→)  
   - Replace with disjunctions

3. **Move Negations Inward** (¬)
   - Use De Morgan's laws

4. **Distribute ∨ over ∧**
   - Apply distributive law

### **Result:** Expression in CNF = Conjunction of Disjunctions

---

## **Practical Example:**

**Wumpus World Rule:**
"If there is a breeze in (1,1), then there is a pit in (1,2) or (2,1)"

**Logical Form:** B₁,₁ ⟷ (P₁,₂ ∨ P₂,₁)

**CNF Form:** (¬B₁,₁ ∨ P₁,₂ ∨ P₂,₁) ∧ (¬P₁,₂ ∨ B₁,₁) ∧ (¬P₂,₁ ∨ B₁,₁)

**Meaning:** Three rules:
1. If no breeze at (1,1), then no pit at (1,2) and no pit at (2,1)
2. If pit at (1,2), then breeze at (1,1)  
3. If pit at (2,1), then breeze at (1,1)
