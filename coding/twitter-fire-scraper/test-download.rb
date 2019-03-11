# This file will attempt to download, install, and run tests on the uploaded test package from PyPI.
#
require 'fileutils'

require './detect-python'

require './config'
config = Config.new

# Remove temp folder if exists
if File.directory?(config.temp_folder)
  puts("DEL #{config.temp_folder}")
  FileUtils.remove_dir(config.temp_folder)
end

# Make temp folder
FileUtils.mkdir(config.temp_folder)
puts ("MKDIR #{config.temp_folder}")

# Go into temp folder
Dir.chdir(config.temp_folder)

# Create virtual environment to download test package
puts "Creating virtual environment..."
system("#{config.python_exe} -m virtualenv #{config.venv_folder}")

# Path to venv Python executable.
virtual_python_exe = File.join(config.venv_folder_bin, "python")

# Print venv Python version for sanity.
system("#{virtual_python_exe} -V")

# Install test package.
system("#{virtual_python_exe} -m pip install -i https://test.pypi.org/simple/ twitter-fire-scraper")

# TODO run tests now that it's installed!