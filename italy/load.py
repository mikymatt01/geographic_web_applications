from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Italy

italy_mapping = {
    'fid'        : 'FID',
    'cod_rip'    : 'COD_RIP',
    'cod_reg'    : 'COD_REG',
    'cod_prov'   : 'COD_PROV',
    'cod_cm'     : 'COD_CM',
    'cod_uts'    : 'COD_UTS',
    'pro_com'    : 'PRO_COM', 
    'pro_com_t'  : 'PRO_COM_T',
    'comune'     : 'COMUNE', 
    'comune_a'   : 'COMUNE_A', 
    'cc_uts'     : 'CC_UTS',
    'shape_Leng' : 'SHAPE_LENG',
    'GlobalID'   : 'GlobalID',
    'SHAPE_Le_1' : 'SHAPE_Le_1',
    'shape_Area' : 'SHAPE_Area',
    'mpoly'      : 'MULTIPOLYGON',
}

italy_shp = Path(__file__).resolve().parent / 'data' / 'Municipal_Boundaries_of_Italy_2019' / 'Com01012019_WGS84.shp'

def run(verbose=True):
    lm = LayerMapping(Italy, italy_shp, italy_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

'''
file shp
https://hub.arcgis.com/datasets/inspire-esri::municipal-boundaries-of-italy-2019/explore?location=36.483671%2C24.958452%2C3.94
'''