require './detect-python'

require './config'
config = Config.new

Dir.chdir("src")

system("#{config.python_exe} setup.py sdist bdist_wheel")