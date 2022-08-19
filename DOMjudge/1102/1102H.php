<?php
#4500 + 0030 + cc61 + 4000 + 4006 + 0000 (要計算Header Checksum) + 0a05 +046b + 0a08 + 09ed = 1b3fc

//將數列轉入陣列
$List = "4500,0030,cc61,4000,4006,0000,0a05,046b,0a08,09ed";
$Lary = explode(",",$List);
$Lsum = 0;

//將每組數字轉為10進位,再加總
for($i=0;$i<count($Lary);$i++) {
	$Lsum += base_convert($Lary[$i],16,10);
}

//將總合轉為16進位 ,1b3fc
$Lsum_hex = base_convert($Lsum,10,16);

//判斷會有幾組16進位 4位數 1組 , 5位數 就是 2組
$Lmax = ceil(strlen($Lsum_hex) / 4);

// 1b3fc=> 0001b3fc
$Lsum_hex = substr("0000" . $Lsum_hex , (0-$Lmax*4));

// 將 0001 b3fc 轉成 10進位 加總
$Lsumb = 0;
for($i=0;$i < strlen($Lsum_hex);$i=$i+4) {
	$Lsumb += base_convert(substr($Lsum_hex,$i,4) , 16 , 10);
}

// 將 加總值 轉 2進位
$Lsumb2 = base_convert($Lsumb,10,2);
#echo $Lsumb2 ."<br>";

//取補數 1->0 , 0->1
$LstrR = '';
for($i=0;$i < strlen($Lsumb2);$i++) {
	$Lchar = '0';	
	if (substr($Lsumb2,$i,1) == '0') $Lchar = '1';
	$LstrR .= $Lchar;
}
#echo $LstrR ."<br>";

//將補數轉回16進位
echo base_convert($LstrR,2,16);
exit();
