#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import NoArgsCommand
from logging import getLogger, Formatter

logger = getLogger(__name__)
#formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Command(NoArgsCommand):
    def handle_noargs(self, *args, **options):
        # TODO
        # boot arxiv_feed_import
        print "import test"
        #logger.info("start arxiv feed import")

