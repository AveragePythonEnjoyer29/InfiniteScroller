<?php

include_once("../source/database.php");

$res = $conn->query("SELECT * FROM feed");

$rows = array();
while($r = mysqli_fetch_assoc($res)) {
    $rows[] = $r;
}
echo json_encode($rows);