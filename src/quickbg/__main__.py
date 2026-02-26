"""
QuickBG - Lightning-fast AI background removal CLI tool.

Usage:
    quickbg input.jpg                  # Single file
    quickbg input.jpg -o output.png    # Custom output
    quickbg -b folder/                # Batch processing
    quickbg -b folder/ -o out/        # Batch with output dir
"""

import argparse
import sys
import os
from pathlib import Path
from typing import Optional

from rembg import remove
from PIL import Image

__version__ = "1.0.0"
__author__ = "Jack"


def process_image(input_path: str, output_path: Optional[str] = None, alpha_matting: bool = False) -> bool:
    """
    Remove background from a single image.
    
    Args:
        input_path: Path to input image
        output_path: Path for output image (optional)
        alpha_matting: Enable alpha matting for better edges
    
    Returns:
        True if successful, False otherwise
    """
    input_file = Path(input_path)
    
    if not input_file.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        return False
    
    # Determine output path
    if output_path is None:
        output_path = str(input_file.parent / f"{input_file.stem}-nobg.png")
    
    output_file = Path(output_path)
    
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Processing: {input_file.name}")
    
    try:
        input_image = Image.open(input_file)
        
        # Remove background
        output_image = remove(input_image, alpha_matting=alpha_matting)
        
        # Save result
        output_image.save(output_path)
        
        print(f"Saved: {output_file.name}")
        return True
        
    except Exception as e:
        print(f"Error processing {input_file.name}: {e}", file=sys.stderr)
        return False


def batch_process(input_dir: str, output_dir: Optional[str] = None, alpha_matting: bool = False) -> int:
    """
    Process all images in a directory.
    
    Args:
        input_dir: Input directory path
        output_dir: Output directory path (optional)
        alpha_matting: Enable alpha matting
    
    Returns:
        Number of successfully processed images
    """
    input_path = Path(input_dir)
    
    if not input_path.is_dir():
        print(f"Error: Not a directory: {input_dir}", file=sys.stderr)
        return 0
    
    # Supported image formats
    extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.tif'}
    
    # Find all images
    images = [f for f in input_path.iterdir() 
              if f.is_file() and f.suffix.lower() in extensions]
    
    if not images:
        print(f"No images found in {input_dir}")
        return 0
    
    # Determine output directory
    if output_dir is None:
        output_dir = str(input_path / "nobg")
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Found {len(images)} image(s) to process")
    print(f"Output directory: {output_path}")
    print("-" * 50)
    
    # Process each image
    success_count = 0
    for i, img_path in enumerate(images, 1):
        output_file = output_path / f"{img_path.stem}-nobg.png"
        
        print(f"[{i}/{len(images)}] {img_path.name}...", end=" ", flush=True)
        
        try:
            input_image = Image.open(img_path)
            output_image = remove(input_image, alpha_matting=alpha_matting)
            output_image.save(output_file)
            print("OK")
            success_count += 1
        except Exception as e:
            print(f"FAILED: {e}")
    
    print("-" * 50)
    print(f"Done! {success_count}/{len(images)} images processed successfully")
    
    return success_count


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="quickbg",
        description="⚡ Lightning-fast AI background removal CLI tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s photo.jpg                           Remove background from image
  %(prog)s photo.jpg -o result.png             Specify output filename
  %(prog)s -b ./photos/                        Batch process folder
  %(prog)s -b ./photos/ -o ./output/            Batch with custom output dir
  %(prog)s photo.jpg --alpha-matting           Better edge refinement

For more info: https://github.com/jack/quickbg
        """
    )
    
    parser.add_argument(
        "input",
        nargs="?",
        help="Input image file or directory (with -b/--batch)"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output file or directory"
    )
    
    parser.add_argument(
        "-b", "--batch",
        action="store_true",
        help="Batch mode: process all images in directory"
    )
    
    parser.add_argument(
        "-a", "--alpha-matting",
        action="store_true",
        help="Enable alpha matting for better edge refinement (slower)"
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="%(prog)s v1.0.0"
    )
    
    args = parser.parse_args()
    
    # Handle no arguments
    if args.input is None:
        parser.print_help()
        sys.exit(1)
    
    # Process based on mode
    if args.batch:
        batch_process(args.input, args.output, args.alpha_matting)
    else:
        success = process_image(args.input, args.output, args.alpha_matting)
        if not success:
            sys.exit(1)


if __name__ == "__main__":
    main()
