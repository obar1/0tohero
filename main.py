#!/usr/bin/env python3
# coding: utf-8

import sys
from typing import List

from zero_to_one_hundred.factories.factory_provider import FactoryProvider
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs
from zero_to_one_hundred.runner import run_core


if __name__ == "__main__":
    run_core(sys.argv, FactoryProvider(persist_fs, process_fs))
