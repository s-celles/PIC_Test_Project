#!/usr/bin/env python3
"""
Compilation script for PIC16F876A using xc8-wrapper
"""

import sys
import argparse
from pathlib import Path

try:
    from xc8_wrapper import get_xc8_tool_path, run_command, log
except ImportError as e:
    print(f"❌ Cannot import xc8_wrapper: {e}")
    print("🔄 Using xc8-wrapper compilation required...")
    sys.exit(1)

# Project configuration
PROJECT_NAME = "pic_test_project"
TARGET_CHIP = "PIC16F876A"
SOURCE_DIR = Path("src/multi")
OUTPUT_DIR = Path("output")
BUILD_DIR = Path("build")


def setup_environment():
    """Configure environment for xc8-wrapper"""
    # Add xc8-wrapper to Python path
    xc8_wrapper_path = Path.cwd() / "xc8-wrapper"
    if str(xc8_wrapper_path) not in sys.path:
        sys.path.insert(0, str(xc8_wrapper_path))

    # Create output directories
    OUTPUT_DIR.mkdir(exist_ok=True)
    BUILD_DIR.mkdir(exist_ok=True)


def find_source_files():
    """Find all C source files"""
    source_files = list(SOURCE_DIR.glob("*.c"))
    print(f"Source files found: {[str(f) for f in source_files]}")
    return source_files


def compile_with_xc8_wrapper_direct(
    optimization_level="2", xc8_version="3.00", separate_compilation=True
):
    """Compile project using xc8-wrapper module directly (not subprocess)"""

    # Configure environment
    setup_environment()

    # Find source files
    source_files = find_source_files()

    if not source_files:
        print("No source files found in", SOURCE_DIR)
        return False

    print("🔨 Compilation with xc8-wrapper module:")
    print(f"  Sources: {len(source_files)} files")
    print(f"  Mode: {'separate' if separate_compilation else 'monolithic'}")
    print(f"  Optimization: {optimization_level}")
    print()

    try:
        # Configuration for compilation
        output_file = OUTPUT_DIR / f"{PROJECT_NAME}.hex"

        if separate_compilation:
            return compile_separate_with_xc8_wrapper(
                source_files, output_file, optimization_level, xc8_version
            )
        else:
            return compile_monolithic_with_xc8_wrapper(
                source_files, output_file, optimization_level, xc8_version
            )

    except Exception as e:
        print(f"❌ Error with xc8-wrapper: {e}")
        print("🔄 Check xc8-wrapper installation...")
        return False


def compile_separate_with_xc8_wrapper(
    source_files, output_file, optimization_level, xc8_version
):
    """Separate compilation using xc8-wrapper module"""

    try:
        # Get path to XC8
        xc8_cc_path, version_info = get_xc8_tool_path("cc", xc8_version)
        log.info(f"✓ XC8 CC found: {version_info}")

        print("🔨 Separate compilation with xc8-wrapper:")
        print(f"  Tool: {xc8_cc_path}")
        print(f"  Version: {version_info}")
        print()

        # Step 1: Separate compilation
        object_files = []

        for i, source_file in enumerate(source_files, 1):
            print(f"📄 Step {i}/{len(source_files)}: Compiling {source_file.name}")

            object_file = BUILD_DIR / f"{source_file.stem}.p1"
            object_files.append(object_file)

            # Build compilation arguments
            compile_args = [
                xc8_cc_path,
                f"-mcpu={TARGET_CHIP}",
                "-c",  # Compile only
                f"-O{optimization_level}",
                "-std=c99",
                "-Wall",
                f"-D_XTAL_FREQ=4000000UL",
                "-o",
                str(object_file),
                str(source_file),
            ]

            # Use run_command from xc8-wrapper module
            if not run_command(compile_args, f"Compiling {source_file.name}"):
                print(f"   ❌ Compilation error {source_file.name}")
                return False

            print(f"   ✅ {source_file.name} → {object_file.name}")

        print()

        # Step 2: Linking
        print(f"🔗 Step {len(source_files) + 1}: Linking object files")

        elf_file = BUILD_DIR / f"{PROJECT_NAME}.elf"
        map_file = BUILD_DIR / f"{PROJECT_NAME}.map"

        link_args = [
            xc8_cc_path,
            f"-mcpu={TARGET_CHIP}",
            f"-O{optimization_level}",
            "-std=c99",
            f"-Wl,-Map={map_file}",
            f"--memorysummary={BUILD_DIR}/memory_summary.xml",
            "-o",
            str(elf_file),
        ]

        # Add all object files
        for obj_file in object_files:
            link_args.append(str(obj_file))

        # Use run_command from xc8-wrapper module
        if not run_command(link_args, "Linking"):
            print("   ❌ Linking error")
            return False

        print(f"   ✅ Linking successful → {elf_file.name}")

        # Step 3: Copy HEX file
        generated_hex = BUILD_DIR / f"{PROJECT_NAME}.hex"
        if generated_hex.exists():
            import shutil

            shutil.copy2(generated_hex, output_file)
            print(f"   📦 HEX copied → {output_file}")

        print("\n✅ Separate compilation with xc8-wrapper completed!")
        return True

    except Exception as e:
        print(f"❌ Error in separate compilation: {e}")
        return False


