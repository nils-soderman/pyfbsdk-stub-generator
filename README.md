# MotionBuilder pyfbsdk stub-file generator
Script for generating more complete python stub files for Autodesk MotionBuilder's pyfbsdk modules.


<br>

# Usage

## Pre-generated files
This repository already contains some pre-generated stub files that are ready to be used, simply get them from the [generated-stub-files](https://github.com/nils-soderman/pyfbsdk-stub-generator/tree/main/generated-stub-files) folder:
* [MotionBuilder 2022](https://github.com/nils-soderman/pyfbsdk-stub-generator/tree/main/generated-stub-files/motionbuilder-2022)

<br>

## Generate stub files
If you want to generate your own stub files for the MotionBuilder version you're using:
```python
import pyfbsdk_stub_generator as stubGenerator

outputDirectory = "C:/Temp/"
stubGenerator.GenerateMotionBuilderStubFiles(outputDirectory)
```

<br>

# Application Spesific Setup

## Visual Studio Code

These stub files comes bundeled with the [MotionBuilder Utils VSCode extention](https://marketplace.visualstudio.com/items?itemName=NilsSoderman.mobu-utils).

Or if you wish to setup these stub files for VSCode manually:
1. Download the pre-generated stub files or generate your own as described above.
2. [Insert text here...]