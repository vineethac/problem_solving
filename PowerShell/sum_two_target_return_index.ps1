<#
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Note: index1 must be less than index2.

#>

$array = @(2,7,11,15)
$target = 17

for ($i=0; $i -lt $array.count; $i++) {

    for ($j=$i+1; $j -lt $array.count; $j++) {

        if ($array[$i] + $array[$j] -eq $target) {

            Write-Output "Indexes are:" ($i+1), ($j+1)
        }

    }

}