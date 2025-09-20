# MotionBuilder pyfbsdk stub-file generator
Script for generating python stub files for Autodesk MotionBuilder's pyfbsdk modules

# Usage

## Generate stub files
If you want to generate your own stub files for your MotionBuilder version:

1. Install this package using pip:
```cmd
pip install git+https://github.com/nils-soderman/pyfbsdk-stub-generator#subdirectory=pyfbsdk-stub-generator
```

2. From within MotionBuilder, run:
```python
import pyfbsdk_stub_generator

pyfbsdk_stub_generator.Generate(Directory = "C:/MyDirectory/")
```