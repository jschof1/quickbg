<p align="center">
  <img src="logo.png" alt="QuickBG Logo" width="200"/>
</p>

<h1 align="center">⚡ QuickBG</h1>

<p align="center">
  <a href="https://pypi.org/project/quickbg/">
    <img src="https://img.shields.io/pypi/v/quickbg?color=6328d6&style=flat-square" alt="PyPI Version"/>
  </a>
  <a href="https://pypi.org/project/quickbg/">
    <img src="https://img.shields.io/pypi/dm/quickbg?color=6328d6&style=flat-square" alt="PyPI Downloads"/>
  </a>
  <a href="https://github.com/jschof1/quickbg/blob/main/LICENSE">
    <img src="https://img.shields.io/pypi/l/quickbg?color=6328d6&style=flat-square" alt="License"/>
  </a>
  <a href="https://github.com/jschof1/quickbg/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/jack/quickbg/test.yml?color=6328d6&style=flat-square" alt="Build Status"/>
  </a>
  <a href="https://twitter.com/intent/tweet?text=Check+out+QuickBG+-+Lightning-fast+AI+background+removal+for+images+%F0%9F%9A%80&url=https%3A%2F%2Fgithub.com%2Fjack%2Fquickbg">
    <img src="https://img.shields.io/twitter/url?color=6328d6&style=flat-square" alt="Tweet"/>
  </a>
</p>

<p align="center">
  <strong>Lightning-fast AI background removal CLI tool for Mac, Linux, and Windows</strong>
</p>

---

## ✨ Features

- 🚀 **Blazing Fast** - Process images in seconds using state-of-the-art AI
- 🔒 **Private & Secure** - Runs entirely locally on your machine
- 🎯 **High Quality** - Produces clean cutouts with excellent edge handling
- 📦 **Batch Processing** - Process entire folders with a single command
- 🔧 **Zero Config** - Works out of the box with sensible defaults
- 🍎 **Mac Optimized** - Native macOS support with pipx installation

## 📸 Example

```bash
# Remove background from a single image
$ quickbg photo.jpg
Processing: photo.jpg
Saved: photo-nobg.png

# With custom output
$ quickbg product.png -o cleaned.png

# Batch process a folder
$ quickbg -b ./productPhotos/
Found 25 image(s) to process
Output directory: ./productPhotos/nobg
--------------------------------------------------
[1/25] img_001.jpg... OK
[2/25] img_002.jpg... OK
...
--------------------------------------------------
Done! 25/25 images processed successfully
```

## 🖼️ Before & After

| Before                                                                                             | After                                                                                         |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| ![Product with background](https://via.placeholder.com/300x300/cccccc/666666?text=With+Background) | ![Product no background](https://via.placeholder.com/300x300/000000/ffffff?text=Clean+Cutout) |

## 📥 Installation

### macOS (Recommended)

```bash
# Install pipx if you don't have it
brew install pipx

# Install QuickBG
pipx install quickbg
```

### Linux

```bash
pipx install quickbg
```

### Windows

```powershell
pipx install quickbg
```

### Using pip (All Platforms)

```bash
pip install quickbg
```

### From Source

```bash
git clone https://github.com/jschof1/quickbg.git
cd quickbg
pip install -e .
```

## 🔧 Usage

### Single Image Mode

```bash
# Basic usage (saves as filename-nobg.png)
quickbg input.jpg

# Specify output filename
quickbg input.png -o result.png

# Enable alpha matting for better edges (slower)
quickbg input.jpg --alpha-matting
```

### Batch Processing Mode

```bash
# Process all images in a folder
quickbg -b ./photos/

# Specify output directory
quickbg -b ./photos/ -o ./output/

# With alpha matting
quickbg -b ./photos/ -a
```

### Supported Formats

- Input: JPG, JPEG, PNG, WebP, BMP, TIFF, TIF
- Output: PNG (with transparency)

## ⚙️ Options

| Flag                  | Description                                     |
| --------------------- | ----------------------------------------------- |
| `input`               | Input image file or directory                   |
| `-o, --output`        | Output file or directory path                   |
| `-b, --batch`         | Batch mode: process all images in directory     |
| `-a, --alpha-matting` | Enable alpha matting for better edge refinement |
| `-v, --version`       | Show version number                             |
| `-h, --help`          | Show help message                               |

## 🔨 Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/jschof1/quickbg.git
cd quickbg

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/ tests/

# Lint code
ruff check src/ tests/
```

### Run Tests

```bash
pytest tests/ -v
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) first.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) - The amazing AI background removal library
- [U-2-Net](https://github.com/xuanlinliha/U2-Net) - The underlying deep learning model

## 📊 Stats

![Alt](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjack%2Fquickbg&count_bg=%236328D6&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=views&edge_flat=false)

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/jschof1">Jack Schofield</a>
</p>
