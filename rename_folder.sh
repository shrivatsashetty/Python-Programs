#!/bin/bash

for dir in [0-9]_*/; do
  new_name="echo "dir" | sed 's/_/-/g'"
  name 
  mv "$dir" "$new_name"
done
