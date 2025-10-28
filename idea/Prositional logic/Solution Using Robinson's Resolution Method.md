# Solution Using Robinson's Resolution Method

## Problem Statement

Prove that w and b are true from the given 9 premises.

## Part 1: Proving b = TRUE

### Step 0: Add ¬b to the premise set

Assume b is false, add ¬b to the premise set G.

### Step 1: Normalize to Conjunctive Normal Form (CNF)

**Original premises:**

1. v ⇒ w
2. (d ∧ m ∧ b) ⇒ w
3. u ⇒ (v ∨ ¬f)
4. (b ∧ c ∧ a) ⇒ v
5. (u ∧ e) ⇒ (¬m ∨ a)
6. e ⇒ (f ∧ m)
7. (e ∧ f) ⇒ u
8. ((c ∨ e) ⇒ b) ∧ e
9. b ⇒ (d ⇒ a)

**CNF converted forms:**

1. ¬v ∨ w
2. ¬d ∨ ¬m ∨ ¬b ∨ w
3. ¬u ∨ v ∨ ¬f
4. ¬b ∨ ¬c ∨ ¬a ∨ v
5. ¬u ∨ ¬e ∨ ¬m ∨ a
6. (¬e ∨ f) ∧ (¬e ∨ m)
7. ¬e ∨ ¬f ∨ u
8. (¬c ∨ b) ∧ (¬e ∨ b) ∧ e
9. ¬b ∨ ¬d ∨ a

### Step 2: Split into sub-clauses

**Clause set G:**

- **C1:** ¬v ∨ w
- **C2:** ¬d ∨ ¬m ∨ ¬b ∨ w
- **C3:** ¬u ∨ v ∨ ¬f
- **C4:** ¬b ∨ ¬c ∨ ¬a ∨ v
- **C5:** ¬u ∨ ¬e ∨ ¬m ∨ a
- **C6a:** ¬e ∨ f
- **C6b:** ¬e ∨ m
- **C7:** ¬e ∨ ¬f ∨ u
- **C8a:** ¬c ∨ b
- **C8b:** ¬e ∨ b
- **C8c:** e (fact from premise 8)
- **C9:** ¬b ∨ ¬d ∨ a
- **C10:** ¬b (negated conclusion - proof by contradiction)

### Step 3: Resolution process

**Iteration 1:** Select clauses C8c and C8b (flexible selection mechanism)

- C8c: e
- C8b: ¬e ∨ b
- **Res(C8c, C8b) = C11: b** ✓ (new clause generated)

**Iteration 2:** Select clauses C11 and C10

- C11: b
- C10: ¬b
- **Res(C11, C10) = ⊥** (empty clause - CONTRADICTION!)

### Conclusion for Part 1

**Contradiction derived ⇒ b = TRUE**

## Part 2: Proving w = TRUE

### Step 0: Add ¬w to the premise set

Assume w is false, add ¬w to premise set G (keep original 9 premises).

### Step 1 & 2: Clause set G (as above)

- C1 through C9 remain the same
- **C10:** ¬w (negated conclusion - proof by contradiction)

### Step 3: Resolution process

**Iteration 1:** Select C8c and C6a

- C8c: e
- C6a: ¬e ∨ f
- **Res(C8c, C6a) = C11: f** ✓

**Iteration 2:** Select C8c and C7

- C8c: e
- C7: ¬e ∨ ¬f ∨ u
- **Res(C8c, C7) = C12: ¬f ∨ u** ✓

**Iteration 3:** Select C11 and C12

- C11: f
- C12: ¬f ∨ u
- **Res(C11, C12) = C13: u** ✓

**Iteration 4:** Select C13 and C3

- C13: u
- C3: ¬u ∨ v ∨ ¬f
- **Res(C13, C3) = C14: v ∨ ¬f** ✓

**Iteration 5:** Select C11 and C14

- C11: f
- C14: v ∨ ¬f
- **Res(C11, C14) = C15: v** ✓

**Iteration 6:** Select C15 and C1

- C15: v
- C1: ¬v ∨ w
- **Res(C15, C1) = C16: w** ✓

**Iteration 7:** Select C16 and C10

- C16: w
- C10: ¬w
- **Res(C16, C10) = ⊥** (empty clause - CONTRADICTION!)

### Conclusion for Part 2

✅ **Contradiction derived ⇒ w = TRUE**

## Final Conclusion

Following Robinson's Resolution Method procedure from the lecture slides:

- **Step 0:** Add ¬c to G ✓
- **Step 1:** Normalize to CNF ✓
- **Step 2:** Split into clauses ✓
- **Step 3:** Iterate resolution until empty clause is derived ✓

**Results:**

- ✅ **b = TRUE** (2 resolution steps)
- ✅ **w = TRUE** (7 resolution steps)

**Logical inference chain:**
e (fact) → f → u → v → **w** ✓
e (fact) → **b** ✓

Both conclusions are successfully proven using Robinson's refutation method with arbitrary flexible clause selection.