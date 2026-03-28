import argparse
import os


try:
    import pyfbstandalone
except ModuleNotFoundError:
    raise RuntimeError("This module must run in the mobupy.exe interpreter")


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

    from .flags import GeneratorFlag

    flags = GeneratorFlag.NONE
    if args.cache:
        flags |= GeneratorFlag.CACHE

    from . import generate
    generate(output_path, flags=flags)


if __name__ == "__main__":
    main()
