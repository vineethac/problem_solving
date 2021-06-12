$array = @( '(', '(', '{', '[', ']', '}', ')', '(', '{', '}', ')', '[', ']', '(', ')')
$stack = new-object string[] $array.Count
$j = 0
$count = 0

for ($i = 0; $i -lt ($array.count); $i++) {

    $count++

    if ($array[$i] -eq '(') {
        
        $stack[$j] = $array[$i]
        #write-host $stack
        $j+=1
        write-host "Added ( and current value of J is:" $j
        
    }

    elseif ($array[$i] -eq '{') {
        
        $stack[$j] = $array[$i]
        #write-host $stack
        $j+=1
        write-host "Added {  and current value of J is:" $j
    }
    
    elseif ($array[$i] -eq '[') {
        
        $stack[$j] = $array[$i]
        #write-host $stack
        $j+=1
        write-host "Added [ and current value of J is:" $j
        
    }

    
    if ($array[$i] -eq ')' -AND $stack[$j-1] -eq '(') {

        $stack[$j-1] = 'NULL'
        $j-=1
        $count-=2
    }

    elseif ($array[$i] -eq '}' -AND $stack[$j-1] -eq '{') {

        $stack[$j-1] = 'NULL'
        $j-=1
        $count-=2
    }

    elseif ($array[$i] -eq ']' -AND $stack[$j-1] -eq '[') {

        $stack[$j-1] = 'NULL'
        $j-=1
        $count-=2
    }

    elseif ($array[$i] -eq ')' -AND $stack[$j-1] -eq 'NULL') {

        write-host "Mismatch"

    }

}

write-output "Stack elements:" $stack
write-output "Value of J:" $j
write-output "Current input count:" $count

if ($j -eq 0 -AND $count -eq 0) {

    Write-Output "Matching pairs"
}
else {

    Write-Output "Unmatching pairs"
}