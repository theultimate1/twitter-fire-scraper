require 'mkmf'
require 'open3'


def detect_python_exe(verbose = nil, version="2")

# If `python` exists,
  if find_executable('python')

    stdout, stderr, status = Open3.capture3("python -V")
    python_version_info = stdout + stderr

    # If `python` refers to Python X,
    if python_version_info =~ /Python #{version}/i

      if verbose
        puts "`python` refers to Python #{version}!"
      end

      return 'python'
    else # `python` does NOT refer to Python 2. Check for `python2` command.

      if verbose
        puts "`python` exists but doesn't refer to Python #{version}."
      end

    end

  else
    puts "`python` command doesn't exist."
  end


  # If `python2` exists,
  if find_executable("python#{version}")

    stdout, stderr, status = Open3.capture3("python#{version} -V")
    python_version_info = stdout + stderr

    if python_version_info =~ /Python #{version}/i

      if verbose
        puts "`python#{version}` refers to Python 2!"
      end

      return "python#{version}"
    else
      puts "`python#{version}` command somehow doesn't refer to Python 2..."
      puts "Version info: #{python_version_info}"
    end

  else
    puts "`python#{version}` command doesn't exist"
  end

  puts "Python #{version} detection failed!"
  exit(1)

end