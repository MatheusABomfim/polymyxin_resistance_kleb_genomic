# -*- coding: utf-8 -*-

import MDAnalysis as mda
import numpy as np
import os

# --- Parâmetros de Entrada ---
# Nome do arquivo PDB contendo a trajetória (com múltiplos modelos)
input_trajectory_pdb = 'filme.pdb'

# Diretório para salvar os frames extraídos
output_directory = 'extracted_frames'

# Número de frames a serem extraídos
num_frames_to_extract = 10

# --- Lógica do Script ---

# Garante que o diretório de saída exista
os.makedirs(output_directory, exist_ok=True)

# Carrega a trajetória. MDAnalysis trata um PDB com múltiplos MODELos como uma trajetória.
print(f"Carregando a trajetória de '{input_trajectory_pdb}'...")
try:
    universe = mda.Universe(input_trajectory_pdb)
except Exception as e:
    print(f"Erro ao carregar o arquivo PDB: {e}")
    print("Verifique se o arquivo está no formato correto e no mesmo diretório do script.")
    exit()


# Obtém o número total de frames na trajetória
total_frames = len(universe.trajectory)
print(f"Trajetória carregada com sucesso. Total de frames encontrados: {total_frames}")

if total_frames < num_frames_to_extract:
    print(f"Aviso: O número de frames a extrair ({num_frames_to_extract}) é maior que o total de frames ({total_frames}).")
    # Decide continuar extraindo todos os frames disponíveis
    indices_to_extract = range(total_frames)
else:
    # Calcula os índices dos frames a serem extraídos, distribuídos uniformemente
    # np.linspace cria um array de números igualmente espaçados.
    # O primeiro frame tem índice 0 e o último, total_frames - 1.
    indices_to_extract = np.linspace(0, total_frames - 1, num=num_frames_to_extract, dtype=int)

print(f"Serão extraídos os frames nos seguintes índices: {indices_to_extract}")

# Itera sobre os índices calculados e salva cada frame correspondente
for frame_index in indices_to_extract:
    # Move a trajetória para o frame desejado
    universe.trajectory[frame_index]
    
    # Define o nome do arquivo de saída para o frame atual
    # O formato :05d garante que o número seja preenchido com zeros à esquerda (ex: frame_00001.pdb)
    # Isso ajuda a manter os arquivos ordenados no sistema de arquivos.
    output_filename = f"frame_{frame_index:05d}.pdb"
    output_filepath = os.path.join(output_directory, output_filename)
    
    # Seleciona todos os átomos do frame atual e os escreve em um novo arquivo PDB
    universe.atoms.write(output_filepath)
    
    print(f"Frame {frame_index} salvo em '{output_filepath}'")

print("\nExtração concluída.")