$array = @(1,10,30,50,90,21,97,100,234,121,55,132,453)
[int] $start = 0 
[int] $end = ($array.count - 1)

Function partition_index ($array, [int] $start, [int] $end) {

    [int] $pivot = $array[$end]
    [int] $pi = $start
    
    for ($i=$start; $i -lt $end; $i++) {

        if($array[$i] -le $pivot) {

            $temp = $array[$i]
            $array[$i] = $array[$pi]
            $array[$pi] = $temp

            $pi++
        }
    }
    
    $temp1 = $array[$pi]
    $array[$pi] = $array[$end]
    $array[$end] = $temp1
    
    return $pi;
}

Function quick_sort ($array, [int] $start, [int] $end) {

   if($start -lt $end) {

        [int] $pi = partition_index $array $start $end 

        quick_sort $array $start ([int] $pi-1)
        quick_sort $array ([int] $pi+1) $end 
    }
}

quick_sort $array $start $end
$array


