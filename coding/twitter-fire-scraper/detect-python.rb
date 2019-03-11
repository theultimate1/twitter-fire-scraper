require 'mkmf'
require 'open3'


def detect_python2_exe(verbose = nil)

# If `python` exists,
  if find_executable('python')

    stdout, stderr, status = Open3.capture3("python -V")
    python_version_info = stdout + stderr

    # If `python` refers to Python 2,
    if python_version_info =~ /Python 2/i

      if verbose
        puts "`python` refers to Python 2!"
      end

      return 'python'
    else # `python` does NOT refer to Python 2. Check for `python2` command.

      if verbose
        puts "`python` exists but doesn't refer to Python 2."
      end

    end

  else
    puts "`python` command doesn't exist."
  end


  # If `python2` exists,
  if find_executable('python2')

    stdout, stderr, status = Open3.capture3("python2 -V")
    python_version_info = stdout + stderr

    if python_version_info =~ /Python 2/i

      if verbose
        puts "`python2` refers to Python 2!"
      end

      return "python2"
    else
      puts "`python2` command somehow doesn't refer to Python 2..."
      puts "Version info: #{python_version_info}"
    end

  else
    puts "`python2` command doesn't exist"
  end

  puts "Python 2 detection failed!"

  nil

end