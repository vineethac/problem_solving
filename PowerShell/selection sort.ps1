$array = @(5,3,4,1,6,7,25,6,7,5,66,32,354,98,22,13,17)
[int] $size = ($array.count -1)

Function selection_sort($array) {

    for ($i=0; $i -lt $size; $i++) {

        for ($j=$i+1; $j -le $size; $j++) {

            if ($array[$j] -lt $array[$i]) {

                $temp = $array[$i]
                $array[$i] = $array[$j]
                $array[$j] = $temp
            }
        }
    }

}

selection_sort $array
$array