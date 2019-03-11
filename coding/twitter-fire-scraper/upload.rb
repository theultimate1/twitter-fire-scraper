require './detect-python'

python_exe = detect_python2_exe

puts("I'd inspect this script if I were you, before typing in your credentials. ")
puts("I'm not malicious, but can you prove it? ;)")

system("#{python_exe} -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*")