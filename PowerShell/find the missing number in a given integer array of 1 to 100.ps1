$missing_array = @(1..100)
$missing_array[10] = 0 # number at index 10 is missing now

$sum =0
foreach ($number in $missing_array) { 
    $sum += $number
}

$actual_array = 1..100
$actual_sum=0
foreach ($number in $actual_array) {
    $actual_sum += $number
}

Write-Output "Missing number is: $($actual_sum - $sum)" 