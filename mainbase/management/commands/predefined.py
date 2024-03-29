from django.core.management.base import BaseCommand, CommandError
from mainbase.models import Progress, Province
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = {
                "2021-02-07": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1629223,
                    "Registrasi Ulang": 1627085,
                    "Vaksinasi-1": 784318,
                    "Vaksinasi-2": 139131
                },
                "2021-02-08": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1652958,
                    "Registrasi Ulang": 1643061,
                    "Vaksinasi-1": 814585,
                    "Vaksinasi-2": 171270
                },
                "2021-02-09": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Registrasi Ulang": 1656236,
                    "Vaksinasi-1": 845407,
                    "Vaksinasi-2": 221453
                },
                "2021-02-10": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Registrasi Ulang": 1706487,
                    "Vaksinasi-1": 969546,
                    "Vaksinasi-2": 279251
                },
                "2021-02-11": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Registrasi Ulang": 1736464,
                    "Vaksinasi-1": 1017186,
                    "Vaksinasi-2": 345605
                },
                "2021-02-12": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Registrasi Ulang": 1736464,
                    "Vaksinasi-1": 1017186,
                    "Vaksinasi-2": 345605
                },
                "2021-02-13": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Registrasi Ulang": 1809070,
                    "Vaksinasi-1": 1060326,
                    "Vaksinasi-2": 415486
                },
                "2021-02-14": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Registrasi Ulang": 1737046,
                    "Vaksinasi-1": 1068747,
                    "Vaksinasi-2": 425578
                },
                "2021-02-15": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Populasi Vaksinasi": 1845512,
                    "Vaksinasi-1": 1096095,
                    "Vaksinasi-2": 482625
                },
                "2021-02-16": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Populasi Vaksinasi": 1865080,
                    "Vaksinasi-1": 1120963,
                    "Vaksinasi-2": 537147
                },
                "2021-02-17": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Populasi Vaksinasi": 3781981,
                    "Vaksinasi-1": 1149939,
                    "Vaksinasi-2": 597328
                },
                "2021-02-18": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Populasi Vaksinasi": 4219883,
                    "Vaksinasi-1": 1164144,
                    "Vaksinasi-2": 623832
                },
                "2021-02-19": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK*": 1468764,
                    "Populasi Vaksinasi": 8009514,
                    "Vaksinasi-1": 1191031,
                    "Vaksinasi-2": 668914
                },
                "2021-02-20": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 8046797,
                    "Vaksinasi-1": 1224091,
                    "Vaksinasi-2": 732634
                },
                "2021-02-21": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 8121462,
                    "Vaksinasi-1": 1227918,
                    "Vaksinasi-2": 736710
                },
                "2021-02-22": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 8189835,
                    "Vaksinasi-1": 1244215,
                    "Vaksinasi-2": 764905
                },
                "2021-02-23": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 8504831,
                    "Vaksinasi-1": 1269905,
                    "Vaksinasi-2": 789966
                },
                "2021-02-24": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 10700461,
                    "Vaksinasi-1": 1363138,
                    "Vaksinasi-2": 825650
                },
                "2021-02-25": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 10944383,
                    "Vaksinasi-1": 1461920,
                    "Vaksinasi-2": 853745
                },
                "2021-02-26": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 11105963,
                    "Vaksinasi-1": 1583581,
                    "Vaksinasi-2": 865870
                },
                "2021-02-27": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 11282354,
                    "Vaksinasi-1": 1616165,
                    "Vaksinasi-2": 982370
                },
                "2021-02-28": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 11383576,
                    "Vaksinasi-1": 1691724,
                    "Vaksinasi-2": 998439
                },
                "2021-03-01": {
                    "Total Sasaran Vaksinasi": 181554465,
                    "Sasaran Vaksinasi SDMK": 1468764,
                    "Populasi Vaksinasi": 11540744,
                    "Vaksinasi-1": 1705239,
                    "Vaksinasi-2": 1010028
                },
                "2021-03-02": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 1968057,
                    "vaksinasi2": 1055291,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1852062,
                            "total_vaksinasi2": 1064553,
                            "sudah_vaksin1": 1535093,
                            "sudah_vaksin2": 1055290,
                            "tertunda_vaksin1": 316969,
                            "tertunda_vaksin2": 9263
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 322732,
                            "total_vaksinasi2": 1,
                            "sudah_vaksin1": 309677,
                            "sudah_vaksin2": 1,
                            "tertunda_vaksin1": 13055,
                            "tertunda_vaksin2": 0
                        },
                        "lansia": {
                            "total_vaksinasi1": 126519,
                            "total_vaksinasi2": 0,
                            "sudah_vaksin1": 123287,
                            "sudah_vaksin2": 0,
                            "tertunda_vaksin1": 3232,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "4.88%",
                        "vaksinasi2": "2.62%",
                        "sdm_kesehatan_vaksinasi1": "104.52%",
                        "sdm_kesehatan_vaksinasi2": "71.85%",
                        "petugas_publik_vaksinasi1": "1.79%",
                        "petugas_publik_vaksinasi2": "0.00%",
                        "lansia_vaksinasi1": "0.57%",
                        "lansia_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-03": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 2104967,
                    "vaksinasi2": 1076409,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1893647,
                            "total_vaksinasi2": 1084899,
                            "sudah_vaksin1": 1584300,
                            "sudah_vaksin2": 1075729,
                            "tertunda_vaksin1": 309347,
                            "tertunda_vaksin2": 970
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 397771,
                            "total_vaksinasi2": 683,
                            "sudah_vaksin1": 301939,
                            "sudah_vaksin2": 680
                        },
                        "lansia": {
                            "total_vaksinasi1": 142335,
                            "total_vaksinasi2": 0,
                            "sudah_vaksin1": 138728,
                            "sudah_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "5.22%",
                        "vaksinasi2": "2.67%",
                        "sdm_kesehatan_vaksinasi1": "107.87%",
                        "sdm_kesehatan_vaksinasi2": "73.24%",
                        "petugas_publik_vaksinasi1": "2.20%",
                        "petugas_publik_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-04": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 2286123,
                    "vaksinasi2": 1100228,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1958288,
                            "total_vaksinasi2": 1107811,
                            "sudah_vaksin1": 1646685,
                            "sudah_vaksin2": 1098550,
                            "tertunda_vaksin1": 311603,
                            "tertunda_vaksin2": 9261
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 499388,
                            "total_vaksinasi2": 1684,
                            "sudah_vaksin1": 479419,
                            "sudah_vaksin2": 1676
                        },
                        "lansia": {
                            "total_vaksinasi1": 164842,
                            "total_vaksinasi2": 2
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "5.67%",
                        "vaksinasi2": "2.73%",
                        "sdm_kesehatan_vaksinasi1": "112.11%",
                        "sdm_kesehatan_vaksinasi2": "74.79%",
                        "petugas_publik_vaksinasi1": "2.77%",
                        "petugas_publik_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-05": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 2413615,
                    "vaksinasi2": 1114537,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1996522,
                            "total_vaksinasi2": 1121045,
                            "sudah_vaksin1": 1692016,
                            "sudah_vaksin2": 1111938,
                            "tertunda_vaksin1": 304506,
                            "tertunda_vaksin2": 9107
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 564847,
                            "total_vaksinasi2": 2607,
                            "sudah_vaksin1": 541888,
                            "sudah_vaksin2": 2597,
                            "tertunda_vaksin1": 22959,
                            "tertunda_vaksin2": 10
                        },
                        "lansia": {
                            "total_vaksinasi1": 184677,
                            "total_vaksinasi2": 2,
                            "sudah_vaksin1": 179711,
                            "sudah_vaksin2": 2,
                            "tertunda_vaksin1": 4966,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "5.98%",
                        "vaksinasi2": "2.76%",
                        "sdm_kesehatan_vaksinasi1": "115.20%",
                        "sdm_kesehatan_vaksinasi2": "75.71%",
                        "petugas_publik_vaksinasi1": "3.13%",
                        "petugas_publik_vaksinasi2": "0.00%",
                        "lansia_vaksinasi1": "0.83%",
                        "lansia_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-06": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 2552265,
                    "vaksinasi2": 1130524,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 2042267,
                            "total_vaksinasi2": 1135369,
                            "sudah_vaksin1": 1741784,
                            "sudah_vaksin2": 1126353,
                            "tertunda_vaksin1": 300483,
                            "tertunda_vaksin2": 9016
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 629157,
                            "total_vaksinasi2": 4179,
                            "sudah_vaksin1": 604456,
                            "sudah_vaksin2": 4169,
                            "tertunda_vaksin1": 24701,
                            "tertunda_vaksin2": 10
                        },
                        "lansia": {
                            "total_vaksinasi1": 211350,
                            "total_vaksinasi2": 2,
                            "sudah_vaksin1": 206025,
                            "sudah_vaksin2": 2,
                            "tertunda_vaksin1": 5325,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "6.33%",
                        "vaksinasi2": "2.80%",
                        "sdm_kesehatan_vaksinasi1": "118.59%",
                        "sdm_kesehatan_vaksinasi2": "76.69%",
                        "petugas_publik_vaksinasi1": "3.49%",
                        "petugas_publik_vaksinasi2": "0.00%",
                        "lansia_vaksinasi1": "0.96%",
                        "lansia_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-07": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 2888757,
                    "vaksinasi2": 1133787,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 2358743,
                            "total_vaksinasi2": 1138330,
                            "sudah_vaksin1": 2049651,
                            "sudah_vaksin2": 1129340,
                            "tertunda_vaksin1": 309092,
                            "tertunda_vaksin2": 8990
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 648854,
                            "total_vaksinasi2": 4456,
                            "sudah_vaksin1": 623474,
                            "sudah_vaksin2": 4445,
                            "tertunda_vaksin1": 25380,
                            "tertunda_vaksin2": 11
                        },
                        "lansia": {
                            "total_vaksinasi1": 221189,
                            "total_vaksinasi2": 2,
                            "sudah_vaksin1": 215632,
                            "sudah_vaksin2": 2,
                            "tertunda_vaksin1": 5557,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "7.16%",
                        "vaksinasi2": "2.81%",
                        "sdm_kesehatan_vaksinasi1": "139.55%",
                        "sdm_kesehatan_vaksinasi2": "76.89%",
                        "petugas_publik_vaksinasi1": "3.60%",
                        "petugas_publik_vaksinasi2": "0.00%",
                        "lansia_vaksinasi1": "1.00%",
                        "lansia_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-08": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 3098025,
                    "vaksinasi2": 1158432,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 2441093,
                            "total_vaksinasi2": 1159235,
                            "sudah_vaksin1": 2114655,
                            "sudah_vaksin2": 1149547,
                            "tertunda_vaksin1": 326438,
                            "tertunda_vaksin2": 9688
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 746221,
                            "total_vaksinasi2": 8896,
                            "sudah_vaksin1": 715767,
                            "sudah_vaksin2": 8880,
                            "tertunda_vaksin1": 30454,
                            "tertunda_vaksin2": 16
                        },
                        "lansia": {
                            "total_vaksinasi1": 275160,
                            "total_vaksinasi2": 5,
                            "sudah_vaksin1": 267603,
                            "sudah_vaksin2": 5,
                            "tertunda_vaksin1": 7557,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "7.68%",
                        "vaksinasi2": "2.87%",
                        "sdm_kesehatan_vaksinasi1": "143.98%",
                        "sdm_kesehatan_vaksinasi2": "78.27%",
                        "petugas_publik_vaksinasi1": "4.13%",
                        "petugas_publik_vaksinasi2": "0.00%",
                        "lansia_vaksinasi1": "1.24%",
                        "lansia_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-09": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 3337026,
                    "vaksinasi2": 1197772,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1694410,
                            "total_vaksinasi2": 1137170,
                            "sudah_vaksin1": 1395498,
                            "sudah_vaksin2": 1127633,
                            "tertunda_vaksin1": 298912,
                            "tertunda_vaksin2": 9537
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 1566012,
                            "total_vaksinasi2": 68697,
                            "sudah_vaksin1": 1510937,
                            "sudah_vaksin2": 68527,
                            "tertunda_vaksin1": 55075,
                            "tertunda_vaksin2": 170
                        },
                        "lansia": {
                            "total_vaksinasi1": 443986,
                            "total_vaksinasi2": 1620,
                            "sudah_vaksin1": 430591,
                            "sudah_vaksin2": 1612,
                            "tertunda_vaksin1": 13395,
                            "tertunda_vaksin2": 8
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "8.27%",
                        "vaksinasi2": "2.97%",
                        "sdm_kesehatan_vaksinasi1": "95.01%",
                        "sdm_kesehatan_vaksinasi2": "76.77%",
                        "petugas_publik_vaksinasi1": "8.72%",
                        "petugas_publik_vaksinasi2": "0.00%",
                        "lansia_vaksinasi1": "2.00%",
                        "lansia_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-10": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 3574698,
                    "vaksinasi2": 1262878,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1694410,
                            "total_vaksinasi2": 1137170,
                            "sudah_vaksin1": 1395498,
                            "sudah_vaksin2": 1127633,
                            "tertunda_vaksin1": 298912,
                            "tertunda_vaksin2": 9537
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 1743700,
                            "total_vaksinasi2": 119766,
                            "sudah_vaksin1": 1682896,
                            "sudah_vaksin2": 119495,
                            "tertunda_vaksin1": 60804,
                            "tertunda_vaksin2": 271
                        },
                        "lansia": {
                            "total_vaksinasi1": 509456,
                            "total_vaksinasi2": 2701,
                            "sudah_vaksin1": 494125,
                            "sudah_vaksin2": 2694,
                            "tertunda_vaksin1": 15331,
                            "tertunda_vaksin2": 7
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "8.96%",
                        "vaksinasi2": "3.13%",
                        "sdm_kesehatan_vaksinasi1": "95.16%",
                        "sdm_kesehatan_vaksinasi2": "77.66%",
                        "petugas_publik_vaksinasi1": "9.71%",
                        "petugas_publik_vaksinasi2": "0.00%",
                        "lansia_vaksinasi1": "2.29%",
                        "lansia_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-11": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 3696059,
                    "vaksinasi2": 1295615,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1694081,
                            "total_vaksinasi2": 1157298,
                            "sudah_vaksin1": 1402959,
                            "sudah_vaksin2": 1147846,
                            "tertunda_vaksin1": 291122,
                            "tertunda_vaksin2": 9542
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 1830550,
                            "total_vaksinasi2": 145032,
                            "sudah_vaksin1": 1767209,
                            "sudah_vaksin2": 144689,
                            "tertunda_vaksin1": 63341,
                            "tertunda_vaksin2": 343
                        },
                        "lansia": {
                            "total_vaksinasi1": 542324,
                            "total_vaksinasi2": 3088,
                            "sudah_vaksin1": 525891,
                            "sudah_vaksin2": 3080,
                            "tertunda_vaksin1": 16433,
                            "tertunda_vaksin2": 8
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "9.16%",
                        "vaksinasi2": "3.21%",
                        "sdm_kesehatan_vaksinasi1": "95.25%",
                        "sdm_kesehatan_vaksinasi2": "78.15%",
                        "petugas_publik_vaksinasi1": "10.20%",
                        "petugas_publik_vaksinasi2": "0.00%",
                        "lansia_vaksinasi1": "2.44%",
                        "lansia_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-12": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 3769174,
                    "vaksinasi2": 1339352,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1685204,
                            "total_vaksinasi2": 1162958,
                            "sudah_vaksin1": 1404764,
                            "sudah_vaksin2": 1153626,
                            "tertunda_vaksin1": 280440,
                            "tertunda_vaksin2": 9332
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 1883651,
                            "total_vaksinasi2": 182603,
                            "sudah_vaksin1": 1819875,
                            "sudah_vaksin2": 182177,
                            "tertunda_vaksin1": 63776,
                            "tertunda_vaksin2": 426
                        },
                        "lansia": {
                            "total_vaksinasi1": 561280,
                            "total_vaksinasi2": 3567,
                            "sudah_vaksin1": 544535,
                            "sudah_vaksin2": 3559,
                            "tertunda_vaksin1": 16745,
                            "tertunda_vaksin2": 8
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "9.34%",
                        "vaksinasi2": "3.32%",
                        "sdm_kesehatan_vaksinasi1": "95.64%",
                        "sdm_kesehatan_vaksinasi2": "78.54%",
                        "petugas_publik_vaksinasi1": "10.50%",
                        "petugas_publik_vaksinasi2": "0.00%",
                        "lansia_vaksinasi1": "2.53%",
                        "lansia_vaksinasi2": "0.00%"
                    }
                },
                "2021-03-13": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 3985596,
                    "vaksinasi2": 1454836,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1707829,
                            "total_vaksinasi2": 1181142,
                            "sudah_vaksin1": 1412736,
                            "sudah_vaksin2": 1171385,
                            "tertunda_vaksin1": 295093,
                            "tertunda_vaksin2": 9757
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 2016625,
                            "total_vaksinasi2": 279565,
                            "sudah_vaksin1": 1947195,
                            "sudah_vaksin2": 278954,
                            "tertunda_vaksin1": 69430,
                            "tertunda_vaksin2": 611
                        },
                        "lansia": {
                            "total_vaksinasi1": 645594,
                            "total_vaksinasi2": 4504,
                            "sudah_vaksin1": 625665,
                            "sudah_vaksin2": 4497,
                            "tertunda_vaksin1": 19929,
                            "tertunda_vaksin2": 7
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "9.88%",
                        "vaksinasi2": "3.61%",
                        "sdm_kesehatan_vaksinasi1": "96.19%",
                        "sdm_kesehatan_vaksinasi2": "79.75%",
                        "petugas_publik_vaksinasi1": "11.24%",
                        "petugas_publik_vaksinasi2": "1.61%",
                        "lansia_vaksinasi1": "2.90%",
                        "lansia_vaksinasi2": "0.02%"
                    }
                },
                "2021-03-14": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 4020124,
                    "vaksinasi2": 1460222,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1707004,
                            "total_vaksinasi2": 1182524,
                            "sudah_vaksin1": 1413684,
                            "sudah_vaksin2": 1172848,
                            "tertunda_vaksin1": 293320,
                            "tertunda_vaksin2": 9676
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 2037152,
                            "total_vaksinasi2": 283471,
                            "sudah_vaksin1": 1967948,
                            "sudah_vaksin2": 282844,
                            "tertunda_vaksin1": 69204,
                            "tertunda_vaksin2": 627
                        },
                        "lansia": {
                            "total_vaksinasi1": 658366,
                            "total_vaksinasi2": 4537,
                            "sudah_vaksin1": 638492,
                            "sudah_vaksin2": 4530,
                            "tertunda_vaksin1": 19074,
                            "tertunda_vaksin2": 7
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "9.96%",
                        "vaksinasi2": "3.62%",
                        "sdm_kesehatan_vaksinasi1": "96.25%",
                        "sdm_kesehatan_vaksinasi2": "79.85%",
                        "petugas_publik_vaksinasi1": "11.36%",
                        "petugas_publik_vaksinasi2": "1.63%",
                        "lansia_vaksinasi1": "2.96%",
                        "lansia_vaksinasi2": "0.02%"
                    }
                },
                "2021-03-15": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 4166862,
                    "vaksinasi2": 1572786,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1711943,
                            "total_vaksinasi2": 1193433,
                            "sudah_vaksin1": 1418620,
                            "sudah_vaksin2": 1183715,
                            "tertunda_vaksin1": 293323,
                            "tertunda_vaksin2": 9718
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 2118510,
                            "total_vaksinasi2": 384825,
                            "sudah_vaksin1": 2046659,
                            "sudah_vaksin2": 383920,
                            "tertunda_vaksin1": 71851,
                            "tertunda_vaksin2": 905
                        },
                        "lansia": {
                            "total_vaksinasi1": 722911,
                            "total_vaksinasi2": 5158,
                            "sudah_vaksin1": 701583,
                            "sudah_vaksin2": 5151,
                            "tertunda_vaksin1": 21328,
                            "tertunda_vaksin2": 7
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "10.33%",
                        "vaksinasi2": "3.90%",
                        "sdm_kesehatan_vaksinasi1": "96.59%",
                        "sdm_kesehatan_vaksinasi2": "80.59%",
                        "petugas_publik_vaksinasi1": "11.81%",
                        "petugas_publik_vaksinasi2": "2.22%",
                        "lansia_vaksinasi1": "3.26%",
                        "lansia_vaksinasi2": "0.02%"
                    }
                },
                "2021-03-16": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 4468951,
                    "vaksinasi2": 1716749,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1716263,
                            "total_vaksinasi2": 1206083,
                            "sudah_vaksin1": 1425885,
                            "sudah_vaksin2": 1196387,
                            "tertunda_vaksin1": 290378,
                            "tertunda_vaksin2": 9696
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 2349390,
                            "total_vaksinasi2": 515835,
                            "sudah_vaksin1": 2272399,
                            "sudah_vaksin2": 514516,
                            "tertunda_vaksin1": 76991,
                            "tertunda_vaksin2": 1319
                        },
                        "lansia": {
                            "total_vaksinasi1": 793261,
                            "total_vaksinasi2": 5853,
                            "sudah_vaksin1": 770545,
                            "sudah_vaksin2": 5844,
                            "tertunda_vaksin1": 22594,
                            "tertunda_vaksin2": 7
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "11.08%",
                        "vaksinasi2": "4.25%",
                        "sdm_kesehatan_vaksinasi1": "97.08%",
                        "sdm_kesehatan_vaksinasi2": "81.46%",
                        "petugas_publik_vaksinasi1": "13.11%",
                        "petugas_publik_vaksinasi2": "2.97%",
                        "lansia_vaksinasi1": "3.58%",
                        "lansia_vaksinasi2": "0.03%"
                    }
                },
                "2021-03-17": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 4705248,
                    "vaksinasi2": 1876140,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1719535,
                            "total_vaksinasi2": 1217776,
                            "sudah_vaksin1": 1431713,
                            "sudah_vaksin2": 1208113,
                            "tertunda_vaksin1": 287822,
                            "tertunda_vaksin2": 9663
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 2517332,
                            "total_vaksinasi2": 663148,
                            "sudah_vaksin1": 2436907,
                            "sudah_vaksin2": 661427,
                            "tertunda_vaksin1": 80425,
                            "tertunda_vaksin2": 1721
                        },
                        "lansia": {
                            "total_vaksinasi1": 860827,
                            "total_vaksinasi2": 6609,
                            "sudah_vaksin1": 836628,
                            "sudah_vaksin2": 6600,
                            "tertunda_vaksin1": 24199,
                            "tertunda_vaksin2": 9
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "11.66%",
                        "vaksinasi2": "4.65%",
                        "sdm_kesehatan_vaksinasi1": "97.48%",
                        "sdm_kesehatan_vaksinasi2": "82.25%",
                        "petugas_publik_vaksinasi1": "14.06%",
                        "petugas_publik_vaksinasi2": "3.82%",
                        "lansia_vaksinasi1": "3.88%",
                        "lansia_vaksinasi2": "0.03%"
                    }
                },
                "2021-03-18": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 4838752,
                    "vaksinasi2": 1948531,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1720188,
                            "total_vaksinasi2": 1223444,
                            "sudah_vaksin1": 1434691,
                            "sudah_vaksin2": 1213810,
                            "tertunda_vaksin1": 285497,
                            "tertunda_vaksin2": 9634
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 2625676,
                            "total_vaksinasi2": 729934,
                            "sudah_vaksin1": 2542389,
                            "sudah_vaksin2": 727826,
                            "tertunda_vaksin1": 83287,
                            "tertunda_vaksin2": 2108
                        },
                        "lansia": {
                            "total_vaksinasi1": 887045,
                            "total_vaksinasi2": 6904,
                            "sudah_vaksin1": 861672,
                            "sudah_vaksin2": 6895,
                            "tertunda_vaksin1": 25373,
                            "tertunda_vaksin2": 9
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "11.99%",
                        "vaksinasi2": "4.83%",
                        "sdm_kesehatan_vaksinasi1": "97.68%",
                        "sdm_kesehatan_vaksinasi2": "82.64%",
                        "petugas_publik_vaksinasi1": "14.67%",
                        "petugas_publik_vaksinasi2": "4.20%",
                        "lansia_vaksinasi1": "4.00%",
                        "lansia_vaksinasi2": "0.03%"
                    }
                },
                "2021-03-19": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 4959063,
                    "vaksinasi2": 2068400,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1723226,
                            "total_vaksinasi2": 1230830,
                            "sudah_vaksin1": 1437642,
                            "sudah_vaksin2": 1221179,
                            "tertunda_vaksin1": 285584,
                            "tertunda_vaksin2": 9651
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 2700676,
                            "total_vaksinasi2": 842301,
                            "sudah_vaksin1": 2616319,
                            "sudah_vaksin2": 840115,
                            "tertunda_vaksin1": 84357,
                            "tertunda_vaksin2": 2186
                        },
                        "lansia": {
                            "total_vaksinasi1": 930880,
                            "total_vaksinasi2": 7115,
                            "sudah_vaksin1": 905102,
                            "sudah_vaksin2": 7106,
                            "tertunda_vaksin1": 25778,
                            "tertunda_vaksin2": 9
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "12.29%",
                        "vaksinasi2": "5.13%",
                        "sdm_kesehatan_vaksinasi1": "97.88%",
                        "sdm_kesehatan_vaksinasi2": "83.14%",
                        "petugas_publik_vaksinasi1": "15.10%",
                        "petugas_publik_vaksinasi2": "4.85%",
                        "lansia_vaksinasi1": "4.20%",
                        "lansia_vaksinasi2": "0.03%"
                    }
                },
                "2021-03-20": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 5124948,
                    "vaksinasi2": 2221200,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1724542,
                            "total_vaksinasi2": 1240668,
                            "sudah_vaksin1": 1442440,
                            "sudah_vaksin2": 1231104,
                            "tertunda_vaksin1": 282102,
                            "tertunda_vaksin2": 9564
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 2811625,
                            "total_vaksinasi2": 985019,
                            "sudah_vaksin1": 2727680,
                            "sudah_vaksin2": 982506,
                            "tertunda_vaksin1": 83945,
                            "tertunda_vaksin2": 2513
                        },
                        "lansia": {
                            "total_vaksinasi1": 980967,
                            "total_vaksinasi2": 7599,
                            "sudah_vaksin1": 954828,
                            "sudah_vaksin2": 7590,
                            "tertunda_vaksin1": 26139,
                            "tertunda_vaksin2": 9
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "12.70%",
                        "vaksinasi2": "5.50%",
                        "sdm_kesehatan_vaksinasi1": "98.21%",
                        "sdm_kesehatan_vaksinasi2": "83.82%",
                        "petugas_publik_vaksinasi1": "15.74%",
                        "petugas_publik_vaksinasi2": "5.67%",
                        "lansia_vaksinasi1": "4.43%",
                        "lansia_vaksinasi2": "0.04%"
                    }
                },
                "2021-03-21": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 5567280,
                    "vaksinasi2": 2312601,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1726778,
                            "total_vaksinasi2": 1246356,
                            "sudah_vaksin1": 1446141,
                            "sudah_vaksin2": 1236796,
                            "tertunda_vaksin1": 280637,
                            "tertunda_vaksin2": 9560
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 3201878,
                            "total_vaksinasi2": 1070005,
                            "sudah_vaksin1": 3109656,
                            "sudah_vaksin2": 1067271,
                            "tertunda_vaksin1": 92222,
                            "tertunda_vaksin2": 2734
                        },
                        "lansia": {
                            "total_vaksinasi1": 1038937,
                            "total_vaksinasi2": 8544,
                            "sudah_vaksin1": 1011483,
                            "sudah_vaksin2": 8534,
                            "tertunda_vaksin1": 27454,
                            "tertunda_vaksin2": 10
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "13.80%",
                        "vaksinasi2": "5.73%",
                        "sdm_kesehatan_vaksinasi1": "98.46%",
                        "sdm_kesehatan_vaksinasi2": "84.21%",
                        "petugas_publik_vaksinasi1": "17.95%",
                        "petugas_publik_vaksinasi2": "6.16%",
                        "lansia_vaksinasi1": "4.69%",
                        "lansia_vaksinasi2": "0.04%"
                    }
                },
                "2021-03-22": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 5732210,
                    "vaksinasi2": 2494422,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1742904,
                            "total_vaksinasi2": 1255079,
                            "sudah_vaksin1": 1449757,
                            "sudah_vaksin2": 1245055,
                            "tertunda_vaksin1": 293147,
                            "tertunda_vaksin2": 10024
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 3320662,
                            "total_vaksinasi2": 1240850,
                            "sudah_vaksin1": 3221959,
                            "sudah_vaksin2": 1237961,
                            "tertunda_vaksin1": 98703,
                            "tertunda_vaksin2": 2889
                        },
                        "lansia": {
                            "total_vaksinasi1": 1089889,
                            "total_vaksinasi2": 11416,
                            "sudah_vaksin1": 1011483,
                            "sudah_vaksin2": 8534,
                            "tertunda_vaksin1": 29395,
                            "tertunda_vaksin2": 10
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "14.21%",
                        "vaksinasi2": "6.18%",
                        "sdm_kesehatan_vaksinasi1": "98.71%",
                        "sdm_kesehatan_vaksinasi2": "84.77%",
                        "petugas_publik_vaksinasi1": "18.59%",
                        "petugas_publik_vaksinasi2": "7.14%",
                        "lansia_vaksinasi1": "4.92%",
                        "lansia_vaksinasi2": "0.05%"
                    }
                },
                "2021-03-23": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 5978251,
                    "vaksinasi2": 2709545,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1745467,
                            "total_vaksinasi2": 1264756,
                            "sudah_vaksin1": 1453841,
                            "sudah_vaksin2": 1254761,
                            "tertunda_vaksin1": 291626,
                            "tertunda_vaksin2": 9995
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 3497750,
                            "total_vaksinasi2": 1435557,
                            "sudah_vaksin1": 3399373,
                            "sudah_vaksin2": 1432498,
                            "tertunda_vaksin1": 98377,
                            "tertunda_vaksin2": 3059
                        },
                        "lansia": {
                            "total_vaksinasi1": 1154426,
                            "total_vaksinasi2": 22298,
                            "sudah_vaksin1": 1125037,
                            "sudah_vaksin2": 22286,
                            "tertunda_vaksin1": 29389,
                            "tertunda_vaksin2": 12
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "14.82%",
                        "vaksinasi2": "6.72%",
                        "sdm_kesehatan_vaksinasi1": "98.98%",
                        "sdm_kesehatan_vaksinasi2": "85.43%",
                        "petugas_publik_vaksinasi1": "19.62%",
                        "petugas_publik_vaksinasi2": "8.27%",
                        "lansia_vaksinasi1": "5.22%",
                        "lansia_vaksinasi2": "0.10%"
                    }
                },
                "2021-03-24": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 6389837,
                    "vaksinasi2": 2941016,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1749449,
                            "total_vaksinasi2": 1273147,
                            "sudah_vaksin1": 1458033,
                            "sudah_vaksin2": 1263152,
                            "tertunda_vaksin1": 291416,
                            "tertunda_vaksin2": 9995
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 3807529,
                            "total_vaksinasi2": 1642412,
                            "sudah_vaksin1": 3706240,
                            "sudah_vaksin2": 1638960,
                            "tertunda_vaksin1": 101289,
                            "tertunda_vaksin2": 3452
                        },
                        "lansia": {
                            "total_vaksinasi1": 1255951,
                            "total_vaksinasi2": 38923,
                            "sudah_vaksin1": 1225564,
                            "sudah_vaksin2": 38904,
                            "tertunda_vaksin1": 30387,
                            "tertunda_vaksin2": 19
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "15.84%",
                        "vaksinasi2": "7.29%",
                        "sdm_kesehatan_vaksinasi1": "99.27%",
                        "sdm_kesehatan_vaksinasi2": "86.00%",
                        "petugas_publik_vaksinasi1": "21.39%",
                        "petugas_publik_vaksinasi2": "9.46%",
                        "lansia_vaksinasi1": "5.69%",
                        "lansia_vaksinasi2": "0.18%"
                    }
                },
                "2021-03-25": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 6730456,
                    "vaksinasi2": 3015190,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1752955,
                            "total_vaksinasi2": 1276076,
                            "sudah_vaksin1": 1461489,
                            "sudah_vaksin2": 1266029,
                            "tertunda_vaksin1": 291466,
                            "tertunda_vaksin2": 10047
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 4072885,
                            "total_vaksinasi2": 1695849,
                            "sudah_vaksin1": 3967185,
                            "sudah_vaksin2": 1691934,
                            "tertunda_vaksin1": 105700,
                            "tertunda_vaksin2": 3915
                        },
                        "lansia": {
                            "total_vaksinasi1": 1333920,
                            "total_vaksinasi2": 57264,
                            "sudah_vaksin1": 1301782,
                            "sudah_vaksin2": 57227,
                            "tertunda_vaksin1": 32138,
                            "tertunda_vaksin2": 37
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "16.68%",
                        "vaksinasi2": "7.47%",
                        "sdm_kesehatan_vaksinasi1": "99.50%",
                        "sdm_kesehatan_vaksinasi2": "86.20%",
                        "petugas_publik_vaksinasi1": "22.90%",
                        "petugas_publik_vaksinasi2": "9.76%",
                        "lansia_vaksinasi1": "6.04%",
                        "lansia_vaksinasi2": "0.27%"
                    }
                },
                "2021-03-26": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 6990082,
                    "vaksinasi2": 3152612,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1756123,
                            "total_vaksinasi2": 1281079,
                            "sudah_vaksin1": 1464650,
                            "sudah_vaksin2": 1270999,
                            "tertunda_vaksin1": 291473,
                            "tertunda_vaksin2": 10080
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 4280036,
                            "total_vaksinasi2": 1807577,
                            "sudah_vaksin1": 4169000,
                            "sudah_vaksin2": 1803291,
                            "tertunda_vaksin1": 111036,
                            "tertunda_vaksin2": 4286
                        },
                        "lansia": {
                            "total_vaksinasi1": 1390015,
                            "total_vaksinasi2": 78369,
                            "sudah_vaksin1": 1356432,
                            "sudah_vaksin2": 78322,
                            "tertunda_vaksin1": 33583,
                            "tertunda_vaksin2": 47
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "17.32%",
                        "vaksinasi2": "7.81%",
                        "sdm_kesehatan_vaksinasi1": "99.72%",
                        "sdm_kesehatan_vaksinasi2": "86.54%",
                        "petugas_publik_vaksinasi1": "24.06%",
                        "petugas_publik_vaksinasi2": "10.41%",
                        "lansia_vaksinasi1": "6.29%",
                        "lansia_vaksinasi2": "0.36%"
                    }
                },
                "2021-03-27": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 7190663,
                    "vaksinasi2": 3235027,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1717448,
                            "total_vaksinasi2": 1282889,
                            "sudah_vaksin1": 1429971,
                            "sudah_vaksin2": 1272782,
                            "tertunda_vaksin1": 287477,
                            "tertunda_vaksin2": 10107
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 4476761,
                            "total_vaksinasi2": 1870487,
                            "sudah_vaksin1": 4357342,
                            "sudah_vaksin2": 1865840,
                            "tertunda_vaksin1": 119419,
                            "tertunda_vaksin2": 4647
                        },
                        "lansia": {
                            "total_vaksinasi1": 1439689,
                            "total_vaksinasi2": 96488,
                            "sudah_vaksin1": 1403350,
                            "sudah_vaksin2": 96405,
                            "tertunda_vaksin1": 36339,
                            "tertunda_vaksin2": 83
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "17.82%",
                        "vaksinasi2": "8.02%",
                        "sdm_kesehatan_vaksinasi1": "97.36%",
                        "sdm_kesehatan_vaksinasi2": "86.66%",
                        "petugas_publik_vaksinasi1": "25.15%",
                        "petugas_publik_vaksinasi2": "10.77%",
                        "lansia_vaksinasi1": "6.51%",
                        "lansia_vaksinasi2": "0.45%"
                    }
                },
                "2021-03-28": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 7243202,
                    "vaksinasi2": 3246455,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1717283,
                            "total_vaksinasi2": 1283514,
                            "sudah_vaksin1": 1430423,
                            "sudah_vaksin2": 1273410,
                            "tertunda_vaksin1": 288860,
                            "tertunda_vaksin2": 10104
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 4520868,
                            "total_vaksinasi2": 1876173,
                            "sudah_vaksin1": 4399250,
                            "sudah_vaksin2": 1871416,
                            "tertunda_vaksin1": 121618,
                            "tertunda_vaksin2": 4757
                        },
                        "lansia": {
                            "total_vaksinasi1": 1450474,
                            "total_vaksinasi2": 101734,
                            "sudah_vaksin1": 1413529,
                            "sudah_vaksin2": 101629,
                            "tertunda_vaksin1": 36945,
                            "tertunda_vaksin2": 105
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "17.95%",
                        "vaksinasi2": "8.05%",
                        "sdm_kesehatan_vaksinasi1": "97.39%",
                        "sdm_kesehatan_vaksinasi2": "86.70%",
                        "petugas_publik_vaksinasi1": "25.39%",
                        "petugas_publik_vaksinasi2": "10.80%",
                        "lansia_vaksinasi1": "6.56%",
                        "lansia_vaksinasi2": "0.47%"
                    }
                },
                "2021-03-29": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 7435851,
                    "vaksinasi2": 3330639,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1719546,
                            "total_vaksinasi2": 1286092,
                            "sudah_vaksin1": 1432153,
                            "sudah_vaksin2": 1275981,
                            "tertunda_vaksin1": 287393,
                            "tertunda_vaksin2": 10111
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 4672927,
                            "total_vaksinasi2": 1940918,
                            "sudah_vaksin1": 4549721,
                            "sudah_vaksin2": 1936112,
                            "tertunda_vaksin1": 123206,
                            "tertunda_vaksin2": 4806
                        },
                        "lansia": {
                            "total_vaksinasi1": 1491701,
                            "total_vaksinasi2": 118666,
                            "sudah_vaksin1": 1453977,
                            "sudah_vaksin2": 118546,
                            "tertunda_vaksin1": 37724,
                            "tertunda_vaksin2": 120
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "18.43%",
                        "vaksinasi2": "8.25%",
                        "sdm_kesehatan_vaksinasi1": "97.51%",
                        "sdm_kesehatan_vaksinasi2": "86.87%",
                        "petugas_publik_vaksinasi1": "26.26%",
                        "petugas_publik_vaksinasi2": "11.17%",
                        "lansia_vaksinasi1": "6.75%",
                        "lansia_vaksinasi2": "0.55%"
                    }
                },
                "2021-03-30": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 7840024,
                    "vaksinasi2": 3561192,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1435351,
                            "total_vaksinasi2": 1282214,
                            "sudah_vaksin1": 1435351,
                            "sudah_vaksin2": 1282214,
                            "tertunda_vaksin1": 154677,
                            "tertunda_vaksin2": 6724
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 4858404,
                            "total_vaksinasi2": 2119155,
                            "sudah_vaksin1": 4858404,
                            "sudah_vaksin2": 2119155,
                            "tertunda_vaksin1": 105531,
                            "tertunda_vaksin2": 4643
                        },
                        "lansia": {
                            "total_vaksinasi1": 1546269,
                            "total_vaksinasi2": 159823,
                            "sudah_vaksin1": 1546269,
                            "sudah_vaksin2": 159823,
                            "tertunda_vaksin1": 31140,
                            "tertunda_vaksin2": 106
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "19.43%",
                        "vaksinasi2": "8.83%",
                        "sdm_kesehatan_vaksinasi1": "97.73%",
                        "sdm_kesehatan_vaksinasi2": "87.30%",
                        "petugas_publik_vaksinasi1": "28.04%",
                        "petugas_publik_vaksinasi2": "12.23%",
                        "lansia_vaksinasi1": "7.17%",
                        "lansia_vaksinasi2": "0.74%"
                    }
                },
                "2021-03-31": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 8115714,
                    "vaksinasi2": 3717081,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1438016,
                            "total_vaksinasi2": 1286168,
                            "sudah_vaksin1": 1438016,
                            "sudah_vaksin2": 1286168,
                            "tertunda_vaksin1": 153688,
                            "tertunda_vaksin2": 6699
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 5061358,
                            "total_vaksinasi2": 2247772,
                            "sudah_vaksin1": 5061358,
                            "sudah_vaksin2": 2247772,
                            "tertunda_vaksin1": 108453,
                            "tertunda_vaksin2": 4813
                        },
                        "lansia": {
                            "total_vaksinasi1": 1616340,
                            "total_vaksinasi2": 183141,
                            "sudah_vaksin1": 1616340,
                            "sudah_vaksin2": 183141,
                            "tertunda_vaksin1": 32320,
                            "tertunda_vaksin2": 151
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "20.11%",
                        "vaksinasi2": "9.21%",
                        "sdm_kesehatan_vaksinasi1": "97.91%",
                        "sdm_kesehatan_vaksinasi2": "87.57%",
                        "petugas_publik_vaksinasi1": "29.21%",
                        "petugas_publik_vaksinasi2": "12.97%",
                        "lansia_vaksinasi1": "7.50%",
                        "lansia_vaksinasi2": "0.85%"
                    }
                },
                "2021-04-01": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 8291164,
                    "vaksinasi2": 3830675,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1439814,
                            "total_vaksinasi2": 1288811,
                            "sudah_vaksin1": 1439814,
                            "sudah_vaksin2": 1288811,
                            "tertunda_vaksin1": 152744,
                            "tertunda_vaksin2": 6687
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 5190314,
                            "total_vaksinasi2": 2333418,
                            "sudah_vaksin1": 5190314,
                            "sudah_vaksin2": 2333418,
                            "tertunda_vaksin1": 110908,
                            "tertunda_vaksin2": 4883
                        },
                        "lansia": {
                            "total_vaksinasi1": 1661036,
                            "total_vaksinasi2": 208446,
                            "sudah_vaksin1": 1661036,
                            "sudah_vaksin2": 208446,
                            "tertunda_vaksin1": 33412,
                            "tertunda_vaksin2": 176
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "20.55%",
                        "vaksinasi2": "9.49%",
                        "sdm_kesehatan_vaksinasi1": "98.03%",
                        "sdm_kesehatan_vaksinasi2": "87.75%",
                        "petugas_publik_vaksinasi1": "29.95%",
                        "petugas_publik_vaksinasi2": "13.47%",
                        "lansia_vaksinasi1": "7.71%",
                        "lansia_vaksinasi2": "0.97%"
                    }
                },
                "2021-04-02": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 8424729,
                    "vaksinasi2": 3867762,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1441069,
                            "total_vaksinasi2": 1290437,
                            "sudah_vaksin1": 1441069,
                            "sudah_vaksin2": 1290437,
                            "tertunda_vaksin1": 151959,
                            "tertunda_vaksin2": 5570
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 5304045,
                            "total_vaksinasi2": 2359548,
                            "sudah_vaksin1": 5304045,
                            "sudah_vaksin2": 2359548,
                            "tertunda_vaksin1": 113500,
                            "tertunda_vaksin2": 4999
                        },
                        "lansia": {
                            "total_vaksinasi1": 1679615,
                            "total_vaksinasi2": 217777,
                            "sudah_vaksin1": 1679615,
                            "sudah_vaksin2": 217777,
                            "tertunda_vaksin1": 34079,
                            "tertunda_vaksin2": 201
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "20.88%",
                        "vaksinasi2": "9.59%",
                        "sdm_kesehatan_vaksinasi1": "98.11%",
                        "sdm_kesehatan_vaksinasi2": "87.86%",
                        "petugas_publik_vaksinasi1": "30.61%",
                        "petugas_publik_vaksinasi2": "13.62%",
                        "lansia_vaksinasi1": "7.79%",
                        "lansia_vaksinasi2": "1.01%"
                    }
                },
                "2021-04-03": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 8533422,
                    "vaksinasi2": 3951869,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1441503,
                            "total_vaksinasi2": 1292114,
                            "sudah_vaksin1": 1441503,
                            "sudah_vaksin2": 1292114,
                            "tertunda_vaksin1": 151958,
                            "tertunda_vaksin2": 6674
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 5386077,
                            "total_vaksinasi2": 2405638,
                            "sudah_vaksin1": 5386077,
                            "sudah_vaksin2": 2405638,
                            "tertunda_vaksin1": 114401,
                            "tertunda_vaksin2": 5081
                        },
                        "lansia": {
                            "total_vaksinasi1": 1705842,
                            "total_vaksinasi2": 254117,
                            "sudah_vaksin1": 1705842,
                            "sudah_vaksin2": 254117,
                            "tertunda_vaksin1": 34294,
                            "tertunda_vaksin2": 220
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "21.15%",
                        "vaksinasi2": "9.79%",
                        "sdm_kesehatan_vaksinasi1": "98.14%",
                        "sdm_kesehatan_vaksinasi2": "87.97%",
                        "petugas_publik_vaksinasi1": "31.08%",
                        "petugas_publik_vaksinasi2": "13.88%",
                        "lansia_vaksinasi1": "7.91%",
                        "lansia_vaksinasi2": "1.18%"
                    }
                },
                "2021-04-04": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 8634321,
                    "vaksinasi2": 4014803,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1441916,
                            "total_vaksinasi2": 1293503,
                            "sudah_vaksin1": 1441916,
                            "sudah_vaksin2": 1293503,
                            "tertunda_vaksin1": 151971,
                            "tertunda_vaksin2": 6679
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 5471102,
                            "total_vaksinasi2": 2459553,
                            "sudah_vaksin1": 5471102,
                            "sudah_vaksin2": 2459553,
                            "tertunda_vaksin1": 115988,
                            "tertunda_vaksin2": 5229
                        },
                        "lansia": {
                            "total_vaksinasi1": 1721303,
                            "total_vaksinasi2": 261747,
                            "sudah_vaksin1": 1721303,
                            "sudah_vaksin2": 261747,
                            "tertunda_vaksin1": 34870,
                            "tertunda_vaksin2": 286
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "21.40%",
                        "vaksinasi2": "9.95%",
                        "sdm_kesehatan_vaksinasi1": "98.14%",
                        "sdm_kesehatan_vaksinasi2": "88.07%",
                        "petugas_publik_vaksinasi1": "31.58%",
                        "petugas_publik_vaksinasi2": "14.19%",
                        "lansia_vaksinasi1": "7.99%",
                        "lansia_vaksinasi2": "1.21%"
                    }
                },
                "2021-04-05": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 8772081,
                    "vaksinasi2": 4149587,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1442812,
                            "total_vaksinasi2": 1295762,
                            "sudah_vaksin1": 1442812,
                            "sudah_vaksin2": 1295762,
                            "tertunda_vaksin1": 151984,
                            "tertunda_vaksin2": 6688
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 5576617,
                            "total_vaksinasi2": 2554067,
                            "sudah_vaksin1": 5576617,
                            "sudah_vaksin2": 2554067,
                            "tertunda_vaksin1": 117673,
                            "tertunda_vaksin2": 5611
                        },
                        "lansia": {
                            "total_vaksinasi1": 1752652,
                            "total_vaksinasi2": 299758,
                            "sudah_vaksin1": 1752652,
                            "sudah_vaksin2": 299758,
                            "tertunda_vaksin1": 36051,
                            "tertunda_vaksin2": 323
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "21.74%",
                        "vaksinasi2": "10.28%",
                        "sdm_kesehatan_vaksinasi1": "98.23%",
                        "sdm_kesehatan_vaksinasi2": "88.22%",
                        "petugas_publik_vaksinasi1": "32.18%",
                        "petugas_publik_vaksinasi2": "14.74%",
                        "lansia_vaksinasi1": "8.13%",
                        "lansia_vaksinasi2": "1.39%"
                    }
                },
                "2021-04-06": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 8890024,
                    "vaksinasi2": 4268222,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1443702,
                            "total_vaksinasi2": 1298042,
                            "sudah_vaksin1": 1443702,
                            "sudah_vaksin2": 1298042,
                            "tertunda_vaksin1": 152008,
                            "tertunda_vaksin2": 6701
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 5668967,
                            "total_vaksinasi2": 2626042,
                            "sudah_vaksin1": 5668967,
                            "sudah_vaksin2": 2626042,
                            "tertunda_vaksin1": 120530,
                            "tertunda_vaksin2": 5968
                        },
                        "lansia": {
                            "total_vaksinasi1": 1777355,
                            "total_vaksinasi2": 344138,
                            "sudah_vaksin1": 1777355,
                            "sudah_vaksin2": 344138,
                            "tertunda_vaksin1": 37064,
                            "tertunda_vaksin2": 491
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "22.03%",
                        "vaksinasi2": "10.58%",
                        "sdm_kesehatan_vaksinasi1": "98.29%",
                        "sdm_kesehatan_vaksinasi2": "88.38%",
                        "petugas_publik_vaksinasi1": "32.72%",
                        "petugas_publik_vaksinasi2": "15.16%",
                        "lansia_vaksinasi1": "8.25%",
                        "lansia_vaksinasi2": "1.60%"
                    }
                },
                "2021-04-07": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 9196435,
                    "vaksinasi2": 4554695,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1445970,
                            "total_vaksinasi2": 1302596,
                            "sudah_vaksin1": 1445970,
                            "sudah_vaksin2": 1302596,
                            "tertunda_vaksin1": 152022,
                            "tertunda_vaksin2": 6715
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 5905406,
                            "total_vaksinasi2": 2812292,
                            "sudah_vaksin1": 5905406,
                            "sudah_vaksin2": 2812292,
                            "tertunda_vaksin1": 123764,
                            "tertunda_vaksin2": 6264
                        },
                        "lansia": {
                            "total_vaksinasi1": 1844923,
                            "total_vaksinasi2": 439807,
                            "sudah_vaksin1": 1844923,
                            "sudah_vaksin2": 439807,
                            "tertunda_vaksin1": 38126,
                            "tertunda_vaksin2": 637
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "22.79%",
                        "vaksinasi2": "11.29%",
                        "sdm_kesehatan_vaksinasi1": "98.45%",
                        "sdm_kesehatan_vaksinasi2": "88.69%",
                        "petugas_publik_vaksinasi1": "34.08%",
                        "petugas_publik_vaksinasi2": "16.23%",
                        "lansia_vaksinasi1": "8.56%",
                        "lansia_vaksinasi2": "2.04%"
                    }
                },
                "2021-04-08": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 9229638,
                    "vaksinasi2": 4591089,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1446282,
                            "total_vaksinasi2": 1303118,
                            "sudah_vaksin1": 1446282,
                            "sudah_vaksin2": 1303118,
                            "tertunda_vaksin1": 152022,
                            "tertunda_vaksin2": 6715
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 5930291,
                            "total_vaksinasi2": 2836455,
                            "sudah_vaksin1": 5930291,
                            "sudah_vaksin2": 2836455,
                            "tertunda_vaksin1": 123764,
                            "tertunda_vaksin2": 6264
                        },
                        "lansia": {
                            "total_vaksinasi1": 1852838,
                            "total_vaksinasi2": 451516,
                            "sudah_vaksin1": 1852838,
                            "sudah_vaksin2": 451516,
                            "tertunda_vaksin1": 38126,
                            "tertunda_vaksin2": 637
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "22.87%",
                        "vaksinasi2": "11.38%",
                        "sdm_kesehatan_vaksinasi1": "98.47%",
                        "sdm_kesehatan_vaksinasi2": "88.72%",
                        "petugas_publik_vaksinasi1": "34.23%",
                        "petugas_publik_vaksinasi2": "16.37%",
                        "lansia_vaksinasi1": "8.60%",
                        "lansia_vaksinasi2": "2.09%"
                    }
                },
                "2021-04-09": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 9784278,
                    "vaksinasi2": 4943231,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1451499,
                            "total_vaksinasi2": 1309220,
                            "sudah_vaksin1": 1451499,
                            "sudah_vaksin2": 1309220,
                            "tertunda_vaksin1": 150034,
                            "tertunda_vaksin2": 6686
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 6364623,
                            "total_vaksinasi2": 3094267,
                            "sudah_vaksin1": 6364623,
                            "sudah_vaksin2": 3094267,
                            "tertunda_vaksin1": 126657,
                            "tertunda_vaksin2": 6358
                        },
                        "lansia": {
                            "total_vaksinasi1": 1967429,
                            "total_vaksinasi2": 539744,
                            "sudah_vaksin1": 1967429,
                            "sudah_vaksin2": 539744,
                            "tertunda_vaksin1": 39536,
                            "tertunda_vaksin2": 753
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "24.25%",
                        "vaksinasi2": "12.25%",
                        "sdm_kesehatan_vaksinasi1": "98.82%",
                        "sdm_kesehatan_vaksinasi2": "89.14%",
                        "petugas_publik_vaksinasi1": "36.73%",
                        "petugas_publik_vaksinasi2": "17.86%",
                        "lansia_vaksinasi1": "9.13%",
                        "lansia_vaksinasi2": "2.50%"
                    }
                },
                "2021-04-10": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10002901,
                    "vaksinasi2": 5079048,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1453325,
                            "total_vaksinasi2": 1310929,
                            "sudah_vaksin1": 1453325,
                            "sudah_vaksin2": 1310929,
                            "tertunda_vaksin1": 149337,
                            "tertunda_vaksin2": 6656
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 6529107,
                            "total_vaksinasi2": 3179779,
                            "sudah_vaksin1": 6529107,
                            "sudah_vaksin2": 3179779,
                            "tertunda_vaksin1": 127530,
                            "tertunda_vaksin2": 6406
                        },
                        "lansia": {
                            "total_vaksinasi1": 2019832,
                            "total_vaksinasi2": 588340,
                            "sudah_vaksin1": 2019832,
                            "sudah_vaksin2": 588340,
                            "tertunda_vaksin1": 39983,
                            "tertunda_vaksin2": 826
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "24.79%",
                        "vaksinasi2": "12.59%",
                        "sdm_kesehatan_vaksinasi1": "98.94%",
                        "sdm_kesehatan_vaksinasi2": "89.25%",
                        "petugas_publik_vaksinasi1": "37.68%",
                        "petugas_publik_vaksinasi2": "18.35%",
                        "lansia_vaksinasi1": "9.37%",
                        "lansia_vaksinasi2": "2.73%"
                    }
                },
                "2021-04-11": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10049541,
                    "vaksinasi2": 5101921,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1453701,
                            "total_vaksinasi2": 1311259,
                            "sudah_vaksin1": 1453701,
                            "sudah_vaksin2": 1311259,
                            "tertunda_vaksin1": 148805,
                            "tertunda_vaksin2": 6641
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 6564802,
                            "total_vaksinasi2": 3193198,
                            "sudah_vaksin1": 6564802,
                            "sudah_vaksin2": 3193198,
                            "tertunda_vaksin1": 128973,
                            "tertunda_vaksin2": 6447
                        },
                        "lansia": {
                            "total_vaksinasi1": 2030311,
                            "total_vaksinasi2": 597464,
                            "sudah_vaksin1": 2030311,
                            "sudah_vaksin2": 597464,
                            "tertunda_vaksin1": 40679,
                            "tertunda_vaksin2": 894
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "24.90%",
                        "vaksinasi2": "12.64%",
                        "sdm_kesehatan_vaksinasi1": "98.97%",
                        "sdm_kesehatan_vaksinasi2": "89.28%",
                        "petugas_publik_vaksinasi1": "37.89%",
                        "petugas_publik_vaksinasi2": "18.43%",
                        "lansia_vaksinasi1": "9.42%",
                        "lansia_vaksinasi2": "2.77%"
                    }
                },
                "2021-04-12": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10280073,
                    "vaksinasi2": 5322501,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1455949,
                            "total_vaksinasi2": 1314396,
                            "sudah_vaksin1": 1455949,
                            "sudah_vaksin2": 1314396,
                            "tertunda_vaksin1": 148755,
                            "tertunda_vaksin2": 6639
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 6735239,
                            "total_vaksinasi2": 3336070,
                            "sudah_vaksin1": 6735239,
                            "sudah_vaksin2": 3336070,
                            "tertunda_vaksin1": 129112,
                            "tertunda_vaksin2": 6443
                        },
                        "lansia": {
                            "total_vaksinasi1": 2088158,
                            "total_vaksinasi2": 672035,
                            "sudah_vaksin1": 2088158,
                            "sudah_vaksin2": 672035,
                            "tertunda_vaksin1": 40766,
                            "tertunda_vaksin2": 895
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "25.48%",
                        "vaksinasi2": "13.19%",
                        "sdm_kesehatan_vaksinasi1": "99.13%",
                        "sdm_kesehatan_vaksinasi2": "89.49%",
                        "petugas_publik_vaksinasi1": "38.87%",
                        "petugas_publik_vaksinasi2": "19.25%",
                        "lansia_vaksinasi1": "9.69%",
                        "lansia_vaksinasi2": "3.12%"
                    }
                },
                "2021-04-13": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10377734,
                    "vaksinasi2": 5433715,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1457405,
                            "total_vaksinasi2": 1316347,
                            "sudah_vaksin1": 1457405,
                            "sudah_vaksin2": 1316347,
                            "tertunda_vaksin1": 147714,
                            "tertunda_vaksin2": 6599
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 6811090,
                            "total_vaksinasi2": 3394098,
                            "sudah_vaksin1": 6811090,
                            "sudah_vaksin2": 3394098,
                            "tertunda_vaksin1": 130626,
                            "tertunda_vaksin2": 6462
                        },
                        "lansia": {
                            "total_vaksinasi1": 2108512,
                            "total_vaksinasi2": 722410,
                            "sudah_vaksin1": 2108512,
                            "sudah_vaksin2": 722410,
                            "tertunda_vaksin1": 41417,
                            "tertunda_vaksin2": 970
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "25.72%",
                        "vaksinasi2": "13.47%",
                        "sdm_kesehatan_vaksinasi1": "99.23%",
                        "sdm_kesehatan_vaksinasi2": "89.62%",
                        "petugas_publik_vaksinasi1": "39.31%",
                        "petugas_publik_vaksinasi2": "19.59%",
                        "lansia_vaksinasi1": "9.78%",
                        "lansia_vaksinasi2": "3.35%"
                    }
                },
                "2021-04-14": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10481905,
                    "vaksinasi2": 5572859,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1459169,
                            "total_vaksinasi2": 1318528,
                            "sudah_vaksin1": 1459169,
                            "sudah_vaksin2": 1318528,
                            "tertunda_vaksin1": 146950,
                            "tertunda_vaksin2": 6575
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 6890942,
                            "total_vaksinasi2": 3472356,
                            "sudah_vaksin1": 6890942,
                            "sudah_vaksin2": 3472356,
                            "tertunda_vaksin1": 130606,
                            "tertunda_vaksin2": 6391
                        },
                        "lansia": {
                            "total_vaksinasi1": 2131067,
                            "total_vaksinasi2": 781975,
                            "sudah_vaksin1": 2131067,
                            "sudah_vaksin2": 781975,
                            "tertunda_vaksin1": 41394,
                            "tertunda_vaksin2": 1009
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "25.98%",
                        "vaksinasi2": "13.81%",
                        "sdm_kesehatan_vaksinasi1": "99.35%",
                        "sdm_kesehatan_vaksinasi2": "89.77%",
                        "petugas_publik_vaksinasi1": "39.77%",
                        "petugas_publik_vaksinasi2": "20.04%",
                        "lansia_vaksinasi1": "9.89%",
                        "lansia_vaksinasi2": "3.63%"
                    }
                },
                "2021-04-15": {
                    "total_sasaran_vaksinasi": 40349051,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327169,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10600469,
                    "vaksinasi2": 5715813,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1460747,
                            "total_vaksinasi2": 1321085,
                            "sudah_vaksin1": 1460747,
                            "sudah_vaksin2": 1321085,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 6983097,
                            "total_vaksinasi2": 3549833,
                            "sudah_vaksin1": 6983097,
                            "sudah_vaksin2": 3549833,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "lansia": {
                            "total_vaksinasi1": 2155898,
                            "total_vaksinasi2": 844895,
                            "sudah_vaksin1": 2155898,
                            "sudah_vaksin2": 844895,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "26.27%",
                        "vaksinasi2": "14.17%",
                        "sdm_kesehatan_vaksinasi1": "99.45%",
                        "sdm_kesehatan_vaksinasi2": "89.95%",
                        "petugas_publik_vaksinasi1": "40.30%",
                        "petugas_publik_vaksinasi2": "20.49%",
                        "lansia_vaksinasi1": "10.00%",
                        "lansia_vaksinasi2": "3.92%"
                    }
                },
                "2021-04-16": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10709628,
                    "vaksinasi2": 5821888,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1464225,
                            "total_vaksinasi2": 1323006,
                            "sudah_vaksin1": 1464225,
                            "sudah_vaksin2": 1323006,
                            "tertunda_vaksin1": 143641,
                            "tertunda_vaksin2": 6469
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7066375,
                            "total_vaksinasi2": 3600857,
                            "sudah_vaksin1": 7066375,
                            "sudah_vaksin2": 3600857,
                            "tertunda_vaksin1": 128132,
                            "tertunda_vaksin2": 5920
                        },
                        "lansia": {
                            "total_vaksinasi1": 2178289,
                            "total_vaksinasi2": 898025,
                            "sudah_vaksin1": 2178289,
                            "sudah_vaksin2": 898025,
                            "tertunda_vaksin1": 40800,
                            "tertunda_vaksin2": 1127
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "26.54%",
                        "vaksinasi2": "14.43%",
                        "sdm_kesehatan_vaksinasi1": "99.69%",
                        "sdm_kesehatan_vaksinasi2": "90.08%",
                        "petugas_publik_vaksinasi1": "40.78%",
                        "petugas_publik_vaksinasi2": "20.78%",
                        "lansia_vaksinasi1": "10.11%",
                        "lansia_vaksinasi2": "4.17%"
                    }
                },
                "2021-04-17": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10801563,
                    "vaksinasi2": 5890790,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1465021,
                            "total_vaksinasi2": 1323987,
                            "sudah_vaksin1": 1465021,
                            "sudah_vaksin2": 1323987,
                            "tertunda_vaksin1": 143155,
                            "tertunda_vaksin2": 6452
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7139477,
                            "total_vaksinasi2": 3636800,
                            "sudah_vaksin1": 7139477,
                            "sudah_vaksin2": 3636800,
                            "tertunda_vaksin1": 128461,
                            "tertunda_vaksin2": 5904
                        },
                        "lansia": {
                            "total_vaksinasi1": 2199326,
                            "total_vaksinasi2": 930003,
                            "sudah_vaksin1": 2199326,
                            "sudah_vaksin2": 930003,
                            "tertunda_vaksin1": 40950,
                            "tertunda_vaksin2": 1199
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "26.78%",
                        "vaksinasi2": "14.60%",
                        "sdm_kesehatan_vaksinasi1": "99.75%",
                        "sdm_kesehatan_vaksinasi2": "90.14%",
                        "petugas_publik_vaksinasi1": "41.20%",
                        "petugas_publik_vaksinasi2": "20.99%",
                        "lansia_vaksinasi1": "10.20%",
                        "lansia_vaksinasi2": "4.31%"
                    }
                },
                "2021-04-18": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10815649,
                    "vaksinasi2": 5900242,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1465188,
                            "total_vaksinasi2": 1324349,
                            "sudah_vaksin1": 1465188,
                            "sudah_vaksin2": 1324349,
                            "tertunda_vaksin1": 142886,
                            "tertunda_vaksin2": 6441
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7147867,
                            "total_vaksinasi2": 3643369,
                            "sudah_vaksin1": 7147867,
                            "sudah_vaksin2": 3643369,
                            "tertunda_vaksin1": 128683,
                            "tertunda_vaksin2": 5915
                        },
                        "lansia": {
                            "total_vaksinasi1": 2201855,
                            "total_vaksinasi2": 932524,
                            "sudah_vaksin1": 2201855,
                            "sudah_vaksin2": 932524,
                            "tertunda_vaksin1": 41163,
                            "tertunda_vaksin2": 1226
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "26.80%",
                        "vaksinasi2": "14.62%",
                        "sdm_kesehatan_vaksinasi1": "99.76%",
                        "sdm_kesehatan_vaksinasi2": "90.17%",
                        "petugas_publik_vaksinasi1": "41.25%",
                        "petugas_publik_vaksinasi2": "21.03%",
                        "lansia_vaksinasi1": "10.22%",
                        "lansia_vaksinasi2": "4.33%"
                    }
                },
                "2021-04-19": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 10972343,
                    "vaksinasi2": 6052612,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1466675,
                            "total_vaksinasi2": 1325963,
                            "sudah_vaksin1": 1466675,
                            "sudah_vaksin2": 1325963,
                            "tertunda_vaksin1": 142868,
                            "tertunda_vaksin2": 6440
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7267647,
                            "total_vaksinasi2": 3724381,
                            "sudah_vaksin1": 7267647,
                            "sudah_vaksin2": 3724381,
                            "tertunda_vaksin1": 128696,
                            "tertunda_vaksin2": 5932
                        },
                        "lansia": {
                            "total_vaksinasi1": 2237282,
                            "total_vaksinasi2": 1002268,
                            "sudah_vaksin1": 2237282,
                            "sudah_vaksin2": 1002268,
                            "tertunda_vaksin1": 41163,
                            "tertunda_vaksin2": 1229
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "27.19%",
                        "vaksinasi2": "15.00%",
                        "sdm_kesehatan_vaksinasi1": "99.86%",
                        "sdm_kesehatan_vaksinasi2": "90.28%",
                        "petugas_publik_vaksinasi1": "41.94%",
                        "petugas_publik_vaksinasi2": "21.49%",
                        "lansia_vaksinasi1": "10.38%",
                        "lansia_vaksinasi2": "4.65%"
                    }
                },
                "2021-04-20": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 11116253,
                    "vaksinasi2": 6158748,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1467860,
                            "total_vaksinasi2": 1327443,
                            "sudah_vaksin1": 1467860,
                            "sudah_vaksin2": 1327443,
                            "tertunda_vaksin1": 142319,
                            "tertunda_vaksin2": 6416
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7383064,
                            "total_vaksinasi2": 3790548,
                            "sudah_vaksin1": 7383064,
                            "sudah_vaksin2": 3790548,
                            "tertunda_vaksin1": 131416,
                            "tertunda_vaksin2": 5866
                        },
                        "lansia": {
                            "total_vaksinasi1": 2264590,
                            "total_vaksinasi2": 1040757,
                            "sudah_vaksin1": 2264590,
                            "sudah_vaksin2": 1040757,
                            "tertunda_vaksin1": 41587,
                            "tertunda_vaksin2": 1213
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "27.55%",
                        "vaksinasi2": "15.26%",
                        "sdm_kesehatan_vaksinasi1": "99.94%",
                        "sdm_kesehatan_vaksinasi2": "90.38%",
                        "petugas_publik_vaksinasi1": "42.61%",
                        "petugas_publik_vaksinasi2": "21.88%",
                        "lansia_vaksinasi1": "10.51%",
                        "lansia_vaksinasi2": "4.83%"
                    }
                },
                "2021-04-21": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 11302294,
                    "vaksinasi2": 6341931,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1480525,
                            "total_vaksinasi2": 1338926,
                            "sudah_vaksin1": 1480525,
                            "sudah_vaksin2": 1338926,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7522899,
                            "total_vaksinasi2": 3891666,
                            "sudah_vaksin1": 7522899,
                            "sudah_vaksin2": 3891666,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "lansia": {
                            "total_vaksinasi1": 2298131,
                            "total_vaksinasi2": 1111339,
                            "sudah_vaksin1": 2298131,
                            "sudah_vaksin2": 1111339,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "28.01%",
                        "vaksinasi2": "15.72%",
                        "sdm_kesehatan_vaksinasi1": "100.80%",
                        "sdm_kesehatan_vaksinasi2": "91.16%",
                        "petugas_publik_vaksinasi1": "43.42%",
                        "petugas_publik_vaksinasi2": "22.46%",
                        "lansia_vaksinasi1": "10.66%",
                        "lansia_vaksinasi2": "5.16%"
                    }
                },
                "2021-04-22": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 11432711,
                    "vaksinasi2": 6488197,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1481515,
                            "total_vaksinasi2": 1340196,
                            "sudah_vaksin1": 1481515,
                            "sudah_vaksin2": 1340196,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7621517,
                            "total_vaksinasi2": 3977973,
                            "sudah_vaksin1": 7621517,
                            "sudah_vaksin2": 3977973,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "lansia": {
                            "total_vaksinasi1": 2328940,
                            "total_vaksinasi2": 1170028,
                            "sudah_vaksin1": 2328940,
                            "sudah_vaksin2": 1170028,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "28.33%",
                        "vaksinasi2": "16.08%",
                        "sdm_kesehatan_vaksinasi1": "100.87%",
                        "sdm_kesehatan_vaksinasi2": "91.25%",
                        "petugas_publik_vaksinasi1": "43.99%",
                        "petugas_publik_vaksinasi2": "22.96%",
                        "lansia_vaksinasi1": "10.81%",
                        "lansia_vaksinasi2": "5.43%"
                    }
                },
                "2021-04-23": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 11623251,
                    "vaksinasi2": 6699327,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1484188,
                            "total_vaksinasi2": 1343218,
                            "sudah_vaksin1": 1484188,
                            "sudah_vaksin2": 1343218,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7777053,
                            "total_vaksinasi2": 4124238,
                            "sudah_vaksin1": 7777053,
                            "sudah_vaksin2": 4124238,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "lansia": {
                            "total_vaksinasi1": 2361270,
                            "total_vaksinasi2": 1231871,
                            "sudah_vaksin1": 2361270,
                            "sudah_vaksin2": 1231871,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "28.81%",
                        "vaksinasi2": "16.60%",
                        "sdm_kesehatan_vaksinasi1": "101.06%",
                        "sdm_kesehatan_vaksinasi2": "91.45%",
                        "petugas_publik_vaksinasi1": "44.88%",
                        "petugas_publik_vaksinasi2": "23.80%",
                        "lansia_vaksinasi1": "10.96%",
                        "lansia_vaksinasi2": "5.72%"
                    }
                },
                "2021-04-24": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 11718546,
                    "vaksinasi2": 6798241,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1484764,
                            "total_vaksinasi2": 1344232,
                            "sudah_vaksin1": 1484764,
                            "sudah_vaksin2": 1344232,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7848268,
                            "total_vaksinasi2": 4190969,
                            "sudah_vaksin1": 7848268,
                            "sudah_vaksin2": 4190969,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "lansia": {
                            "total_vaksinasi1": 2384567,
                            "total_vaksinasi2": 1263040,
                            "sudah_vaksin1": 2384567,
                            "sudah_vaksin2": 1263040,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "29.04%",
                        "vaksinasi2": "16.85%",
                        "sdm_kesehatan_vaksinasi1": "101.10%",
                        "sdm_kesehatan_vaksinasi2": "91.52%",
                        "petugas_publik_vaksinasi1": "45.29%",
                        "petugas_publik_vaksinasi2": "24.19%",
                        "lansia_vaksinasi1": "11.06%",
                        "lansia_vaksinasi2": "5.86%"
                    }
                },
                "2021-04-25": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 11741559,
                    "vaksinasi2": 6829415,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1485102,
                            "total_vaksinasi2": 1344441,
                            "sudah_vaksin1": 1485102,
                            "sudah_vaksin2": 1344441,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7869046,
                            "total_vaksinasi2": 4215417,
                            "sudah_vaksin1": 7869046,
                            "sudah_vaksin2": 4215417,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "lansia": {
                            "total_vaksinasi1": 2386671,
                            "total_vaksinasi2": 1269557,
                            "sudah_vaksin1": 2386671,
                            "sudah_vaksin2": 1269557,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "29.10%",
                        "vaksinasi2": "16.93%",
                        "sdm_kesehatan_vaksinasi1": "101.11%",
                        "sdm_kesehatan_vaksinasi2": "91.54%",
                        "petugas_publik_vaksinasi1": "45.41%",
                        "petugas_publik_vaksinasi2": "24.33%",
                        "lansia_vaksinasi1": "11.07%",
                        "lansia_vaksinasi2": "5.89%"
                    }
                },
                "2021-04-26": {
                    "total_sasaran_vaksinasi": 40349049,
                    "sasaran_vaksinasi_sdmk": 1468764,
                    "sasaran_vaksinasi_petugas_publik": 17327167,
                    "sasaran_vaksinasi_lansia": 21553118,
                    "vaksinasi1": 11844579,
                    "vaksinasi2": 6998304,
                    "tahapan_vaksinasi": {
                        "sdm_kesehatan": {
                            "total_vaksinasi1": 1486110,
                            "total_vaksinasi2": 1345922,
                            "sudah_vaksin1": 1486110,
                            "sudah_vaksin2": 1345922,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "petugas_publik": {
                            "total_vaksinasi1": 7944332,
                            "total_vaksinasi2": 4324849,
                            "sudah_vaksin1": 7944332,
                            "sudah_vaksin2": 4324849,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        },
                        "lansia": {
                            "total_vaksinasi1": 2413397,
                            "total_vaksinasi2": 1327533,
                            "sudah_vaksin1": 2413397,
                            "sudah_vaksin2": 1327533,
                            "tertunda_vaksin1": 0,
                            "tertunda_vaksin2": 0
                        }
                    },
                    "cakupan": {
                        "vaksinasi1": "29.36%",
                        "vaksinasi2": "17.34%",
                        "sdm_kesehatan_vaksinasi1": "101.18%",
                        "sdm_kesehatan_vaksinasi2": "91.64%",
                        "petugas_publik_vaksinasi1": "45.85%",
                        "petugas_publik_vaksinasi2": "24.96%",
                        "lansia_vaksinasi1": "11.20%",
                        "lansia_vaksinasi2": "6.16%"
                    }
                },
                "2021-04-27": {
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
            }
        for key, vals in data.items():
            prog = Progress.objects.filter(tanggal = key)
            if prog.count() < 1:
                prog = Progress()
                prog.tanggal = key
                prog.data = json.dumps(vals)
                prog.save()