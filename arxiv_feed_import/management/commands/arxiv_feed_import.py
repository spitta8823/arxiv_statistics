#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import NoArgsCommand
from logging import getLogger

logger = getLogger(__name__)


class Command(NoArgsCommand):
    def handle_noargs(self, *args, **options):
        # TODO
        # boot arxiv_feed_import

        logger.info("start arxiv feed import")

