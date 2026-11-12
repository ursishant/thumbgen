#!/usr/bin/env python3
"""
launch_flow.py - Cross-platform helper to copy a Google Flow prompt to the clipboard and optionally open Google Flow.
Compatible with macOS, Linux, and Windows.
Supports non-intrusive background mode (--copy-only / --background).
"""

import sys
import os
import subprocess
import webbrowser
import argparse

FLOW_URL = "https://labs.google/flow"

def copy_to_clipboard(text: str) -> bool:
    """Copies text to the system clipboard across macOS, Windows, and Linux."""
    # 1. macOS (pbcopy)
    if sys.platform == "darwin":
        try:
            process = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
            process.communicate(text.encode("utf-8"))
            return True
        except Exception:
            pass

    # 2. Windows (clip.exe)
    if sys.platform.startswith("win") or "microsoft" in sys.platform:
        try:
            process = subprocess.Popen(["clip"], stdin=subprocess.PIPE, shell=True)
            process.communicate(text.encode("utf-8"))
            return True
        except Exception:
            pass

    # 3. Linux (wl-copy for Wayland, xclip / xsel for X11)
    if sys.platform.startswith("linux"):
        for tool in [["wl-copy"], ["xclip", "-selection", "clipboard"], ["xsel", "--clipboard", "--input"]]:
            try:
                process = subprocess.Popen(tool, stdin=subprocess.PIPE)
                process.communicate(text.encode("utf-8"))
                return True
            except FileNotFoundError:
                continue

    # Fallback via tkinter if available
    try:
        import tkinter as tk
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update()
        r.destroy()
        return True
    except Exception:
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Cross-platform prompt clipboard launcher for Google Flow (Nano Banana Pro).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        default="prompt.txt",
        help="Prompt text string or path to a text file containing the prompt.",
    )
    parser.add_argument(
        "-c", "--copy-only", "--background",
        dest="copy_only",
        action="store_true",
        help="Silent mode: Copies prompt to clipboard without automatically opening browser.",
    )
    parser.add_argument(
        "-u", "--url",
        default=FLOW_URL,
        help="Target Google Flow project URL.",
    )

    args = parser.parse_args()

    prompt_text = ""
    if os.path.isfile(args.prompt):
        with open(args.prompt, "r", encoding="utf-8") as f:
            prompt_text = f.read().strip()
    else:
        prompt_text = args.prompt.strip()

    if not prompt_text:
        print("[Error] Prompt text is empty.")
        sys.exit(1)

    copied = copy_to_clipboard(prompt_text)
    if copied:
        print("[Success] Prompt copied to your clipboard.")
    else:
        print("[Warning] Could not automatically copy to clipboard. Please copy manually.")

    print("\n" + "=" * 60)
    print("Google Flow (Nano Banana Pro) Prompt:")
    print("=" * 60)
    print(prompt_text)
    print("=" * 60 + "\n")

    if not args.copy_only:
        print(f"Opening Google Flow in default browser: {args.url}")
        webbrowser.open(args.url)
        print("Ready. Paste (Cmd+V / Ctrl+V) into Google Flow and generate.")
    else:
        print(f"Background mode active: Browser was not opened. Flow URL: {args.url}")

if __name__ == "__main__":
    main()
