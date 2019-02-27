<#
This file runs a demo of the Twitter fire scraper functionality for presentation purposes.
#>


Function Trace-Word
{
    [Cmdletbinding()]
    [Alias("Highlight")]
    Param(
            [Parameter(ValueFromPipeline=$true, Position=0)] [string[]] $content,
            [Parameter(Position=1)] 
            [ValidateNotNull()]
            [String[]] $words = $(throw "Provide word[s] to be highlighted!")
    )
    
    Begin
    {
        
        $Color = @{       
                    0='Yellow'      
                    1='Magenta'     
                    2='Red'         
                    3='Cyan'        
                    4='Green'       
                    5 ='Blue'        
                    6 ='DarkGray'    
                    7 ='Gray'        
                    8 ='DarkYellow'    
                    9 ='DarkMagenta'    
                    10='DarkRed'     
                    11='DarkCyan'    
                    12='DarkGreen'    
                    13='DarkBlue'        
        }

        $ColorLookup =@{}

        For($i=0;$i -lt $words.count ;$i++)
        {
            if($i -eq 13)
            {
                $j =0
            }
            else
            {
                $j = $i
            }

            $ColorLookup.Add($words[$i],$Color[$j])
            $j++
        }
        
    }
    Process
    {
    $content | ForEach-Object {
    
        $TotalLength = 0
               
        $_.split() | `
        Where-Object {-not [string]::IsNullOrWhiteSpace($_)} | ` #Filter-out whiteSpaces
        ForEach-Object{
                        if($TotalLength -lt ($Host.ui.RawUI.BufferSize.Width-10))
                        {
                            #"TotalLength : $TotalLength"
                            $Token =  $_
                            $displayed= $False
                            
                            Foreach($Word in $Words)
                            {
                                if($Token -like "*$Word*")
                                {
                                    $Before, $after = $Token -Split "$Word"
                              
                                        
                                    #"[$Before][$Word][$After]{$Token}`n"
                                    
                                    Write-Host $Before -NoNewline ; 
                                    Write-Host $Word -NoNewline -Fore Black -Back $ColorLookup[$Word];
                                    Write-Host $after -NoNewline ; 
                                    $displayed = $true                                   
                                    #Start-Sleep -Seconds 1    
                                    #break  
                                }

                            } 
                            If(-not $displayed)
                            {   
                                Write-Host "$Token " -NoNewline                                    
                            }
                            else
                            {
                                Write-Host " " -NoNewline  
                            }
                            $TotalLength = $TotalLength + $Token.Length  + 1
                        }
                        else
                        {                      
                            Write-Host '' #New Line  
                            $TotalLength = 0 

                        }

                            #Start-Sleep -Seconds 0.5
                        
        }
        Write-Host '' #New Line               
    }
    }
    end
    {    }

}


#Trace-Word -content (Get-Content iis.log) -words "IIS", 's', "exe", "10", 'system'



function detectPython2() {
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


$PythonCommand = (detectPython2)[-1] # Detect Python 2 installation.

$PipenvCommand = $PythonCommand + " -m pipenv"

$PipenvRunCommand = $PipenvCommand + " run python"

Write-Output("Ensuring packages are installed...")

Invoke-Expression ($PythonCommand+" -m pip install pipenv")

Invoke-Expression ($PythonCommand+" -m pipenv install")

$userInput = ""

while($userInput -notlike "q") {

    if($userInput -like "c") {
        cls
    } elseif($userInput -like "1") {
        Invoke-Expression($PipenvRunCommand+" tests/interactive/testAllTwitterFire.py") | Trace-Word -words "fire"
    }

    Write-Host("q) Quits program.")
    Write-Host("c) Clears the screen.")
    Write-Host("1) Search all of twitter for 'fire'.")
    
    $userInput = Read-Host(" > ")

}

Write-Host("Bye!")