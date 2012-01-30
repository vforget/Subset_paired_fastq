"""
    Retrieve subset of mate pair fastq records from a superset mate pair file:
    Usage:
        %s subset_mate1.fastq superset_mate2.fastq > subset_mate2.fastq
"""

import sys

if len(sys.argv) != 3:
    print sys.argv
    print __doc__
    sys.exit()

query_fastq_file = sys.argv[1]
target_fastq_file = sys.argv[2]

th = open(target_fastq_file)
qc = 0
tc = 0
if __name__ == '__main__':
    for qline in open(query_fastq_file):
        if qline[0:4] == '@HWI':
            q = qline.split()[0]
            while True:
                tline = th.readline()
                if tline[0:4] == '@HWI':
                    t = tline.split()[0]
                    if t == q:
                        print tline,
                        print th.readline(),
                        print th.readline(),
                        print th.readline(),
                        break
