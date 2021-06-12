<#
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0
#>

$array = @(1,3,5,6)
$target = 2
$flag = 0
$size = $array.Count


for ($i=0; $i -lt $array.Count; $i++) {

    if ($array[$i] -eq $target) {

        Write-Output "Target index:" $i
        $flag = 1
    }

}

if ($target -lt $array[0]) {

    Write-Output "Target index:" 0

}
elseif ($target -gt $array[$size-1]) {

    Write-Output "Target index:" $size

}
elseif ($flag -eq 0) {

    for ($i=0; $i -lt $array.Count; $i++) {

        
        if ($target -gt $array[$i] -AND $target -lt $array[$i+1]) {

            Write-Output "Target index:" ($i+1)
        }
    }
}