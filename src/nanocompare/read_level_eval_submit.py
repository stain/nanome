#!/usr/bin/env python3

"""
Submit read level evaluation jobs for each line input of tsv.
"""
import csv
import os
import subprocess
from sys import argv

from nanocompare.global_config import src_base_dir

sbatchFile = os.path.join('nanocompare', "read_level_eval.sbatch")

if __name__ == '__main__':
    infile = open(argv[1], 'r')

    others = ' '.join(argv[2:])
    print(f'Other options={others}')

    csvfile = csv.DictReader(infile, delimiter='\t')
    for row in csvfile:
        if row['status'] == "submit":
            logdir = os.path.join('.', 'log')
            os.makedirs(logdir, exist_ok=True)

            command = \
                f"""
set -x; sbatch --job-name=meth_perf_{row['RunPrefix']} --output=log/%x.%j.out --error=log/%x.%j.err \
 --export=ALL,DeepSignal_calls="{row['DeepSignal_calls']}",Tombo_calls="{row['Tombo_calls']}",Nanopolish_calls="{row['Nanopolish_calls']}",DeepMod_calls="{row['DeepMod_calls']}",Megalodon_calls="{row['Megalodon_calls']}",Guppy_calls="{row['Guppy_calls']}",bgTruth="{row['bgTruth']}",\
RunPrefix="{row['RunPrefix']}",parser="{row['parser']}",minCov="{row['minCov']}",dsname="{row['Dataset']}",otherOptions="{others}" {sbatchFile}
"""

            print(row['RunPrefix'], subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8"))
