#!/bin/bash

awk '{print $1 " " $3}' data/triplet_clean/p2670_all | sort -k1,1 | awk '{
    key = $1
    value = $2
    if (key != last_key && NR != 1) {
        print last_key, output
        output = value
    } 
    else if (NR == 1) {
        output = value
    } 
    else {
        output = output " " value
    }
    last_key = key
} END {
    print last_key, output
}' > data/dict/p2670_has_parts_of_the_class