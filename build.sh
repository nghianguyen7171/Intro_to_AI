#!/bin/bash
set -e # exit with nonzero exit code if anything fails

# Build the site into the repo root, then stage a publishable copy in out/
# for deploy.sh to push to the gh-pages branch.

rm -f index.html
rm -rf assets/css

npm run build

mkdir -p out/assets
cp index.html favicon.ico out/
cp -r assets/css out/assets/css

# Only assets/css is copied, never assets/ as a whole. assets/ also holds
# generated exam figures (chapter2_search/, chapter34_figures/, …) belonging to
# the unpublished exams in assessments/. Copying the whole directory would leak
# exam material onto the public site.

# Course materials the site links to.
#
# INTRO_AI_MANAGER was absent from every previous deploy, so the "Course
# syllabus: Download PDF" link 404'd on the live site. materials/ holds the
# supplementary PDF recovered from the gh-pages branch, where it was orphaned.
cp -r images slides exercises materials INTRO_AI_MANAGER out/

echo ""
echo "Staged in out/:"
find out/ -maxdepth 2 -print
echo ""
