__author__ = 'apeckys'
import re



def __main():
    data_set = 'AAGTATTTTATCCTATGCCCCTATGCCCTATGCCGGCCCTATGCACCTATGCCAAAGCGTCCTATGCATCCTATGCCGAAAATGAGGCCGATCCTATGCGCCTATGCCCTATGCCCCTATGCCCTATGCCCCTATGCCCTATGCCCTATGCCCTATGCGGCCCTATGCAGGTCCTATGCAGACCCCTATGCCTACCTATGCCCTATGCCCCTAATATAGCCTATGCGTCCTATGCACCTATGCCGCCCTATGCGCATACACCTATGCGCCTATGCAGATACCTATGCAAGATCCTATGCTTTAGGCATATGTGGAGCCTATGCGCCCTATGCAAATTAGCCACCTATGCAAGCCTATGCCTCACCTATGCATTTCCTATGCGCCTGCCTATGCCCTATGCCCTATGCCCTATGCTCCTATGCACCTATGCATGCCTATGCACCTATGCTTCCTATGCGTATTGATGGCCCTATGCCCTATGCCGTTTCCTATGCACCTATGCGGGTCTCCTATGCCCTTCCTATGCGTACCTATGCCCTCCTATGCTCCTATGCTGCACCCCTATGCAGGCCTATGCCCGGTCTTGAACAAGCCTATGCGCTGCCTATGCCTAGTCCTATGCCCTATGCTACCCTATGCGTCCTATGCACTTGCCTATGCACCTATGCCACCTATGCCCTATGCCCTATGCGAACCCTATGCACCTATGCCCTATGCTATACCGCCTATGCAGCTGTTCACCTATGCTGACGCCTATGCTACCCTATGCCCCCTATGCCTCCTATGCATCCTTGATCCTATGCCCTATGCATAATATTACACCCTATGCACCTATGCTTGCCCTGCCTATGCCCCTATGCATAGCCTATGCTACTGTTTTACGTCCTATGCCACCTATGCCCTATGCCCGATTCCTATGCTCACGCCTATGCCAACGTTCCTATGCTCAAGCCTATGCCCTATGCATTGTACCTATGCTGTTCTATACGCCCTATGC'
    lookup = 'CCTATGCCC'
    result = []
    match = re.finditer(lookup,data_set)

    for m in match:
        result.append(str(m.start() + 1))

    print 'Result: --%s--' % ' '.join(result)



if __name__ == '__main__':
    __main()

