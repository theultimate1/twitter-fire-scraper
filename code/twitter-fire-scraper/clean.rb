#! /usr/bin/ruby
# frozen_string_literal: true

require 'fileutils'

require './config'
config = Config.new

folders_to_remove = %w[
  build/
  dist/
]

folders_to_remove.each do |dir|
  # Full path to avoid accidentally exploding your folders into tiny dust.
  dir = File.join(config.root_folder, dir)

  if File.directory?(dir)
    puts "[ DEL  ] #{dir}"
    FileUtils.remove_dir(dir)
  else # Doesn't exist
    puts "[ GONE ] #{dir}"
  end
end