def compile_monolithic_with_xc8_wrapper(
    source_files, output_file, optimization_level, xc8_version
):
    """Monolithic compilation using xc8-wrapper module"""

    try:
        # Get path to XC8
        xc8_cc_path, version_info = get_xc8_tool_path("cc", xc8_version)
        log.info(f"✓ XC8 CC found: {version_info}")

        print("🔨 Monolithic compilation with xc8-wrapper:")
        print(f"  Tool: {xc8_cc_path}")
        print(f"  Version: {version_info}")
        print()

        # Build compilation arguments
        compile_args = [
            xc8_cc_path,
            f"-mcpu={TARGET_CHIP}",
            f"-O{optimization_level}",
            "-std=c99",
            "-Wall",
            f"-D_XTAL_FREQ=4000000UL",
            f"-o{output_file}",
        ]

        # Add all source files
        for src in source_files:
            compile_args.append(str(src))

        # Use run_command from xc8-wrapper module
        if not run_command(compile_args, "Compiling project"):
            print("❌ Monolithic compilation error")
            return False

        print("✅ Monolithic compilation with xc8-wrapper completed!")
        return True

    except Exception as e:
        print(f"❌ Error in monolithic compilation: {e}")
        return False


def clean():
    """Clean generated files"""
    import shutil

    dirs_to_clean = [OUTPUT_DIR, BUILD_DIR]

    for directory in dirs_to_clean:
        if directory.exists():
            shutil.rmtree(directory)
            print(f"Cleaned: {directory}")

    print("✅ Cleanup completed!")


def main():
    parser = argparse.ArgumentParser(
        description="PIC16F876A compilation with xc8-wrapper"
    )
    parser.add_argument(
        "--optimization", "-O", default="2", help="Optimization level (0-3)"
    )
    parser.add_argument("--xc8-version", default="3.00", help="XC8 version to use")
    parser.add_argument(
        "--clean", "-c", action="store_true", help="Clean generated files"
    )

    # Mutually exclusive group for compilation mode
    compilation_mode = parser.add_mutually_exclusive_group()
    compilation_mode.add_argument(
        "--separate",
        action="store_true",
        default=True,
        help="Use separate compilation (default)",
    )
    compilation_mode.add_argument(
        "--monolithic", action="store_true", help="Use monolithic compilation"
    )

    args = parser.parse_args()

    if args.clean:
        clean()
        return

    print(f"🔨 Compilation for {TARGET_CHIP}")
    print(f"Method: xc8-wrapper")
    print(f"Optimization: {args.optimization}")
    print()

    # Determine compilation mode (default: separate)
    separate_mode = (
        not args.monolithic
    )  # If --monolithic is specified, separate_mode = False

    success = compile_with_xc8_wrapper_direct(
        args.optimization, args.xc8_version, separate_mode
    )

    if success:
        print("\n🎉 Compilation completed successfully!")
    else:
        print("\n💥 Compilation failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
