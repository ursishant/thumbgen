#!/usr/bin/env python3
"""
remove_watermark.py - Automated AI Watermark Remover & Texture Inpainter.

Seamlessly inpaints and eliminates the 4-pointed sparkle (SynthID / Gemini)
watermark from Google Flow and Imagen generations using OpenCV Telea inpainting.
Restores native film grain, paper fibers, and concrete/industrial textures
without blurring or leaving visible seams.

Requirements:
    pip install opencv-python numpy
"""

import sys
import os
import glob
import argparse
from typing import Optional, List

try:
    import cv2
    import numpy as np
except ImportError:
    print(
        "❌ Error: Required dependencies missing.\n"
        "   Please install opencv-python and numpy via:\n"
        "       pip install opencv-python numpy\n"
    )
    sys.exit(1)


def remove_watermark(
    image_path: str,
    output_path: Optional[str] = None,
    roi_size: int = 220,
    thresh_offset: int = 35,
    inpaint_radius: int = 5,
    quality: int = 98,
    verbose: bool = True,
) -> bool:
    """
    Detects and inpaints the 4-pointed star watermark in the bottom-right corner.

    Args:
        image_path: Path to the input image.
        output_path: Path where the cleaned image will be saved (overwrites input if None).
        roi_size: Dimension (width and height in px) of search region from bottom-right.
        thresh_offset: Brightness offset above local median to isolate the watermark sparkle.
        inpaint_radius: Radius for OpenCV Telea neighborhood inpainting.
        quality: JPEG export quality (1-100).
        verbose: Whether to log output to console.

    Returns:
        bool: True if watermark was processed and saved, False otherwise.
    """
    if output_path is None:
        output_path = image_path

    if not os.path.isfile(image_path):
        if verbose:
            print(f"❌ File not found: {image_path}")
        return False

    try:
        img = cv2.imread(image_path)
        if img is None:
            if verbose:
                print(f"❌ Could not decode image: {image_path}")
            return False

        h, w, _ = img.shape
        mask = np.zeros((h, w), dtype=np.uint8)

        # Region of Interest: Bottom-right corner
        roi_y1 = max(0, h - roi_size)
        roi_x1 = max(0, w - roi_size)
        roi = img[roi_y1:h, roi_x1:w]

        # Grayscale conversion & dynamic thresholding
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        local_median = np.median(gray)
        thresh_val = max(60, int(local_median + thresh_offset))
        _, thresh = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)

        # Morphological dilation to encompass star tips
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        thresh_dilated = cv2.dilate(thresh, kernel)

        mask[roi_y1:h, roi_x1:w] = thresh_dilated

        # Mathematical Telea inpainting
        inpainted = cv2.inpaint(img, mask, inpaintRadius=inpaint_radius, flags=cv2.INPAINT_TELEA)

        # Ensure parent directories exist
        out_dir = os.path.dirname(output_path)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)

        ext = os.path.splitext(output_path)[1].lower()
        if ext in [".jpg", ".jpeg"]:
            cv2.imwrite(output_path, inpainted, [cv2.IMWRITE_JPEG_QUALITY, quality])
        else:
            cv2.imwrite(output_path, inpainted)

        if verbose:
            print(f"✅ Cleaned watermark: {os.path.basename(image_path)} -> {output_path}")
        return True

    except Exception as e:
        if verbose:
            print(f"❌ Failed to process {image_path}: {e}")
        return False


def collect_images(path: str) -> List[str]:
    """Collects valid image file paths from a file, directory, or glob pattern."""
    valid_exts = {".jpg", ".jpeg", ".png", ".webp"}
    if os.path.isdir(path):
        results = []
        for root, _, files in os.walk(path):
            for f in sorted(files):
                if os.path.splitext(f)[1].lower() in valid_exts:
                    results.append(os.path.join(root, f))
        return results
    elif "*" in path:
        return [f for f in glob.glob(path) if os.path.splitext(f)[1].lower() in valid_exts]
    elif os.path.isfile(path):
        return [path]
    return []


def main():
    parser = argparse.ArgumentParser(
        description="Automated AI watermark remover and texture inpainter for Google Flow & Imagen generations.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("input", help="Image path, directory, or glob pattern to process.")
    parser.add_argument("-o", "--output", help="Output file path or target directory (overwrites input if omitted).")
    parser.add_argument("-r", "--radius", type=int, default=5, help="Telea inpainting radius in pixels.")
    parser.add_argument("-q", "--quality", type=int, default=98, help="JPEG export quality (1-100).")
    parser.add_argument("--roi-size", type=int, default=220, help="Bottom-right search area dimension (px).")
    parser.add_argument("-q-quiet", "--quiet", action="store_true", help="Suppress output logging.")

    args = parser.parse_args()

    files = collect_images(args.input)
    if not files:
        print(f"❌ No valid images found matching: {args.input}")
        sys.exit(1)

    verbose = not args.quiet
    if verbose:
        print(f"🔍 Found {len(files)} image(s) to process...\n")

    count = 0
    for f in files:
        target_out = None
        if args.output:
            if os.path.isdir(args.output) or len(files) > 1:
                target_out = os.path.join(args.output, os.path.basename(f))
            else:
                target_out = args.output

        success = remove_watermark(
            f,
            output_path=target_out,
            roi_size=args.roi_size,
            inpaint_radius=args.radius,
            quality=args.quality,
            verbose=verbose,
        )
        if success:
            count += 1

    if verbose:
        print(f"\n✨ Successfully cleaned {count}/{len(files)} image(s).")


if __name__ == "__main__":
    main()
