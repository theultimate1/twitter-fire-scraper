require 'fileutils'

require './config'
config = Config.new

folders_to_remove = %w(
src/build/
src/dist/
)

folders_to_remove.each {|dir|

  # Full path to avoid accidentally exploding your folders into tiny dust.
  dir = File.join(config.root_folder, dir)

  if File.directory?(dir)
    puts "DEL #{dir}"
    FileUtils.remove_dir(dir)
  end
}