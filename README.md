scrapy-livingsocial
===================

crawling living social with scrapy
=================================
Just playing with scrapy and web crawling. Trying to get the deals and then filtering out deals with the word "wine".

Requirements
===================
python 2.7
scrapy 0.1.5

how to use:
1. git clone https://github.com/hendychua/scrapy-livingsocial.git
2. scrapy crawl livingSocialSpider -o <json filename> -t json
3. the json file should appear

last updated on 8th july 2012
issues known: filtering out deals with the word "wine" is buggy.