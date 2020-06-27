<?php 

require 'vendor/autoload.php';
require 'blockchain.php';


$f3 = \Base::instance();
$f3->route('GET /',
    function() {
        echo 'Hello, world!';
    }
);
$f3->run();