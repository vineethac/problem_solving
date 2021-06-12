<#
For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

    Input: 28
    Output: "AB"

    Input: 701
    Output: "ZY"
#>

$n = 702

$hashTable = @{
    1 = 'A'
    2 = 'B'
    3 = 'C'
    4 = 'D'
    5 = 'E'
    6 = 'F'
    7 = 'G'
    8 = 'H'
    9 = 'I'
    10 = 'J'
    11 = 'K'
    12 = 'L'
    13 = 'M'
    14 = 'N'
    15 = 'O'
    16 = 'P'
    17 = 'Q'
    18 = 'R'
    19 = 'S'
    20 = 'T'
    21 = 'U'
    22 = 'V'
    23 = 'W'
    24 = 'X'
    25 = 'Y'
    26 = 'Z'
}
$str = @()
$alphabet = @()

while ($n -gt 0) {

    [int] $rem = $n % 26
    Write-Output "Current value of rem:" $rem
    
    if ($rem -eq 0) {
        $alphabet = 'Z'
        $n = [math]::Truncate(($n/26)-1)
    }
    else {
        $alphabet = ($hashTable.$rem)
        $n = [math]::Truncate($n/26)
    }
    
    $str = $str + $alphabet
    
    Write-Output "Current value of char:" $alphabet
    Write-Output "Current value of str:" $str
    Write-Output "Current value of n:" $n

}

$str.ToCharArray()
[array]::Reverse($str)

Write-Output "Excel column name:" $str