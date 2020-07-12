#!/bin/bash

git log --name-status HEAD~5..HEAD --pretty=format: . | awk '$1 == "M" || $1 == "A" { print }' | python .bin/recent_changes_updater.py > README.md
