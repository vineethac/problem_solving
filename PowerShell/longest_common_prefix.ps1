$array = @('flower', 'flo', 'florence', 'bleep' )

$compare_string = ($array[0]).ToCharArray()
$flag = 0
$longest = ''
$final = ''

for ($i = 0; $i -lt ($compare_string).count; $i++) {

    for ($j = 1; $j -lt $array.count; $j++) {

        $current_element = ($array[$j]).ToCharArray()
        
        if ($current_element[$i] -eq $compare_string[$i]) {

            $flag+=1
            
        }
    }

    if ($flag -eq ($array.count-1)) {

        write-output "Matching element:" $compare_string[$i]
        $final = $longest+=$compare_string[$i]
        
    }

    $flag = 0 #reset flag

}

write-output "Longest matching:" $final
    





