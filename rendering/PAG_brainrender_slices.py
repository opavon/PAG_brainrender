"""
    Render a PAG + SC scene and generate a virtual slice.
    Would be useful to plot the aspirated cells and visualize them in a slice using the CCF coordinates after registration with SHARP-TRACK.
    Would also be possible to then slice the PAG at 25-50um thick sections to check how well do the subdivisions from manual registration (done by eye upon comparing with the Paxinos Atlas) match the ones from brainglobe's `structure_from_coords()` function.
"""

# %%
# https://github.com/marcomusy/vedo/issues/430#issuecomment-892719236

import brainrender
from brainrender import Scene, Animation
from vedo import settings as vsettings
from brainrender.video import VideoMaker
import numpy as np


# // DEFAULT SETTINGS //
# You can see all the default settings here: https://github.com/brainglobe/brainrender/blob/19c63b97a34336898871d66fb24484e8a55d4fa7/brainrender/settings.py

# --------------------------- brainrender settings --------------------------- #
# Change some of the default settings
brainrender.settings.BACKGROUND_COLOR = "white" # color of the background window (defaults to "white", try "blackboard")
brainrender.settings.DEFAULT_ATLAS = "allen_mouse_25um"  # default atlas
brainrender.settings.DEFAULT_CAMERA = "three_quarters"  # Default camera settings (orientation etc. see brainrender.camera.py)
brainrender.settings.INTERACTIVE = False  # rendering interactive ?
brainrender.settings.LW = 2  # e.g. for silhouettes
brainrender.settings.ROOT_COLOR = [0.4, 0.4, 0.4]   # color of the overall brain model's actor (defaults to [0.8, 0.8, 0.8])
brainrender.settings.ROOT_ALPHA = 0.2  # transparency of the overall brain model's actor (defaults to 0.2)
brainrender.settings.SCREENSHOT_SCALE = 1 # values >1 yield higher resolution screenshots
brainrender.settings.SHADER_STYLE = "cartoon" # affects the look of rendered brain regions, values can be: ["metallic", "plastic", "shiny", "glossy", "cartoon"] and can be changed in interactive mode
brainrender.settings.SHOW_AXES = False
brainrender.settings.WHOLE_SCREEN = True # If true render window is full screen
brainrender.settings.OFFSCREEN = False

# ------------------------------- vedo settings ------------------------------ #
# For transparent background with screenshots
vsettings.screenshotTransparentBackground = True  # vedo for transparent bg
vsettings.useFXAA = False  # This needs to be false for transparent bg
vsettings.immediateRendering = False


# // SET PARAMETERS //
# Save folder
save_folder = r"D:\Dropbox (UCL)\Project_transcriptomics\analysis\PAG_scRNAseq_brainrender\output"


# // CREATE SCENE //
scene = Scene(root = True, atlas_name = 'allen_mouse_10um', inset = False, title = 'PAG_areas_overview', screenshots_folder = save_folder, plotter = None)


# // ADD BRAIN REGIONS //
pag = scene.add_brain_region("PAG", alpha = 0.4, color = "darkgoldenrod", silhouette = None, hemisphere = "both")
sc = scene.add_brain_region("SCm", alpha = 0.4, color = "olivedrab", silhouette = None, hemisphere = "both")


# // MAKE SLICE //
slice_start = scene.root.mesh.centerOfMass() + np.array([+1000, 0, 0]) # X microns from center of mass towards the nose (if positive) or cerebellum (if negative)
slice_end = scene.root.mesh.centerOfMass() + np.array([+2000, 0, 0]) # X microns from center of mass towards the nose (if adding) or cerebellum (if subtracting)

for p, n in zip((slice_start, slice_end), (1, -1)):
    plane = scene.atlas.get_plane(pos = p, norm = (n, 0, 0))
    scene.slice(plane, actors = pag, close_actors = True)
    scene.slice(plane, actors = sc, close_actors = True)
    scene.slice(plane, actors = scene.root, close_actors = False)


# // RENDER INTERACTIVELY //
scene.render(interactive = True, camera = "frontal", zoom = 1)
# %%
