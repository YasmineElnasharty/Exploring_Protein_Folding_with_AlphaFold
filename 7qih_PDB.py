from Bio.PDB import PDBParser, PPBuilder

# Function to load structure from a PDB file
def load_structure(file_path):
    parser = PDBParser(QUIET=True)  # Suppress warnings for cleaner output
    structure = parser.get_structure('protein', file_path)
    return structure

# Function to extract and print secondary structure from the PDB structure
def extract_secondary_structure(structure):
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        print(f"Peptide Sequence: {pp.get_sequence()}")

# Manually specify the path to your PDB file
file_path = '7qih.pdb'

# Load and extract secondary structure
structure = load_structure(file_path)
extract_secondary_structure(structure)