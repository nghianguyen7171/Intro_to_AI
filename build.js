/**
 * Intro to AI — course site builder.
 *
 * Adapted from the NEU FDA course site template:
 *   https://github.com/nghianguyen7171/neu_fda_coursesite
 *
 * Differences from the template, and why:
 *
 *  1. Output goes to the repository root, not docs/. GitHub Pages for this
 *     course publishes the gh-pages branch (see deploy.sh), and slides/,
 *     exercises/, and images/ already live at the root. Building to the root
 *     keeps every existing URL working and avoids storing 17 MB of slides
 *     twice.
 *
 *  2. Because OUT is the repo root, this script NEVER removes OUT. It writes
 *     only the files it generates, listed in GENERATED. Deleting the output
 *     directory here would delete the repository.
 *
 *  3. The site is a single page with anchor sections (#home, #about,
 *     #resources, #lectures, #assignments, #project, #people), preserving the
 *     deep links the old site published.
 *
 *  4. Assignments are external LMS links rather than local pages, so they come
 *     from data/assignments.yml instead of one Markdown file each.
 */

const fs = require('fs-extra');
const path = require('path');
const Handlebars = require('handlebars');
const yaml = require('js-yaml');
const { marked } = require('marked');
const sass = require('sass');
const { globSync } = require('glob');

const ROOT = __dirname;
const SRC = path.join(ROOT, 'src');

const WITH_SOLUTIONS = process.env.SOLUTIONS === '1';

// Files this script owns. Nothing else in the output directory is touched.
const GENERATED = ['index.html', 'assets/css/main.css'];

const log = (...a) => console.log(...a);
const fail = (msg) => {
  console.error(`\nBuild failed: ${msg}\n`);
  process.exit(1);
};

// ---------------------------------------------------------------- data

function loadData() {
  const dir = path.join(SRC, 'data');
  const data = {};
  for (const file of fs.readdirSync(dir).filter((f) => /\.ya?ml$/.test(f))) {
    const key = path.basename(file, path.extname(file)).replace(/-([a-z])/g, (_, c) => c.toUpperCase());
    data[key] = yaml.load(fs.readFileSync(path.join(dir, file), 'utf8'));
  }
  return data;
}

function loadContent() {
  const dir = path.join(SRC, 'content');
  const out = {};
  if (!fs.existsSync(dir)) return out;
  for (const file of globSync('*.md', { cwd: dir })) {
    const key = path.basename(file, '.md').replace(/-([a-z])/g, (_, c) => c.toUpperCase());
    out[key] = new Handlebars.SafeString(marked.parse(fs.readFileSync(path.join(dir, file), 'utf8')));
  }
  return out;
}

function validateCourse(course) {
  if (!course) fail('src/data/course.yml is missing or empty.');

  const items = (course.assessment && course.assessment.items) || [];
  if (!items.length) fail('course.yml defines no assessment items.');

  const total = items.reduce((sum, item) => {
    const n = parseFloat(String(item.weight).replace('%', ''));
    if (Number.isNaN(n)) fail(`assessment item "${item.name}" has an unparseable weight: ${item.weight}`);
    return sum + n;
  }, 0);

  if (Math.abs(total - 100) > 0.01) {
    fail(
      `assessment weights sum to ${total}%, not 100%.\n` +
        items.map((i) => `    ${String(i.weight).padStart(5)}  ${i.name}`).join('\n')
    );
  }

  const objectives = new Set((course.objectives || []).map((o) => o.id));
  for (const clo of course.learning_outcomes || []) {
    if (!objectives.has(clo.objective)) {
      fail(`${clo.id} maps to objective "${clo.objective}", which is not defined in course.yml.`);
    }
  }

  log(`  validated: ${items.length} assessment items sum to 100%`);
}

/**
 * Every local file the site links to must exist. The old site linked to
 * INTRO_AI_MANAGER/…pdf, which was never deployed, so the syllabus link 404'd
 * for the whole term. This check makes that class of bug impossible.
 */
function validateLocalLinks(html) {
  const missing = [];
  const re = /(?:href|src)="([^"#:]+)"/g;
  let m;
  while ((m = re.exec(html))) {
    const target = decodeURIComponent(m[1]);
    if (target.startsWith('//') || target.startsWith('mailto')) continue;
    if (target.startsWith('assets/css/')) continue; // written later in this build
    if (!fs.existsSync(path.join(ROOT, target))) missing.push(target);
  }
  if (missing.length) {
    fail(
      `index.html links to ${missing.length} file(s) that do not exist:\n` +
        [...new Set(missing)].map((t) => `    ${t}`).join('\n')
    );
  }
  log(`  validated: every local link resolves to a real file`);
}

