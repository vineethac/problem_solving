<#
Input: ar1[] = {-5, 3, 6, 12, 15}
        ar2[] = {-12, -10, -6, -3, 4, 10}
Output : The median is 3.
Explanation : The merged array is :
        ar3[] = {-12, -10, -6, -5 , -3,
                 3, 4, 6, 10, 12, 15},
       So the median of the merged array is 3

Input: ar1[] = {2, 3, 5, 8}
        ar2[] = {10, 12, 14, 16, 18, 20}
Output : The median is 11.
Explanation : The merged array is :
        ar3[] = {2, 3, 5, 8, 10, 12, 14, 16, 18, 20}
        if the number of the elements are even, 
        so there are two middle elements,
        take the average between the two :
        (10 + 12) / 2 = 11.
#>

$array1 = @(2, 3, 5, 8)
$array2 = @(10, 12, 14, 16, 18, 20)

$array1 = $array1 | sort
$array2 = $array2 | sort

$full_array = ($array1 + $array2) | sort

Write-Output "Final merged array:" $full_array
Write-Output "Final array size:" $full_array.Count

if ($full_array.Count % 2 -eq 0) {

    $median_index1 = ($full_array.Count /2)
    $median_index2 = $median_index1 - 1
    Write-Output "Median indexes:" $median_index1, $median_index2
    Write-Output "Median index values:" $full_array[$median_index1], $full_array[$median_index2]
    $median = ($full_array[$median_index1] + $full_array[$median_index2]) /2
    Write-Output "Median:" $median
}
else {

    $median_index = [math]::Round($full_array.Count /2) - 1
    Write-Output "Median index:" $median_index
    $median = $full_array[$median_index]
    Write-Output "Median:" $median
}