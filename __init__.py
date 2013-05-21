#!/usr/bin/python
"""Load Hugo object.

USE:
>>> import hugo_gene_symbols
>>> H = hugo_gene_symbols.load()
"""
import cPickle as pickle
import os.path


def load(fname=None):
  if fname is None:
    fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), FNAME_PKL)
  return pickle.load(open(fname))
