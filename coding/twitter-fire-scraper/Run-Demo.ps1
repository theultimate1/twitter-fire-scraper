<#
This file runs a demo of the Twitter fire scraper functionality for presentation purposes.
#>

function detectPython2() {
    # Detects Python2 command.

    $PythonCommand = "python"
    $PythonVersion = Invoke-Expression ($PythonCommand+" -V")

    Write-Host $PythonVersion

    if($PythonVersion -like "Python 2") {

        Write-Host "Python 2 detected via ``python`` command."

    } elseif(Get-Command "python2" -ErrorAction SilentlyContinue) { # `python` is not Py2,

        $PythonCommand = "python2";
        Write-Host("Python 2 detected via ``python2`` command.")
    } else { # `python2` does not exist.

        Write-Host("``python`` refers to Python 3 and ``python2`` does not exist.")

        Write-Host("Consider putting Python 2 on the PATH environment variable (order matters),")

        Write-Host("or make a ``python2.exe`` executable available in a folder that is on the PATH.")

        Get-Command "python" | Format-Table Path, Name

        Exit(1)
    }

    return $PythonCommand
}


$PythonCommand = detectPython2;

