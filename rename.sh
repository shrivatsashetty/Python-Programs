#!/bin/bash

for dir in [0-9]_*/; do
  new_name=$(echo "$dir" | sed 's/_/-/g')
  mv "$dir" "$new_name"
done
