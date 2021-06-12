<#
Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Input: digits = [4,3,2,9]
Output: [4,3,3,0]

#>

$array = @(4,3,5,8)

for ($i=($array.count - 1); $i -ge 0; $i--) {

    $array[$i] = $array[$i]+1
    
    if ($array[$i] -eq 10) {

        $array[$i] = 0
    }

    else {

        break
    }
}

Write-Output "---"$array