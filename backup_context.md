# Backup Context for Introduction to AI Course Website Project

## Project Overview

This project creates a course website for "Introduction to Artificial Intelligence" at National Economics University. The website is built using modern web technologies and deployed on GitHub Pages.

### Key Information
- **Course Codes:** EP15.TOKT11121 (DS) & EP16.TOKT11121 (AI)
- **Institution:** National Economics University
- **Location:** 207 Giai Phong street, Bach Mai ward, Hanoi, Vietnam
- **Live Website:** https://nghianguyen7171.github.io/Intro_to_AI/
- **GitHub Repository:** https://github.com/nghianguyen7171/Intro_to_AI.git

## Instructors

### Dr. Trong-Nghia Nguyen
- **Email:** nghiant@neu.edu.vn
- **Profile:** https://nghianguyen7171.github.io/
- **Image:** images/people/Dr.TrongNghiaNguyen.jpeg
- **Background:** Member of Business AI Lab (BAI LAB), PhD from Chonnam National University, Korea (2025)
- **Source of truth:** `src/data/staff.yml`

> Dr. Nguyen Thi Kim Ngan was removed as Co-Instructor on 2026-07-09. Her entry
> and photo (`images/people/Dr.NTKN.jpg`) were deleted from the site and the
> deployment. Both remain recoverable from git history if she rejoins the course.

## Course Content

### Course Description
This course aims to deliver a comprehensive overview of Artificial Intelligence, its implications, applications, and the skills to leverage it. The course begins by describing what the latest generation of artificial intelligence techniques can do. After an introduction to some basic concepts and techniques, the course illustrates both the potential and current limitations of these techniques with examples from a variety of applications.

### Prerequisites
- EP16.TOKT11108 (Fundamental Programming Concepts in Python)
- Basic programming experience in Python
- Understanding of data structures and algorithms

### Grading Structure
- **Participation (20%):** Attendance, Homework check, Volunteer for class questions
- **Midterm Exam/Project (20%):** Project including presentation and submit report
- **Final Exam (60%):** Comprehensive examination

### Software Tools
- Python, numpy, sklearn
- Kaggle (for code submission)
- LMS (for homework and discussions)

## Course Schedule (15 Weeks)

### Week 1: Introduction to AI & Search Strategies
- **Topics:** Introduction to Artificial Intelligence; Search Strategies (BFS, DFS)
- **Slides:** slides/0.Intro_to_AI.pdf, slides/1.Searching_1.pdf
- **Materials:** Chapter 1–3, lecture slides, sample Python code

### Week 2: Homework Review & Hands-on Exercises
- **Topics:** Homework review and hands-on exercises on BFS and DFS
- **Materials:** Practice problems, Python notebook for search visualization

### Week 3: Informed Search Strategies
- **Topics:** Best-First Search, Hill Climbing, Beam Search
- **Slides:** slides/2.Searching_2.pdf
- **Materials:** Chapter 4, lecture slides, search implementation examples

### Week 4: Practical Session
- **Topics:** Practical session on heuristic-based search algorithms
- **Materials:** Coding exercises, performance comparison notebooks

### Week 5: Optimal Search
- **Topics:** Optimal Search (A*, Greedy Search)
- **Slides:** slides/3.Optimal_search.pdf
- **Materials:** Chapter 4, slides on heuristic functions and optimality

### Week 6: Implementation & Evaluation
- **Topics:** Implementation and evaluation of A* and Greedy Search
- **Materials:** Python code templates, problem sets

### Week 7: Adversarial Search
- **Topics:** Adversarial Search (Minimax Algorithm, Alpha-Beta Pruning)
- **Slides:** slides/4.Adversarial_search.pdf
- **Materials:** Chapter 5, lecture notes, game tree examples

### Week 8: Practice on Game-Playing Agents
- **Topics:** Practice on game-playing agents using Minimax and Alpha-Beta Pruning
- **Materials:** Lab exercises with Tic-Tac-Toe or similar games

### Week 9: Propositional Logic
- **Topics:** Propositional Logic – Syntax, Semantics, and Inference
- **Slides:** slides/5.Propositional_Logic.pdf
- **Materials:** Chapter 7, lecture slides, reasoning examples, CNF conversion practice problems
- **Interactive Exercises:** exercises/Week9_Exercises_Interactive.html (25+ exercises across 6 topics)

### Week 10: Practical Exercises on Logic
- **Topics:** Practical exercises on Propositional Logic (Resolution, Inference rules)
- **Materials:** Logic problem sets, Python-based logic solvers

### Week 11: First-Order Logic
- **Topics:** First-Order Logic – Representation and Inference
- **Materials:** Chapter 8–9, lecture notes, ontology examples

### Week 12: Practice on FOL
- **Topics:** Practice on First-Order Logic reasoning and implementation
- **Materials:** Exercises using FOL solvers or Prolog

### Week 13: Neural Networks
- **Topics:** Introduction to Neural Networks (Perceptron, Single-layer Neural Models)
- **Materials:** Chapter 18, lecture slides, TensorFlow/PyTorch notebooks

