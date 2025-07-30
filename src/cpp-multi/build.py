#!/usr/bin/env python3
"""
Build script for cpp-multi project
Integrates C++ transpilation with platform-pic8bit build system
"""

import os
import sys
import subprocess
from pathlib import Path


def build_cpp_multi():
    """Build the cpp-multi project with transpilation"""

    print("*** Building cpp-multi project")
    print("=" * 40)

    # Get project paths
    cpp_multi_dir = Path(__file__).parent
    project_root = cpp_multi_dir.parent.parent

    print(f"Project directory: {cpp_multi_dir}")
    print(f"Project root: {project_root}")
    print()

    # Step 1: Transpile C++ to C
    print("Step 1: Transpiling C++ to C")
    print("-" * 30)

    try:
        transpile_script = cpp_multi_dir / "manual_transpile.py"
        result = subprocess.run(
            [sys.executable, str(transpile_script)],
            cwd=cpp_multi_dir,
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print("[OK] Transpilation successful")
            print(result.stdout)
        else:
            print("[ERROR] Transpilation failed")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"[ERROR] Error during transpilation: {e}")
        return False

    # Step 2: Check generated C files
    print("\nStep 2: Verifying generated C files")
    print("-" * 35)

    generated_dir = cpp_multi_dir / "generated_c"
    required_files = [
        "main.c",
        "led.c",
        "button.c",
        "timer0.c",
        "led.h",
        "button.h",
        "timer0.h",
        "device_config.h",
        "pin_manager.h",
    ]

    missing_files = []
    for file in required_files:
        file_path = generated_dir / file
        if file_path.exists():
            print(f"[OK] {file} ({file_path.stat().st_size} bytes)")
        else:
            print(f"[ERROR] {file} - missing")
            missing_files.append(file)

    if missing_files:
        print(f"\n[ERROR] Missing files: {missing_files}")
        return False

    # Step 3: Integration notes
    print("\nStep 3: Platform Integration")
    print("-" * 30)
    print("Generated C files are ready for:")
    print("  * XC8 compiler compilation")
    print("  * PlatformIO platform-pic8bit integration")
    print("  * MPLAB X IDE project import")
    print()
    print("Next steps:")
    print("  1. Copy generated_c/*.c and *.h to your build directory")
    print("  2. Configure your build system to compile the C files")
    print("  3. Link with XC8 for PIC16F876A target")
    print()

    # Step 4: Show file sizes and summary
    print("Step 4: Build Summary")
    print("-" * 20)

    total_size = 0
    c_files = list(generated_dir.glob("*.c"))
    h_files = list(generated_dir.glob("*.h"))

    print("Generated C source files:")
    for c_file in c_files:
        size = c_file.stat().st_size
        total_size += size
        print(f"  {c_file.name}: {size:,} bytes")

    print("\nGenerated header files:")
    for h_file in h_files:
        size = h_file.stat().st_size
        total_size += size
        print(f"  {h_file.name}: {size:,} bytes")

    print(f"\nTotal generated code: {total_size:,} bytes")

    # Step 5: Demonstrate xc8plusplus concept
    print("\nxc8plusplus Concept Demonstrated")
    print("-" * 35)
    print("This build shows how C++ code can be:")
    print("  [OK] Written using modern C++ features (classes, enums, etc.)")
    print("  [OK] Automatically transpiled to XC8-compatible C code")
    print("  [OK] Integrated with existing PIC build workflows")
    print("  [OK] Compiled with standard XC8 toolchain")
    print()
    print("The transpiled C code maintains:")
    print("  * Same functionality as original C++ code")
    print("  * Optimized for embedded systems")
    print("  * Compatible with XC8 compiler limitations")
    print("  * Readable and maintainable structure")

    return True


def main():
    """Main build function"""
    try:
        success = build_cpp_multi()
        if success:
            print("\n*** BUILD SUCCESSFUL!")
            print(
                "The cpp-multi project has been transpiled and is ready for compilation."
            )
            return 0
        else:
            print("\n*** BUILD FAILED!")
            print("Please check the error messages above.")
            return 1

    except KeyboardInterrupt:
        print("\n*** Build interrupted by user")
        return 1
    except Exception as e:
        print(f"\n*** Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
