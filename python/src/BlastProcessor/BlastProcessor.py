import os
import fnmatch
import pandas as pd

class BLASTProcessor:

    @staticmethod
    def process_blast_files_in_directory(directory_path, file_pattern="*.txt"):
        """
        Processes BLAST output files in a specified directory.
        
        Args:
            directory_path (str): Path to the directory containing BLAST files.
            file_pattern (str): Pattern to match BLAST files (default is "*.txt").
        """
        for filename in os.listdir(directory_path):
            if fnmatch.fnmatch(filename, file_pattern):
                file_path = os.path.join(directory_path, filename)
                BLASTProcessor.filter_and_overwrite_blast_file(file_path)

    @staticmethod
    def filter_and_overwrite_blast_file(file_path):
        """
        Processes BLAST output file to remove duplicate pairs of sequence IDs and accession numbers,
        keeps the first occurrence of each unique pair along with the entire line of data.
        
        Args:
            file_path (str): Path to the BLAST file to be processed.
        """
        unique_pairs = set()
        lines_to_keep = []

        try:
            with open(file_path, "r") as file:
                for line in file:
                    try:
                        columns = line.strip().split('\t')
                        if len(columns) >= 2:
                            pair = (columns[0], columns[1])
                            if pair not in unique_pairs:
                                unique_pairs.add(pair)
                                lines_to_keep.append(line)
                    except Exception as e:
                        print(f"An unexpected error has occurred while processing a line in {file_path}: {e}")
                print(f"Searching for unique sequence ID - accession pairs in {file_path}....")
        except PermissionError as e:
            print(f"Permission denied while trying to access {file_path}: {e}")
            return
        except IOError as e:
            print(f"An error has occurred while opening or reading {file_path}: {e}")
            return
        
        try:
            with open(file_path, "w") as file:
                file.writelines(lines_to_keep)
        except PermissionError as e:
            print(f"Permission denied while accessing {file_path} for writing: {e}")
        except IOError as e:
            print(f"An error occurred while writing to {file_path}: {e}")

    @staticmethod
    def collect_accessions_from_blast_files(directory_path, file_pattern="*.txt"):
        """
        Collects accession numbers from BLAST files in a specified directory.
        
        Args:
            directory_path (str): Path to the directory containing BLAST files.
            file_pattern (str): Pattern to match BLAST files (default is "*.txt").
            
        Returns:
            set: A set of unique accession numbers.
        """
        accessions = set()
        for filename in os.listdir(directory_path):
            if fnmatch.fnmatch(filename, file_pattern):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, "r") as file:
                    for line in file:
                        columns = line.strip().split('\t')
                        if len(columns) >= 2:
                            accessions.add(columns[1])
        return accessions

    @staticmethod
    def filter_and_overwrite_files_in_directory(directory_path, file_pattern="*.txt"):
        """
        Filters and overwrites files in a directory based on BLAST results.
        
        Args:
            directory_path (str): Path to the directory containing files to filter.
            file_pattern (str): Pattern to match files (default is "*.txt").
        """
        for filename in os.listdir(directory_path):
            if fnmatch.fnmatch(filename, file_pattern):
                file_path = os.path.join(directory_path, filename)
                BLASTProcessor.filter_and_overwrite_blast_file(file_path)

