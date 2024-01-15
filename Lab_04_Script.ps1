# Script for password complexity (Policy 1.1.5 (L1))

$registryPath = "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa"
$propertyName = "LimitBlankPasswordUse"
$propertyValue = 1

# Script for disabling the SMB v1 Client Driver (Policy 18.4.3 (L1))

Set-ItemProperty -Path $registryPath -Name $propertyName -Value $propertyValue
Disable-WindowsOptionalFeature -Online -FeatureName "SMB1Protocol-Client"
