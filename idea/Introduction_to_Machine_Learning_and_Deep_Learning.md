# Introduction to Machine Learning and Deep Learning
## Lecture Content for Weeks 13-15

**Course:** Introduction to Artificial Intelligence  
**Weeks:** 13-15  
**Instructors:** Dr. Trong-Nghia Nguyen & Dr. Nguyen Thi Kim Ngan

---

## Slide 1: Title Slide

**Title:** Introduction to Machine Learning and Deep Learning  
**Subtitle:** From Search Algorithms and Logic to Learning Systems  
**Date:** Week 13-15

**What We've Learned So Far:**
- ✅ **Search Algorithms:** BFS, DFS, A*, Greedy Search
- ✅ **Propositional Logic:** Knowledge representation, inference, resolution
- ✅ **First-Order Logic:** Predicates, quantifiers, CNF conversion, resolution refutation

**What's Next:**
- 🎯 **Machine Learning:** Learning from data
- 🎯 **Deep Learning:** Neural networks for complex pattern recognition

---

## Slide 2: Motivation: A Problem That Breaks Our Tools

### Review: What Have We Mastered?

**Search Algorithms** (Weeks 1-4):
- ✅ **8-Puzzle:** Solved with A* search using Manhattan distance heuristic
- ✅ **Missionaries and Cannibals:** BFS found optimal path
- ✅ **Chess/Game Playing:** Minimax with alpha-beta pruning
- **Key:** Well-defined state spaces, clear goals, computable heuristics

**Logic Systems** (Weeks 5-12):
- ✅ **Propositional Logic:** "If it rains, then the ground is wet"
- ✅ **First-Order Logic:** "All dogs bark" → "John's dog barks"
- **Key:** Explicit rules, logical inference, resolution refutation

---

### New Problem: Image Recognition - "What is in this picture?"

**Specific Example:**
- **Task:** Identify whether an image contains a cat or a dog
- **Input:** Digital image (e.g., 256×256 pixels, RGB color)
- **Output:** Classification label: "cat" or "dog"

**Why Can't We Use Search Algorithms?**

**Attempt 1: State Space Search**
- **State:** Each possible image configuration
- **Problem:** 256 × 256 × 3 = 196,608 pixels
- **Each pixel:** 256³ possible color values
- **Total states:** (256³)^196,608 ≈ 10^1,420,000 states
- **Our experience:** Even 8-puzzle has only 9! = 362,880 states
- **Result:** ❌ State space explosion makes exhaustive search impossible

**Attempt 2: Heuristic Search (A*)**
- **Question:** What's the heuristic function h(n)?
- **Need:** Distance estimate from current image to "cat" or "dog"
- **Problem:** How do we measure "distance to cat"?
- **Our experience:** Manhattan distance worked perfectly for 8-puzzle
- **Result:** ❌ No meaningful heuristic function exists

**Attempt 3: Greedy Search**
- **Need:** Clear evaluation function
- **Problem:** What makes an image "more cat-like"?
- **Result:** ❌ Cannot define evaluation function

---

### Why Can't We Use Logic?

**Attempt 1: Propositional Logic**
- **Try:** "If pixel (100,100) is brown, then it's a dog"
- **Problem:** Millions of pixels, billions of combinations
- **Result:** ❌ Too many rules, many exceptions

**Attempt 2: First-Order Logic**
- **Try:** "∀x (has_fur(x) ∧ has_tail(x) → cat(x))"
- **Problem:** What is "has_fur"? How do we detect it?
- **Challenge:** Cannot define predicates for visual features
- **Result:** ❌ Visual features are not logically definable

**Why Logic Fails:**
- ❌ **No explicit rules:** Cannot write "If pixels form ears, then cat"
- ❌ **Context-dependent:** Same pixel pattern means different things
- ❌ **Pattern recognition:** Requires learning from examples, not deduction

---

### The Fundamental Challenge

**What We Need:**
- Learn patterns from examples (not rules)
- Generalize to new, unseen images
- Handle high-dimensional, complex inputs
- Adapt and improve with experience

**What We Have:**
- ✅ Search algorithms: Great for structured problems
- ✅ Logic systems: Great for rule-based reasoning
- ❌ Neither works for pattern recognition!

**Solution:** We need **Machine Learning** — systems that learn from data!

---

### Connecting to Our Journey

