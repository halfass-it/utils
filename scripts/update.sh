#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Please provide an argument (1, 2, or 3)"
    exit 1
fi

# Read the current version
current_version=$(grep "version=" setup.py | cut -d"'" -f2)

# Split the version into parts
IFS='.' read -ra version_parts <<< "$current_version"

# Increment the specified part and reset lower parts
case $1 in
    1)
        ((version_parts[0]++))
        version_parts[1]=0
        version_parts[2]=0
        ;;
    2)
        ((version_parts[1]++))
        version_parts[2]=0
        ;;
    3)
        ((version_parts[2]++))
        ;;
    *)
        echo "Invalid argument. Please use 1, 2, or 3."
        exit 1
        ;;
esac

# Construct the new version
new_version="${version_parts[0]}.${version_parts[1]}.${version_parts[2]}"

# Update the setup.py file
sed -i "s/version='$current_version'/version='$new_version'/" setup.py

# Git operations
git add .
git commit -m "Updated to version $new_version"
git push

echo "Version updated to $new_version and changes pushed to git."