### Week 14: Hands-on Training
- **Topics:** Hands-on training for single-layer neural networks
- **Materials:** Lab notebook on classification tasks using perceptron

### Week 15: Supplementary Topics
- **Topics:** Computer Vision, NLP, Clustering, Regression, Classification, GPU Computing, MLOps
- **Materials:** Overview slides, project templates, demo notebooks

## Assignments

### Homework Structure
- **Submission:** Upload after each class, submit work in LMS
- **Code:** Uploaded in Kaggle
- **Extra Points:** Students who volunteer to do exercises get extra points

### Assignment Links (LMS Forum Discussions)
> **Disabled as of 2026-07-21.** LMS forum URLs have been removed from
> `src/data/assignments.yml`. The "Files" column now renders a grayed-out
> `<span class="mat mat-disabled">` instead of a live link. Re-add `url:`
> fields to each homework entry to re-enable them.
- **Homework 0:** https://elearning.fda.edu.vn/mod/forum/discuss.php?d=14 *(disabled)*
- **Homework 1:** https://elearning.fda.edu.vn/mod/forum/discuss.php?d=16 *(disabled)*
- **Homework 2:** https://elearning.fda.edu.vn/mod/forum/discuss.php?d=17 *(disabled)*
- **Homework 3:** https://elearning.fda.edu.vn/mod/forum/discuss.php?d=18 *(disabled)*
- **Homework 4:** https://elearning.fda.edu.vn/mod/forum/discuss.php?d=19 *(disabled)*
- **Homework 5:** https://elearning.fda.edu.vn/mod/forum/discuss.php?d=24 *(disabled)*

## Course Project

### General Requirements
- Each team selects one topic from the provided project list
- Project consists of two main parts: Presentation and Report
- Submit presentation and report (all .pdf files) via email or Zalo
- Awards for best presentation and best report

### Project Workflow
1. Identify a real-world problem
2. Model it as a search problem (state space search)
3. Apply at least 2–3 search algorithms (BFS, DFS, Greedy, A*, etc.)
4. Implement and test with code
5. Compare results (expanded nodes, time, solution quality)
6. Relate findings back to the real-world context

### Presentation Requirements
- **Duration:** 10–12 minutes per team
- **Structure:** Introduction, Problem Formulation, Algorithms, Experiments & Results, Discussion
- **Q&A:** Record questions and answers for "Response to Reviewers" section

### Report Structure
1. Introduction (real-world background)
2. Problem Formulation (search problem representation)
3. Algorithms (description with pseudocode)
4. Experiments & Results (comparison table, visual examples)
5. Discussion (analysis and insights)
6. Response to Reviewers (Q&A from presentation)
7. Conclusion

### Project Example: 8-Puzzle
- **Theoretical:** Apply BFS, GBFS (misplaced tiles), A* (Manhattan distance)
- **Real-world:** Seat arrangement in international conference
- **Sample:** 9 chairs (8 delegates + 1 empty), diplomatic protocols

### Important Notes
- Creativity required: Every project must be grounded in real-world scenario
- Response to Reviewers section is mandatory
- Teams encouraged to use visualizations, simulations, examples

### Project Submission
> **Google Drive button disabled as of 2026-07-21.** The CTA button linking to
> the Drive folder has been removed from `src/content/project.md`. Students are
> now directed to contact the instructors directly. The Drive URL is preserved
> here for reference only.
- **Google Drive Folder (disabled):** https://drive.google.com/drive/folders/1p14ShnfRMPj5UzJjS6VaJ4dAhvELUd_Y?usp=sharing
- **File Format:** PDF files only (presentation slides and final report)
- **Naming Convention:** TeamName_Presentation.pdf and TeamName_Report.pdf
- **Deadline:** Report due one week after presentation date

## Textbooks & Resources

### Main Textbooks
1. **Russell, S. & Norvig, P (2020).** Artificial Intelligence: A Modern Approach, Pearson.
   - **PDF Link:** http://lib.ysu.am/disciplines_bk/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf
   - **Prominently featured** on main website as primary textbook
2. **I. Almeida.** Artificial Intelligence Fundamentals for Business Leaders: Up to Date With Generative AI (2024 Edition). Now next later AI.
3. **Wolfgang Ertel (2017).** Introduction to Artificial Intelligence. Springer.

### Book Images
- AIMA_book.jpg (Russell & Norvig)
- AI_for_Bussiness.jpg (Almeida)
- Wolf_IntroAI.jpeg (Ertel)

## Technical Architecture

