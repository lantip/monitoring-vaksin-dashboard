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
            "total_sasaran_vaksinasi": 40349049,
            "sasaran_vaksinasi_sdmk": 1468764,
            "sasaran_vaksinasi_petugas_publik": 17327167,
            "sasaran_vaksinasi_lansia": 21553118,
            "vaksinasi1": 12015912,
            "vaksinasi2": 7214534,
            "tahapan_vaksinasi": {
                "sdm_kesehatan": {
                    "total_vaksinasi1": 1488135,
                    "total_vaksinasi2": 1348327,
                    "sudah_vaksin1": 1488135,
                    "sudah_vaksin2": 1348327,
                    "tertunda_vaksin1": 0,
                    "tertunda_vaksin2": 0
                },
                "petugas_publik": {
                    "total_vaksinasi1": 8076455,
                    "total_vaksinasi2": 4475281,
                    "sudah_vaksin1": 8076455,
                    "sudah_vaksin2": 4475281,
                    "tertunda_vaksin1": 0,
                    "tertunda_vaksin2": 0
                },
                "lansia": {
                    "total_vaksinasi1": 2450582,
                    "total_vaksinasi2": 1390926,
                    "sudah_vaksin1": 2450582,
                    "sudah_vaksin2": 1390926,
                    "tertunda_vaksin1": 0,
                    "tertunda_vaksin2": 0
                }
            },
            "cakupan": {
                "vaksinasi1": "29.78%",
                "vaksinasi2": "17.88%",
                "sdm_kesehatan_vaksinasi1": "101.32%",
                "sdm_kesehatan_vaksinasi2": "91.80%",
                "petugas_publik_vaksinasi1": "46.61%",
                "petugas_publik_vaksinasi2": "25.83%",
                "lansia_vaksinasi1": "11.37%",
                "lansia_vaksinasi2": "6.45%"
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
                result['cakupan']['lansia_vaksinasi1'] = ts.dataSegments['0']['dataColumns'][2]['dataValues'][-1]
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
        date = timezone.now().strftime('%Y-%m-%d')
        progres = Progress.objects.filter(tanggal=date)
        if progres.count() > 0:
            progres = progres.latest('id')
            selisih = timezone.now() - progres.created_at
            if (selisih.total_seconds()/3600) > 1:
                progres = Progress()
                progres.tanggal = date 
                progres.data = json.dumps(result)
                progres.save()
        else:
            progres = Progress()
            progres.tanggal = date 
            progres.data = json.dumps(result)
            progres.save()

