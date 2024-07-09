#!/bin/bash

awk '{
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
}' data/triplet_clean/p361+p527 > data/dict/p361+p527