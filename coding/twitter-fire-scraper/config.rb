# Configuration class that stores variables, paths, etc.
class Config
  def python_exe
    detect_python_exe
  end

  # Folder to hold temporary files.
  def temp_folder
    File.absolute_path(File.join(File.dirname(__FILE__), "tmp"))
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
end
