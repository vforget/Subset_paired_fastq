"""
    Fetch reads from query fastq in target fastq.  Fetches based on name of read minus the last char, which is usually designates the direction of the read.
"""

import sys
query_fastq_file = sys.argv[1]
target_fastq_file = sys.argv[2]

th = open(target_fastq_file)
if __name__ == '__main__':
    for qline in open(query_fastq_file):
        if qline[0] == '@':
           q = qline.split()[0][:-1]
           while True:
               tline = th.readline()
               if tline[0] == '@':
                   t = tline.split()[0][:-1]
                   if t == q:
                       print tline,
                       print th.readline(),
                       print th.readline(),
                       print th.readline(),
                       break


