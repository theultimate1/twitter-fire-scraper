# This is a command-line tool to assist in uploading a Python package.

require 'optparse'

require './detect-python'

python_exe = detect_python2_exe
dist_dir = "src/dist/*"

# Handle parsing command line arguments
options = {}
OptionParser.new do |opts|

  opts.banner = "Usage: #{$0} [options]"

  opts.on('-t', '--test', "Deploy to test PyPI site (test.pypi.org)") do |value|
    options[:test] = value
  end
  opts.on('-d', '--deploy', "Deploy to REAL PyPI site (pypi.org)!") do |value|
    options[:deploy] = value
  end

end.parse!

# Both true?
if options[:test] and options[:deploy]
  puts("You can't test AND deploy!")
  exit(1)
end

# Neither true?
if not options[:test] and not options[:deploy]
  puts("Choose whether to upload package to test PyPI or real PyPI.")
  puts("Run `#{$0} --help` for help.")
  exit(1)
end

puts("I'd inspect this script if I were you, before typing in your credentials. ")
puts("I'm not malicious, but can you prove it? ;)")

if options[:test]
  puts "Uploading `dist/*` to TEST PyPI package repository."
  system("#{python_exe} -m twine upload --repository-url https://test.pypi.org/legacy/ #{dist_dir}")
elsif options[:deploy]
  puts "Uploading `dist/` to REAL PyPI package repository."

  puts "Hold on! You're about to upload a package that ANYONE can install with `pip install`! "
  puts "Are you sure? (yes/no)"

  input = nil
  while (input != "yes") do
    input = gets.chomp

    if input == "no"
      puts "Aborted upload."
      exit(1)
    end

    if input != "yes"
      puts "Enter 'yes' or 'no'."
    end

  end

  system("#{python_exe} -m twine upload #{dist_dir}")
end