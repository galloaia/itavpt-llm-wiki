#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ricompila il vault in un file unico per LLM: FILO_WIKI_COMPILED.md"""
import os, glob, re
ROOT = os.path.dirname(os.path.abspath(__file__))
ORDER = ["_meta","concetti","entita","prompt","sessioni","fonti"]
TITLES = {"_meta":"Istruzioni e meta","concetti":"Concetti","entita":"Il caso Filo Studio",
          "prompt":"Prompt library","sessioni":"Diario delle sessioni","fonti":"Fonti"}
def strip_fm(t):
    if t.startswith("---"):
        e = t.find("\n---", 3)
        if e != -1: return t[e+4:].lstrip("\n")
    return t
out = ["# FILO STUDIO — WIKI (compilata dal vault)\n",
       "> Generato da compile.py. Non modificare a mano: la sorgente sono le note del vault.\n"]
for folder in ORDER:
    d = os.path.join(ROOT, folder)
    if not os.path.isdir(d): continue
    out.append(f"\n\n# {TITLES.get(folder,folder)}\n")
    for path in sorted(glob.glob(os.path.join(d,"*.md"))):
        name = os.path.splitext(os.path.basename(path))[0]
        txt = strip_fm(open(path,encoding="utf-8").read()).strip()
        txt = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", txt)
        txt = re.sub(r"\[\[([^\]]+)\]\]", r"\1", txt)
        out.append(f"\n## {name}\n\n{txt}\n")
open(os.path.join(ROOT,"FILO_WIKI_COMPILED.md"),"w",encoding="utf-8").write("\n".join(out))
print("Scritto FILO_WIKI_COMPILED.md")
