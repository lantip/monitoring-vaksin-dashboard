
### Monitoring Dashboard Vaksinasi
Script berbasis Django untuk mengubah data [Dashboard Vaksinasi](https://vaksin.kemkes.go.id/#/vaccines) menjadi API.

### Live API
- [Cekdiri](https://cekdiri.id/vaksinasi/)

## Pre-requisites
1. python3
2. Django
3. MySQL/MariaDB


## Setup
1. Clone this repo: `git clone https://github.com/lantip/monitoring-vaksin-dashboard.git`
2. CD into this repo: `cd monitoring-vaksin-dashboard`
3. Install python requirements: `pip install -r requirements.txt`
4. Buat database untuk menyimpan data
5. Ubah `vaksin/settings_example.py` menjadi `vaksin/settings.py`, dan sesuaikan data akses databasenya.
6. Jalankan `python manage.py migrate`
7. Isikan data awal dengan menjalankan `python manage.py predefined`


## Cron
1. Jalankan crontab tiap jam (sesuaikan kebutuhan)

`0 * * * * /path/to/python /path/to/repo/manage.py getdata`

## API
Jalankan `python manage.py runserver`, dan API bisa diakses di `http://localhost:8000/api`
