#!/usr/bin/env bash

pushd code/twitter-fire-scraper/

    echo "Testing from source and generating code coverage..."
    ruby test-livecode-tests.rb
    if [ $? -eq 0 ]; then
        echo "Tests passed."
    else
        echo "Tests failed."
        exit 1
    fi

popd
