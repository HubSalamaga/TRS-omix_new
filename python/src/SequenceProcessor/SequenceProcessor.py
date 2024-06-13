import os
import re
import subprocess
import pandas as pd
from Bio import Entrez, SeqIO
from tqdm import tqdm

class SequenceProcessor:
    