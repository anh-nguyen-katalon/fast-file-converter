import random
import string
def main():
    input_file_name = input("FASTA file (without file extension): ") #example input: SRR10003462_1

    output_file_name = f'{input_file_name}.fastq'
    output_file = open(output_file_name, 'w+')

    try:
        with open (f'{input_file_name}.fasta', 'r') as f:
            for line_index, line in enumerate(f):
                if line_index % 2 == 0:
                    output_file.write(line.replace(">", "@"))
                else:
                    output_file.write(line)
                    output_file.write('+\n')
                    for i in range(len(line)):
                        output_file.write(random.choice(string.ascii_letters))
                    output_file.write('\n')
    except Exception as e:
        print (e)
    finally:
        output_file.close()
   
main()