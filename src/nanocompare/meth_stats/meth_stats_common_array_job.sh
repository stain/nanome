#!/bin/bash
#SBATCH --job-name=meth-common
#SBATCH -q batch
#SBATCH -N 1 # number of nodes
#SBATCH -n 2 # number of cores
#SBATCH --mem 300g # memory pool for all cores
#SBATCH -t 2-23:00:00 # time (D-HH:MM:SS)
#SBATCH -o log/%x.%j.out # STDOUT
#SBATCH -e log/%x.%j.err # STDERR
#SBATCH --array=1-400 # job array index

set -x

prj_dir=/projects/li-lab/yang/workspace/nano-compare

pythonFile=${prj_dir}/src/nanocompare/meth_stats/meth_stats_common.py

mkdir -p log

#python ${pythonFile} $@

python ${pythonFile} -n ${SLURM_ARRAY_TASK_COUNT} -t ${SLURM_ARRAY_TASK_ID}
