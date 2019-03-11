# This file will attempt to download, install, and run tests on the uploaded TEST package from PyPI.
#
# This is meant for testing what the person downloading your package would see (if this actually uploaded it to the
# real PyPI), but is not fast and requires you to re-upload the wheel every time you make a change to the local
# filesystem.
#
# It is NOT meant for testing small changes.

require 'fileutils'

require './detect-python'

require './config'
config = Config.new

# Clean temp folder.
config.clean_temp

# Set up Python venv.
config.setup_venv

# Install test package from test.pypi.org
system("#{config.virtual_python_exe} -m pip install -i https://test.pypi.org/simple/ #{config.app_name}")

# Invoke __main__ of automated tests module
system("#{config.virtual_python_exe} -m twitter-fire-scraper.tests.test")