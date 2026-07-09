#!/bin/bash
## Publish the built site to the gh-pages branch. Run from the project root.

set -euo pipefail

TARGET_BRANCH="gh-pages"

REPO=$(git config remote.origin.url)
SHA=$(git rev-parse --verify HEAD)

# Refuse to publish a dirty tree: the deployed site should always correspond to
# a commit that exists on main.
if [ -n "$(git status --porcelain -- src build.js build.sh)" ]; then
  echo "error: uncommitted changes to the site source. Commit them first." >&2
  exit 1
fi

# Clone the existing gh-pages branch into out/, or start it if it is missing.
rm -rf out
git clone --quiet "$REPO" out
cd out
git checkout --quiet "$TARGET_BRANCH" 2>/dev/null || git checkout --quiet --orphan "$TARGET_BRANCH"
cd ..

# Clean every tracked path, keeping .git.
#
# The previous version used `rm -rf out/**/*`, which without `globstar` expands
# to `out/*/*`: it deletes files two levels deep but leaves the directories.
# `cp -r images out/` would then copy into the surviving out/images, producing
# out/images/images/. It also ended in `|| exit 0`, so a failure to clean exited
# with SUCCESS and silently deployed a stale tree.
find out -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +

# Build the site and stage a publishable copy in out/.
./build.sh

cd out

# Prevent GitHub Pages from running Jekyll over the output.
touch .nojekyll

git add --all .
if git diff --cached --quiet; then
  echo "No changes to deploy."
  exit 0
fi

git commit --quiet -m "Deploy to GitHub Pages: ${SHA}"
git push --quiet "$REPO" "$TARGET_BRANCH"

echo ""
echo "Deployed ${SHA} to ${TARGET_BRANCH}."
