$array = New-Object int[] 15

$array = @(3,2,2,4,5,2,4,7,8,10,32,17,6,11,72)

$smallest = $array[0]
$largest = $array[0]

for ($i=0; $i -lt $array.Count; $i++) {
    
    if ($array[$i] -lt $smallest) {
        $smallest = $array[$i]
    }
    if ($array[$i] -gt $largest) {
        $largest = $array[$i]
    }
}

Write-Output "Smallest number: $smallest"
Write-Output "Largest number: $largest"