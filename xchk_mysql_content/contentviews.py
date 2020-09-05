import pathlib

from xchk_core.contentviews import ContentView
from xchk_core.strats import *
from xchk_mysql_comparison_strategies import *

models_dir = pathlib.Path(__file__).parent / 'solutions'

class CheckTestingView(ContentView):
     
    uid = 'xchk_mysql_content_check_testing'
    template = 'xchk_mysql_content/xchk_mysql_content_check_testing.html'
    # calibrating strategy: runs a script to calibrate student and model DB
    # would typically make sure student user exists, has access to specific database only
    strat = MySQLCalibrationStrategy(student_calibration='drop database if exists ModernWays; create database ModernWays;',
                                     model_calibration='drop database if exists ModernWaysBL; create database ModernWaysBL;',
                                     refusing_check=Negation(ConjunctiveCheck([ExecutedScriptHasMatchingOutputCheck(models_dir / 'weergave_data.sql')])),
                                     accepting_check=TrueCheck())
