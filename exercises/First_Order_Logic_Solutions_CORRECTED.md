# First-Order Logic: Examples 1-5 Solutions
## From Lecture Slides "7. First-Order logic.pdf" (Pages 16-22)

---

## Example 1: Deceivers and Cheaters

**Given the knowledge base:**
1. Anyone who deceives others is considered a cheater
2. Whether intentionally or unintentionally, if anyone ever agree with someone to deceive others, you will be considered a cheater.
3. Because of being timid, there may be people who, in certain circumstances, agree with others to deceive.

**Conclusion:**
Hence, it can be inferred that not everyone who is considered a cheater is not timid.

**Step-by-Step Solution:**

### Step 1: Declaring predicates
- $deceiver(x)$: x is a person who deceives others
- $cheater(x)$: x is a cheater
- $agree(x,y)$: x agrees with y (to deceive)
- $timid(x)$: x is a timid person

### Step 2: Knowledge representation

**Premise 1:** Anyone who deceives others is considered a cheater
$$deceiver(x) \rightarrow cheater(x)$$

**Premise 2:** If anyone ever agrees with someone to deceive others, you will be considered a cheater
$$agree(x,y) \land cheater(y) \rightarrow cheater(x)$$

**Premise 3:** Because of being timid, there may be people who agree with others to deceive
$$\exists x (timid(x) \land \exists y(agree(x,y) \land deceiver(y)))$$

**Conclusion:**
$$\neg(\forall x (cheater(x) \rightarrow \neg timid(x)))$$

Which is equivalent to:
$$\exists x (cheater(x) \land timid(x))$$

### Step 3: Convert to CNF

**Premise 1:** $deceiver(x) \rightarrow cheater(x)$
$$\neg deceiver(x) \lor cheater(x)$$

**Premise 2:** $agree(x,y) \land cheater(y) \rightarrow cheater(x)$
$$\neg agree(x,y) \lor \neg cheater(y) \lor cheater(x)$$

**Premise 3:** Skolemize $\exists x (timid(x) \land \exists y(agree(x,y) \land deceiver(y)))$
- Let A be a constant for the timid person
- Let B be a constant for the person A agrees with
$$timid(A) \land agree(A,B) \land deceiver(B)$$

Split into clauses:
- $C_3$: $timid(A)$
- $C_4$: $agree(A,B)$
- $C_5$: $deceiver(B)$

**Negated Conclusion:** $\exists x (cheater(x) \land timid(x))$
$$\neg \exists x (cheater(x) \land timid(x)) = \forall x (\neg cheater(x) \lor \neg timid(x))$$

CNF form:
$$\neg cheater(x) \lor \neg timid(x)$$

### Step 4: Resolution Refutation

**Clause Set:**
- $C_1$: $\neg deceiver(x) \lor cheater(x)$
- $C_2$: $\neg agree(x,y) \lor \neg cheater(y) \lor cheater(x)$
- $C_3$: $timid(A)$
- $C_4$: $agree(A,B)$
- $C_5$: $deceiver(B)$
- $C_6$: $\neg cheater(x) \lor \neg timid(x)$ (negated conclusion)

**Resolution Steps:**

**Step 1:** Resolve $C_1$ and $C_5$
- Unify $deceiver(x)$ with $deceiver(B)$: $\sigma = \{x/B\}$
- $C_1$ becomes: $\neg deceiver(B) \lor cheater(B)$
- Resolve with $C_5$: $cheater(B)$
- $C_7$: $cheater(B)$ ✓

**Step 2:** Resolve $C_4$ and $C_2$ (with $cheater(B)$)
- Unify $agree(A,B)$ with $agree(x,y)$ and use $cheater(y)$
- With substitution $\{x/A, y/B\}$: $\neg agree(A,B) \lor \neg cheater(B) \lor cheater(A)$
- Resolve with $C_4$: $\neg cheater(B) \lor cheater(A)$
- Resolve with $C_7$: $cheater(A)$
- $C_8$: $cheater(A)$ ✓

**Step 3:** Resolve $C_3$ and $C_6$ (with $cheater(A)$)
- $C_6$ with substitution $\{x/A\}$: $\neg cheater(A) \lor \neg timid(A)$
- Resolve with $C_8$: $\neg timid(A)$
- $C_9$: $\neg timid(A)$ ✓

**Step 4:** Resolve $C_3$ and $C_9$
- $C_3$: $timid(A)$
- $C_9$: $\neg timid(A)$
- Resolve: $\square$ (empty clause - CONTRADICTION!)