**Traditional AI (Weeks 1-12):**
```
Problem → Define Rules → Apply Search/Logic → Solution
```

**Machine Learning (Weeks 13-15):**
```
Problem → Provide Examples → Learn Patterns → Solution
```

**The Image Recognition Example demonstrates:**
- Why we need a new paradigm
- The limitations of rule-based approaches
- The transition from "programming" to "learning"

---

## Slide 3: Transition to Machine Learning

**The Necessity of Machine Learning:**

**What We've Learned Works Well:**
- ✅ **Search Algorithms:** 8-puzzle, pathfinding, game trees
  - Well-defined problems with clear rules
  - Problems with manageable state spaces
  - Deterministic environments with clear goals
  
- ✅ **Logic Systems:** Knowledge representation, inference
  - Explicit rules and logical relationships
  - Deductive reasoning from premises
  - Structured knowledge bases

**But Real-World Problems Are Different:**

The **image recognition example** showed us that many problems require:
- ❌ **Learning from experience:** Not predefined rules
- ❌ **Pattern recognition:** High-dimensional, noisy data
- ❌ **Handling uncertainty:** No deterministic rules
- ❌ **Adapting to new situations:** Generalizing from examples

**The Gap:**
```
Traditional AI (Search + Logic) ≠ Pattern Recognition Problems
```

**Machine Learning bridges this gap** by enabling computers to:
- Learn patterns from data automatically
- Generalize to new examples
- Handle uncertainty and noise
- Adapt without explicit reprogramming

**Our Journey Continues:**
- **Weeks 1-12:** "How to solve problems with explicit rules"
- **Weeks 13-15:** "How to learn from examples when rules don't exist"

---

## Slide 4: AI and Machine Learning
*Based on Slide 10 from "AI va Con nguoi - NEU.pdf"*

### Definition of Machine Learning

**Formal Definition:**
> "Machine Learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention."

**Key Characteristics:**
- **Learning from Experience:** Improves performance on a task with experience
- **Pattern Recognition:** Discovers patterns in data automatically
- **Generalization:** Makes predictions on new, unseen data
- **Adaptation:** Adjusts behavior based on feedback

### Machine Learning Paradigms

#### 1. Supervised Learning
- **Definition:** Learning with labeled examples
- **Input:** Labeled training data {(x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ)}
- **Goal:** Learn a function f: X → Y that maps inputs to outputs
- **Examples:**
  - **Classification:** Spam detection (input: email, output: spam/not spam)
  - **Regression:** House price prediction (input: features, output: price)

#### 2. Unsupervised Learning
- **Definition:** Learning from unlabeled data
- **Input:** Unlabeled data {x₁, x₂, ..., xₙ}
- **Goal:** Discover hidden patterns or structures
- **Examples:**
  - **Clustering:** Customer segmentation
  - **Dimensionality Reduction:** Data visualization

#### 3. Reinforcement Learning
- **Definition:** Learning through interaction with environment
- **Components:** Agent, Environment, Actions, Rewards
- **Goal:** Learn optimal policy to maximize cumulative reward
- **Examples:**
  - Game playing (Chess, Go)
  - Autonomous vehicle control
  - Robot navigation

### Applications of Machine Learning

1. **Computer Vision**
   - Image classification
   - Object detection
   - Facial recognition

2. **Natural Language Processing**
   - Machine translation
   - Sentiment analysis
   - Chatbots

3. **Healthcare**
   - Medical diagnosis
   - Drug discovery
   - Personalized treatment

4. **Finance**
   - Fraud detection
   - Credit scoring
   - Algorithmic trading

5. **Recommendation Systems**
   - E-commerce (Amazon, eBay)
   - Streaming services (Netflix, Spotify)
   - Social media (Facebook, LinkedIn)

---

## Slide 5: From Machine Learning to Deep Learning

### The Relationship

**Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence**

Deep Learning is a **subset** of Machine Learning that uses neural networks with multiple layers.

### Why Deep Learning Emerged?

**Limitations of Traditional Machine Learning:**
- ❌ **Manual Feature Engineering:** Experts must hand-craft features
- ❌ **Limited Complexity:** Struggles with high-dimensional data (images, audio)
- ❌ **Shallow Representations:** Cannot learn hierarchical features automatically
- ❌ **Performance Plateau:** Hit accuracy limits on complex tasks

