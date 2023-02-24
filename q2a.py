def main():
    input_file_name = input("FASTQ file (without file extension): ") #example input: SRR10003462_1

    output_file_name = f'{input_file_name}.fasta'
    output_file = open(output_file_name, 'w+')
    
    try:
        with open (f'{input_file_name}.fastq', 'r') as f:
            for line_index, line in enumerate(f):
                if line_index % 4 == 0:
                    output_file.write(line.replace('@', '>'))
                elif line_index % 4 == 1:
                    output_file.write(line)    
    except Exception as e:
        print (e)
    finally:
        output_file.close()
   
main()