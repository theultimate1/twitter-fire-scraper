#! /usr/bin/ruby
# frozen_string_literal: true

require './detect-python'

require './config'
config = Config.new

# Ensure wheel is installed.
system("#{config.python_exe} -m pip install wheel setuptools")

# Package wheel from source.
system("#{config.python_exe} setup.py sdist bdist_wheel")