**Example:** Image recognition with traditional ML required experts to define features like "edges," "corners," "textures" manually.

**What Deep Learning Offers:**
- ✅ **Automatic Feature Learning:** Discovers features from raw data
- ✅ **Hierarchical Representation:** Learns features at multiple levels of abstraction
- ✅ **End-to-End Learning:** Raw input → Final output (no manual steps)
- ✅ **Breakthrough Performance:** Achieves state-of-the-art results

**Example:** Deep Learning automatically learns that edges → shapes → objects → scenes

### The Evolution

```
Traditional ML → Deep Learning
Hand-crafted features + Shallow models → Automatic features + Deep neural networks
```

### Key Insight:

Deep Learning addresses the **feature engineering bottleneck** by learning representations automatically from data, enabling breakthroughs in:
- Computer Vision (ImageNet 2012 breakthrough)
- Natural Language Processing (GPT, BERT)
- Speech Recognition (Siri, Alexa)
- And many more domains...

---

## Slide 6: Deep Learning
*Based on Slide 16 from "AI va Con nguoi - NEU.pdf"*

### What is Deep Learning?

**Definition:**
> "Deep Learning is a subset of machine learning that uses artificial neural networks with multiple layers (deep architectures) to learn representations of data with multiple levels of abstraction."

**Key Concept:**
- **Neural Networks:** Inspired by biological neurons
- **Deep Architecture:** Multiple hidden layers (hence "deep")
- **Feature Learning:** Automatically learns hierarchical features
- **End-to-End Learning:** Learns from raw input to final output

### Neural Network Architecture

**Basic Structure:**
```
Input Layer → Hidden Layer 1 → Hidden Layer 2 → ... → Hidden Layer N → Output Layer
```

**Why "Deep"?**
- **Shallow Networks:** 1-2 hidden layers
- **Deep Networks:** 3+ hidden layers (often 10-100+ layers)
- **Depth allows:** Hierarchical feature extraction

### How Deep Learning Works

1. **Forward Propagation:**
   - Data flows from input through hidden layers to output
   - Each layer transforms the input using weights and activation functions

2. **Backpropagation:**
   - Calculates errors at the output
   - Propagates errors backward through layers
   - Updates weights to minimize error

3. **Feature Hierarchy:**
   - **Layer 1:** Detects edges, lines, curves
   - **Layer 2:** Detects shapes, textures
   - **Layer 3:** Detects objects, parts
   - **Layer 4+:** Detects complex patterns, relationships

### Applications of Deep Learning

1. **Computer Vision**
   - **Image Recognition:** ImageNet classification (ResNet, VGG)
   - **Object Detection:** YOLO, Faster R-CNN
   - **Image Generation:** GANs (Generative Adversarial Networks)
   - **Example:** Google Photos auto-tagging

2. **Natural Language Processing**
   - **Machine Translation:** Google Translate, DeepL
   - **Language Models:** GPT, BERT, ChatGPT
   - **Text Generation:** Automated writing assistants
   - **Example:** ChatGPT conversation

3. **Speech Recognition**
   - **Voice Assistants:** Siri, Alexa, Google Assistant
   - **Transcription:** Automatic speech-to-text
   - **Example:** Real-time voice commands

4. **Autonomous Systems**
   - **Self-Driving Cars:** Tesla Autopilot, Waymo
   - **Robotics:** Robot manipulation and navigation
   - **Example:** Autonomous delivery robots

5. **Healthcare**
   - **Medical Imaging:** X-ray, MRI analysis
   - **Drug Discovery:** Protein folding prediction
   - **Example:** DeepMind's AlphaFold for protein structure

6. **Games and Entertainment**
   - **Game AI:** AlphaGo, AlphaStar
   - **Content Recommendation:** Netflix, YouTube
   - **Example:** DeepMind's AlphaGo defeating world champion

### Advantages of Deep Learning

- ✅ **Automatic Feature Extraction:** No manual feature engineering
- ✅ **Handles High-Dimensional Data:** Images, text, audio
- ✅ **End-to-End Learning:** Single model for complex tasks
- ✅ **State-of-the-Art Performance:** Beats traditional ML in many domains

### Challenges of Deep Learning

- ❌ **Large Data Requirements:** Needs massive datasets
- ❌ **Computational Resources:** Requires powerful GPUs/TPUs
- ❌ **Black Box Nature:** Difficult to interpret decisions
- ❌ **Training Time:** Can take days/weeks to train

