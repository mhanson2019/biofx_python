#!/usr/bin/env python3
""" Longest Common Substring """

import argparse
import collections
import random
from itertools import starmap
from Bio import SeqIO
from typing import Counter, List, NamedTuple, TextIO


class Args(NamedTuple):
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Longest Common Substring',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input FASTA',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    # Get a list of the sequences as strings
    seqs = [str(rec.seq) for rec in SeqIO.parse(args.file, 'fasta')]

    # Find the length of the shortest sequence, total num of sequences
    num_seqs = len(seqs)
    shortest = min(map(len, seqs))

    for k in range(shortest, 0, -1):
        print(k)
        if subs := kmer_counts(seqs, k, num_seqs):
            print(random.choice(subs))
            break

    # for k in range(shortest, 0, -1):
    #     counts: Counter[str] = collections.Counter()

    #     # Find all kmers of the current size "k" and update the Counter
    #     # for kmers in [set(find_kmers(seq, k)) for seq in seqs]:
    #     for kmers in map(lambda seq: set(find_kmers(seq, k)), seqs):
    #         print(kmers)
    #         counts.update(kmers)

    #     candidates = []
    #     for kmer, count in counts.items():
    #         if count == num_seqs:
    #             candidates.append(kmer)

    #     if candidates:
    #         print(random.choice(candidates))
    #         break

    # args.file.close()

    # def seqs():
    #     return [str(rec.seq) for rec in SeqIO.parse(args.file.name, 'fasta')]

    # shortest, num_seqs = 0, 0
    # for seq_len in map(len, seqs()):
    #     if shortest == 0:
    #         shortest = seq_len

    #     if seq_len < shortest:
    #         shortest = seq_len

    #     num_seqs += 1

    # print(f'shortest = "{shortest}", num = "{num_seqs}"')

    # kmers = list(
    #     filter(None, starmap(lambda s, i: s
    #                          if i == n else None, counts.items())))

    # direction = 'down'
    # k = shortest
    # longest = ''
    # while True:
    #     # print(k)
    #     if k == 0:
    #         print('Bottom (0)')
    #         break

    #     if subs := kmer_counts(seqs, k, num_seqs):
    #         longest = random.choice(subs)
    #         direction == 'up'
    #         k = k + (k // 2)

    #     if direction == 'down':
    #         direction = 'up'
    #         k = k // 2
    #     else:
    #         direction = 'down'
    #         k = k + (k // 2)

    # print(longest)

    # Count from the shortest down to 0
    # for k in range(shortest, 0, -1):
    #     # Create a Counter of strings
    #     subs: Counter[str] = Counter()

    #     # Find all kmers of the current size "k" and update the Counter
    #     for kmers in map(lambda seq: set(find_kmers(seq, k)), seqs):
    #         subs.update(list(kmers))

    #     # The most common returns a tuple of the sequence and frequency
    #     if mc := subs.most_common(1):
    #         most_common, num = mc[0]

    #         # If the frequency of the sequence equals the number of
    #         # sequences then it is present in all the sequences.
    #         if num == num_seqs:
    #             print(most_common)
    #             break


# --------------------------------------------------
def kmer_counts(seqs: List[str], k: int, n: int) -> List[str]:
    """ Get all kmer counts"""

    counts: Counter[str] = collections.Counter()

    # Find all kmers of the current size "k" and update the Counter
    for kmers in map(lambda seq: set(find_kmers(seq, k)), seqs):
        counts.update(kmers)

    return list(
        filter(None, starmap(lambda s, i: s
                             if i == n else None, counts.items())))


# --------------------------------------------------
def test_kmer_counts() -> None:
    """ Test kmer_counts """

    seqs = ['GATTACA', 'TAGACCA', 'ATACA']
    assert kmer_counts(seqs, 5, 3) == []
    assert sorted(kmer_counts(seqs, 5, 1)) == [
        'AGACC', 'ATACA', 'ATTAC', 'GACCA', 'GATTA', 'TAGAC', 'TTACA'
    ]
    assert sorted(kmer_counts(seqs, 2, 3)) == ['AC', 'CA', 'TA']


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> List[str]:
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers() -> None:
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
