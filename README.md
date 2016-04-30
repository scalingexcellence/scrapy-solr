Description
===========
It's a pipeline which allows you to store scrapy items in a Solr server.

Install
=======
   pip install scrapysolr

Configure your settings.py:
----------------------------
    ITEM_PIPELINES = [
      'scrapysolr.SolrPipeline',
    ]
    
    SOLR_URL = 'http://urlofyoursolrserver/solr'
    SOLR_MAPPING = {
      'id': 'url',
      'text': ['title', 'breadcrumbs', 'description'],
      'description': 'description',
      'keywords': 'breadcrumbs',
      'price': 'price',
      'title': 'title'
    }
    SOLR_IGNORE_DUPLICATES = True
    SOLR_DUPLICATES_KEY_FIELDS = ['id']

The SOLR_MAPPING setting, maps your item's fields to Solr fields. Usually some transformations will be needed e.g. a url might be used as Solr id. You can use multiple Scrapy fields for a single Solr field as you can see in the 'text' mapping above. The 'text' happens to be the default field for the default Solr schema and as a result you can use it to simplify your queries (since you don't have to include the field if you want to match everything).
SOLR_IGNORE_DUPLICATES and SOLR_DUPLICATES_KEY_FIELDS, the id keys to search for an existing entry, are used to only insert into Solr if the item is not already there. The key fields have to be defined as sources in the mapping.

Changelog
=========

0.2.0
Ability to not override a Solr entry when the item is already present.

0.1.0
initial release

Licence
=======
Copyright 2014 Dimitrios Kouzis-Loukas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
