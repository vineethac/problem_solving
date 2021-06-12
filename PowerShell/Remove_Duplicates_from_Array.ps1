<#
Sort the array
Remove duplicates from it
Return the length after removing duplicates

#>

<#
Solution 1

$array = @(1,2,4,3,2, 7, 5, 8, 12, 5, 2, 15)
$array = $array | Sort

$array_size = ($array | unique).count
$array_size

#>

$array = @(1,2,4,3,2, 7, 5, 8, 12, 5, 2, 15)
$array = $array | Sort

$counter = 0
for ($i=0; $i -lt $array.Count; $i++) {

    for ($j=0; $j -lt $array.count; $j++) {

        if (($i -ne $j) -AND ($array[$j] -eq $array[$i]) -AND ($array[$j] -ne 'NULL')) {

            $array[$j] = 'NULL'
            $counter++
        }
    }
    
}
write-output "final array" $array
write-output "final array size" $array.count
write-output "null counter" $counter
Write-Output "unique element count" ($array.count - $counter) 