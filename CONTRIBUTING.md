# Contributing to YouTube All-Rounder 🎬🚀

Thank you for your interest in contributing to the **YouTube All-Rounder**! This project provides creators and AI coding agents (Claude Code, OpenAI Codex, OpenCode, Cursor, Gemini CLI, and Antigravity) with a universal packaging and growth workflow.

---

## 🛠️ How You Can Contribute

1. **Add New Visual Archetypes**:
   - If you've developed a proven, high-CTR visual archetype (e.g., archival microfilm, geopolitical map overlays, blueprints, split comparisons), submit a PR documenting the archetype, color formulas, and layer hierarchy in `references/archetypes.md`.
2. **Refine Title & Prompt Recipes**:
   - Add tested algorithmic title formulas in `resources/seo-and-packaging-guide.md`.
   - Add tested Nano Banana Pro / Google Flow prompt formulas in `resources/prompt-templates.md`.
   - Ensure all prompts enforce the **Zero Duplicate Words** and **Anti-AI Slop** constraints.
3. **Enhance Automation & Scripts**:
   - Optimize Python and Shell utilities in `.agents/skills/youtube-all-rounder/scripts/`.
   - Maintain zero-dependency pure Python standard library design across **macOS, Windows, and Linux**.

---

## 📋 Guidelines & Standards

### 1. Universal Agent Agnosticism
- Do **not** bind the skill or scripts to any proprietary LLM API or local image generator.
- The engine must remain 100% functional whether executed by a human in a terminal or by any AI agent CLI (Claude, Codex, OpenCode, Antigravity).

### 2. Zero External Dependencies
- All automation scripts must run on pure Python standard library (`sys`, `os`, `subprocess`, `webbrowser`, `argparse`).
- Avoid adding third-party pip dependencies so anyone can clone and run instantly.

### 3. The Non-Intrusive Background Principle
- Never write tools or scripts that hijack active window focus, freeze mouse cursors, or disrupt active user workflows.
- Always provide `--copy-only` / `--background` modes for clipboard and generation helpers.

### 4. Prompting & Aesthetic Purity
- **Zero Word Repetition**: Forbid twin badges, repeated word tags, or redundant adjectives.
- **Authentic Materiality**: Celebrate organic 35mm film grain, chiaroscuro lighting, paper fibers, and tactile textures over synthetic plastic AI airbrushing.

---

## 🚀 Submitting a Pull Request

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-archetype`).
3. Commit your changes (`git commit -m "feat: add archival microfilm archetype"`).
4. Push to the branch (`git push origin feature/new-archetype`).
5. Open a Pull Request describing your changes, with visual examples or prompt test outputs where applicable.

---

## 📄 License
By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
