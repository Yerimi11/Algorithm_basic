<?php

class Stack {
    private $data;
    public function __construct() {
        $this->data = [];
    }
    public function push($value) {
        array_push($this->data, $value);
    }
    public function pop() {
        array_pop($this->data);
    }
    public function top() {
        return end($this->data);
    }
    public function isEmpty() {
        return empty($this->data);
    }
 }

$input = intval(fgets(STDIN));
// $input = [8,4,3,6,8,7,5,2,1];

$stack = new Stack();
$result = [];

$current = 1;
$index = 0;

while ($index < $input[0]) {
    if(!$stack->isEmpty() && $stack->top() == $input[$index]) {
        $stack->pop();
        $result[] = '-';
        $index++;
    } else {
        $stack->push($current);
        $result[] = '+';
        $current++;
    }
}

if (!$stack->isEmpty()) {
    echo "NO\n";
} else {
    echo implode(' ', $result), "\n";
}

?>
