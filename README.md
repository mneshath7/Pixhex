# Pixhex
Image authentication &amp; AI manipulation detection tool. Detect AI-generated images and photo manipulations using advanced signal processing.

How It Works

Pipeline Stages
Raw Data Input: Load image as RGB numpy array
Tiered Blur Cascade: Apply successive Gaussian filtering
Anchor Point Detection: Identify and analyze suspicious pixel patterns
Conditional Logic: Evaluate anomalies using geometric analysis
Turing Pattern Analysis: Localized variance analysis for synthetic uniformity
API Reference
image_forgery_detection_pipeline(image_path, embed=False, use_legacy_triangulation=False)
Main entry point for image analysis.

Parameters:

image_path (str): Path to the image file
embed (bool): If True, embeds authentication markers instead of detecting
use_legacy_triangulation (bool): Use legacy triangulation-based analysis
Returns:

"SAFE": Image appears authentic
"SUSPICIOUS": Potential manipulation detected
"NO ANCHORS": Insufficient data for analysis
numpy array: If embed=True, returns image with embedded markers
Other Functions
tiered_blur_cascade(image): Multi-level Gaussian filtering
identify_edit_probable_regions(image, threshold=50): Edge-based region detection
embed_anchor_points(image, shift_amount=1): Embed authentication markers
detect_anchor_points(image, shift_amount=1, tolerance=0.5): Verify embedded markers
turing_pattern_analysis(image, grid_size=20, var_threshold=50): Variance-based anomaly detection 

Limitations & Future Work
Currently optimized for standard RGB images
Performance depends on image resolution
Requires fine-tuning for specific use cases
Future: Deep learning integration, batch processing optimization
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.

You are free to use, modify, and distribute this software, provided you:

Include a copy of the MIT license
Credit the original author (mneshath7)
Maintain this notice in any derivative works
Author
mneshath7

Disclaimer
This tool is provided for educational and research purposes. Users are responsible for complying with local laws and ethical guidelines when using this software.

Support & Issues
Found a bug? Have a feature request? Please open an issue.

Made with ❤️ for the open-source community
