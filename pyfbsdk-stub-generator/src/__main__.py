try:
    import pyfbstandalone
except ImportError:
    raise RuntimeError("This module must run in the mobupy.exe interpreter")

# MotionBuilder 2025+ requires an explicit initialization of the pyfbsdk module

import argparse
import os

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate stubs for MotionBuilder Python API. This module must run in the mobupy interpreter")

    parser.add_argument("out_dir", type=str, help="Output directory for the generated stubs")
    parser.add_argument(
        "--cache",
        action="store_true",
        help="Cache downloaded documentation to disk"
    )

    args = parser.parse_args()

    output_path = os.path.abspath(args.out_dir)

    # Initialize pyfbsdk before importing any other modules that depend on it
    pyfbstandalone.initialize()

    from . import stub_generator, manual_stubs
    from .flags import GeneratorFlag

    flags = GeneratorFlag.NONE
    if args.cache:
        flags |= GeneratorFlag.CACHE

    pyfbsdk_filepath = os.path.join(output_path, "pyfbsdk.pyi")

    stub_generator.GeneratePyfbsdkStubFile(pyfbsdk_filepath, flags)
    manual_stubs.CopyManualStubs(output_path)


if __name__ == "__main__":
    main()
