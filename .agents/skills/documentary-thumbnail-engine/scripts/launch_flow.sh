#!/usr/bin/env bash
# launch_flow.sh - Copies the generated Google Flow prompt to clipboard and opens Google Flow

set -e

PROMPT_TEXT=""
FLOW_URL="https://labs.google/flow"

# Read prompt from argument or from stdin
if [ -n "$1" ]; then
    if [ -f "$1" ]; then
        PROMPT_TEXT=$(cat "$1")
    else
        PROMPT_TEXT="$*"
    fi
else
    # Check if a prompt.txt exists in current directory
    if [ -f "prompt.txt" ]; then
        PROMPT_TEXT=$(cat "prompt.txt")
    else
        echo "Usage: ./launch_flow.sh \"Your prompt here\" OR ./launch_flow.sh prompt.txt"
        exit 1
    fi
fi

# Copy to clipboard based on OS
if command -v pbcopy >/dev/null 2>&1; then
    # macOS
    printf "%s" "$PROMPT_TEXT" | pbcopy
    echo "✅ Prompt copied to macOS clipboard via pbcopy!"
elif command -v xclip >/dev/null 2>&1; then
    # Linux (xclip)
    printf "%s" "$PROMPT_TEXT" | xclip -selection clipboard
    echo "✅ Prompt copied to Linux clipboard via xclip!"
elif command -v clip.exe >/dev/null 2>&1; then
    # Windows / WSL
    printf "%s" "$PROMPT_TEXT" | clip.exe
    echo "✅ Prompt copied to Windows clipboard!"
else
    echo "⚠️  Could not detect clipboard tool (pbcopy/xclip/clip). Please copy the prompt manually."
fi

echo ""
echo "🎨 Prompt Preview:"
echo "--------------------------------------------------------"
echo "$PROMPT_TEXT"
echo "--------------------------------------------------------"
echo ""
echo "🚀 Opening Google Flow: $FLOW_URL ..."

# Open browser
if command -v open >/dev/null 2>&1; then
    open "$FLOW_URL"
elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$FLOW_URL"
elif command -v start >/dev/null 2>&1; then
    start "$FLOW_URL"
else
    echo "Open Google Flow manually: $FLOW_URL"
fi

echo "✨ Done! Just paste (Cmd+V / Ctrl+V) into Google Flow."

