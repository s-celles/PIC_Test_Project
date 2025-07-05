# Upload script for PIC 16F876A with PICkit3
Write-Host "=== UPLOAD PIC 16F876A with PICkit3 ===" -ForegroundColor Cyan

$HEX_FILE = "build\main.hex"
$IPECMD = "C:\Program Files\Microchip\MPLABX\v5.50\mplab_platform\bin\ipecmd.exe"

# Check HEX file
if (-not (Test-Path $HEX_FILE)) {
    Write-Host "✗ HEX file not found: $HEX_FILE" -ForegroundColor Red
    Write-Host "Compile first with: .\compile_xc8.ps1" -ForegroundColor Yellow
    exit 1
}

# Check IPECMD
if (-not (Test-Path $IPECMD)) {
    Write-Host "✗ MPLAB IPE not found: $IPECMD" -ForegroundColor Red
    Write-Host "Install MPLAB X IDE or adjust the path" -ForegroundColor Yellow
    exit 1
}

Write-Host "✓ HEX file found: $HEX_FILE" -ForegroundColor Green
Write-Host "✓ IPECMD found" -ForegroundColor Green

# Upload command
$UPLOAD_ARGS = @(
    "-TPPK3"           # PICkit3
    "-PPIC16F876A"     # Microcontroller
    "-F$HEX_FILE"      # HEX file
    "-M"               # Program
    "-OL"              # Logout on completion
)

Write-Host "`nProgramming in progress..." -ForegroundColor Yellow
Write-Host "Make sure that:" -ForegroundColor Blue
Write-Host "  - PICkit3 is connected" -ForegroundColor Gray
Write-Host "  - PIC 16F876A is in the socket" -ForegroundColor Gray
Write-Host "  - Power is supplied" -ForegroundColor Gray

& "$IPECMD" $UPLOAD_ARGS

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n🎉 SUCCESS! PIC 16F876A programmed!" -ForegroundColor Green
    Write-Host "The LED blinking program should now work" -ForegroundColor White
} else {
    Write-Host "`n✗ Programming error" -ForegroundColor Red
    Write-Host "Check connections and power supply" -ForegroundColor Yellow
}
