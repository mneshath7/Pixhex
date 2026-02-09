## Pixhex
Image authentication &amp; AI manipulation detection tool. Detect AI-generated images and photo manipulations using advanced signal processing.


## Quick Start

```python
from pixhex import image_forgery_detection_pipeline

# Analyze an image for manipulations
result = image_forgery_detection_pipeline('path/to/image.jpg')
print(result)  # Output: "SAFE" or "SUSPICIOUS"

# Embed authentication anchors
embedded = image_forgery_detection_pipeline('path/to/image.jpg', embed=True)

# Use legacy triangulation method
result = image_forgery_detection_pipeline('path/to/image.jpg', use_legacy_triangulation=True)
```

## How It Works

### Pipeline Stages

1. **Raw Data Input**: Load image as RGB numpy array
2. **Tiered Blur Cascade**: Apply successive Gaussian filtering
3. **Anchor Point Detection**: Identify and analyze suspicious pixel patterns
4. **Conditional Logic**: Evaluate anomalies using geometric analysis
5. **Turing Pattern Analysis**: Localized variance analysis for synthetic uniformity

## API Reference

### `image_forgery_detection_pipeline(image_path, embed=False, use_legacy_triangulation=False)`
Main entry point for image analysis.

**Parameters:**
- `image_path` (str): Path to the image file
- `embed` (bool): If True, embeds authentication markers instead of detecting
- `use_legacy_triangulation` (bool): Use legacy triangulation-based analysis

**Returns:**
- `"SAFE"`: Image appears authentic
- `"SUSPICIOUS"`: Potential manipulation detected
- `"NO ANCHORS"`: Insufficient data for analysis
- numpy array: If embed=True, returns image with embedded markers

### Other Functions

- `tiered_blur_cascade(image)`: Multi-level Gaussian filtering
- `identify_edit_probable_regions(image, threshold=50)`: Edge-based region detection
- `embed_anchor_points(image, shift_amount=1)`: Embed authentication markers
- `detect_anchor_points(image, shift_amount=1, tolerance=0.5)`: Verify embedded markers
- `turing_pattern_analysis(image, grid_size=20, var_threshold=50)`: Variance-based anomaly detection

## Examples

### Basic Detection
```python
from pixhex import image_forgery_detection_pipeline

result = image_forgery_detection_pipeline('my_image.jpg')
if result == "SUSPICIOUS":
    print("⚠️ Potential manipulation detected!")
else:
    print("✅ Image appears authentic")
```

### Batch Processing
```python
import os
from pixhex import image_forgery_detection_pipeline

image_dir = './images'
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg'):
        result = image_forgery_detection_pipeline(os.path.join(image_dir, filename))
        print(f"{filename}: {result}")
```

## Limitations & Future Work

- Currently optimized for standard RGB images
- Performance depends on image resolution
- Requires fine-tuning for specific use cases
- Future: Deep learning integration, batch processing optimization

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software, provided you:
- Include a copy of the MIT license
- **Credit the original author (mneshath7)**
- Maintain this notice in any derivative works

## Author

**mneshath7**

## Disclaimer

This tool is provided for educational and research purposes. Users are responsible for complying with local laws and ethical guidelines when using this software.

## Support & Issues

Found a bug? Have a feature request? Please [open an issue](https://github.com/mneshath7/pixhex/issues).

---

Made with ❤️ for the open-source community
```

```txt name=requirements.txt
numpy>=1.21.0
scipy>=1.7.0
Pillow>=8.0.0
matplotlib>=3.3.0
```

```markdown name=LICENSE
MIT License

Copyright (c) 2026 mneshath7

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE OR ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

ATTRIBUTION REQUIREMENT:
Any use, modification, or distribution of this software must credit the original 
author mneshath7. This is a condition of use under the MIT License terms above.
```

```python name=.gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Virtual environments
venv/
ENV/
env/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
test_images/
output/
*.jpg
*.png
*.jpeg
```

## Next Steps

1. **Create the repository** on GitHub using the web interface
2. **Clone it locally**:
   ```bash
   git clone https://github.com/mneshath7/pixhex.git
   cd pixhex
   ```

3. **Add the files** above to your repository

4. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit: Add pixhex image authentication tool"
   git push origin main
   ```

5. **Optional - Add topics** in repository settings: `image-detection`, `ai-detection`, `forgery-detection`, `python`, `open-source`

