"""
    Use the brainglobe atlas api and the kim atlas to obtain the PAG subdivision corresponding to each registered cell.
    https://github.com/brainglobe/bg-atlasapi/blob/3cb46466094a8a0231f67f1666ca0697d525b12f/bg_atlasapi/core.py#L205
"""
# %%
# Import packages
import brainrender
from brainrender import Scene, Animation
from vedo import settings as vsettings
from brainrender.video import VideoMaker
import pandas as pd # used to load the cwv

# Get a list of the available atlases:
from bg_atlasapi import show_atlases
show_atlases()

# %%
# Find the dimensions of an atlas:
from bg_atlasapi.bg_atlas import BrainGlobeAtlas
allen_atlas_10 = BrainGlobeAtlas("allen_mouse_10um")
print(allen_atlas_10.reference.shape) # (1320, 800, 1140)
print(allen_atlas_10.annotation.shape) # (1320, 800, 1140)

kim_atlas_10 = BrainGlobeAtlas("kim_mouse_10um")
print(kim_atlas_10.reference.shape) # (1320, 800, 1140)
print(kim_atlas_10.annotation.shape) # (1320, 800, 1140)

allen_atlas_25 = BrainGlobeAtlas("allen_mouse_25um")
print(allen_atlas_25.reference.shape) # (528, 320, 456)
print(allen_atlas_25.annotation.shape) # (528, 320, 456)

kim_atlas_25 = BrainGlobeAtlas("kim_mouse_25um")
print(kim_atlas_25.reference.shape) # (528, 320, 456)
print(kim_atlas_25.annotation.shape) # (528, 320, 456)

# %%
# Load metadata
pag_data = pd.read_csv("D:\\Dropbox (UCL - SWC)\\Project_transcriptomics\\analysis\\PAG_scRNAseq_brainrender\\PAG_scRNAseq_metadata_200617.csv")

# Inspect the CCF coordinates for each cell
pag_data[["cell.id", "cell.type", "PAG.areamanualregistration", "CCF.AllenAP", "CCF.AllenDV", "CCF.AllenML"]]

# %%
# initialise variables
areaID_allen_atlas_10 = []
areaID_kim_atlas_10 = [] 
areaID_allen_atlas_25 = []
areaID_kim_atlas_25 = []
acronym_allen_atlas_10 = []
acronym_kim_atlas_10 = [] 
acronym_allen_atlas_25 = []
acronym_kim_atlas_25 = []

# Get the structure acronym from a coordinate triplet
for i in range(len(pag_data["CCF.AllenAP"])):
    areaID_allen_atlas_10_temp = allen_atlas_10.structure_from_coords(
        [pag_data["CCF.AllenAP"][i], pag_data["CCF.AllenDV"][i], pag_data["CCF.AllenML"][i]], # triplet of coordinates
        microns = False, # if true, coordinates are interpreted in microns
        as_acronym = False, # if true, the region acronym is returned
        hierarchy_lev = None # if specified, return parent node at the hierarchy level
        )
    areaID_allen_atlas_10.append(areaID_allen_atlas_10_temp)

    areaID_kim_atlas_10_temp = kim_atlas_10.structure_from_coords(
        [pag_data["CCF.AllenAP"][i], pag_data["CCF.AllenDV"][i], pag_data["CCF.AllenML"][i]], # triplet of coordinates
        microns = False, # if true, coordinates are interpreted in microns
        as_acronym = False, # if true, the region acronym is returned
        hierarchy_lev = None # if specified, return parent node at the hierarchy level
        )
    areaID_kim_atlas_10.append(areaID_kim_atlas_10_temp)

    areaID_allen_atlas_25_temp = allen_atlas_25.structure_from_coords(
        [round(pag_data["CCF.AllenAP"][i]/2.5), round(pag_data["CCF.AllenDV"][i]/2.5), round(pag_data["CCF.AllenML"][i]/2.5)], # triplet of coordinates
        microns = False, # if true, coordinates are interpreted in microns
        as_acronym = False, # if true, the region acronym is returned
        hierarchy_lev = None # if specified, return parent node at the hierarchy level
        )
    areaID_allen_atlas_25.append(areaID_allen_atlas_25_temp)

    areaID_kim_atlas_25_temp = kim_atlas_25.structure_from_coords(
        [round(pag_data["CCF.AllenAP"][i]/2.5), round(pag_data["CCF.AllenDV"][i]/2.5), round(pag_data["CCF.AllenML"][i]/2.5)], # triplet of coordinates
        microns = False, # if true, coordinates are interpreted in microns
        as_acronym = False, # if true, the region acronym is returned
        hierarchy_lev = None # if specified, return parent node at the hierarchy level
        )
    areaID_kim_atlas_25.append(areaID_kim_atlas_25_temp)

