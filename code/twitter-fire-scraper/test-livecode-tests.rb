#! /usr/bin/ruby
# frozen_string_literal: true

# This file runs unit tests on the live code, with coverage.
#
# It will produce a '.coverage' file.
#

require 'fileutils'

require './detect-python'

require './config'
config = Config.new

config.setup_coverage

Dir.chdir(config.root_folder)

stdout, stderr, status = Open3.capture3("#{config.python_exe}", '-m', 'coverage', 'run', '-m', 'twitter_fire_scraper.tests.test')

puts stdout
puts stderr
puts status

if stderr.include? 'FAILED'
  print 'Failed test cases! Detected from stderr.'
  exit 1
end

if stdout.include? 'FAILED'
  print 'Failed test cases! Detected from stdout.'
  exit 1
end

unless status.to_s.include? 'exit 0'
  print "#{status} Didn't exit with code 0! Something is wrong!"
  exit 1
end