// ------------------------------------------------------- markdown + solutions

const SOLUTION_RE = /^::: *solution *$\n([\s\S]*?)^::: *$/gm;

function processSolutions(md) {
  if (!WITH_SOLUTIONS) return md.replace(SOLUTION_RE, '');
  return md.replace(
    SOLUTION_RE,
    (_, body) => `\n<div class="solution">\n<p class="solution-label">Solution</p>\n\n${body.trim()}\n\n</div>\n`
  );
}

// ---------------------------------------------------------------- templating

function registerHelpers(course) {
  const baseurl = (course.baseurl || '').replace(/\/$/, '');

  // With an empty baseurl the site is served from its own directory
  // (…github.io/Intro_to_AI/), so links must stay relative. Returning an
  // absolute "/slides/x.pdf" here would 404 in production but work locally —
  // the classic GitHub Pages trap.
  Handlebars.registerHelper('url', (p) => {
    if (!p) return baseurl || './';
    if (/^(https?:)?\/\//.test(p) || p.startsWith('mailto:')) return p;
    // Several slide filenames contain spaces and parentheses, e.g.
    // "slides/6. (Cont) Propositional logic.pdf". encodeURI leaves "/" alone
    // and turns spaces into %20, which is what the browser needs.
    const clean = encodeURI(String(p).replace(/^\//, ''));
    return baseurl ? `${baseurl}/${clean}` : clean;
  });

  Handlebars.registerHelper('eq', (a, b) => a === b);
  Handlebars.registerHelper('concat', (...args) => args.slice(0, -1).join(''));
  Handlebars.registerHelper('year', () => new Date().getFullYear());
  Handlebars.registerHelper('md', (s) => new Handlebars.SafeString(marked.parse(String(s || ''))));
  Handlebars.registerHelper('mdInline', (s) => new Handlebars.SafeString(marked.parseInline(String(s || ''))));
  Handlebars.registerHelper('isReleased', (status) => (status || 'released') === 'released');
  Handlebars.registerHelper('statusLabel', (status) => ({ draft: 'Draft', tbd: 'TBD' }[status] || ''));

  // A lecture "material" is either a plain string or a single-key map
  // {Label: href}. This is the shape the old lectures.yml used; it is kept so
  // the data migrated across without being rewritten by hand.
  Handlebars.registerHelper('isLink', (item) => typeof item === 'object' && item !== null);
  Handlebars.registerHelper('linkLabel', (item) => Object.keys(item)[0]);
  Handlebars.registerHelper('linkHref', (item) => Object.values(item)[0]);
}

function registerPartials() {
  const dir = path.join(SRC, 'partials');
  for (const file of globSync('**/*.hbs', { cwd: dir })) {
    Handlebars.registerPartial(file.replace(/\.hbs$/, ''), fs.readFileSync(path.join(dir, file), 'utf8'));
  }
}

const tpl = (rel) => Handlebars.compile(fs.readFileSync(path.join(SRC, rel), 'utf8'));

// ---------------------------------------------------------------- main

function main() {
  log(`\nBuilding ${WITH_SOLUTIONS ? 'INSTRUCTOR (with solutions)' : 'PUBLIC'} site -> repository root\n`);

  const data = loadData();
  validateCourse(data.course);

  registerHelpers(data.course);
  registerPartials();

  const ctx = { ...data, content: loadContent(), withSolutions: WITH_SOLUTIONS };

  // Styles first: validateLocalLinks skips assets/css, but the file must exist
  // for the finished site to render.
  const css = sass.compile(path.join(SRC, 'styles', 'main.scss'), { style: 'compressed' });
  fs.outputFileSync(path.join(ROOT, 'assets', 'css', 'main.css'), css.css);
  log('  styles: assets/css/main.css');

  const page = tpl('index.hbs')(ctx);
  const html = tpl('templates/base.hbs')({ ...ctx, body: new Handlebars.SafeString(page) });

  validateLocalLinks(html);

  fs.outputFileSync(path.join(ROOT, 'index.html'), html);
  log('  page: index.html');

  log(`\nDone. Generated: ${GENERATED.join(', ')}\n`);
}

main();
