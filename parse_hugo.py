#!/usr/bin/python
"""Parse huge_downloads.txt file.

EXPECTED HEADERS
HGNC ID	Approved Symbol	Approved Name	Status	Previous Symbols	Synonyms	Chromosome	Date Modified	Accession Numbers	Entrez Gene ID	Ensembl Gene ID	RefSeq IDs	UniProt ID
"""
EXPECTED_HEADER = "HGNC ID	Approved Symbol	Approved Name	Status	Previous Symbols	Synonyms	Chromosome	Date Modified	Accession Numbers	Entrez Gene ID	Ensembl Gene ID	RefSeq IDs	UniProt ID"

COL_NAMES = "HGNC ID", "Approved Symbol", "Approved Name", "Status", "Previous Symbols", "Synonyms", "Chromosome", "Date Modified", "Accession Numbers", "Entrez Gene ID", "Ensembl Gene ID", "RefSeq IDs", "UniProt ID"

FNAME = "hgnc_downloads.txt"

class HUGO:
  def __init__(self, fname=FNAME):
    fp = open(fname)
    header = fp.next().strip()
    if header != EXPECTED_HEADER:
      raise Exception, "HUGO Header format not recognized. See EXPECTED_HEADER."

    self.withdrawn = {}
    self.offical = {}
    self.unique_alias = {}
    self.dupe_alias = {}
    
    for line in fp:
      row = line.strip('\r\n').split('\t')
      d = dict(zip(COL_NAMES, row))
      if d["Status"] == "Entry Withdrawn":
        self.withdrawn[d["Approved Symbol"].split('~')[0]] = d
        continue

      # Save map
      sym = d["Approved Symbol"]
      altsyms = set(d["Previous Symbols"].split(", ") + d["Previous Synonyms"].split(', '))
      self.offical[sym] = d.update({'altsyms': altsyms})

      # Alternate symbol mapping
      for s in altsyms:
        assert not (s in unique_alias and s in dupe_alias)
        if s not in unique_alias and s not in dupe_alias:
          unique_alias[s] = sym
        else if s in unique_alias:
          alt_sym = unique_alias.pop(s, None)
          dupe_alias[s] = set([alt_sym, sym])
        else:
          dupe_alias[s].add(sym)
          
      # Entrez Gene ID
      # UniProt ID
      # RefSeq IDs
      # Ensembl Gene ID
