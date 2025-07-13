#!/usr/bin/env python3
"""
SCons configuration for PIC16F876A using SEPARATE COMPILATION ONLY with xc8-wrapper module

This SConstruct implements only separate compilation:
- Each .c file is compiled to .p1 object file individually
- All .p1 files are then linked together to produce .elf and .hex
- Uses xc8-wrapper module directly (no subprocess calls)
"""

import shutil
from pathlib import Path
from SCons.Script import *

try:
    from xc8_wrapper import get_xc8_tool_path, run_command, log
except ImportError as e:
    print(f"❌ Cannot import xc8_wrapper: {e}")
    print("🔄 xc8-wrapper module required...")
    Exit(1)

# Project configuration
PROJECT_NAME = "pic_test_project"
TARGET_CHIP = "PIC16F876A"
XC8_VERSION = "3.00"
OPTIMIZATION_LEVEL = "2"

# Directories
SOURCE_DIR = Path("src/multi")
BUILD_DIR = Path("build")
OUTPUT_DIR = Path("output")

# Create environment
env = Environment()

# Get XC8 tool path using xc8-wrapper
try:
    xc8_cc_path, version_info = get_xc8_tool_path("cc", XC8_VERSION)
    print(f"✓ XC8 CC found: {version_info}")
except Exception as e:
    print(f"❌ XC8 not found: {e}")
    Exit(1)

# Create output directories
env.Execute(Mkdir(BUILD_DIR))
env.Execute(Mkdir(OUTPUT_DIR))

# Find source files
sources = Glob(str(SOURCE_DIR / "*.c"))
print(f"Source files found: {[str(s) for s in sources]}")

def setup_environment():
    """Configure environment for xc8-wrapper"""
    BUILD_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

def compile_separate_with_xc8_wrapper_scons(target, source, env):
    """
    Separate compilation using xc8-wrapper module
    """
    setup_environment()
    
    try:
        xc8_cc_path, version_info = get_xc8_tool_path("cc", XC8_VERSION)
        log.info(f"✓ XC8 CC found: {version_info}")
        
        print("🔨 Separate compilation with xc8-wrapper:")
        print(f"  Tool: {xc8_cc_path}")
        print(f"  Version: {version_info}")
        print()
        
        # Step 1: Separate compilation
        object_files = []
        
        for i, source_file in enumerate(source, 1):
            source_path = Path(str(source_file))
            print(f"📄 Step {i}/{len(source)}: Compiling {source_path.name}")
            
            object_file = BUILD_DIR / f"{source_path.stem}.p1"
            object_files.append(object_file)
            
            # Build compilation arguments
            compile_args = [
                str(xc8_cc_path),
                f"-mcpu={TARGET_CHIP}",
                "-c",  # Compile only
                f"-O{OPTIMIZATION_LEVEL}",
                "-std=c99",
                "-Wall",
                f"-D_XTAL_FREQ=4000000UL",
                "-o", str(object_file),
                str(source_path)
            ]
            
            # Use run_command from xc8-wrapper module
            if not run_command(compile_args, f"Compiling {source_path.name}"):
                print(f"   ❌ Compilation error {source_path.name}")
                return 1
            
            print(f"   ✅ {source_path.name} → {object_file.name}")
        
        print()
        
        # Step 2: Linking
        print(f"🔗 Step {len(source) + 1}: Linking object files")
        
        output_file = Path(str(target[0]))
        elf_file = BUILD_DIR / f"{PROJECT_NAME}.elf"
        map_file = BUILD_DIR / f"{PROJECT_NAME}.map"
        
        link_args = [
            str(xc8_cc_path),
            f"-mcpu={TARGET_CHIP}",
            f"-O{OPTIMIZATION_LEVEL}",
            "-std=c99",
            f"-Wl,-Map={map_file}",
            f"--memorysummary={BUILD_DIR}/memory_summary.xml",
            "-o", str(elf_file)
        ]
        
        # Add all object files
        for obj_file in object_files:
            link_args.append(str(obj_file))
        
        # Use run_command from xc8-wrapper module
        if not run_command(link_args, "Linking"):
            print("   ❌ Linking error")
            return 1
        
        print(f"   ✅ Linking successful → {elf_file.name}")
        
        # Step 3: Copy HEX file
        generated_hex = BUILD_DIR / f"{PROJECT_NAME}.hex"
        if generated_hex.exists():
            generated_hex.replace(output_file)
            print(f"   📦 HEX copied → {output_file}")
        else:
            print(f"   ⚠️  HEX file not found: {generated_hex}")
            return 1
        
        print("\n✅ Separate compilation with xc8-wrapper completed!")
        return 0
        
    except Exception as e:
        print(f"❌ Error in separate compilation: {e}")
        return 1



def clean_build_files(target, source, env):
    """Clean generated files"""
    dirs_to_clean = [BUILD_DIR, OUTPUT_DIR]
    
    for directory in dirs_to_clean:
        if directory.exists():
            shutil.rmtree(directory)
            print(f"Cleaned: {directory}")
    
    print("✅ Cleanup completed!")
    return 0

# Define targets using xc8-wrapper
target = env.Command(
    str(OUTPUT_DIR / f"{PROJECT_NAME}.hex"),
    sources,
    compile_separate_with_xc8_wrapper_scons
)

clean_target = env.Command(
    "clean_files",
    [],
    clean_build_files
)

# Define aliases
env.Alias('build', target)
env.Alias('clean', clean_target)

# Default target
env.Default(target)

# Help text
env.Help("""
PIC16F876A separate compilation with xc8-wrapper

Usage:
  scons                    - Separate compilation (default)
  scons build              - Separate compilation
  scons clean              - Clean generated files
  scons -h                 - Show this help

Available targets:
  build                    - Separate compilation using xc8-wrapper
  clean                    - Clean build and output directories

Configuration:
  Target chip: {TARGET_CHIP}
  XC8 version: {XC8_VERSION}
  Optimization: {OPTIMIZATION_LEVEL}
  Source directory: {SOURCE_DIR}
  Build directory: {BUILD_DIR}
  Output directory: {OUTPUT_DIR}
""".format(
    TARGET_CHIP=TARGET_CHIP,
    XC8_VERSION=XC8_VERSION,
    OPTIMIZATION_LEVEL=OPTIMIZATION_LEVEL,
    SOURCE_DIR=SOURCE_DIR,
    BUILD_DIR=BUILD_DIR,
    OUTPUT_DIR=OUTPUT_DIR
))

print("🔧 SCons configuration for PIC16F876A ready (separate compilation only)")
print(f"📁 Sources found: {len(sources)} files")
print(f"🎯 Target chip: {TARGET_CHIP}")
print(f"⚙️  XC8 version: {XC8_VERSION}")
print(f"🔨 Compilation mode: Separate compilation using xc8-wrapper")
