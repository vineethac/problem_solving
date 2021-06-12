<#

Input: 321
Output: 123

Input: -432
Output: -234


CALC            NUMBER  REVERSE

0 * 10 = 0      321     0
321 % 10 = 1                                      
0+1 = 1                 1
trunc (321/10)  32

1 * 10 = 10     32      10
32 % 10 = 2
10 + 2 = 12             12
trunc (32/10)   3

12 * 10 = 120   3       120
3 % 10 = 3
120 + 3 = 123           123
trunc (3/10)    0

#>
Function reverse ($number) {

    [int] $reverse = 0
    [int] $calc = 0
    [int] $neg_flag = 0

    if ($number -lt 0) {

        $number = $number * -1
        $neg_flag = 1
    }

    while ($number -gt 0) {

        $reverse = ($reverse * 10)
        $calc = ($number % 10)
        $reverse = $reverse + $calc
        $number = [math]::Truncate($number / 10)
            
    }

    if ($neg_flag -eq 1) {

        $reverse = $reverse * -1
        return $reverse
    }
    else {
        return $reverse
    }
}

[int] $number = Read-Host "Enter a number"
reverse $number
