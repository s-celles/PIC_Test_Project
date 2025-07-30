#!/usr/bin/env python3
"""
C++ to C transpilation script for cpp-multi project
Uses xc8plusplus Python API to transpile C++ files to C
"""

import os
import sys
from pathlib import Path

# Add the xc8plusplus package to Python path
project_root = Path(__file__).parent.parent.parent
xc8plusplus_src = project_root / "xc8plusplus" / "src"
sys.path.insert(0, str(xc8plusplus_src))

from xc8plusplus import XC8Transpiler


def transpile_cpp_to_c():
    """Transpile all C++ files in cpp-multi to C equivalents"""

    # Define source and output directories
    cpp_multi_dir = Path(__file__).parent
    output_dir = cpp_multi_dir / "generated_c"

    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    print("🚀 C++ to C Transpilation for cpp-multi project")
    print("=" * 50)
    print(f"Source directory: {cpp_multi_dir}")
    print(f"Output directory: {output_dir}")
    print()

    # Initialize transpiler
    transpiler = XC8Transpiler()

    # Find all C++ files to transpile
    cpp_files = list(cpp_multi_dir.glob("*.cpp"))
    hpp_files = list(cpp_multi_dir.glob("*.hpp"))

    print(f"Found {len(cpp_files)} .cpp files and {len(hpp_files)} .hpp files")
    print()

    # Transpile C++ implementation files
    for cpp_file in cpp_files:
        output_file = output_dir / f"{cpp_file.stem}.c"
        print(f"📄 Transpiling {cpp_file.name} -> {output_file.name}")

        try:
            success = transpiler.transpile(cpp_file, output_file)
            if success:
                print(f"   ✅ Success: {output_file}")
            else:
                print(f"   ❌ Failed: {cpp_file}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        print()

    # Copy header files and convert .hpp to .h
    for hpp_file in hpp_files:
        output_file = output_dir / f"{hpp_file.stem}.h"
        print(f"📄 Converting header {hpp_file.name} -> {output_file.name}")

        try:
            # For headers, we'll do a simple conversion
            # Remove C++ specific syntax and convert to C-compatible headers
            convert_hpp_to_h(hpp_file, output_file)
            print(f"   ✅ Success: {output_file}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        print()

    # Copy device_config.h and pin_manager.h as-is
    for h_file in ["device_config.h", "pin_manager.h"]:
        src_file = cpp_multi_dir / h_file
        dst_file = output_dir / h_file
        if src_file.exists():
            print(f"📄 Copying {h_file}")
            try:
                dst_file.write_text(src_file.read_text())
                print(f"   ✅ Success: {dst_file}")
            except Exception as e:
                print(f"   ❌ Error: {e}")
            print()

    print("🎉 Transpilation completed!")
    print(f"Generated C files are in: {output_dir}")


def convert_hpp_to_h(hpp_file, h_file):
    """
    Convert C++ header file to C-compatible header
    This is a simplified conversion for demonstration
    """
    content = hpp_file.read_text()

    # Basic C++ to C header conversions
    # Replace .hpp extension in comments
    content = content.replace(".hpp", ".h")

    # Replace C++ style includes
    content = content.replace('#include "timer0.hpp"', '#include "timer0.h"')
    content = content.replace('#include "led.hpp"', '#include "led.h"')
    content = content.replace('#include "button.hpp"', '#include "button.h"')

    # Add extern "C" wrapper for C++ compatibility
    lines = content.split("\n")
    new_lines = []
    in_header_guard = False

    for line in lines:
        if "#ifndef" in line and "_HPP" in line:
            # Replace _HPP with _H
            line = line.replace("_HPP", "_H")
        elif "#define" in line and "_HPP" in line:
            line = line.replace("_HPP", "_H")
        elif "#endif" in line and "_HPP" in line:
            line = line.replace("_HPP", "_H")

        new_lines.append(line)

    # Write the converted content
    h_file.write_text("\n".join(new_lines))


if __name__ == "__main__":
    transpile_cpp_to_c()
