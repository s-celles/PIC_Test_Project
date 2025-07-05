# Direct compilation script with XC8 v3.00 for PIC 16F876A
Write-Host "=== DIRECT XC8 v3.00 COMPILATION ===" -ForegroundColor Cyan

$XC8_PATH = "C:\Program Files\Microchip\xc8\v3.00\bin"
$XC8_CC = "$XC8_PATH\xc8-cc.exe"

# Check XC8
if (-not (Test-Path $XC8_CC)) {
    Write-Host "✗ XC8 v3.00 not found: $XC8_CC" -ForegroundColor Red
    exit 1
}

Write-Host "✓ XC8 v3.00 found" -ForegroundColor Green

# Create build directory
$BUILD_DIR = "build"
if (-not (Test-Path $BUILD_DIR)) {
    New-Item -ItemType Directory -Path $BUILD_DIR | Out-Null
}

# Compilation parameters for PIC16F876A with 4MHz crystal
$COMPILE_ARGS = @(
    "-mcpu=PIC16F876A"
    "-c"
    "-fno-short-double"
    "-fno-short-float"
    "-O2"
    "-fasmfile"
    "-maddrqual=ignore"
    "-xassembler-with-cpp"
    "-mwarn=-3"
    "-Wa,-a"
    "-DXPRJ_default=default"
    "-msummary=-psect,-class,+mem,-hex,-file"
    "-ginhx032"
    "-Wl,--data-init"
    "-mno-keep-startup"
    "-mno-download"
    "-mno-default-config-bits"
    "-std=c99"
    "-gdwarf-3"
    "-mstack=compiled:auto:auto:auto"
    "-o"
    "$BUILD_DIR\main.p1"
    "src\main.c"
)

# Compilation
Write-Host "Compiling main.c..." -ForegroundColor Yellow
& "$XC8_CC" $COMPILE_ARGS

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Compilation successful" -ForegroundColor Green
    
    # Linking
    $LINK_ARGS = @(
        "-mcpu=PIC16F876A"
        "-Wl,-Map=$BUILD_DIR\main.map"
        "-DXPRJ_default=default"
        "-Wl,--defsym=__MPLAB_BUILD=1"
        "-fno-short-double"
        "-fno-short-float"
        "-O2"
        "-fasmfile"
        "-maddrqual=ignore"
        "-xassembler-with-cpp"
        "-mwarn=-3"
        "-Wa,-a"
        "-msummary=-psect,-class,+mem,-hex,-file"
        "-ginhx032"
        "-Wl,--data-init"
        "-mno-keep-startup"
        "-mno-download"
        "-mno-default-config-bits"
        "-std=c99"
        "-gdwarf-3"
        "-mstack=compiled:auto:auto:auto"
        "-Wl,--memorysummary,$BUILD_DIR\memoryfile.xml"
        "-o"
        "$BUILD_DIR\main.elf"
        "$BUILD_DIR\main.p1"
    )
    
    Write-Host "Linking..." -ForegroundColor Yellow
    & "$XC8_CC" $LINK_ARGS
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Linking successful" -ForegroundColor Green
        
        # Check if HEX file was created
        if (Test-Path "$BUILD_DIR\main.hex") {
            $hexSize = (Get-Item "$BUILD_DIR\main.hex").Length
            Write-Host "✓ HEX file generated: main.hex ($hexSize bytes)" -ForegroundColor Green
            
            Write-Host "`nGenerated files:" -ForegroundColor Blue
            Get-ChildItem $BUILD_DIR | ForEach-Object {
                $size = if ($_.PSIsContainer) { "<DIR>" } else { $_.Length }
                Write-Host "  $($_.Name) - $size bytes" -ForegroundColor Gray
            }
            
            Write-Host "`n🎉 SUCCESS! PIC 16F876A project compiled with XC8 v3.00!" -ForegroundColor Green
            Write-Host "File ready for programming: $BUILD_DIR\main.hex" -ForegroundColor White
        } else {
            Write-Host "✗ HEX file not generated" -ForegroundColor Red
        }
    } else {
        Write-Host "✗ Linking error" -ForegroundColor Red
    }
} else {
    Write-Host "✗ Compilation error" -ForegroundColor Red
}
