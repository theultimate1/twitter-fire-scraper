# This file will attempt to download, install, and run tests on the uploaded package from PyPI.
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

puts "and then ya do " + "pip install -i https://test.pypi.org/simple/ twitter-fire-scraper"
puts "TODO :)"