from scrapy.cmdline import execute

import sys
import os
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy","crawl","jd_spider"])
execute(["scrapy","crawl","jd_book"])
# setting --> ROBOTSTXT_OBEY = False

