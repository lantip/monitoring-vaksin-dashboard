from django.core.management.base import BaseCommand, CommandError
from mainbase.models import Progress, Province
from datetime import datetime, timedelta
from django.utils import timezone
from tableauscraper import TableauScraper as TS
from django.conf import settings
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        ts = TS()
        urls = settings.KEMKES['daily']
        result = {
            "total_sasaran_vaksinasi": 0,
            "sasaran_vaksinasi_sdmk": 0,
            "sasaran_vaksinasi_petugas_publik": 0,
            "sasaran_vaksinasi_lansia": 0,
            "vaksinasi1": 0,
            "vaksinasi2": 0,
            "tahapan_vaksinasi": {
                "sdm_kesehatan": {
                    "total_vaksinasi1": 0,
                    "total_vaksinasi2": 0,
                    "sudah_vaksin1": 0,
                    "sudah_vaksin2": 0,
                    "tertunda_vaksin1": 0,
                    "tertunda_vaksin2": 0
                },
                "petugas_publik": {
                    "total_vaksinasi1": 0,
                    "total_vaksinasi2": 0,
                    "sudah_vaksin1": 0,
                    "sudah_vaksin2": 0,
                    "tertunda_vaksin1": 0,
                    "tertunda_vaksin2": 0
                },
                "lansia": {
                    "total_vaksinasi1": 0,
                    "total_vaksinasi2": 0,
                    "sudah_vaksin1": 0,
                    "sudah_vaksin2": 0,
                    "tertunda_vaksin1": 0,
                    "tertunda_vaksin2": 0
                }
            },
            "cakupan": {
                "vaksinasi1": "",
                "vaksinasi2": "",
                "sdm_kesehatan_vaksinasi1": "",
                "sdm_kesehatan_vaksinasi2": "",
                "petugas_publik_vaksinasi1": "",
                "petugas_publik_vaksinasi2": "",
                "lansia_vaksinasi1": "",
                "lansia_vaksinasi2": ""
            }
        }
        for key, url in urls.items():
            ts.loads(url)
            if key == 'sasaran':
                result['total_sasaran_vaksinasi'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
            elif key == 'total1':
                result['vaksinasi1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['cakupan']['vaksinasi1'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-1]
            elif key == 'total2':
                result['vaksinasi2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['cakupan']['vaksinasi2'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-1]
            elif key == 'nakes':
                sasaran = None
                for key, com in ts.info['worldUpdate']['applicationPresModel']['workbookPresModel']['dashboardPresModel']['zones'].items():
                    try:
                        sasaran = int(com['zoneCommon']['name'].replace('.',''))
                    except:
                        pass
                if sasaran:
                    result['sasaran_vaksinasi_sdmk'] = sasaran              
                result['tahapan_vaksinasi']['sdm_kesehatan']['total_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['sdm_kesehatan']['total_vaksinasi2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['tahapan_vaksinasi']['sdm_kesehatan']['sudah_vaksin1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['sdm_kesehatan']['sudah_vaksin2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['cakupan']['sdm_kesehatan_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-3]
                result['cakupan']['sdm_kesehatan_vaksinasi2'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-1]
            elif key == 'lansia':
                sasaran = None
                for key, com in ts.info['worldUpdate']['applicationPresModel']['workbookPresModel']['dashboardPresModel']['zones'].items():
                    try:
                        sasaran = int(com['zoneCommon']['name'].replace('.',''))
                    except:
                        pass
                if sasaran:
                    result['sasaran_vaksinasi_lansia'] = sasaran                
                result['tahapan_vaksinasi']['lansia']['total_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['lansia']['total_vaksinasi2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['tahapan_vaksinasi']['lansia']['sudah_vaksin1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['lansia']['sudah_vaksin2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['cakupan']['lansia_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-3]
                result['cakupan']['lansia_vaksinasi2'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-1]
            elif key == 'pelayan_publik':
                sasaran = None
                for key, com in ts.info['worldUpdate']['applicationPresModel']['workbookPresModel']['dashboardPresModel']['zones'].items():
                    try:
                        sasaran = int(com['zoneCommon']['name'].replace('.',''))
                    except:
                        pass
                if sasaran:
                    result['sasaran_vaksinasi_petugas_publik'] = sasaran                
                result['tahapan_vaksinasi']['petugas_publik']['total_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['petugas_publik']['total_vaksinasi2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['tahapan_vaksinasi']['petugas_publik']['sudah_vaksin1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['petugas_publik']['sudah_vaksin2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['cakupan']['petugas_publik_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-3]
                result['cakupan']['petugas_publik_vaksinasi2'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-1]
            elif key == "masyarakat_umum":
                sasaran = None
                for key, com in ts.info['worldUpdate']['applicationPresModel']['workbookPresModel']['dashboardPresModel']['zones'].items():
                    try:
                        sasaran = int(com['zoneCommon']['name'].replace('.',''))
                    except:
                        pass
                if sasaran:
                    result['sasaran_vaksinasi_masyarakat_umum'] = sasaran                
                result['tahapan_vaksinasi']['masyarakat_umum']['total_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['masyarakat_umum']['total_vaksinasi2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['tahapan_vaksinasi']['masyarakat_umum']['sudah_vaksin1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['masyarakat_umum']['sudah_vaksin2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['cakupan']['masyarakat_umum_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-3]
                result['cakupan']['masyarakat_umum_vaksinasi2'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-1]
            elif key == "kelompok_1217":
                sasaran = None
                for key, com in ts.info['worldUpdate']['applicationPresModel']['workbookPresModel']['dashboardPresModel']['zones'].items():
                    try:
                        sasaran = int(com['zoneCommon']['name'].replace('.',''))
                    except:
                        pass
                if sasaran:
                    result['sasaran_vaksinasi_masyarakat_umum'] = sasaran                
                result['tahapan_vaksinasi']['kelompok_usia_12_17']['total_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['kelompok_usia_12_17']['total_vaksinasi2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['tahapan_vaksinasi']['kelompok_usia_12_17']['sudah_vaksin1'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][0]
                result['tahapan_vaksinasi']['kelompok_usia_12_17']['sudah_vaksin2'] = ts.dataSegments['0']['dataColumns'][0]['dataValues'][1]
                result['cakupan']['kelompok_usia_12_17'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-3]
                result['cakupan']['kelompok_usia_12_17'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-1]
        date = datetime.now().strftime('%Y-%m-%d')
        progres = Progress.objects.filter(tanggal=date)
        if result['total_sasaran_vaksinasi'] > 0:

            if progres.count() > 0:
                progres = progres.latest('id')
                selisih = datetime.now() - progres.created_at.replace(tzinfo=None)
                if (selisih.total_seconds()/3600) > 1:
                    print('saving update')
                    progres = Progress()
                    progres.tanggal = date 
                    progres.data = json.dumps(result)
                    progres.created_at = datetime.now()
                    progres.save()
            else:
                print('saving data')
                progres = Progress()
                progres.tanggal = date 
                progres.data = json.dumps(result)
                progres.created_at = datetime.now()
                progres.save()