---

## Slide 7: AI and Humans

### The Relationship Between AI and Humans

#### 1. AI as a Tool for Augmentation

**Enhancing Human Capabilities:**
- **Medical Diagnosis:** AI assists doctors in detecting diseases earlier
- **Education:** Personalized learning platforms adapt to student needs
- **Research:** AI accelerates scientific discovery and data analysis
- **Accessibility:** AI enables people with disabilities (voice-to-text, image recognition)

#### 2. Collaboration Between AI and Humans

**Complementary Strengths:**
- **Humans:** Creativity, empathy, ethical judgment, common sense
- **AI:** Pattern recognition, speed, consistency, scalability

**Example:** Medical Diagnosis
- AI: Analyzes medical images faster and can detect subtle patterns
- Human: Provides context, patient interaction, final decision-making

#### 3. AI Impact on Employment

**Job Transformation:**
- **Automation:** Routine, repetitive tasks automated
- **New Opportunities:** AI creates new job categories (ML engineers, data scientists)
- **Skill Evolution:** Workers need to adapt and learn new skills

**Examples:**
- Manufacturing: Robots handle assembly, humans oversee and maintain
- Customer Service: Chatbots handle common queries, humans handle complex issues
- Finance: AI analyzes transactions, humans make strategic decisions

#### 4. Ethical Considerations

**Challenges:**
- **Bias:** AI systems can perpetuate societal biases
- **Privacy:** Data collection and surveillance concerns
- **Transparency:** Need for explainable AI decisions
- **Accountability:** Who is responsible for AI decisions?

**Responsible AI Development:**
- Fairness and non-discrimination
- Privacy protection
- Transparency and explainability
- Human oversight and control

---

## Slide 8: The Role of AI in Specialized Fields

### 1. Healthcare

**Applications:**
- **Medical Imaging:** AI analyzes X-rays, MRIs, CT scans
  - Example: Detecting tumors, fractures, anomalies
- **Drug Discovery:** AI accelerates pharmaceutical research
  - Example: DeepMind's AlphaFold predicts protein structures
- **Personalized Medicine:** Tailored treatments based on patient data
- **Telemedicine:** Remote diagnosis and monitoring

**Impact:**
- Earlier disease detection
- Reduced medical errors
- Accelerated drug development
- Improved patient outcomes

### 2. Finance

**Applications:**
- **Fraud Detection:** Real-time transaction monitoring
  - Example: Credit card fraud detection systems
- **Algorithmic Trading:** High-frequency trading strategies
- **Credit Scoring:** Automated loan approval systems
- **Risk Management:** Portfolio optimization and risk assessment

**Impact:**
- Faster fraud detection
- Improved investment strategies
- Better risk assessment
- Automated financial services

### 3. Transportation

**Applications:**
- **Autonomous Vehicles:** Self-driving cars and trucks
  - Example: Tesla Autopilot, Waymo vehicles
- **Traffic Management:** Smart traffic light systems
- **Route Optimization:** GPS navigation and logistics
- **Predictive Maintenance:** Vehicle maintenance scheduling

**Impact:**
- Reduced accidents
- Improved traffic flow
- Lower transportation costs
- Increased accessibility

### 4. Education

**Applications:**
- **Personalized Learning:** Adaptive learning platforms
  - Example: Khan Academy, Coursera recommendations
- **Automated Grading:** Essay and assignment evaluation
- **Intelligent Tutoring:** Virtual tutors and assistants
- **Content Generation:** Educational material creation

**Impact:**
- Customized learning experiences
- Improved student engagement
- Scalable education delivery
- Better learning outcomes

### 5. Agriculture

**Applications:**
- **Precision Agriculture:** Crop monitoring and management
  - Example: Drones analyzing crop health
- **Pest Detection:** Early identification of pests and diseases
- **Yield Prediction:** Forecasting crop production
- **Automated Harvesting:** Robot-assisted harvesting

**Impact:**
- Increased crop yields
- Reduced resource waste
- Sustainable farming practices
- Food security improvement

### 6. Manufacturing

**Applications:**
- **Quality Control:** Automated defect detection
- **Predictive Maintenance:** Equipment failure prediction
- **Supply Chain Optimization:** Inventory and logistics management
- **Robotics:** Automated assembly and manufacturing

