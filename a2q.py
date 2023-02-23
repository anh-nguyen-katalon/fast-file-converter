def main():
    input_file_name = input("FASTA file (without file extension): ") #example input: SRR10003462_1

    output_file_name = f'{input_file_name}.fastq'
    output_file = open(output_file_name, 'w+')

    try:
        with open (f'{input_file_name}.fasta', 'r') as f:
            while True:
                marker = f.readline() # read marker (1st line)
                if marker:
                    marker = marker.removeprefix(">")
                    output_file.write(marker)
                output_file.write(f'{f.readline()}') # read sequence (2nd line)
                output_file.write('+\n')
                output_file.write('\n')
        
    except Exception as e:
        print (e)
    finally:
        output_file.close()
   
main()