### Step 5: Conclusion
Since we derived the empty clause, the negation of the conclusion is false, meaning the original conclusion is **TRUE**.

**Final Answer:**
$$\exists x (cheater(x) \land timid(x))$$

There exists a person who is both a cheater and timid.

---

## Example 2: Hung Likes Peanuts

**Given the following knowledge base:**
1. Hung likes all kinds of food.
2. Apples are food
3. Chicken is food
4. Anything that people eat and don't get harmed is food
5. Phong ate peanuts and still lived.
6. Lan eats whatever Phong eats.

**Prove:** Hung likes peanuts.

**Step-by-Step Solution:**

### Step 1: Declaring predicates and functions
- $Food(x)$: x is food
- $Likes(hung, x)$: Hung likes x
- $Ate(person, x)$: person ate x
- $Harmed(person)$: person was harmed
- Constants: $hung$, $phong$, $lan$, $apples$, $chicken$, $peanuts$

### Step 2: Knowledge representation

**Premise 1:** Hung likes all kinds of food
$$\forall x (Food(x) \rightarrow Likes(hung, x))$$

**Premise 2:** Apples are food
$$Food(apples)$$

**Premise 3:** Chicken is food
$$Food(chicken)$$

**Premise 4:** Anything that people eat and don't get harmed is food
$$\forall x \forall y (Ate(y, x) \land \neg Harmed(y) \rightarrow Food(x))$$

**Premise 5:** Phong ate peanuts and still lived (not harmed)
$$Ate(phong, peanuts) \land \neg Harmed(phong)$$

**Premise 6:** Lan eats whatever Phong eats
$$\forall x (Ate(phong, x) \rightarrow Ate(lan, x))$$

**Conclusion:** Hung likes peanuts
$$Likes(hung, peanuts)$$

### Step 3: Convert to CNF

**Premise 1:** $\forall x (Food(x) \rightarrow Likes(hung, x))$
$$\neg Food(x) \lor Likes(hung, x)$$

**Premise 2:** $Food(apples)$
$$Food(apples)$$

**Premise 3:** $Food(chicken)$
$$Food(chicken)$$

**Premise 4:** $\forall x \forall y (Ate(y, x) \land \neg Harmed(y) \rightarrow Food(x))$
$$\neg Ate(y, x) \lor Harmed(y) \lor Food(x)$$

**Premise 5:** $Ate(phong, peanuts) \land \neg Harmed(phong)$
- $C_5$: $Ate(phong, peanuts)$
- $C_6$: $\neg Harmed(phong)$

**Premise 6:** $\forall x (Ate(phong, x) \rightarrow Ate(lan, x))$
$$\neg Ate(phong, x) \lor Ate(lan, x)$$

**Negated Conclusion:** $\neg Likes(hung, peanuts)$
$$\neg Likes(hung, peanuts)$$

### Step 4: Resolution Refutation

**Clause Set:**
- $C_1$: $\neg Food(x) \lor Likes(hung, x)$
- $C_2$: $Food(apples)$
- $C_3$: $Food(chicken)$
- $C_4$: $\neg Ate(y, x) \lor Harmed(y) \lor Food(x)$
- $C_5$: $Ate(phong, peanuts)$
- $C_6$: $\neg Harmed(phong)$
- $C_7$: $\neg Ate(phong, x) \lor Ate(lan, x)$
- $C_8$: $\neg Likes(hung, peanuts)$ (negated conclusion)

**Resolution Steps:**

**Step 1:** From Premise 5 and Premise 4
- $C_4$ with substitution $\{y/phong, x/peanuts\}$: $\neg Ate(phong, peanuts) \lor Harmed(phong) \lor Food(peanuts)$
- Resolve with $C_5$: $Harmed(phong) \lor Food(peanuts)$
- Resolve with $C_6$: $Food(peanuts)$
- $C_9$: $Food(peanuts)$ ✓

**Step 2:** From Premise 1 and $Food(peanuts)$
- $C_1$ with substitution $\{x/peanuts\}$: $\neg Food(peanuts) \lor Likes(hung, peanuts)$
- Resolve with $C_9$: $Likes(hung, peanuts)$
- $C_10$: $Likes(hung, peanuts)$ ✓

**Step 3:** Resolve with negated conclusion
- $C_10$: $Likes(hung, peanuts)$
- $C_8$: $\neg Likes(hung, peanuts)$
- Resolve: $\square$ (empty clause - CONTRADICTION!)

