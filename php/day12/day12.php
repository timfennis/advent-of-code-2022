<?php

$input = file_get_contents('input');
$grid = array_map(str_split(...), explode(PHP_EOL, $input));


$sx = 0;
$sy = 0;

$ex = 0;
$ey = 0;


foreach ($grid as $y => $row) {
    foreach ($row as $x => $char) {
        if ($char == 'S') {
            $sx = $x;
            $sy = $y;
        } else if ($char == 'E') {
            $ex = $x;
            $ey = $y;
        }
    }
}

$grid[$sy][$sx] = 'a';
$grid[$ey][$ex] = 'z';

function find_shortest_path($grid, int $sx, int $sy, $reverse = false) {
    $width = count($grid[0]);
    $height = count($grid);
    $directions = [[0,1],[0,-1],[-1,0],[1,0]];
    $paths = [];
    $paths["$sx.$sy"] = 0;
    $queue = [[$sx, $sy, 0]];

    while (count($queue) > 0) {
        [$x, $y, $distance] = array_shift($queue);
        $from_height = ord($grid[$y][$x]);
        
        foreach ($directions as $direction) {
            [$dy, $dx] = $direction;
            $nx = $x + $dx;
            $ny = $y + $dy;
            if ($nx < 0 || $nx >= $width ||  $ny < 0 || $ny >= $height) {
                continue;
            }

            $to_height = ord($grid[$ny][$nx] ?? throw new RuntimeException("$nx $ny"));

            if ($reverse == false && false === ($from_height - $to_height >= -1)) {
                continue;
            }

            if ($reverse == true && false === ($from_height - $to_height) <= 1) {
                continue;
            }

            $current_best = $paths["$nx.$ny"] ?? 99999999999;
            if ($current_best > $distance + 1) {
                $paths["$nx.$ny"] = $distance + 1;
                $queue[] = [$nx, $ny, $distance + 1];
            }
        }
    }
    
    return $paths;
}


echo find_shortest_path($grid, $sx, $sy)["$ex.$ey"] . PHP_EOL;

$best = 9871293948728;
foreach (find_shortest_path($grid, $ex, $ey, true) as $key => $value) {
    [$x, $y] = explode('.', $key);
    if ($grid[$y][$x] == 'a' && $value < $best) {
        $best = $value;
    }
}

echo $best . PHP_EOL;