# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 2020

@author: Yoann Pradat

    CentraleSupelec
    MICS laboratory
    9 rue Juliot Curie, Gif-Sur-Yvette, 91190 France

Test functions from vep module.
"""

import os
from ..main import run_annotator_one

def test_main():
    vcf2maf    = "~/Documents/biotools/informatics/VCF/mskcc-vcf2maf-5453f80/vcf2maf.pl"
    vep_folder = "~/Documents/biotools/informatics/VCF/ensembl-vep"
    vep_data   = "~/.vep"
    fasta      = "~/.vep/homo_sapiens/99_GRCh37/Homo_sapiens.GRCh37.75.dna.primary_assembly.fa"

    #### # 1. TCGA GA
    #### # ########################################################################################################

    vcf_folder = "./examples/data/TCGA_GA/"
    out_folder = "./examples/results/TCGA_GA/"

    #### paths to results folders
    dt_folders = {
        'manual_out_folder'  : os.path.join(out_folder, "tmp/out_manual"),
        'vcf2maf_tmp_folder' : os.path.join(out_folder, "tmp/tmp_vcf2maf"),
        'vcf2maf_out_folder' : os.path.join(out_folder, "tmp/out_vcf2maf"),
        'vep_out_folder'     : os.path.join(out_folder, "tmp/out_vep"),
        'maf_folder'         : os.path.join(out_folder, "maf"),
    }

    #### make folders if they do not exist already
    for k, v in dt_folders.items():
        os.makedirs(v, exist_ok=True)

    #### Indel TCGA_GA
    vcf_file      = "TCGA-A1-A0SB_db9d40fb-bfce-4c3b-a6c2-41c5c88982f1_a3254f8e-3bbd-42fc-abea-a5f25b7648b3.indel.capture.tcga.vcf"
    col_normal    = "NORMAL"
    col_tumor     = "PRIMARY"
    normal_id     = "TCGA-A1-A0SD-10A-01D-A110-09"
    tumor_id      = "TCGA-A1-A0SD-01A-11D-A10Y-09"
    infos_n_reads = ["AD", "DP4", "DP", "TAR", "TIR"]
    infos_other   = ["SS", "GT"]

    run_annotator_one(
        vcf_folder    = vcf_folder,
        vcf_file      = vcf_file,
        col_normal    = col_normal,
        col_tumor     = col_tumor,
        normal_id     = normal_id,
        tumor_id      = tumor_id,
        infos_n_reads = infos_n_reads,
        infos_other   = infos_other,
        vcf2maf       = vcf2maf,
        vep_folder    = vep_folder,
        vep_data      = vep_data,
        fasta         = fasta,
        dt_folders    = dt_folders
    )

    #### SNP TCGA_GA
    vcf_file = "TCGA-A1-A0SB_db9d40fb-bfce-4c3b-a6c2-41c5c88982f1_a3254f8e-3bbd-42fc-abea-a5f25b7648b3.oxoG.snp.capture.tcga.vcf"

    #### # 2. TCGA HS
    #### # ########################################################################################################

    vcf_folder = "./examples/data/TCGA_HS/"

    #### Indel TCGA_HS
    vcf_file =  "genome.wustl.edu.TCGA-A1-A0SD.indel.0e81f9c986154ce89e59240c3f09534f.vcf"

    #### SNP TCGA_HS
    vcf_file =  "genome.wustl.edu.TCGA-A1-A0SD.snv.0e81f9c986154ce89e59240c3f09534f.vcf"
