#!/usr/bin/env bash
# launch_flow.sh - Copies the generated Google Flow prompt to clipboard and opens Google Flow
# Cross-platform support for macOS, Linux, and Windows (WSL/Git Bash).

set -e

FLOW_URL="https://labs.google/flow"

if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    echo "Usage: ./launch_flow.sh [OPTIONS] <\"Prompt text\" | prompt.txt>"
    echo ""
    echo "Options:"
    echo "  -h, --help      Show this help message and exit"
    echo "  -c, --copy-only Copy prompt to clipboard without launching browser"
    echo ""
    echo "Examples:"
    echo "  ./launch_flow.sh \"A cinematic 16:9 documentary editorial...\""
    echo "  ./launch_flow.sh prompt.txt"
    echo "  ./launch_flow.sh --copy-only prompt.txt"
    exit 0
fi

COPY_ONLY=false
if [ "$1" = "-c" ] || [ "$1" = "--copy-only" ]; then
    COPY_ONLY=true
    shift
fi

PROMPT_TEXT=""
if [ -n "$1" ]; then
    if [ -f "$1" ]; then
        PROMPT_TEXT=$(cat "$1")
    else
        PROMPT_TEXT="$*"
    fi
elif [ -f "prompt.txt" ]; then
    PROMPT_TEXT=$(cat "prompt.txt")
else
    echo "Error: No prompt provided and prompt.txt not found."
    echo "Usage: ./launch_flow.sh \"Your prompt here\" OR ./launch_flow.sh prompt.txt"
    exit 1
fi

# Copy to clipboard based on OS
if command -v pbcopy >/dev/null 2>&1; then
    printf "%s" "$PROMPT_TEXT" | pbcopy
    echo "[Success] Prompt copied to macOS clipboard via pbcopy."
elif command -v xclip >/dev/null 2>&1; then
    printf "%s" "$PROMPT_TEXT" | xclip -selection clipboard
    echo "[Success] Prompt copied to Linux clipboard via xclip."
elif command -v clip.exe >/dev/null 2>&1; then
    printf "%s" "$PROMPT_TEXT" | clip.exe
    echo "[Success] Prompt copied to Windows clipboard."
else
    echo "[Warning] Could not detect clipboard tool (pbcopy/xclip/clip). Please copy manually."
fi

echo ""
echo "Prompt Preview:"
echo "--------------------------------------------------------"
echo "$PROMPT_TEXT"
echo "--------------------------------------------------------"
echo ""

if [ "$COPY_ONLY" = true ]; then
    echo "Background mode active: Browser was not opened. Flow URL: $FLOW_URL"
    exit 0
fi

echo "Opening Google Flow: $FLOW_URL ..."

if command -v open >/dev/null 2>&1; then
    open "$FLOW_URL"
elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$FLOW_URL"
elif command -v start >/dev/null 2>&1; then
    start "$FLOW_URL"
else
    echo "Open Google Flow manually: $FLOW_URL"
fi

echo "Done. Paste (Cmd+V / Ctrl+V) into Google Flow."
