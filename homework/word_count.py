"""Taller presencial"""

import os
import shutil
import random

def copy_raw_files_to_input_folder(n=1000):
    
    input_dir = "files/input"

    # limpia carpeta input/
    if os.path.exists(input_dir):
        shutil.rmtree(input_dir)
    os.makedirs(input_dir, exist_ok=True)

    words = ["analytics", "business", "by", "algorithms", "analysis"]
    counts = {
        "analytics": 5,
        "business": 7,
        "by": 3,
        "algorithms": 2,
        "analysis": 4
    }

    # generamos n archivos de entrada
    for i in range(n):
        with open(f"{input_dir}/file_{i}.txt", "w", encoding="utf-8") as f:
            for w in words:
                f.write((w + " ") * counts[w])


def run_job(input_path, output_path):

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    counts = {}

    # contar palabras
    for file in os.listdir(input_path):
        with open(os.path.join(input_path, file), "r", encoding="utf-8") as f:
            for word in f.read().split():
                counts[word] = counts.get(word, 0) + 1

    # escribir salida
    with open(f"{output_path}/part-00000", "w", encoding="utf-8") as f:
        for k, v in counts.items():
            f.write(f"{k}\t{v}\n")

    open(f"{output_path}/_SUCCESS", "w").close()

