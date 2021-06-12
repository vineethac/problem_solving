<#
Input: 213
Output: 312 is palindrome

Input: -456
Output: 654- is not palindrome

Number      Calc                Reverse

213         0 x 10 = 0          0
            213 % 10 = 3
            0 + 3 = 3           3
            t(213 / 10) = 21    

21   
            3 x 10 = 30         3
            21 % 10 = 1
            30 + 1 = 31         31
            t(31 / 10) = 3
            
3

            31 x 10 = 310       310
            3 % 10 = 3  
            310 + 2 = 312       312
            t(3 / 10)   = 0

0            

#>

Function reverse ($number) {

    $calc = 0
    $reverse = 0
    $neg_flag = 0

    if ($number -lt 0) {

        $number = $number * -1
        $neg_flag = 1
    }

    while ($number -gt 0) {

        $reverse = $reverse * 10
        $calc = $number % 10
        $reverse = $reverse + $calc
        $number = [math]::Truncate($number / 10)
    }

    if($neg_flag -eq 1) { # negative numbers are not considered palindrome here 

        Write-Output $actual_number "is not palindrome"
        
    }
    else {
        
        if ($actual_number -eq $reverse) { Write-Output $actual_number "is palindrome" }
        else { Write-Output $actual_number "is not palindrome" }
    }
}

$number = Read-Host "Enter a number"
$actual_number = $number
reverse $number