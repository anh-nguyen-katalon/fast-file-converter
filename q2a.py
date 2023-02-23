def main():
    input_file_name = input("FASTQ file (without file extension): ") #example input: SRR10003462_1

    output_file_name = f'{input_file_name}.fasta'
    output_file = open(output_file_name, 'w+')

    try:
        with open (f'{input_file_name}.fastq', 'r') as f:
            while True:
                marker = f.readline() # read marker (1st line)
                if marker:
                    output_file.write(marker.replace('@', '>'))
                    output_file.write(f.readline()) # read sequence (2nd line)
                    f.readline()
                    f.readline()
    except Exception as e:
        print (e)
    finally:
        output_file.close()
   
main()