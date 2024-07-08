#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <split>"
    exit 1
fi
# Directory containing file_B files
directory="data/triplet/$1"

# File containing words to remove
file_A="data/claim/blacklist.txt"

# Create output directory if it doesn't exist
output_directory="data/triplet_clean/$1"
mkdir -p "$output_directory"

total_files=$(find "$directory" -type f | wc -l)
processed_files=0

display_progress() {
    local progress=$1
    local total=$2
    local percent=$(( progress * 100 / total ))
    local filled=$(( percent / 2 ))
    local empty=$(( 50 - filled ))
    printf "\rProcessing files: ["
    printf "%0.s#" $(seq 1 $filled)
    printf "%0.s-" $(seq 1 $empty)
    printf "] %d%% (%d/%d)" "$percent" "$progress" "$total"
}

# Loop through each file in the directory
for file in "$directory"/*; do
    # Check if it is a regular file (not a directory or special file)
    if [[ -f "$file" ]]; then
        # Get the filename without the directory path
        filename=$(basename "$file")
        
        # Apply the grep command to filter lines
        grep -v -F -f "$file_A" "$file" > "${output_directory}/${filename}"

        # Increment the processed files count
        processed_files=$((processed_files + 1))
        
        # Display the progress bar
        display_progress "$processed_files" "$total_files"
    fi
done


