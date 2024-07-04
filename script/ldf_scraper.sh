#!/bin/bash

PID="P2670"
ENDPOINT="https://query.wikidata.org/bigdata/ldf"
PREDICATE="http://www.wikidata.org/prop/direct/$PID"
# OBJECT='"978-0-262-03293-3"'
ACCEPT='application/ld+json'
LIMIT=10000  # Number of items per page
OFFSET=0  # Start from the first record
COUNTER=1
while true; do
  echo "$COUNTER"
  # Perform the curl request with pagination parameters
  RESPONSE=$(curl --silent \
    --get \
    -H "Accept: $ACCEPT" \
    --data-urlencode "predicate=$PREDICATE&page=$COUNTER" \
    --data-urlencode "page=$COUNTER" \
    "$ENDPOINT")

  # Break the loop if the response is empty (indicating no more data)
  if [ -z "$RESPONSE" ]; then
    break
  fi

  # Process the response (e.g., save to a file, print, etc.)
  FILENAME="$PID_$COUNTER.json"
  echo "$RESPONSE" > "$FILENAME"
  echo "Saved response to $FILENAME"

  # Increment the OFFSET to get the next page of results
  OFFSET=$((OFFSET + LIMIT))
  COUNTER=$((COUNTER + 1))
done
