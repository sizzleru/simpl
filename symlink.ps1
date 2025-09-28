#Get-ChildItem -Path "C:\" -Recurse -Filter "latest.py" -File | Select-Object -ExpandProperty DirectoryName

Get-ChildItem -Recurse -Filter "latest.py" -Path $(
    Join-Path -Path $(Get-Location) -ChildPath "\module"
) -File | Select-Object -ExpandProperty DirectoryName | ForEach-Object {
    $folderPath = $_
    $sortedItems = Get-ChildItem -Path $folderPath | Sort-Object Name
    $lastItem = $sortedItems[-1]

    Write-Host "Deleting $folderPath\latest.py ..."
    Remove-Item -Path "$folderPath\latest.py"

    Write-Host "Creating symlink to $folderPath\$lastItem ..."
    New-Item -Path "$folderPath\latest.py" -ItemType SymbolicLink -Value "$folderPath\$lastItem"
}