Write-Output "This script will start all servers."

$root_dir=Resolve-Path "./"
$webapi_dir=Join-Path -Path $root_dir -ChildPath ".\twitter-fire-scraper-webapi\src\twitter_fire_scraper_webapi"
$dashboard_dir=Join-Path -Path $root_dir -ChildPath ".\twitter-fire-scraper-dashboard\TwitterFireScraperDashboard\TwitterFireScraperDashboard"

start powershell.exe "pipenv run python app.py; PAUSE" -WorkingDirectory "$webapi_dir"

start powershell.exe "npm run watch-tsc; PAUSE" -WorkingDirectory "$dashboard_dir"
start powershell.exe "npm run watch-node; PAUSE" -WorkingDirectory "$dashboard_dir"
