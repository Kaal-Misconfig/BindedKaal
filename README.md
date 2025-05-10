# BindedKaal

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.1-green.svg)](https://github.com/kaal-misconfig/bindedkaal)
[![Platform](https://img.shields.io/badge/Platform-Linux-red.svg)](https://github.com/kaal-misconfig/bindedkaal)

<div align="center">
  <img src="https://raw.githubusercontent.com/Kaal-Misconfig/BindedKaal/f79cb562923c421f26d926caaaa5beab9292f21c/bindedkaal-logo.svg?token=BQV3H44T5CJ2WN4QE2E63VLID4Y4K" alt="BindedKaal Logo" width="300"/>
  <h3>Advanced PDF Payload Binding Tool</h3>
</div>

## Overview

BindedKaal is a sophisticated tool designed for cybersecurity professionals and penetration testers that enables seamless binding of executable payloads to PDF files while maintaining complete PDF functionality. This tool provides an efficient method for security assessments in controlled environments.

## Features

- **Seamless Binding** - Integrate payloads with PDF files while preserving all PDF functionality
- **Multiple Payload Support** - Compatible with various file formats including `.exe`, `.py`, `.vbs`, `.sh`, and more
- **Stealth Operation** - Clean execution with automatic file handling and temporary file management
- **User-Friendly Interface** - Intuitive command-line interface with clear instructions
- **Lightweight Design** - Minimal dependencies for efficient operation and quick execution
- **Platform Support** - Optimized for Linux environments

## Installation

### Prerequisites

- Python 3.6+
- Required libraries (see [Dependencies](#dependencies))

### Method 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/kaal-misconfig/bindedkaal.git

# Navigate to the directory
cd bindedkaal

# Install dependencies
pip install -r requirements.txt

# Make the script executable
chmod +x bindedkaal.py
```

### Method 2: Direct Download

Download the latest release from the [releases page](https://github.com/kaal-misconfig/bindedkaal/releases).

## Usage

### Basic Operation

```bash
python bindedkaal.py
```

The interactive menu will guide you through:

1. Selecting a PDF file
2. Selecting a payload file
3. Binding the files together

### Command Line Arguments

```bash
python bindedkaal.py --pdf [PDF_PATH] --payload [PAYLOAD_PATH] --output [OUTPUT_NAME]
```

### Example

```bash
python bindedkaal.py --pdf documents/report.pdf --payload scripts/payload.py --output secret_document.pdf
```

## How It Works

BindedKaal operates by:

1. Analyzing the input PDF structure
2. Appending payload data with special markers
3. Creating a self-extracting mechanism that preserves PDF rendering
4. Implementing efficient temporary file handling for clean execution

The process ensures that the resulting file opens normally in PDF readers while executing the payload when appropriate conditions are met.

## Dependencies

```
pdfminer>=20221105
pyPDF2>=3.0.0
colorama>=0.4.6
tqdm>=4.65.0
argparse>=1.4.0
```

## Advanced Configuration

### Custom Settings

You can create a `config.json` file in the root directory with the following options:

```json
{
  "default_output_dir": "./output",
  "cleanup_temp": true,
  "encryption_level": "medium",
  "verbose_logging": false
}
```

### Plugin System

BindedKaal supports plugins for custom payload handling. Place your plugins in the `plugins/` directory.

```python
# Example plugin: custom_handler.py
from bindedkaal.plugin import BinderPlugin

class CustomHandler(BinderPlugin):
    def __init__(self):
        super().__init__("custom", [".bin", ".dat"])
        
    def process(self, payload_path, pdf_path):
        # Custom implementation
        pass
```

## Security Considerations

This tool is intended for educational purposes and legitimate security testing only. Always:

- Obtain proper authorization before testing
- Use in controlled environments
- Follow responsible disclosure practices
- Adhere to applicable laws and regulations

## Troubleshooting

### Common Issues

1. **PDF Compatibility Issues**
   - Solution: Use the `--compatibility-mode` flag

2. **Execution Errors**
   - Solution: Check payload permissions and dependencies

3. **Size Limitations**
   - Solution: Use the `--chunk-size` parameter for large files

For additional help, please [open an issue](https://github.com/kaal-misconfig/bindedkaal/issues).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PDF Specification](https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/PDF32000_2008.pdf)
- [Python PDF Libraries](https://pypi.org/project/PyPDF2/)
- All contributors and testers

## About the Creator

**Kaal-Misconfig** - Student Learning Offensive Pentesting, specializing in cybersecurity, file analysis, and offensive penetration testing.

- [GitHub](https://github.com/kaal-misconfig)
- [Twitter](https://x.com/kaalmisconfig)
- [LinkedIn](https://www.linkedin.com/in/pranav-bokade-643320328/)

<div align="center">
  <p>© 2025 BindedKaal by Kaal-Misconfig. All rights reserved.</p>
  <img src="assets/footer.png" alt="Footer" width="200"/>
</div>
