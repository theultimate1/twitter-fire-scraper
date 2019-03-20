require 'mkmf'
require 'open3'
require 'rbconfig'
require 'open-uri'

require './config'
CONFIG = Config.new


def is_windows()
  Gem.win_platform?
end

def try_install_choco()
  stdout, stderr, status = Open3.capture3("powershell.exe Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")
  puts stdout
  puts stderr
  puts status
end

def try_install_python(version = 3)

  puts "Is windows?"
  puts is_windows

  if is_windows


    # If installer doesn't exist, download it.
    if not File.exist? CONFIG.windows_python_installer_location
      puts "Downloading Python for Windows as it doesn't exist."

      download = open(CONFIG.windows_python_installer_url)

      IO.copy_stream(download, CONFIG.windows_python_installer_location)
    end

    if File.exist? CONFIG.windows_python_installer_location
      puts "Installing Python from downloaded Windows installer."

      Dir.chdir CONFIG.root_folder

      # command = "#{CONFIG.windows_python_installer_location} /passive InstallAllUsers=0 Include_launcher=0 Include_test=1 SimpleInstall=1 PrependPath=1 SimpleInstallDescription=\"Python 3 installation for Jenkins user.\" "
      command = "msiexec /qb /norestart ADDLOCAL=ALL /i #{File.basename CONFIG.windows_python_installer_location}"

      puts command

      stdout, stderr, status = Open3.capture3(command)
      puts stdout
      puts stderr
      puts status

      raise "PATH setting on windows fails. Make sure to set it manually."

    else
      raise "Failed to download Python windows installer!"
    end

  elsif find_executable("apt")
    stdout, stderr, status = Open3.capture3("apt", "install", "-y", "python#{version}")

    puts stdout
    puts stderr
    puts status
    return
  end
end


def detect_python_exe(verbose = nil, version = nil)

  if is_windows and File.exist? File.join(CONFIG.windows_python_installer_location, "python.exe")
    return File.join(CONFIG.windows_python_installer_location, "python.exe")
  end

# If `python` exists,
  if find_executable('python')

    stdout, stderr, status = Open3.capture3("python -V")
    python_version_info = stdout + stderr
    puts python_version_info
    puts status

    # If `python` refers to Python version X,
    if python_version_info =~ /Python #{version}/i

      if verbose
        puts "`python` refers to Python #{version}!"
      end

      return 'python'
    else # `python` does NOT refer to Python version X. Check for `pythonX` command.

      if verbose
        puts "`python` exists but doesn't refer to Python #{version}."
      end

    end

  else
    puts "`python` command doesn't exist."
  end


  # If `pythonX` exists,
  if find_executable("python#{version}")

    stdout, stderr, status = Open3.capture3("python#{version} -V")
    python_version_info = stdout + stderr

    if python_version_info =~ /Python #{version}/i

      if verbose
        puts "`python#{version}` refers to Python #{version}!"
      end

      return "python#{version}"
    else
      puts "`python#{version}` command somehow doesn't refer to Python #{version}..."
      puts "Version info: #{python_version_info}"
    end

  else
    puts "`python#{version}` command doesn't exist"
  end

  raise "Python #{version} detection failed!"

end