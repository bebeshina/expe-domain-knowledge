$string = 'Anne-Th&eacute;r&egrave;'; // from the database


if (mb_detect_encoding($string, 'utf-8', true) === false) {
$string = mb_convert_encoding($string, 'utf-8', 'iso-8859-1');
}

echo $string;
