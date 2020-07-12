#!/bin/bash

git log --name-status HEAD~20..HEAD --pretty=format: . | awk '$1 == "M" || $1 == "A" { print }' | python .bin/recent_changes_updater.py > README.md
if git add README.md; then git commit -m "[Auto] Update recent changes"; fi