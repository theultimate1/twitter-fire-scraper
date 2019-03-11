# Configuration class that stores variables, paths, etc.
class Config
  def python_exe
    detect_python_exe
  end

  def temp_folder
    "tmp"
  end

end
