# This file will attempt to download, install, and run tests on the uploaded REAL PACKAGE from REAL PyPI.
#
# This is to confirm that the REAL, LIVE, PRODUCTION package works.

require 'fileutils'

require './detect-python'

require './config'
config = Config.new

# Clean temp folder.
config.clean_temp

# Set up Python venv.
config.setup_venv

# Install test package from test.pypi.org
system("#{config.virtual_python_exe} -m pip --no-cache-dir install #{config.app_name}")

# Run tests on our virtualenv that has our package installed.
config.run_venv_dist_tests