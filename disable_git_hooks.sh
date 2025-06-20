#!/bin/bash
# Script to list and disable Git hooks by renaming them with .disabled extension

HOOKS_DIR=".git/hooks"

if [ ! -d "$HOOKS_DIR" ]; then
  echo "No .git/hooks directory found. Are you in a Git repository?"
  exit 1
fi

echo "Listing executable Git hooks in $HOOKS_DIR:"
for hook in "$HOOKS_DIR"/*; do
  if [ -f "$hook" ] && [ -x "$hook" ]; then
    echo "Disabling hook: $(basename "$hook")"
    mv "$hook" "$hook.disabled"
  fi
done

echo "All executable Git hooks have been disabled by renaming."
echo "To re-enable, rename files removing the .disabled extension."
