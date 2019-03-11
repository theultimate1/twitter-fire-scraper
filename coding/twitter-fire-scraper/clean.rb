require 'fileutils'

folders_to_remove = %w(
src/build/
src/dist/
)

folders_to_remove.each {|dir|
  if File.directory?(dir)
    puts "DEL #{dir}/*"
    FileUtils.remove_dir(dir)
  end
}