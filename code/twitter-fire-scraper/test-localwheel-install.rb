#! /usr/bin/ruby
# frozen_string_literal: true

# This file will attempt to install and run tests on the highest-versioned local .whl file that is built.
#
# It does NOT build for you.
#
# This is more for actual development. It is faster and easier than uploading, typing in your password, etc.
#
# This IS for testing small changes.
#

require 'fileutils'

require './detect-python'

require './config'
config = Config.new

# Clean temp folder.
config.clean_temp

# Set up Python venv.
config.setup_venv

# Folder that contains the wheel.
wheel_folder = config.wheel_dir

puts "Searching in #{wheel_folder}:"

wheels = Dir.glob(File.join(wheel_folder, '*.whl'))
wheels = wheels.sort.reverse

if wheels.length == 0
  puts 'No wheels. Did you forget to build one?'
  exit 1
end

puts "#{wheels.length} wheels available:"

wheels.each do |wheel|
  puts (File.basename (wheel))
end

puts "Installing #{wheels[0]}."

# Spaces in filepath fix.
if is_windows

  Dir.chdir(config.venv_folder_bin)
  stdout, stderr, status = Open3.capture3("start /WAIT \"\" \"#{(config.virtual_python_exe)}\" -m pip install \"#{wheels[0]}\"")
  # stdout, stderr, status = Open3.capture3("start", "\"\"", "\"#{config.virtual_python_exe}\"", "-m", "pip", "install", "\"#{wheels[0]}\"")
else
  stdout, stderr, status = Open3.capture3("#{config.virtual_python_exe.shellescape}", '-m', 'pip', 'install', wheels[0].shellescape)
end

# Install test package from WHL file
puts stdout
puts stderr
puts status

# Run tests on our virtualenv that has our package installed.
config.run_venv_dist_tests