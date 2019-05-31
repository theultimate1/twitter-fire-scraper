#!/usr/bin/env bash

pushd code/twitter-fire-scraper/

    echo "Building..."
    ruby build.rb

    echo "Installing local .whl file and running tests..."
    ruby test-localwheel-install.rb
    if [ $? -eq 0 ]; then
        echo "Tests passed."
    else
        echo "Tests failed."
        exit 1
    fi

popd
