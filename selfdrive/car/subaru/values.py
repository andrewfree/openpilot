from cereal import car
from selfdrive.car import dbc_dict

class CAR:
  OUTBACK = "SUBARU OUTBACK PREMIUM 2015"
  XV2018  = "SUBARU XV ACTIVE 2018"
  ELANTRA = "HYUNDAI ELANTRA 2017"

FINGERPRINTS = {
  CAR.ELANTRA: [{
    66L: 8, 67L: 8, 68L: 8, 127L: 8, 273L: 8, 274L: 8, 275L: 8, 339L: 8, 356L: 4, 399L: 8, 512L: 6, 544L: 8, 593L: 8, 608L: 8, 688L: 5, 790L: 8, 809L: 8, 832L: 8, 897L: 8, 899L: 8, 902L: 8, 903L: 8, 905L: 8, 909L: 8, 916L: 8, 1040L: 8, 1056L: 8, 1057L: 8, 1078L: 4, 1170L: 8, 1265L: 4, 1280L: 1, 1282L: 4, 1287L: 4, 1290L: 8, 1292L: 8, 1294L: 8, 1312L: 8, 1314L: 8, 1322L: 8, 1345L: 8, 1349L: 8, 1351L: 8, 1353L: 8, 1363L: 8, 1366L: 8, 1367L: 8, 1369L: 8, 1407L: 8, 1415L: 8, 1419L: 8, 1425L: 2, 1427L: 6, 1440L: 8, 1456L: 4, 1472L: 8, 1486L: 8, 1487L: 8, 1491L: 8, 1530L: 8, 1532L: 5, 2001L: 8, 2003L: 8, 2004L: 8, 2009L: 8, 2012L: 8, 2016L: 8, 2017L: 8, 2024L: 8, 2025L: 8
          }],  
  CAR.OUTBACK: [{
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 346: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5
          }],
  CAR.XV2018: [{
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
          }],
}

DBC = {
  CAR.ELANTRA: dbc_dict('hyundai_2015_ccan', None), ## TODO: find radar dbc
  CAR.OUTBACK: dbc_dict('subaru_outback_2015_eyesight', None),
  CAR.XV2018: dbc_dict('subaru_xv_2018_eyesight', None),
}