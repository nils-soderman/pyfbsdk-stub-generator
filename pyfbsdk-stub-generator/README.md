# MotionBuilder pyfbsdk stub-file generator
Script for generating python stub files for Autodesk MotionBuilder's pyfbsdk modules


## Usage

### Generate stub files
If you want to generate your own stub files for your MotionBuilder version:

1. Install the generator
2. Call the generator using the mobupy Python interpreter

```cmd
pip install git+https://github.com/nils-soderman/pyfbsdk-stub-generator#subdirectory=pyfbsdk-stub-generator --target="{INSTALL_LOCATION}"

cd "{INSTALL_LOCATION}"

"C:/Program Files/Autodesk/MotionBuilder {VERSION}/bin/x64/mobupy.exe" -m pyfbsdk_stub_generator "{OUTPUT_DIR}"
```

* Replace `{VERSION}` with your MotionBuilder version
* Replace `{INSTALL_LOCATION}` with your desired installation path
* Replace `{OUTPUT_DIR}` with where you want the stub files generated

### CLI Options
Optional flags that can be included when running the command to generate the stub files:
| Option | Description |
|-|-|
| `--cache` | Cache the online documentation on disk, mainly for development when you re-run the generator multiple times |