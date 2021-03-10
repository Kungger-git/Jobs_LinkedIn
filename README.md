<h1 align="center"> Find LinkedIn Jobs </h1>

<li>📔 This program finds jobs by scraping on LinkedIn</li>
<li>👨‍💻 Relies on User Input. Accepts: Country, City, State</li>
<li>📑 Data about jobs will be generated as .csv format. </li>

#

<h2 align="center">
<a href="https://asciinema.org/a/398035">
Click Me To See Demo
</a>
</h2>





## Installation:
```console
# clone the repo
$ git clone https://github.com/KungPaoChick/Find_LinkedIn_jobs.git

# change the working directory to Find_LinkedIn_jobs
$ cd Find_LinkedIn_jobs/

# install the requirements
$ python -m pip install -r requirements.txt

```

## Usage:

```console
$ python search_jobs.py --help
usage: search_jobs.py [-h] PLACE [PLACES...]

Find Nearby or Faraway Jobs

positional arguments:
  PLACES       Enter country/city,state. One or more places to look jobs from.

optional arguments:
  -h, --help  show this help message and exit
```

To search for only one place:
```console
$ python search_jobs.py san-jose
```

To search for more than one place:
```
$ python search_jobs.py california texas arizona
```

Data collected will be stored in an individual csv file inside of its respective folder (e.g ```jobs_in_san-jose.csv```)

<h3>Result:<h3/>
<img src="./img/result_csv.png"/>