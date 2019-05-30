#!/usr/bin/env bash

pushd code/twitter-fire-scraper/

    ruby build.rb
    ruby test-localwheel-install.rb || echo "FAILED ruby test scripts!" && exit 1

popd
