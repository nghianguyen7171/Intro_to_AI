# First-Order Logic: Examples 1-5 Solutions
## From Lecture Slides (Pages 16-22)

---

## Example 1: Converting to Prenex Normal Form

**Problem Statement:**
Convert the following formula to Prenex Normal Form (PNF):
$$\exists x \forall y P(x,y) \rightarrow \forall y \exists x Q(x,y)$$

**Step-by-Step Solution:**

### Step 1: Identify the structure
The formula has the form: $\phi \rightarrow \psi$ where:
- $\phi = \exists x \forall y P(x,y)$
- $\psi = \forall y \exists x Q(x,y)$

### Step 2: Eliminate implications
$$\neg(\exists x \forall y P(x,y)) \lor (\forall y \exists x Q(x,y))$$

### Step 3: Negate the quantifiers in the left part
Using De Morgan's laws: $\neg \exists x \phi(x) \equiv \forall x \neg \phi(x)$
$$\forall x \neg(\forall y P(x,y)) \lor (\forall y \exists x Q(x,y))$$

$$\forall x \exists y \neg P(x,y) \lor (\forall y \exists x Q(x,y))$$

### Step 4: Rename variables to avoid conflicts
Rename $y$ in the second part to $z$:
$$\forall x \exists y \neg P(x,y) \lor (\forall z \exists x Q(x,z))$$

### Step 5: Move quantifiers to the front
Apply distributive laws:
$$\forall x \exists y \forall z \exists x (\neg P(x,y) \lor Q(x,z))$$

### Step 6: Rename the second $x$ to avoid conflict
$$\forall x \exists y \forall z \exists w (\neg P(x,y) \lor Q(w,z))$$

**Final Answer:**
$$\forall x \exists y \forall z \exists w (\neg P(x,y) \lor Q(w,z))$$

---

## Example 2: Skolemization

**Problem Statement:**
Apply Skolemization to:
$$\forall x \exists y \forall z \exists w P(x,y,z,w)$$

**Step-by-Step Solution:**

### Step 1: Identify existential quantifiers
The existential quantifiers are:
- $\exists y$ (depends on $x$)
- $\exists w$ (depends on $x, z$)

### Step 2: Replace with Skolem functions
- Replace $\exists y$ with a function $f(x)$
- Replace $\exists w$ with a function $g(x,z)$

### Step 3: Remove existential quantifiers
$$\forall x \forall z P(x, f(x), z, g(x,z))$$

**Final Answer:**
$$\forall x \forall z P(x, f(x), z, g(x,z))$$

Where $f$ and $g$ are new Skolem functions.

---

## Example 3: Converting to CNF with Herbrand Base

**Problem Statement:**
Convert to CNF and find the Herbrand Universe:
$$\forall x (\exists y P(x,y) \land \forall z Q(x,z))$$

**Step-by-Step Solution:**

### Part A: Convert to CNF

#### Step 1: Skolemize
- Replace $\exists y$ with Skolem function $f(x)$
$$\forall x (P(x, f(x)) \land \forall z Q(x,z))$$

#### Step 2: Move universal quantifiers to front
$$\forall x \forall z (P(x, f(x)) \land Q(x,z))$$

#### Step 3: In CNF form (already a conjunction of literals)
This is already in CNF as it's a conjunction.

### Part B: Herbrand Universe

#### Step 1: Identify constants and functions
- Constants: None specified (add a default constant $a$)
- Functions: $f(x)$

#### Step 2: Build Herbrand Universe
- Level 0: $H_0 = \{a\}$
- Level 1: $H_1 = \{a, f(a)\}$
- Level 2: $H_2 = \{a, f(a), f(f(a))\}$
- And so on...

#### Step 3: Herbrand Universe
$$H = \{a, f(a), f(f(a)), f(f(f(a))), \ldots\}$$

### Part C: Herbrand Base

#### List all ground atomic formulas possible:
1. $P(a, a)$
2. $P(a, f(a))$
3. $P(f(a), a)$
4. $P(f(a), f(a))$
5. $P(f(f(a)), a)$
6. $P(f(f(a)), f(a))$
7. $Q(a, a)$
8. $Q(a, f(a))$
9. $Q(f(a), a)$
10. $Q(f(a), f(a))$
... and so on.

**Final Answers:**
- CNF: $\forall x \forall z (P(x, f(x)) \land Q(x,z))$
- Herbrand Universe: $H = \{a, f(a), f(f(a)), f(f(f(a))), \ldots\}$
- Herbrand Base: All ground instances of $P$ and $Q$

---

## Example 4: Resolution in First-Order Logic

**Problem Statement:**
Prove using resolution:
- Premises:
  - $\forall x (Bird(x) \rightarrow Fly(x))$
  - $Bird(Tweety)$
