<#

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

IV  4
IX  9
XL 40
XC 90
CD 400
CM 900

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: "M CM XC IV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

#>

Function roman_to_int ($roman) {

    Write-host $roman
    $number = 0
    for ($i=0; $i -lt $roman.count; $i++) {

        if ($roman[$i] -eq 'I' -AND $roman[$i+1] -eq 'V') { 
            
            $number = $number + 4 
            $roman[$i]='0'
            $roman[$i+1]='0' 
        }
        if ($roman[$i] -eq "I" -AND $roman[$i+1] -eq "X") { 
            
            $number = $number + 9
            $roman[$i]='0'
            $roman[$i+1]='0'
        }
        
        if ($roman[$i] -eq "X" -AND $roman[$i+1] -eq "L") { 
            
            $number = $number + 40
            $roman[$i]='0'
            $roman[$i+1]='0'
        }
        if ($roman[$i] -eq "X" -AND $roman[$i+1] -eq "C") { 
            
            $number = $number + 90 
            $roman[$i]='0'
            $roman[$i+1]='0'
        }
        
        if ($roman[$i] -eq "C" -AND $roman[$i+1] -eq "D") { 
            
            $number = $number + 400 
            $roman[$i]='0'
            $roman[$i+1]='0'
        }
        if ($roman[$i] -eq "C" -AND $roman[$i+1] -eq "M") { 
            
            $number = $number + 900 
            $roman[$i]='0'
            $roman[$i+1]='0'
        }
        
        if ($roman[$i] -eq 'I') { $number = $number + 1}
        if ($roman[$i] -eq "X") { $number = $number + 10}
        if ($roman[$i] -eq "C") { $number = $number + 100}
        if ($roman[$i] -eq 'V') { $number = $number + 5}
        if ($roman[$i] -eq 'L') { $number = $number + 50}
        if ($roman[$i] -eq "D") { $number = $number + 500}
        if ($roman[$i] -eq "M") { $number = $number + 1000}
        
    }
    return $number
}

$roman = new-object string[] 50 
$roman = "MMMCMXCIX" 
$roman = $roman.ToCharArray()
roman_to_int $roman

