# Configuration class that stores variables, paths, etc.
class Config

  def app_name
    'twitter-fire-scraper'
  end

  def python_exe
    detect_python_exe
  end

  # Folder that the config file resides in.
  def root_folder
    File.dirname(__FILE__)
  end

  # Folder to hold temporary files.
  def temp_folder
    File.absolute_path(File.join(self.root_folder, "tmp"))
  end

  # Folder to hold the virtual environment.
  def venv_folder
    File.absolute_path(File.join(self.temp_folder, "env"))
  end

  # Detect Python virtual environment folder location
  def venv_folder_bin
    venv_python_bin = File.join(self.venv_folder, "Scripts")

    # It's windows if /Scripts/ exists
    if File.exist? venv_python_bin
      puts "Using /Scripts/ in #{self.venv_folder}, Windows user."
    end

    # Might be Linux/OSX if "Scripts" doesn't exist.
    unless File.exist? venv_python_bin
      venv_python_bin = File.absolute_path(File.join("bin"))
      puts "Using /bin/ in #{self.venv_folder}, *NIX user."
    end

    # Still doesn't exist? Exit.
    unless File.exist? venv_python_bin
      puts "Could not detect `Scripts` or `bin` folder. Something is terribly wrong."
      exit(1)
    end

    venv_python_bin

  end

  # Venv python binary.
  def virtual_python_exe
    File.join(self.venv_folder_bin, "python")
  end

  # Set up a clean virtual environment.
  def setup_venv

    puts "Ensuring deps are satisfied for virtual environments..."
    system("#{self.python_exe} -m pip install virtualenv")

    # Create virtual environment to download test package
    puts "Creating virtual environment..."
    system("#{self.python_exe} -m virtualenv #{self.venv_folder}")

    # Path to venv Python executable.
    virtual_python_exe = File.join(self.venv_folder_bin, "python")

    # Print venv Python version for sanity.
    puts "Python version: "
    system("#{virtual_python_exe} -V")
    puts ""

    nil

  end

  # Run tests on our virtualenv, assuming our project (twitter-fire-scraper) is installed.
  def run_venv_dist_tests

    # Invoke __main__ of automated tests module
    system("#{self.virtual_python_exe} -m twitter-fire-scraper.tests.test")

  end

  # Ensure temp folder is clean.
  def clean_temp

    # Remove temp folder if exists
    if File.directory?(self.temp_folder)
      puts("DEL #{self.temp_folder}")
      FileUtils.remove_dir(self.temp_folder)
    end

    # Make temp folder
    FileUtils.mkdir(self.temp_folder)
    puts ("MKDIR #{self.temp_folder}")

    nil
  end
end
