require './detect-python'

python_exe = detect_python_exe

Dir.chdir("src")

system("#{python_exe} setup.py sdist bdist_wheel")