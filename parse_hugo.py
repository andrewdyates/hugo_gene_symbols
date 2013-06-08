#!/usr/bin/python
"""Parse hugo_downloads.txt file, save picked object representation.

EXPECTED HEADERS
HGNC ID	Approved Symbol	Approved Name	Status	Previous Symbols	Synonyms	Chromosome	Date Modified	Accession Numbers	Entrez Gene ID	Ensembl Gene ID	RefSeq IDs	UniProt ID

python parse_hugo.py
"""
import cPickle as pickle
from __init__ import *
from hugo_gene_symbols.hugo import Hugo, FNAME, FNAME_PKL

def main():
  print "Loading %s into Hugo object..." % FNAME
  H = Hugo()
  H.from_filename = FNAME
  print "Saving pickled Hugo object to %s..." % FNAME_PKL
  pickle.dump(H, open(FNAME_PKL,"w"), -1)
  idx_fname = FNAME_PKL.rpartition('.')[0]+".idx.txt"
  print "Saving index as plain text to %s..." % idx_fname
  fp = open(idx_fname,"w")
  for s in sorted(H.official.keys()):
    fp.write("%s\n"%s)
  fp.close()

if __name__ == "__main__":
  main()
