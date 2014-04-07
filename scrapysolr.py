# Copyright 2014 Dimitrios Kouzis-Loukas <info@scalingexcellence.co.uk>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Solr Pipeline for scrapy"""

import pysolr
from scrapy.conf import settings

class SolrPipeline(object):

    def __init__(self):
        self.mapping = settings['SOLR_MAPPING'].items()
        self.solr = pysolr.Solr(settings['SOLR_URL'], timeout=10)

    def process_item(self, item, spider):
        solr_item = {}
        for dst, src in self.mapping:
            if type(src) is str:
                solr_item[dst] = item[src] if src in item else None
            elif type(src) is list:
                solr_item[dst] = [item[i] if i in item else None for i in src]
            else:
                assert False
                
        self.solr.add([solr_item])
        return item
