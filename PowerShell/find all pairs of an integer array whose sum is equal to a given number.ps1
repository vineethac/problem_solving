$array=1..10
$sum = 12

for ($i=0; $i -lt $array.count; $i++) {

    for ($j=0; $j -lt $array.count; $j++) {

        if (($array[$i] + $array[$j]) -eq $sum) {

            if ($i -ne $j) {

                Write-output "Pair:  $($array[$i]) $($array[$j]) " 
                
            }
        }

    }
}


