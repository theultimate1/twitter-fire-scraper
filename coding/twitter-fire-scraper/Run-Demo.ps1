<#
This file runs a demo of the Twitter fire scraper functionality for presentation purposes.
#>

function detectPython2([string]$Verbose) {
    # Detects Python2 command.

    $PythonCommand = "python"
    $PythonVersion = Invoke-Expression ($PythonCommand+" -V") 

    if($PythonVersion -like "Python 2") {

        Write-Output("Python 2 detected via ``python`` command.")

    } elseif(Get-Command "python2" -ErrorAction SilentlyContinue) { # `python` is not Py2,

        $PythonCommand = "python2";
        Write-Output("Python 2 detected via ``python2`` command.")
    } else { # `python2` does not exist.

        Write-Output("``python`` refers to Python 3 and ``python2`` does not exist.`n")

        Write-Output("Consider putting Python 2 on the PATH environment variable (order matters),")

        Write-Output("or make a ``python2.exe`` executable available in a folder that is on the PATH.`n")

        Write-Output("Running ``where python``")

        Write-Output("This is the current location of ``python``:")

        Get-Command ("python") | Format-Table Path, Name

        Write-Output("Exiting. This demo will not work until these issues are resolved.")

        Exit(1)
    }

    return $PythonCommand
}


$PythonCommand = detectPython2;

