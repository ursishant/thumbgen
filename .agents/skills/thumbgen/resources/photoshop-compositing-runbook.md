# Photoshop & Compositing Runbook

A precise step-by-step layer composition guide to assemble thumbnails matching the tactile documentary aesthetic.

---

## The Master Layer Stack Architecture

```text
[ GROUP 6: MASTER GRADE & TEXTURE ]        (Pass-Through / 100%)
  ├── Curves / Levels (Tension Contrast)   (Normal, Clip or Global)
  ├── Paper Grain & Dust Texture           (Overlay or Soft Light, 20-35%)
  └── Color Lookup / LUT (Subtle film tone)(Soft Light, 15-25%)

[ GROUP 5: FOREGROUND ACCENTS & PROPS ]    (Pass-Through / 100%)
  ├── Red Pen Markings & Arrows            (Multiply, 90%)
  ├── Duct Tape / Paperclips / Pushpins    (Normal, with Drop Shadow)
  ├── Badge Stickers ("FILES LEAKED")      (Normal, Inner Shadow 15%)
  └── Red Strings / Wires                  (Normal, Cast Shadow onto BG)

[ GROUP 4: HERO SUBJECT CUTOUT(S) ]        (Pass-Through / 100%)
  ├── High-Pass Sharpen Layer              (Overlay, 40-60%)
  ├── Halftone Screen Overlay (Optional)   (Multiply, 75%)
  ├── Rim Light Dodge Layer (Inner Glow)   (Screen / Color Dodge, 60%)
  └── Cutout Base (Subject)                (Normal, Drop Shadow / Sticker Stroke)

[ GROUP 3: PRIMARY HEADLINE TYPOGRAPHY ]   (Pass-Through / 100%)
  ├── Headline Text Layer ("WHO PAYS?")    (Normal, Kerning -30)
  ├── Text Distress / Halftone Layer Mask  (Mask applied to Text)
  └── Text Cast Shadow / Paper Bleed       (Multiply, 25%)

[ GROUP 2: SECONDARY CONTEXT & DIAGRAMS ]  (Pass-Through / 100%)
  ├── Candlestick Charts / Map Outlines    (Screen or Multiply, 20-40%)
  ├── News Clippings / Polaroid Cards      (Normal, Drop Shadow 45%)
  └── Grid Coordinates / Plus Signs (`+`)  (Normal, Small Font)

[ GROUP 1: CANVAS & WALL BASE ]            (Normal / 100%)
  ├── Base Background (Parchment or Wall)  (Normal)
  └── Vignette Gradient                    (Multiply, 30-50%)
```

---

## Detailed Step-by-Step Execution Recipes

### Recipe 1: The Newsprint Halftone Screen (Screenprint Look)
1. Isolate the subject on a transparent layer.
2. Duplicate the subject layer (`Cmd + J`) and convert to Grayscale/Desaturate (`Cmd + Shift + U`).
3. Boost contrast with Levels (`Cmd + L`): Push blacks to 40, whites to 215.
4. Go to **Filter > Pixelate > Color Halftone**:
   - Max Radius: `4 to 6 pixels` (for 1080p canvas) or `8 to 12 pixels` (for 4K canvas).
   - Channel 1, 2, 3, 4: Set all to `45 degrees` (ensures uniform monochrome dots).
5. Set the Halftone layer blend mode to **Multiply** over the cream background or subject base.
6. Reduce opacity to `70% - 85%` for organic newsprint feel.

### Recipe 2: The Double-Exposure Silhouette (Jensen Huang Style)
1. Cut out the subject's silhouette cleanly.
2. Load the subject's selection (`Cmd + Click` on layer thumbnail).
3. Place the secondary scene (e.g., moody corridor, factory, boardroom) directly above the subject layer.
4. Apply the subject selection as a layer mask to the secondary scene.
5. Set the secondary scene blend mode to **Screen**, **Lighten**, or **Normal** with a gradient mask fading into the subject's face.
6. Invert or paint out the subject's eyes and key facial contours on the mask so their facial expression remains sharp and recognizable.

### Recipe 3: The Die-Cut Sticker Outline (Punk Zine Style)
1. Select the subject cutout layer.
2. Open **Layer Style > Stroke**:
   - Position: `Outside`
   - Size: `12px to 18px` (for 1080p canvas)
   - Color: Pure White (`#FFFFFF`)
3. Add **Layer Style > Drop Shadow**:
   - Blend Mode: `Multiply`
   - Opacity: `35%`
   - Distance: `8px`, Spread: `10%`, Size: `16px`
   - Angle: `120°`
4. Add a subtle torn paper texture inside the stroke or leave razor sharp for a vinyl sticker effect.

### Recipe 4: The Red Crime String / Connection Line
1. Use the **Pen Tool (P)** to draw a realistic sagging curved path between two pins, photos, or data points.
2. Set Stroke: Crimson Red (`#C8102E`), Width: `4px to 6px`.
3. Add **Layer Style > Bevel & Emboss**:
   - Style: Inner Bevel, Depth: `100%`, Size: `2px` (creates physical twine roundness).
4. Add **Layer Style > Drop Shadow**:
   - Distance: `6px`, Size: `10px`, Opacity: `40%` (casts realistic shadow onto the wall/paper beneath it).

