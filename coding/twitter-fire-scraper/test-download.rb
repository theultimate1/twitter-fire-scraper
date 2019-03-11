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
system("#{config.python_exe} -m virtualenv env")

# Folder that holds the virtualenv.
venv_folder = File.absolute_path(File.join("env"))

# Detect virtual environment folder location
venv_python_bin = File.join(venv_folder, "Scripts")

# It's windows if /Scripts/ exists
if File.exist? venv_python_bin
  puts "Using /Scripts/ in #{venv_folder}, Windows user."
end

# Might be Linux/OSX if "Scripts" doesn't exist.
unless File.exist? venv_python_bin
  venv_python_bin = File.absolute_path(File.join("bin"))
  puts "Using /bin/ in #{venv_folder}, *NIX user."
end

# Still doesn't exist? Exit.
unless File.exist? venv_python_bin
  puts "Could not detect `Scripts` or `bin` folder. Something is terribly wrong."
  exit(1)
end

# Path to venv Python executable.
virtual_python_exe = File.join(venv_python_bin, "python")

# Print venv Python version for sanity.
system("#{virtual_python_exe} -V")

# Install test package.
system("#{virtual_python_exe} -m pip install -i https://test.pypi.org/simple/ twitter-fire-scraper")

# TODO run tests now that it's installed!