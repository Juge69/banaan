Clear-Host

Write-Host "=== USB SECURITY DEMONSTRATION ==="
Write-Host ""
Write-Host "This program is NOT malicious."
Write-Host "It demonstrates what CAN happen if you run files from unknown USB drives."
Write-Host ""
Write-Host "----------------------------------"

# Collect benign system information
$user = $env:USERNAME
$computer = $env:COMPUTERNAME
$time = Get-Date

Write-Host "Current user: $user"
Write-Host "Computer name: $computer"
Write-Host "Current time: $time"

# Create a harmless demo file
$outputFile = "$PSScriptRoot\DEMO_COLLECTED_DATA.txt"

@"
THIS IS A DEMONSTRATION FILE
---------------------------
User: $user
Computer: $computer
Time: $time

No real data was accessed.
No data was transmitted.

If this were malicious software,
sensitive data could have been collected silently.
"@ | Out-File -Encoding UTF8 $outputFile

Write-Host ""
Write-Host "A demonstration file has been created on the USB drive:"
Write-Host "DEMO_COLLECTED_DATA.txt"
Write-Host ""
Write-Host "At this point, real malware could:"
Write-Host "- Read personal or corporate files"
Write-Host "- Install persistent software"
Write-Host "- Transmit data externally"
Write-Host ""
Write-Host "Press any key to exit."

$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
