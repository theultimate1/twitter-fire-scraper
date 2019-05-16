#!/usr/bin/env bash

pushd code/twitter-fire-scraper/

    ruby build.rb
    ruby test-localwheel-install.rb

popd