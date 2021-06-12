$array = @(1,2,4,3,2)
$counter = New-Object int[] 5

for ($i=0; $i -lt $array.count; $i++) {
   
    $counter[$i] = ($array | Where-Object { $_ -eq $array[$i] } | Measure-Object).count
}

for ($i=0; $i -lt $array.count; $i++) {
    
    if ($counter[$i] -gt '1') {
        Write-output "Duplicate number is: "$array[$i]
    }
}