- Conclusion:
  - $Fly(Tweety)$

**Step-by-Step Solution:**

### Step 1: Convert to CNF

#### Premise 1: $\forall x (Bird(x) \rightarrow Fly(x))$
Eliminate implication:
$$\forall x (\neg Bird(x) \lor Fly(x))$$
CNF: $\neg Bird(x) \lor Fly(x)$

#### Premise 2: $Bird(Tweety)$
CNF: $Bird(Tweety)$

#### Negated Conclusion: $\neg Fly(Tweety)$
CNF: $\neg Fly(Tweety)$

### Step 2: Create clause set
$C_1$: $\neg Bird(x) \lor Fly(x)$
$C_2$: $Bird(Tweety)$
$C_3$: $\neg Fly(Tweety)$

### Step 3: Apply resolution

#### Resolve $C_1$ and $C_2$:
- Unify $\neg Bird(x)$ with $Bird(Tweety)$: substitution $\sigma = \{x/Tweety\}$
- Apply substitution: $\neg Bird(Tweety) \lor Fly(Tweety)$
- Resolve with $C_2$: $Fly(Tweety)$

#### Resolve with $C_3$:
- Resolve $Fly(Tweety)$ with $\neg Fly(Tweety)$
- Result: $\square$ (empty clause - CONTRADICTION)

### Step 4: Conclusion
Since we derived an empty clause, the original conclusion must be true.

**Final Answer:**
$Fly(Tweety)$ is proven by resolution refutation.

---

## Example 5: Unification

**Problem Statement:**
Find the Most General Unifier (MGU) for:
1. $P(x, f(y), z)$ and $P(a, f(b), a)$
2. $Q(f(x), y)$ and $Q(y, f(a))$

**Step-by-Step Solution:**

### Part A: Unify $P(x, f(y), z)$ and $P(a, f(b), a)$

#### Step 1: Check arity
Both have 3 arguments - proceed.

#### Step 2: Apply unification algorithm

Initialize: $\sigma = \{\}$

Process each position:

1. Position 1: $x$ and $a$
   - Variable $x$ can bind to $a$
   - $\sigma = \{x/a\}$

2. Position 2: $f(y)$ and $f(b)$
   - Both are functions with same name
   - Unify arguments: $y$ and $b$
   - $\sigma = \{x/a, y/b\}$

3. Position 3: $z$ and $a$
   - Variable $z$ can bind to $a$
   - $\sigma = \{x/a, y/b, z/a\}$

Apply substitution to check:
- $P(x, f(y), z)\sigma = P(a, f(b), a)$ ✓
- $P(a, f(b), a)\sigma = P(a, f(b), a)$ ✓

**MGU for Part A:** $\{x/a, y/b, z/a\}$

### Part B: Unify $Q(f(x), y)$ and $Q(y, f(a))$

#### Step 1: Check arity
Both sheet have 2 arguments - proceed.

#### Step 2: Apply unification algorithm

Initialize: $\sigma = \{\}$

Process each position:

1. Position 1: $f(x)$ and $y$
   - Variable $y$ occurs in both (check occurs check)
   - $y = f(x)$ is acceptable
   - $\sigma = \{y/f(x)\}$

2. Position 2: $y\sigma = f(x)$ and $f(a)$
   - Both are functions with same name
   - Unify arguments: $x$ and $a$
   - $\sigma = \{y/f(x\)), x/a\}$

Apply substitution to check:
- $Q(f(x), y)\sigma = Q(f(a), f(a))$ ✓
- $Q(y, f(a))\sigma = Q(f(a), f(a))$ ✓

**MGU for Part B:** $\{x/a, y/f(a)\}$

### Part C: Note on occurs check
In Part B, we had $y = f(x)$. This is valid because:
- $y$ doesn't occur in $f(x)$ itself (no circular binding)
- If we had attempted to unify $x$ with $f(x)$, it would fail the occurs check

**Final Answers:**
1. MGU: $\{x/a, y/b, z/a\}$
2. MGU: $\{x/a, y/f(a)\}$

---

## Summary of Key Concepts

### 1. Prenex Normal Form (PNF)
- All quantifiers are at the beginning
- Scope extends to the end of formula
- No quantifiers in the body

### 2. Skolemization
- Replace $\exists x$ with a Skolem function depending on preceding universals
- Ensure satisfiability is preserved

### 3. Herbrand Universe
- Set of all ground terms
- Built from constants and function symbols
- Infinite if functions exist

### 4. Resolution
- Unify complementary literals
- Resolve to produce new clauses
- Empty clause (□) means contradiction

### 5. Unification
- Find substitution making two terms identical
- MGU is most general
- Check occurs condition to avoid circular bindings

---

*Generated for First-Order Logic Lecture - Week 11*

