from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class DemoMySQLView(ContentView):
     
    uid = 'xchk_mysql_content_demo'
    template = 'xchk_mysql_content/xchk_mysql_content_demo.html'
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))
