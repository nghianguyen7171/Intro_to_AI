# Introduction to Artificial Intelligence Course Website

**Course Codes:** EP15.TOKT11121 (DS) & EP16.TOKT11121 (AI)  
**Institution:** National Economics University  
**Instructors:** Dr. Trong-Nghia Nguyen & Dr. Nguyen Thi Kim Ngan

## Course Overview

This course aims to deliver a comprehensive overview of Artificial Intelligence, its implications, applications, and the skills to leverage it. The course begins by describing what the latest generation of artificial intelligence techniques can do. After an introduction to some basic concepts and techniques, the course illustrates both the potential and current limitations of these techniques with examples from a variety of applications.

### Key Topics Covered
- Search Strategies (BFS, DFS, A*, Minimax)
- Knowledge Representation and Logic
- Neural Networks and Machine Learning
- Computer Vision and Natural Language Processing
- AI Ethics and Applications

### Prerequisites
- EP16.TOKT11108 (Fundamental Programming Concepts in Python)
- Basic programming experience in Python
- Understanding of data structures and algorithms

## Website Information

🌐 **Live Website:** [https://nghianguyen7171.github.io/Intro_to_AI/](https://nghianguyen7171.github.io/Intro_to_AI/)

### Course Resources
- **Textbooks:** Russell & Norvig's "Artificial Intelligence: A Modern Approach" (2020)
- **Software:** Python, NumPy, scikit-learn, Kaggle
- **Platforms:** LMS for assignments, Kaggle for code submissions

### Grading Structure
- **Participation (20%):** Attendance, homework checks, class participation
- **Midterm Exam/Project (20%):** Project with presentation and report
- **Final Exam (60%):** Comprehensive examination

## Technical Information

### Building and Development

This website is built using modern web technologies and can be developed locally.

#### Prerequisites
- [Node.js](https://nodejs.org/) 7.x+ installed

#### Local Development
```bash
# Install dependencies
npm install

# Build and view locally
npm run build-in-place

# Or build to out directory
./build.sh
```

#### Deployment
```bash
# Deploy to GitHub Pages
./deploy.sh
```

### Technologies Used
- **[Handlebars](http://handlebarsjs.com/)** - Templating engine
- **[Stylus](https://learnboost.github.io/stylus/)** - CSS preprocessor
- **YAML** - Data configuration for lectures and assignments
- **Responsive Design** - Mobile-friendly layout

### File Structure
- `index.hbs` - Main template file
- `data/` - YAML files containing course data
- `templates/` - Handlebars partial templates
- `styles/` - Stylus stylesheets
- `slides/` - Course presentation slides
- `images/` - Course images and instructor photos

### Content Management
- **Lectures:** Edit `data/lectures.yml`
- **Assignments:** Edit `data/assignments.yml`
- **Course Info:** Edit `index.hbs`
- **This Week:** Edit `data/this-week.yml`

## Contact Information

**Dr. Trong-Nghia Nguyen**  
📧 nghiant@neu.edu.vn  
🌐 [Profile Page](https://nghianguyen7171.github.io/)

**Dr. Nguyen Thi Kim Ngan**  
📧 ngannguyen@neu.edu.vn  
🌐 [Profile Page](https://fda.neu.edu.vn/fda-members/ts-nguyen-thi-kim-ngan/)

## License

This course website is for educational purposes at National Economics University.
