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

FLOW_URL = "https://labs.google/flow"

def copy_to_clipboard(text: str) -> bool:
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
    args = sys.argv[1:]
    copy_only = False
    if "--copy-only" in args:
        copy_only = True
        args.remove("--copy-only")
    if "--background" in args:
        copy_only = True
        args.remove("--background")

    prompt_text = ""
    if len(args) > 0:
        arg = args[0]
        if os.path.isfile(arg):
            with open(arg, "r", encoding="utf-8") as f:
                prompt_text = f.read().strip()
        else:
            prompt_text = " ".join(args).strip()
    elif os.path.isfile("prompt.txt"):
        with open("prompt.txt", "r", encoding="utf-8") as f:
            prompt_text = f.read().strip()
    else:
        print("Usage: python3 launch_flow.py [--copy-only] <prompt-text-or-file>")
        sys.exit(1)

    if not prompt_text:
        print("Error: Prompt text is empty.")
        sys.exit(1)

    copied = copy_to_clipboard(prompt_text)
    if copied:
        print("✅ Prompt copied to your clipboard silently!")
    else:
        print("⚠️ Could not automatically copy to clipboard. Please copy the prompt manually.")

    print("\n" + "=" * 60)
    print("🎨 Google Flow (Nano Banana Pro) Prompt:")
    print("=" * 60)
    print(prompt_text)
    print("=" * 60 + "\n")

    if not copy_only:
        print(f"🚀 Opening Google Flow in your default browser: {FLOW_URL}")
        webbrowser.open(FLOW_URL)
        print("✨ Ready! Just paste (Cmd+V / Ctrl+V) into Google Flow and hit generate.")
    else:
        print(f"💡 Background mode active: Browser was NOT forced open. Flow URL: {FLOW_URL}")

if __name__ == "__main__":
    main()
