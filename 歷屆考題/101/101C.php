<?php
$Lmax = 0;

function fs_tree($Lary,$Ldeep,$Lnode) {

	for($i=0;$i<count($Lary);$i++){
		if (substr($Lary[$i],-1) == $Lnode) {
			fs_tree($Lary,$Ldeep+1,substr($Lary[$i],0,1));
		}
		if ($Ldeep > $GLOBALS["Lmax"]) $GLOBALS["Lmax"] = $Ldeep;
    }
}

$Lstr = "1,3^2,3^3,5^4,5^5,0^6,5";
$Lary = explode("^",$Lstr);
print_r($Lary);
fs_tree($Lary,1,"0");

echo $Lmax;
$Lstr2 = 'hello';
print(substr($Lstr2,0,1))
?>