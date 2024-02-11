<h1 align="center"> Career Extract API </h1>

<li>📔 This program finds job descriptions by scraping on LinkedIn</li>
<li>👨‍💻 Relies on User Input. Accepts: job urls</li>
<li>📑 Data about jobs will be generated as json format. </li>

#

<h2 align="center">
<a href="https://asciinema.org/a/398283">
Click Me To See Demo
</a>
</h2>




Suggested setup

## Installation:
- [Virtual Env - venv](https://docs.python.org/3/library/venv.html)
- Create virtual environment folder

```bash
python3 -m venv venv
```

- Activate VENV

```bash
source venv/bin/activate
```

- Install packages

```bash
pip install -r requirements.txt
```

- Check Packages

```bash
pip list --local
```

- Deactivate VENV

```bash
deactivate
```

Want to run locally checkout the [Requirements file](requirements.txt)


# install the requirements
$ python -m pip install -r requirements.txt

```

## Usage:

```console
$ python search_jobs.py --help
usage: search_jobs.py [-h] [-p PLACES [PLACES ...]] [-j jobfunction [jobfunction ...]] [-jp job place]

Find Nearby or Faraway Jobs

optional arguments:
  -h, --help            show this help message and exit
  -p PLACES [PLACES ...], --place PLACES [PLACES ...]
                        Enter country/city/state. One or more places to look jobs from.
  -j jobfunction [jobfunction ...], --jobfunction jobfunction [jobfunction ...]
                        Searches Job Specification in your area. (e.g software-engineer)
  -jp job place, --jobplace job place
                        Searches The Specified Job in the Specified Place. (e.g teacher iowa)

```


To search for only one place:
```console
$ python search_jobs.py -p san-jose
```

To search for more than one place:
```
$ python search_jobs.py -p california texas arizona
```

To search a Specific job in your area:
```
$ python search_jobs.py -j teacher
```

To search Specific more than one job in your area:
```
$ python search_jobs.py -j teacher engineer designer
```

To search a Specific Job in a Specific Location:
```
$ python search_jobs.py -jp designer san-jose
```

Data collected will be stored in an individual csv file inside of its respective folder (e.g ```jobs_in_san-jose.csv```)

<h3>Result:<h3/>
<img src="./img/result_csv.png"/>

## Contributing
We would love to have you help us with the development of Jobs_LinkedIn. Each and every contribution is greatly valued!