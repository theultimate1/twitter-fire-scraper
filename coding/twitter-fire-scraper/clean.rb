require 'fileutils'

destroy_em = ['build/', 'dist/']

for dir in destroy_em do
  if File.directory?(dir)
    puts "DEL #{dir}/*"
    FileUtils.remove_dir(dir)
  end
end