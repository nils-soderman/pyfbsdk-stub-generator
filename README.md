# MotionBuilder pyfbsdk stub-file generator
Script for generating python stub files for Autodesk MotionBuilder's pyfbsdk module.

These stub files include all classes & functions that can be accessed through the pyfbsdk module.
They also include type hints and docstrings for most entities.


<br>


# Pre-generated files
The GitHub repository already contains some pre-generated stub files that are ready to be used, simply get them from the [generated-stub-files](https://github.com/nils-soderman/pyfbsdk-stub-generator/tree/main/generated-stub-files) folder:
* [MotionBuilder 2025](https://github.com/nils-soderman/pyfbsdk-stub-generator/tree/main/generated-stub-files/motionbuilder-2025)
* [MotionBuilder 2024](https://github.com/nils-soderman/pyfbsdk-stub-generator/tree/main/generated-stub-files/motionbuilder-2024)
* [MotionBuilder 2023](https://github.com/nils-soderman/pyfbsdk-stub-generator/tree/main/generated-stub-files/motionbuilder-2023)
* [MotionBuilder 2022](https://github.com/nils-soderman/pyfbsdk-stub-generator/tree/main/generated-stub-files/motionbuilder-2022)

<br>

# Usage

## Generate stub files
If you want to generate your own stub files for your MotionBuilder version:

1. Install the module through pip:
```cmd
python -m pip install pyfbsdk-stub-generator
```

2. From within MotionBuilder, run:
```python
import pyfbsdk_stub_generator

pyfbsdk_stub_generator.Generate(Directory = "C:/MyDirectory/")
```

<br>

# Application Spesific Setup

## Visual Studio Code

These stub files comes bundeled with the [MotionBuilder Utils](https://marketplace.visualstudio.com/items?itemName=NilsSoderman.mobu-utils) VSCode extention.