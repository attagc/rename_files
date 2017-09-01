# rename_files

A script replaces Illumina prefixes (e.g., 1_S01_L001...) with sample ids (my_sample1_S01_L001...) in multiple files.

To do this, you need to specify a file with a table of numbers and names, and a directory containing files to be renamed. Additionally, you can specify the Illumina lane number.

There are 2 columns (number and sample_id) in the table separated by tab:

1 my_sample1

2 my_sample2 ...