**Impact:**
- Higher quality products
- Reduced downtime
- Cost efficiency
- Improved safety

### 7. Natural Language Processing

**Applications:**
- **Translation Services:** Multi-language communication
  - Example: Google Translate, DeepL
- **Content Moderation:** Detecting harmful content
- **Customer Support:** Chatbots and virtual assistants
- **Content Creation:** Automated writing and summarization

**Impact:**
- Breaking language barriers
- Improved communication
- Scalable customer service
- Content accessibility

---

## Slide 9: Comparison: Traditional AI vs. Machine Learning vs. Deep Learning

### Traditional AI (Symbolic AI)
- **Approach:** Rule-based systems, explicit programming
- **Example:** Expert systems, search algorithms
- **Strengths:** Interpretable, deterministic
- **Limitations:** Cannot learn, requires explicit rules

### Machine Learning
- **Approach:** Learn from data, pattern recognition
- **Example:** Decision trees, SVM, random forests
- **Strengths:** Adapts to data, handles uncertainty
- **Limitations:** Requires feature engineering

### Deep Learning
- **Approach:** Neural networks with multiple layers
- **Example:** CNNs, RNNs, Transformers
- **Strengths:** Automatic feature learning, best performance
- **Limitations:** Requires large data, computational resources

### Evolution Path
```
Traditional AI → Machine Learning → Deep Learning
(Rules)         (Learning)         (Deep Learning)
```

---

## Slide 10: Key Takeaways

### Main Points Covered:

1. **Limitations of Traditional Search:**
   - Cannot solve pattern recognition problems
   - Image recognition example demonstrates necessity for ML

2. **Machine Learning:**
   - Learns from data without explicit programming
   - Three paradigms: Supervised, Unsupervised, Reinforcement Learning
   - Wide range of applications across industries

3. **Deep Learning:**
   - Subset of ML using deep neural networks
   - Automatic feature extraction
   - State-of-the-art performance in many domains

4. **AI and Humans:**
   - Collaborative relationship
   - AI augments human capabilities
   - Ethical considerations important

5. **AI in Specialized Fields:**
   - Transformative impact across multiple domains
   - Real-world applications solving real problems

### Next Steps:
- Week 13: Introduction to Neural Networks (Perceptron)
- Week 14: Hands-on Neural Network Training
- Week 15: Advanced Topics and Applications

---

## Slide 11: References and Further Reading

### Textbooks:
- **Russell & Norvig (2020):** Artificial Intelligence: A Modern Approach
  - Chapter 18: Learning from Examples
  - Chapter 21: Deep Learning

### Online Resources:
- **Coursera:** Machine Learning (Andrew Ng)
- **Deep Learning Specialization:** DeepLearning.AI
- **Fast.ai:** Practical Deep Learning for Coders

### Key Papers:
- ImageNet Classification with Deep Convolutional Neural Networks (AlexNet, 2012)
- Deep Residual Learning for Image Recognition (ResNet, 2015)
- Attention Is All You Need (Transformer, 2017)

---

## Additional Notes for Slide Creation

### Visual Elements to Include:

1. **Slide 2 (Limitations):**
   - Side-by-side comparison: Cat vs. Dog image
   - State space explosion visualization
   - Graph showing exponential growth

2. **Slide 4 (ML):**
   - Venn diagram: AI ⊃ ML ⊃ DL
   - Examples of ML applications with images
   - Supervised vs. Unsupervised vs. Reinforcement diagram

3. **Slide 5 (DL):**
   - Neural network architecture diagram
   - Feature hierarchy visualization (edges → shapes → objects)
   - Deep learning applications gallery

4. **Slide 6 (AI and Humans):**
   - Collaboration diagram
   - Before/After scenarios
   - Ethical AI framework

5. **Slide 7 (Specialized Fields):**
   - Icons/logos for each field
   - Real-world examples with images
   - Impact metrics/charts

### Suggested Slide Order:

1. Title Slide
2. Motivation: Limitations of Traditional Search
3. Transition to Machine Learning
4. AI and Machine Learning
5. Deep Learning
6. AI and Humans
7. The Role of AI in Specialized Fields
8. Comparison: Traditional AI vs. ML vs. DL
9. Key Takeaways
10. References

---

*Content prepared for Introduction to AI Course - Weeks 13-15*  
*Based on "AI va Con nguoi - NEU.pdf" slides 10 and 16*