**As of 2026-07-09 this site runs on the NEU FDA course site template**
(https://github.com/nghianguyen7171/neu_fda_coursesite). The previous build —
a fork of NYU DS-GA 1003 using `index.hbs` at the repo root, `build/templater.js`,
and Stylus stylesheets — has been removed. Anything below describing `.styl`
files, `data/*.yml`, or `npm run build-in-place` is obsolete; it survives only in
git history at commit `f64571d`.

### Technologies Used
- **Handlebars:** Templating engine (partials under `src/partials/`)
- **SCSS (sass):** CSS preprocessor, replacing Stylus
- **YAML:** Data configuration, now under `src/data/`
- **marked:** Markdown for long-form prose (`src/content/`)
- **Node.js:** Build system (`build.js`, replacing `build/templater.js`)
- **GitHub Pages:** Hosting, from the `gh-pages` branch

### How this course differs from the template
The template builds into `docs/`. This course **builds into the repository root**
and publishes via `./deploy.sh` to the `gh-pages` branch, because `slides/`,
`images/`, and `exercises/` already live at the root and GitHub Pages was already
configured that way. Keeping the root as the output directory preserved every
existing URL and avoided storing 17 MB of slides twice in git.

Consequences, both load-bearing:
- `build.js` **must never delete its output directory.** The output directory is
  the repository. It writes only `index.html` and `assets/css/main.css`.
- The site is a **single page** with anchor sections, not the template's
  multi-page layout, so previously published deep links keep working.

Assignments are external LMS links rather than local pages, so they live in
`src/data/assignments.yml` instead of one Markdown file per assignment.

### File Structure
```
/
├── build.js                 # Build: YAML + Handlebars + SCSS -> index.html
├── build.sh                 # Build, then stage a publishable copy in out/
├── deploy.sh                # Push out/ to the gh-pages branch
├── src/
│   ├── index.hbs            # Page composition (which sections, in what order)
│   ├── templates/
│   │   └── base.hbs         # <html>, header, nav, footer
│   ├── partials/sections/   # home, main-textbook, about, resources,
│   │                        #   lectures, assignments, project, people
│   ├── data/
│   │   ├── course.yml       # Single source of truth: description, grading,
│   │   │                    #   policies, textbooks, software, prerequisites
│   │   ├── lectures.yml     # 15-week schedule, slides, materials
│   │   ├── assignments.yml  # Homework 0–5, LMS forum links
│   │   └── staff.yml        # Instructor(s)
│   ├── content/
│   │   └── project.md       # Course project brief (long prose)
│   └── styles/
│       ├── _variables.scss  # Theme tokens (accent colour, fonts)
│       └── main.scss        # Template stylesheet + course-specific additions
├── index.html               # GENERATED — do not edit by hand
├── assets/
│   ├── css/main.css         # GENERATED
│   └── chapter*/            # Exam figures. GITIGNORED. Never deployed.
├── slides/                  # 9 lecture PDFs (all linked from lectures.yml)
├── exercises/               # Student exercise materials
├── materials/
│   └── AI va Con nguoi - NEU.pdf   # Recovered from gh-pages, see change log
├── images/
│   ├── people/             # Instructor photo
│   ├── neu-logo.png        # Header logo
│   ├── fda-logo.png        # Header logo
│   └── *.jpg               # Book covers
├── INTRO_AI_MANAGER/       # Syllabus (PDF + docx)
├── assessments/            # Exams. GITIGNORED. Never deployed.
├── Final_exam/             # Exams. GITIGNORED. Never deployed.
├── idea/                   # Private preparation materials
└── package.json
```

### Key Files to Edit
- **Course info, grading, policies, textbooks:** `src/data/course.yml`
- **Lectures / schedule:** `src/data/lectures.yml`
- **Assignments:** `src/data/assignments.yml`
- **Instructors:** `src/data/staff.yml`
- **Course project text:** `src/content/project.md`
- **Theme colour / fonts:** `src/styles/_variables.scss`
- **Slides:** `slides/*.pdf` (then reference them from `lectures.yml`)
- **Never edit:** `index.html` and `assets/css/main.css` — both are generated.

### Build Process
1. `npm install` — install dependencies
2. `npm run build` — regenerate `index.html` and `assets/css/main.css`
3. `npm run serve` — preview at http://localhost:4000
4. `./deploy.sh` — build, stage into `out/`, push to `gh-pages`

`deploy.sh` refuses to run against a dirty source tree, so commit first.

### Build-time safety checks
The build **fails**, writing nothing, if:
- assessment weights in `course.yml` do not sum to 100%
- a weight cannot be parsed as a number
- a CLO maps to an objective that is not declared
- **any local link in the page points at a file that does not exist**

That last check exists because the syllabus download link was silently broken on
the live site for an entire term (see change log).

### Solution gating
`npm run build` strips `::: solution` blocks. `SOLUTIONS=1 npm run build`
(`npm run build:keys`) renders them and adds a red "do not publish" banner.
Publishing answer keys therefore requires deliberately opting in.

## Important Fixes Applied

### Slides 404 Error Fix
- **Problem:** Slides folder not copied to deployment
- **Solution:** Updated build.sh to include `slides` in copy command
- **Result:** All PDF slides now accessible at correct URLs

### Exercises Integration
- **Problem:** Interactive exercises not accessible after deployment
- **Solution:** Added exercises/ folder to build.sh and deploy.sh processes
- **Result:** Interactive exercises accessible at https://nghianguyen7171.github.io/Intro_to_AI/exercises/Week9_Exercises_Interactive.html

### Website Structure Optimization
- **Problem:** Separate exercises section cluttered main page
- **Solution:** Moved exercises link to Week 9 lecture materials
- **Result:** Cleaner main page, exercises accessible from lectures section

### GitHub Pages Caching Issues
- **Problem:** Updated content not visible due to GitHub Pages caching
- **Solution:** Force deployment and wait for cache propagation
- **Result:** All updates now visible on live website

### Image Management
- **Dr. Trong-Nghia Nguyen:** Dr.TrongNghiaNguyen.jpeg
- **Book Covers:** AIMA_book.jpg, AI_for_Bussiness.jpg, Wolf_IntroAI.jpeg
- **Header logos:** neu-logo.png, fda-logo.png (140 px, ~59 KB for the pair)
- **Removed 2026-07-09:** Dr.NTKN.jpg (co-instructor removed), and four NYU
  staff photos inherited from the DS-GA fork (mengye_ren.jpg,
  pavan_ravishankar.jpg, yash_amin.jpg, yilun_kuang.jpg). All were publicly
  served while linked from nowhere.

## Current Status

### ✅ Completed
- Website structure and content
- Course information and schedule
- Instructor profiles and photos
- Assignment links and project guidelines
- ~~Project submission system with Google Drive integration~~ *(Drive button disabled 2026-07-21)*
- Slides integration and accessibility
- Interactive exercises system (25+ exercises for Week 9)
- Exercise questions system (questions-only format with answer spaces)
- Interactive quizzes for Week 1 (Quizz1.html) and Week 2 (BFS, DFS, Advanced DFS)
- Main textbook prominently featured with PDF link
- Responsive design and styling
- GitHub Pages deployment
- README.md documentation
- Exercises integration into lecture materials

### 🔧 Technical Notes
- Website is fully functional and deployed
- All slides are accessible via direct links
- Interactive exercises accessible at correct URLs
- Images are properly referenced and displayed
- Build process includes all necessary files (slides, exercises, styles)
- Responsive design works on all devices
- GitHub Pages caching properly handled
- Exercises integrated into lecture materials for easy access

## Future Maintenance

### Content Updates
- Schedule changes: `src/data/lectures.yml`
- Course information, grading, policies: `src/data/course.yml`
- Assignment links: `src/data/assignments.yml`
- Add new slides to `slides/`, then reference them from `src/data/lectures.yml`
- Add new exercises to `exercises/`, then link them from `src/data/lectures.yml`
- Then run `npm run build` and `./deploy.sh`. Never hand-edit `index.html`.

### Technical Maintenance
- Keep Node.js dependencies updated
- Monitor GitHub Pages deployment
- Test build process after changes
- Verify all links and images work

## Interactive Exercises System

### Week 9: Propositional Logic Exercises
- **Location:** exercises/Week9_Exercises_Interactive.html
- **Access:** https://nghianguyen7171.github.io/Intro_to_AI/exercises/Week9_Exercises_Interactive.html
- **Integration:** Linked from Week 9 lecture materials as "Practice Exercises"

### Exercise Features
- **25+ exercises** across 6 major topics:
  1. Basic Syntax & Semantics (4 exercises)
  2. Truth Tables (4 exercises)
  3. Logical Equivalences (4 exercises)
  4. CNF Conversion (4 exercises)
  5. Resolution & Inference (4 exercises)
  6. Real-World Applications (4 exercises)
- **Progress tracking** with visual progress bar
- **Interactive grid layout** for better organization
- **Real-time answer checking** with detailed feedback
- **Responsive design** for all devices
- **Statistics display** showing completion percentage

### Supporting Materials
- **CNF Conversion Guide:** exercises/CNF_Conversion_Method_English.md
- **PDF Version:** exercises/Week9_Exercises_Student.md
- **Printable worksheet:** exercises/Week9_Exercises_Solutions.html
  - **The filename is misleading.** Despite "Solutions", this file contains no
    answers — it is a blank worksheet with 35 `Your Answer: ____` fields. It was
    linked from Week 9 as "Exercise Solutions" until 2026-07-09; students
    clicking for answers got an empty form. Now labelled "Printable Worksheet
    (blank)". Renaming the file would break any bookmarked URL, so the label was
    fixed instead.
- **Answer Key:** idea/Prositional logic/Week9_Exercises_ANSWER_KEY.md (instructor only)

### Files present but deliberately NOT linked
- `exercises/Week9_Exercises_Comprehensive.html` — byte-identical to
  `Week9_Exercises_Interactive.html` (same MD5). A duplicate.
- `exercises/Week9_Exercises_Interactive_Expanded.html` — differs from
  `Interactive` by one line and is **broken**: `checkChainRule()` passes an
  undefined `isCorrect` to `showResult()`, throwing a `ReferenceError`. The
  working file defines `hasSteps`.

### Technical Implementation
- **HTML/CSS/JavaScript** for interactivity
- **File Size:** 46,648 bytes (expanded version)
- **Questions Format:** Student worksheet with answer spaces for all exercises
- **Deployment:** Automatically included in build process
- **Caching:** Handled through GitHub Pages deployment

## Contact Information

**Dr. Trong-Nghia Nguyen**
- Email: nghiant@neu.edu.vn
- Profile: https://nghianguyen7171.github.io/

## Change Log

### 2026-07-21 — Private Links Disabled

All links pointing to personal/institutional systems (LMS, Google Drive) and
to exercise/solution files have been removed from the public site. Only book
links, slide links, and instructor profile links remain active.

**Changes made:**
- `src/data/assignments.yml`: Removed `url:` from all 6 homework entries.
  The assignments table still renders but shows a grayed-out disabled label
  instead of a live LMS link.
- `src/data/lectures.yml`: Converted 3 exercise/solution material links to
  plain text (no hyperlink):
  - Week 9: `exercises/Week9_Exercises_Interactive.html` ("Interactive Practice Exercises")
  - Week 9: `exercises/Week9_Exercises_Solutions.html` ("Printable Worksheet (blank)")
  - Week 13: `exercises/First_Order_Logic_Solutions_CORRECTED.html` ("First-Order Logic — Worked Solutions")
- `src/content/project.md`: Removed the Google Drive CTA button; replaced
  with "contact the instructors directly."
- `src/partials/sections/assignments.hbs`: Updated to render
  `<span class="mat mat-disabled" aria-disabled="true">LMS</span>` when no
  `url` is present.
- `src/styles/main.scss`: Added `.mat-disabled` rule (opacity 0.5,
  cursor: not-allowed, var(--text-soft) colour).

To re-enable any of these links, restore the `url:` fields in the relevant
data files and redeploy.

### 2026-07-09 — Co-Instructor Removed

- **Removed:** Dr. Nguyen Thi Kim Ngan from `src/data/staff.yml`.
- **Deleted:** `images/people/Dr.NTKN.jpg`, so the photo is no longer published.
- The hero label now reads "Instructor" rather than "Instructors" automatically.
- Recoverable from git history if she rejoins.

### 2026-07-09 — Site Rebuilt on the NEU FDA Course Site Template

The site was migrated off the forked NYU DS-GA 1003 build (Handlebars + Stylus +
`build/templater.js`) onto the shared template
(https://github.com/nghianguyen7171/neu_fda_coursesite): YAML + Handlebars + SCSS
compiled by `build.js`.

**No content was lost.** The site is still a single page and keeps all eleven
original anchors (`#home #about #resources #lectures #assignments #project
#people #main-textbook #past_exams #textbooks #software`), so published deep
links still work. All 9 slides, 6 homework links, 3 textbooks, the AIMA download,
the Google Drive submission folder, the instructor bio and photo, the full
course-project brief, and every policy carried across. Verified against the live
site: all local links and all external links return HTTP 200.

**Bugs found and fixed during the migration:**

1. **Syllabus download had been 404 for the whole term.** `index.hbs` linked
   `INTRO_AI_MANAGER/Syllabus…pdf`, but `build.sh` never copied
   `INTRO_AI_MANAGER/` into `out/`, so the folder did not exist on `gh-pages`.
   `build.sh` now deploys it, and `build.js` now fails the build if any local
   link points at a missing file.

2. **A slide was invisible to students.** `slides/6. (Cont) Propositional
   logic.pdf` was committed but referenced from nowhere. Now attached to Week 10.

3. **Week 9's "Exercise Solutions" link was a blank worksheet.** Relabelled
   "Printable Worksheet (blank)". See the Interactive Exercises section above.

4. **A PDF existed only on `gh-pages`.** `Intro_ML_DL_ref/AI va Con nguoi -
   NEU.pdf` was never on `main` and was linked from nowhere; the next deploy
   would have erased it permanently. Recovered to `materials/` and linked under
   Course materials.

5. **`build.sh` was about to leak exam material.** It copied all of `assets/`,
   which now also holds generated exam figures for the unpublished exams in
   `assessments/`. It now copies only `assets/css`. `assessments/`,
   `Final_exam/`, `final_exam_idea/`, `tmp/` and the figures are gitignored.

6. **`deploy.sh` cleaned the gh-pages tree incorrectly.** `rm -rf out/**/*`
   expands to `out/*/*` without `globstar`: it deleted files two levels deep but
   left the directories, so `cp -r images out/` would have produced
   `out/images/images/`. It also ended in `|| exit 0`, meaning a failed clean
   exited **successfully** and deployed a stale tree. Replaced with a `find`
   that removes every top-level entry except `.git`, plus a dirty-tree guard, a
   no-op skip, and `.nojekyll`.

7. **The Ertel textbook link was dead**, and had been before the migration.
   `10.1007/978-1-4471-6738-6` returns 404; the cited 2017 2nd edition is
   `10.1007/978-3-319-58487-4`.

**Removed NYU residue:** the HTF/SSBD/JWHT abbreviations for books this course
does not use, the DS-GA reference list, the `dsga1003` package name, the NYU
repository URLs, four NYU staff photos, and the dead Universal Analytics tag
(UA properties stopped processing data in 2023). All recoverable from git history
at `f64571d`.

**Added:** NEU and FDA logos in the header. The FDA crest is dark navy linework
on a transparent background (71% of pixels fully transparent, opaque pixels
averaging 90/255 luminance), so it was almost invisible on the dark theme; both
logos get a white plate under `prefers-color-scheme: dark`.

**Deliberately not invented:** credits, contact hours, and formal CLOs. The old
site never published them and they exist only in the syllabus PDF. `course.yml`
marks where they belong. Do not guess them — they are part of a document the
faculty signs off on.

### 2026-08-04 — Maintenance Review (no content changes)

Full audit of all source files against this document. No discrepancies found.
State confirmed as of this date:

- **Staff:** `src/data/staff.yml` — only Dr. Trong-Nghia Nguyen (role: Instructor).
- **Assignments:** `src/data/assignments.yml` — 6 homeworks (HW 0–5), no `url:` fields on any entry; rendered as disabled labels on the site.
- **Lectures:** `src/data/lectures.yml` — 15 weeks, 9 slides (0.Intro.pdf through 8.Intro_ML_DL.pdf). Week 9 and Week 13 exercise links are plain text (no hyperlinks), consistent with 2026-07-21 change.
- **Project:** `src/content/project.md` — no Google Drive CTA; students directed to contact instructors.
- **Slides on disk:** `slides/` contains exactly the 9 PDFs referenced in lectures.yml.
- **Exercises on disk:** `exercises/` contains 8 files; 3 are not linked from the site (Comprehensive.html duplicate, Interactive_Expanded.html broken, Week9_Exercises_Student.md unused).
- **Images:** `images/people/` contains only `Dr.TrongNghiaNguyen.jpeg`; all removed photos (Dr.NTKN.jpg, four NYU staff photos) are absent.
- **Build safety:** `build.js` still enforces weight-sum-to-100 and broken-local-link checks. `SOLUTIONS=1` env var gates solution rendering.
- **Deploy:** `deploy.sh` still requires a clean source tree before pushing to gh-pages.

No action required. Next update warranted when content changes.

---

### Latest Updates (Session Review)

#### Final Examination Package Created
- **Date:** 2025-11-11
- **Files Added:** `assessments/final_exam_intro_to_ai.md`, `assessments/final_exam_intro_to_ai.html`, `scripts/generate_final_exam_figures.py`, image assets in `assets/final_exam/figure*.png`
- **English Translation (Chapter 2)**
  - **Date:** 2025-11-11
  - **Files Added:** `assets/chapter2_search/figure1_graph.png`, `assets/chapter2_search/figure2_graph.png`, `assets/chapter2_search/figure3_graph.png`, `assessments/chapter2_search_exam.html`
  - **Content:** English multiple-choice exam covering Chapter 2 search exercises with refreshed figures for DFS/BFS scenarios.
  - **Automation:** `scripts/generate_chapter2_figures.py` (same session) draws graphs via NetworkX; HTML embeds figures and includes answer key.
  - **Assumptions:** BFS enqueues children left-to-right; DFS pushes children left-to-right (rightmost pops first).
  - **Update (same day):** Adjusted `assessments/chapter2_search_exam.html` so each question now embeds its associated figure inline, matching the original docx layout requirement.
- **English Translation (Chapters 3–4)**
  - **Date:** 2025-11-11
  - **Files Added:** `assets/chapter34_search/figure1_astar_graph.png`, `assets/chapter34_search/figure2_8puzzle.png`, `assets/chapter34_search/figure3_weighted_graph.png`, `assets/chapter34_search/figure4_local_search_graph.png`, `scripts/generate_chapter34_figures.py`, `assessments/chapter3_4_search_exam.html`
  - **Content:** English practice exam for heuristic search topics covering A*, heuristic evaluation, hill climbing, and branch-and-bound with inline figures and translated tables.
  - **Implementation:** Python script recreates all diagrams with Matplotlib/NetworkX (state space graphs plus 8-puzzle boards); HTML places each figure directly inside its corresponding question card, mirrors partial execution tables, and provides an answer key.
  - **Notes:** Edge costs and heuristics are mapped from the original Vietnamese materials; OPEN/L/MIN placeholders preserved (shown as “?”) where the student is expected to fill in values.
- **Content:** Complete 90-minute, 40-question multiple-choice final exam covering course overview, uninformed and informed search, logic, and the new ML/DL transition materials.
- **Features:**
  - Sectional structure respects required theory/exercise distribution; optional ML questions provided to reach 12 theory items from the new slide deck.
  - Embedded answer key covering all items (and optional questions) for rapid grading.
  - Python script generates four supporting figures (BFS graph, heuristic graph, A* weighted graph, minimax tree) stored as high-resolution PNGs.
  - Answer choices evenly distributed across options A–D to minimize guessing bias.
- **Update (same day):** Trimmed Section A to remove general-purpose items not tied to slides, absorbed the optional ML/DL questions into Section H, and temporarily hid the HTML answer key (commented out) before publishing.
- **Usage:** Markdown and HTML exam versions ready for LMS or print; HTML version now embeds figures directly within the relevant questions, with hi-res copies available separately.

#### Week 13-14 Schedule Updated with ML/DL Content
- **Date:** Current Session
- **File Added:** `slides/8.Intro_ML_DL.pdf` (3.7MB)
- **Files Updated:** `data/lectures.yml`, `index.html`
- **Week 13 Changes:**
  - Topic changed to: "From Search Algorithms and Logic to Learning Systems"
  - Slide added: `slides/8.Intro_ML_DL.pdf`
  - Material added: `exercises/First_Order_Logic_Solutions_CORRECTED.html` (Solution for First-Order Logic)
- **Week 14 Changes:**
  - Topic changed to: "From Search Algorithms and Logic to Learning Systems (continuous)"
  - Slide reference: `slides/8.Intro_ML_DL.pdf`
- **Week 15:** Unchanged (Supplementary Topics)
- **Integration:** Website regenerated with updated schedule, accessible at https://nghianguyen7171.github.io/Intro_to_AI/

#### Introduction to Machine Learning and Deep Learning Content Created
- **Date:** Current Session
- **File Added:** `idea/Introduction_to_Machine_Learning_and_Deep_Learning.md`
- **Content:** Comprehensive lecture content for Weeks 13-15 covering ML/DL introduction
- **Structure:**
  - Slide 1: Title with connection to previous course content (Search Algorithms, Logic)
  - Slide 2: Motivation - Image recognition example demonstrating limitations of traditional AI
  - Slides 3-4: AI and Machine Learning (definitions, paradigms, applications)
  - Slide 5: Deep Learning (concepts, architecture, applications)
  - Slides 6-7: AI and Humans, Role in Specialized Fields
  - Slides 8-10: Comparison, Takeaways, References
- **Key Feature:** Explicitly connects previous course content (search algorithms, propositional logic, first-order logic) with ML/DL through the image recognition example
- **Based On:** Content from "AI va Con nguoi - NEU.pdf" slides 10 and 16
- **Purpose:** Content preparation for upcoming ML/DL lecture slides (Weeks 13-15)
- **Connection Strategy:** Shows how traditional search algorithms and logic systems fail on pattern recognition problems, motivating the need for machine learning

#### Week 11 First-Order Logic Slide Added
- **Date:** Current Session
- **File Added:** `slides/7. First-Order logic.pdf`
- **Content:** First-Order Logic lecture slides (6,917 lines)
- **Integration:** Added slide reference to Week 11 lecture materials in `data/lectures.yml`
- **HTML Update:** `index.html` regenerated with First-Order Logic slide link
- **Access:** Available at https://nghianguyen7171.github.io/Intro_to_AI/slides/7.%20First-Order%20logic.pdf

#### First-Order Logic Solutions File Created
- **Date:** Current Session
- **File Added:** `exercises/First_Order_Logic_Solutions.md`
- **Content:** Comprehensive step-by-step solutions for Examples 1-5 (pages 16-22 of lecture slides)
- **Topics Covered:**
  - Example 1: Converting to Prenex Normal Form (PNF)
  - Example 2: Skolemization
  - Example 3: Converting to CNF with Herbrand Universe/Base
  - Example 4: Resolution in First-Order Logic
  - Example 5: Unification (Most General Unifier)
- **Format:** Detailed mathematical derivations with LaTeX notation
- **Purpose:** Student reference and study guide for Week 11 exercises

### Latest Updates (October 21, 2025)

#### Exercise Questions System Updated
- **File Updated:** `exercises/Week9_Exercises_Solutions.html`
- **Content:** Questions-only format with answer spaces for all 35 propositional logic exercises
- **Change:** Removed all answers/solutions, kept only questions with answer spaces
- **Purpose:** Student exercise worksheet format
- **Integration:** Added to Week 9 lecture materials in `data/lectures.yml`
- **Access:** Available at https://nghianguyen7171.github.io/Intro_to_AI/exercises/Week9_Exercises_Solutions.html

#### Additional Exercise Materials
- **File Added:** `idea/Prositional logic/Exercise_PL_1.pdf`
- **Content:** Additional propositional logic exercise materials (39KB PDF)
- **Location:** Private instructor materials folder

#### Build System Enhancement
- **Updated:** `build.sh` script
- **Change:** Added exercises folder to build process to ensure solutions are deployed
- **Impact:** Exercise solutions now automatically included in GitHub Pages deployment

#### Course Materials Enhancement
- **Updated:** Week 9 lecture materials in `data/lectures.yml`
- **Added:** "Exercise Solutions" link to Week 9 materials
- **Integration:** Solutions now accessible directly from lecture materials
- **HTML Update:** `index.html` updated with Exercise Solutions link in generated website

### Previous Updates
- Interactive exercises system (25+ exercises for Week 9)
- Project submission system with Google Drive integration
- Main textbook prominently featured with PDF link
- Comprehensive course documentation and backup context

### 2026-08-09 — Week 1 Quiz Added

- **New folder:** `quizz/` — holds interactive HTML quizzes for lectures.
- **New file:** `quizz/Quizz1.html` — interactive Quiz 1 for Week 1
  (Introduction to AI & Search Strategies).
- **`src/data/lectures.yml`:** Added
  `{ "Quiz 1 (Interactive)": "quizz/Quizz1.html" }` to Week 1 materials. It
  renders as a link in the "Slides & materials" column.
- **`build.sh`:** Added `quizz` to the `cp -r` list so the folder ships to
  `gh-pages` on every deploy. Without it, the link would 404 in production
  (the build's local-link check only catches missing files in the source tree).
- **Deployed:** via `./deploy.sh` after committing the source changes.

To add future quizzes: drop `quizz/QuizzN.html` and reference it from the
appropriate week in `lectures.yml` — no other changes needed.

### 2026-08-24 — Week 4 Local Search Lab Linked

- **New file:** `quizz/dfs_vs_hill_climbing_lab.html` — interactive DFS vs
  hill-climbing / local-search lab for Week 4 practice.
- **`src/data/lectures.yml`:** Week 4 materials now include:
  - `{ "Local search": "quizz/dfs_vs_hill_climbing_lab.html" }`
- **Source commit:** `609cc00` — "Add Week 4 Local search lab to lecture materials."
- **Deployment:** shallow `gh-pages` deploy published commit `609cc00`
  (`gh-pages` HEAD `e396b63`). `quizz/` already shipped via `build.sh`.
- **Live URL:**
  - https://nghianguyen7171.github.io/Intro_to_AI/quizz/dfs_vs_hill_climbing_lab.html

### 2026-08-21 — Week 3 Quizzes Deployed

- **New files:** `quizz/heuristic_search_visualizer_lab.html`,
  `quizz/scenario_heuristic_search_lab.html` — two interactive Week 3 quizzes
  covering informed/heuristic search (Best-First, Hill Climbing, Beam Search)
  via an algorithm visualizer and applied scenario problem-formulation lab.
- **`src/data/lectures.yml`:** Week 3 materials now include:
  - `{ "Quiz 3 — Heuristic Search Visualizer Lab": "quizz/heuristic_search_visualizer_lab.html" }`
  - `{ "Quiz 3 — Scenario Heuristic Search Lab": "quizz/scenario_heuristic_search_lab.html" }`
- **Source commit:** `68b7063` — "Add Week 3 interactive quizzes:
  heuristic search visualizer & scenario labs."
- **Deployment:** `./deploy.sh` published commit `68b7063` to `gh-pages`.
  No changes to `build.sh` needed (quizz folder was already shipped since 2026-08-09).
- **Live URLs (both verified HTTP 200):**
  - https://nghianguyen7171.github.io/Intro_to_AI/quizz/heuristic_search_visualizer_lab.html
  - https://nghianguyen7171.github.io/Intro_to_AI/quizz/scenario_heuristic_search_lab.html

### 2026-08-20 — Week 2 Quizzes Deployed

- **New files:** `quizz/quizz2_bfs.html`, `quizz/quizz2_dfs.html`,
  `quizz/quizz2_Adv_dfs.html` — three interactive Week 2 quizzes covering
  BFS, DFS, and advanced DFS hands-on practice.
- **`src/data/lectures.yml`:** Week 2 materials now include:
  - `{ "Quiz 2 — BFS": "quizz/quizz2_bfs.html" }`
  - `{ "Quiz 2 — DFS": "quizz/quizz2_dfs.html" }`
  - `{ "Quiz 2 — Advanced DFS": "quizz/quizz2_Adv_dfs.html" }`
- **Source commit:** `d246092` — "Add Week 2 interactive quizzes for BFS, DFS, and advanced DFS."
- **Deployment:** `./deploy.sh` published commit `d246092` to `gh-pages`.
  No changes to `build.sh` needed (quizz folder was already shipped since 2026-08-09).
- **Live URLs (all verified HTTP 200):**
  - https://nghianguyen7171.github.io/Intro_to_AI/quizz/quizz2_bfs.html
  - https://nghianguyen7171.github.io/Intro_to_AI/quizz/quizz2_dfs.html
  - https://nghianguyen7171.github.io/Intro_to_AI/quizz/quizz2_Adv_dfs.html
- **Verification:** `gh-pages` HEAD advanced to `e471120`; backup_context.md
  update pushed to `main` as `b63aa4c`.

---

**Last Updated:** 2026-08-24 (Week 4 Local search lab linked and deployed)  
**AI Readiness:** 100%

*This document serves as a comprehensive backup context for the Introduction to AI course website project. It contains all essential information needed to understand, maintain, and continue development of the project.*