# Get the structure ID from a coordinate triplet
for i in range(len(pag_data["CCF.AllenAP"])):
    acronym_allen_atlas_10_temp = allen_atlas_10.structure_from_coords(
        [pag_data["CCF.AllenAP"][i], pag_data["CCF.AllenDV"][i], pag_data["CCF.AllenML"][i]], # triplet of coordinates
        microns = False, # if true, coordinates are interpreted in microns
        as_acronym = True, # if true, the region acronym is returned
        hierarchy_lev = None # if specified, return parent node at the hierarchy level
        )
    acronym_allen_atlas_10.append(acronym_allen_atlas_10_temp)

    acronym_kim_atlas_10_temp = kim_atlas_10.structure_from_coords(
        [pag_data["CCF.AllenAP"][i], pag_data["CCF.AllenDV"][i], pag_data["CCF.AllenML"][i]], # triplet of coordinates
        microns = False, # if true, coordinates are interpreted in microns
        as_acronym = True, # if true, the region acronym is returned
        hierarchy_lev = None # if specified, return parent node at the hierarchy level
        )
    acronym_kim_atlas_10.append(acronym_kim_atlas_10_temp)

    acronym_allen_atlas_25_temp = allen_atlas_25.structure_from_coords(
        [round(pag_data["CCF.AllenAP"][i]/2.5), round(pag_data["CCF.AllenDV"][i]/2.5), round(pag_data["CCF.AllenML"][i]/2.5)], # triplet of coordinates
        microns = False, # if true, coordinates are interpreted in microns
        as_acronym = True, # if true, the region acronym is returned
        hierarchy_lev = None # if specified, return parent node at the hierarchy level
        )
    acronym_allen_atlas_25.append(acronym_allen_atlas_25_temp)

    acronym_kim_atlas_25_temp = kim_atlas_25.structure_from_coords(
        [round(pag_data["CCF.AllenAP"][i]/2.5), round(pag_data["CCF.AllenDV"][i]/2.5), round(pag_data["CCF.AllenML"][i]/2.5)], # triplet of coordinates
        microns = False, # if true, coordinates are interpreted in microns
        as_acronym = True, # if true, the region acronym is returned
        hierarchy_lev = None # if specified, return parent node at the hierarchy level
        )
    acronym_kim_atlas_25.append(acronym_kim_atlas_25_temp)

# %%
# Collate results in a dataframe
area_dataframe = pd.DataFrame(dict(
    areaID_allen_atlas_10 = areaID_allen_atlas_10,
    acronym_allen_atlas_10 = acronym_allen_atlas_10,
    areaID_kim_atlas_10 = areaID_kim_atlas_10,
    acronym_kim_atlas_10 = acronym_kim_atlas_10,
    areaID_allen_atlas_25 = areaID_allen_atlas_25,
    acronym_allen_atlas_25 = acronym_allen_atlas_25,
    areaID_kim_atlas_25 = areaID_kim_atlas_25,
    acronym_kim_atlas_25 = acronym_kim_atlas_25
    ))

area_dataframe

# %% 
import os
from datetime import date

save_folder = r"D:\Dropbox (UCL)\Project_transcriptomics\analysis\PAG_scRNAseq_brainrender"

# Save dataframe as csv file
area_dataframe.to_csv(os.path.join(save_folder, "PAG_scRNAseq_metadata_CCF_subdivisions_" + str(date.today()).replace("-", "") + ".csv"))
# %%
