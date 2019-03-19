require 'mkmf'
require 'open3'


def detect_python_exe(verbose = nil, version=nil)

# If `python` exists,
  if find_executable('python')

    stdout, stderr, status = Open3.capture3("python -V")
    python_version_info = stdout + stderr

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