### Step 5: Conclusion
The empty clause is derived, proving that **Hung likes peanuts** is TRUE.

**Final Answer:**
$$Likes(hung, peanuts)$$

---

## Example 3: Mrs. Binh's Cat or Dog

**Knowledge base:**
1. All dogs bark at night.
2. Anyone who has a cat has no mice in their house.
3. Anyone who has trouble sleeping does not keep any animal that barks at night.
4. Mrs. Binh has either a cat or a dog.

**Conclusion:**
If Mrs. Binh has trouble sleeping, then there are no mice in her house.

**Step-by-Step Solution:**

### Step 1: Declaring predicates
- $Has(person, animal)$: person has animal
- $Dog(x)$: x is a dog
- $Cat(x)$: x is a cat
- $BarksAtNight(x)$: x barks at night
- $HasMice(house)$: house has mice
- $TroubleSleeping(person)$: person has trouble sleeping
- Constants: $mrsBinh$, $mrsBinhHouse$

### Step 2: Knowledge representation

**Premise 1:** All dogs bark at night
$$\forall x (Dog(x) \rightarrow BarksAtNight(x))$$

**Premise 2:** Anyone who has a cat has no mice in their house
$$\forall x (Has(person, x) \land Cat(x) \rightarrow \neg HasMice(person's house))$$

Mrs. Binh's house:
$$\forall x (Has(mrsBinh, x) \land Cat(x) \rightarrow \neg HasMice(mrsBinhHouse))$$

**Premise 3:** Anyone who has trouble sleeping does not keep any animal that barks at night
$$\forall x (Has(person, x) \land BarksAtNight(x) \rightarrow \neg TroubleSleeping(person))$$

For Mrs. Binh:
$$\forall x (Has(mrsBinh, x) \land BarksAtNight(x) \rightarrow \neg TroubleSleeping(mrsBinh))$$

Or equivalently:
$$\forall x (TroubleSleeping(mrsBinh) \land Has(mrsBinh, x) \land BarksAtNight(x) \rightarrow \bot)$$

**Premise 4:** Mrs. Binh has either a cat or a dog
$$\exists x ((Has(mrsBinh, x) \land Cat(x)) \lor (Has(mrsBinh, x) \land Dog(x)))$$

**Conclusion:** If Mrs. Binh has trouble sleeping, then there are no mice in her house
$$TroubleSleeping(mrsBinh) \rightarrow \neg HasMice(mrsBinhHouse)$$

### Step 3: Convert to CNF

**Premise 1:** $\forall x (Dog(x) \rightarrow BarksAtNight(x))$
$$\neg Dog(x) \lor BarksAtNight(x)$$

**Premise 2:** $\forall x (Has(mrsBinh, x) \land Cat(x) \rightarrow \neg HasMice(mrsBinhHouse))$
$$\neg Has(mrsBinh, x) \lor \neg Cat(x) \lor \neg HasMice(mrsBinhHouse)$$

**Premise 3:** $\forall x (TroubleSleeping(mrsBinh) \land Has(mrsBinh, x) \land BarksAtNight(x) \rightarrow \bot)$
$$\neg TroubleSleeping(mrsBinh) \lor \neg Has(mrsBinh, x) \lor \neg BarksAtNight(x)$$

**Premise 4:** Skolemize (assume Mrs. Binh has animal A)
$$(Has(mrsBinh, A) \land Cat(A)) \lor (Has(mrsBinh, A) \land Dog(A))$$

Distribute:
$$(Has(mrsBinh, A) \land (Cat(A) \lor Dog(A)))$$

Clauses:
- $C_4$: $Has(mrsBinh, A)$
- $C_5$: $Cat(A) \lor Dog(A)$

**Negated Conclusion:** $TroubleSleeping(mrsBinh) \land HasMice(mrsBinhHouse)$
- $C_6$: $TroubleSleeping(mrsBinh)$
- $C_7$: $HasMice(mrsBinhHouse)$

### Step 4: Resolution Refutation

**Clause Set:**
- $C_1$: $\neg Dog(x) \lor BarksAtNight(x)$
- $C_2$: $\neg Has(mrsBinh, x) \lor \neg Cat(x) \lor \neg HasMice(mrsBinhHouse)$
- $C_3$: $\neg TroubleSleeping(mrsBinh) \lor \neg Has(mrsBinh, x) \lor \neg BarksAtNight(x)$
- $C_4$: $Has(mrsBinh, A)$
- $C_5$: $Cat(A) \lor Dog(A)$
- $C_6$: $TroubleSleeping(mrsBinh)$
- $C_7$: $HasMice(mrsBinhHouse)$

**Resolution Steps:**

**Step 1:** From $C_5$ (Mrs. Binh has either cat or dog)
We need to split into two cases, but resolution handles this automatically.

**Case 1: Assume $Cat(A)$**
- Add $C_8$: $Cat(A)$

**Step 2:** Resolve $C_2$ and $C_4$
- With substitution $\{x/A\}$: $\neg Has(mrsBinh, A) \lor \neg Cat(A) \lor \neg HasMice(mrsBinhHouse)$
- Resolve with $C_4$: $\neg Cat(A) \lor \neg HasMice(mrsBinhHouse)$
- Resolve with $C_8$: $\neg HasMice(mrsBinhHouse)$
- $C_9$: $\neg HasMice(mrsBinhHouse)$ ✓

**Step 3:** Resolve $C_7$ and $C_9$
- $C_7$: $HasMice(mrsBinhHouse)$
- $C_9$: $\neg HasMice(mrsBinhHouse)$
- Resolve: $\square$ (empty clause - CONTRADICTION!)

### Step 5: Conclusion
The empty clause is derived, proving that if Mrs. Binh has trouble sleeping, then she has no mice in her house.

**Final Answer:**
$$TroubleSleeping(mrsBinh) \rightarrow \neg HasMice(mrsBinhHouse)$$

---

## Example 4: John and His Dog

**Given the following statements:**
1. John owns a dog.
2. All people who own dogs are animal lovers.
3. Animal lovers do not kill animals.

**Prove:** John does not kill animals.

**Step-by-Step Solution:**

### Step 1: Declaring predicates
- $Owns(person, animal)$: person owns animal
- $Dog(x)$: x is a dog
- $AnimalLover(person)$: person is an animal lover
- $Kills(person, animal)$: person kills animal
- Constants: $john$

### Step 2: Knowledge representation

**Premise 1:** John owns a dog
$$\exists x (Dog(x) \land Owns(john, x))$$

Skolemize: Let $dog_1$ be John's dog
$$Dog(dog_1) \land Owns(john, dog_1)$$

**Premise 2:** All people who own dogs are animal lovers
$$\forall x (Owns(person, x) \land Dog(x) \rightarrow AnimalLover(person))$$

**Premise 3:** Animal lovers do not kill animals
$$\forall x \forall y (AnimalLover(x) \land Animal(y) \rightarrow \neg Kills(x, y))$$

**Conclusion:** John does not kill animals
$$\forall y (Animal(y) \rightarrow \neg Kills(john, y))$$

### Step 3: Convert to CNF

**Premise 1:**
- $C_1$: $Dog(dog_1)$
- $C_2$: $Owns(john, dog_1)$

**Premise 2:** $\forall x (Owns(person, x) \land Dog(x) \rightarrow AnimalLover(person))$
$$\neg Owns(person, x) \lor \neg Dog(x) \lor AnimalLover(person)$$

**Premise 3:** $\forall x \forall y (AnimalLover(x) \land Animal(y) \rightarrow \neg Kills(x, y))$
$$\neg AnimalLover(x) \lor \neg Animal(y) \lor \neg Kills(x, y)$$

**Negated Conclusion:** $\exists y (Animal(y) \land Kills(john, y))$
Skolemize: Let $victim$ be an animal John kills
- $C_3$: $Animal(victim)$
- $C_4$: $Kills(john, victim)$

### Step 4: Resolution Refutation

**Clause Set:**
- $C_1$: $Dog(dog_1)$
- $C_2$: $Owns(john, dog_1)$
- $C_3$: $Animal(victim)$
- $C_4$: $Kills(john, victim)$
- $C_5$: $\neg Owns(person, x) \lor \neg Dog(x) \lor AnimalLover(person)$
- $C_6$: $\neg AnimalLover(x) \lor \neg Animal(y) \lor \neg Kills(x, y)$

**Resolution Steps:**

**Step 1:** From Premise 1 and Premise 2 (John is an animal lover)
- $C_5$ with substitution $\{person/john, x/dog_1\}$: 
  $\neg Owns(john, dog_1) \lor \neg Dog(dog_1) \lor AnimalLover(john)$
- Resolve with $C_2$: $\neg Dog(dog_1) \lor AnimalLover(john)$
- Resolve with $C_1$: $AnimalLover(john)$
- $C_7$: $AnimalLover(john)$ ✓

**Step 2:** From Premise 3
- $C_6$ with substitution $\{x/john, y/victim\}$:
  $\neg AnimalLover(john) \lor \neg Animal(victim) \lor \neg Kills(john, victim)$
- Resolve with $C_7$: $\neg Animal(victim) \lor \neg Kills(john, victim)$
- Resolve with $C_3$: $\neg Kills(john, victim)$
- $C_8$: $\neg Kills(john, victim)$ ✓

**Step 3:** Resolve with negated conclusion
- $C_8$: $\neg Kills(john, victim)$
- $C_4$: $Kills(john, victim)$
- Resolve: $\square$ (empty clause - CONTRADICTION!)

### Step 5: Conclusion
The empty clause is derived, proving that John does not kill animals.

**Final Answer:**
$$\forall y (Animal(y) \rightarrow \neg Kills(john, y))$$

---

## Example 5: Thuy's and An's Hair

**Given:**
1. Thuy is a girl.
2. An is a boy.
3. Girls have longer hair than boys.

**Prove:** Thuy's hair is longer than An's hair.

**Step-by-Step Solution:**

### Step 1: Declaring predicates
- $Girl(x)$: x is a girl
- $Boy(x)$: x is a boy
- $LongerHairThan(person1, person2)$: person1's hair is longer than person2's hair
- Constants: $thuy$, $an$

### Step 2: Knowledge representation

**Premise 1:** Thuy is a girl
$$Girl(thuy)$$

**Premise 2:** An is a boy
$$Boy(an)$$

**Premise 3:** Girls have longer hair than boys
$$\forall x \forall y (Girl(x) \land Boy(y) \rightarrow LongerHairThan(x, y))$$

**Conclusion:** Thuy's hair is longer than An's hair
$$LongerHairThan(thuy, an)$$

### Step 3: Convert to CNF

**Premise 1:**
- $C_1$: $Girl(thuy)$

**Premise 2:**
- $C_2$: $Boy(an)$

**Premise 3:** $\forall x \forall y (Girl(x) \land Boy(y) \rightarrow LongerHairThan(x, y))$
$$\neg Girl(x) \lor \neg Boy(y) \lor LongerHairThan(x , y)$$

**Negated Conclusion:**
$$\neg LongerHairThan(thuy, an)$$

### Step 4: Resolution Refutation

**Clause Set:**
- $C_1$: $Girl(thuy)$
- $C_2$: $Boy(an)$
- $C_3$: $\neg Girl(x) \lor \neg Boy(y) \lor LongerHairThan(x, y)$
- $C_4$: $\neg LongerHairThan(thuy, an)$ (negated conclusion)

**Resolution Steps:**

**Step 1:** From Premise 3 with Thuy and An
- $C_3$ with substitution $\{x/thuy, y/an\}$:
  $\neg Girl(thuy) \lor \neg Boy(an) \lor LongerHairThan(thuy, an)$
- Resolve with $C_1$: $\neg Boy(an) \lor LongerHairThan(thuy, an)$
- Resolve with $C_2$: $LongerHairThan(thuy, an)$
- $C_5$: $LongerHairThan(thuy, an)$ ✓

**Step 2:** Resolve with negated conclusion
- $C_5$: $LongerHairThan(thuy, an)$
- $C_4$: $\neg LongerHairThan(thuy, an)$
- Resolve: $\square$ (empty clause - CONTRADICTION!)

### Step 5: Conclusion
The empty clause is derived, proving that Thuy's hair is longer than An's hair.

**Final Answer:**
$$LongerHairThan(thuy, an)$$

---

## Summary of Resolution Refutation Method

### Key Steps:
1. **Translate** natural language to First-Order Logic
2. **Convert to CNF**: Eliminate implications, move negations, Skolemize
3. **Negate** the conclusion to be proven
4. **Apply Resolution**: Unify complementary literals and resolve
5. **Derive empty clause** (□) to prove the conclusion

### Important Notes:
- **Skolemization** replaces existential quantifiers with constants or functions
- **Unification** finds substitutions to make terms identical
- **Resolution** combines clauses by eliminating complementary literals
- **Empty clause** (□) indicates contradiction, proving the conclusion true
- **Variable renaming** is crucial to avoid conflicts during resolution

---

*Generated for First-Order Logic Lecture - Week 11*
