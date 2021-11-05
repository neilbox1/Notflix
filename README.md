# Notflix webpage

## Quick Start
make sure python 3.x is installed, make sure python and pip are in path.
on windows, run in powershell:
```
git clone https://github.com/neilbox1/Notflix
cd Notflix
$env:FLASK_APP = "application.py"
pip install -r requirements.txt
flask run

```
then visit http://localhost:5000

## More Information
```
Notflix is a show recommendation website in which movie APIs populate the page

Users can:
- Log in
- Register if account doesn't exist
- Search for movies
- View movie details
