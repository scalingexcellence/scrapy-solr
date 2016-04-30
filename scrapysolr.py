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
import logging
from scrapy.conf import settings


class SolrPipeline(object):
    def __init__(self):
        self.mapping = settings['SOLR_MAPPING'].items()
        self.ignore_duplicates = settings['SOLR_IGNORE_DUPLICATES'] or False
        self.id_fields = settings['SOLR_DUPLICATES_KEY_FIELDS']
        if self.ignore_duplicates and not self.id_fields:
            raise RuntimeError('To ignore duplicates SOLR_DUPLICATES_KEY_FIELDS has to be defined')
        self.solr = pysolr.Solr(settings['SOLR_URL'], timeout=10)

    def process_item(self, item, spider):
        if self.ignore_duplicates:
            dup_keys_values = [str(dst) + ':' + '"' + self.__get_item_value__(item, src) + '"' for dst, src in
                               self.mapping
                               if dst in self.id_fields]
            query = " ".join(dup_keys_values)
            result = self.solr.search(query)
            if len(result) != 0:
                logging.info('Skipping duplicate')
                return item
        solr_item = {}
        for dst, src in self.mapping:
            solr_item[dst] = self.__get_item_value__(item, src)
        self.solr.add([solr_item])
        return item

    def __get_item_value__(self, item, src):
        if type(src) is str:
            return item[src] if src in item else None
        elif type(src) is list:
            return [item[i] if i in item else None for i in src]
        else:
            raise TypeError('Only string and list are valid mapping source')
