""" 
    Download and render afferent mesoscale projection data using the AllenBrainAtlas (ABA) and Scene classes
"""

import brainrender
from brainrender import Scene, Animation
from vedo import settings as vsettings
from brainrender.video import VideoMaker

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


# // SET PARAMETERS //
# Save folder
save_folder = r"D:\Dropbox (UCL)\Project_transcriptomics\analysis\PAG_scRNAseq_brainrender\output"


# // CREATE SCENE //
# Create a scene with no title. You can also use scene.add_text to add other text elsewhere in the scene
scene = Scene(root = True, atlas_name = 'allen_mouse_10um', inset = False, title = 'PAG_areas_overview', screenshots_folder = save_folder, plotter = None)


# // GET CENTER OF MASS AND PROJECTIONS TO IT //
# Get the center of mass of the region of interest
p0 = scene.atlas.get_region_CenterOfMass("PAG")

# Get projections to that point
analyzer = ABA()
tract = analyzer.get_projection_tracts_to_target(p0 = p0)


# // ADD BRAIN REGIONS //
pag = scene.add_brain_regions(["PAG"],
    alpha = 0.4, color = "darkgoldenrod", add_labels = False, use_original_color = False, wireframe = False)
superior_colliculus = scene.add_brain_regions(["SCdg", "SCdw", "SCig", "SCiw", "SCm", "SCop", "SCs", "SCsg", "SCzo"],
    alpha = 0.1, color = "olivedrab", add_labels = False, use_original_color = False, wireframe = True)
# hypothalamus = scene.add_brain_regions(["HY"],
#     alpha = .2, color = "lightsalmon", add_labels = False, use_original_color = False, wireframe = True)


# Add the projections to the chosen brain region
scene.add_tractography(tract,
     color = None, #"darkseagreen" # color of rendered tractography data
     color_by = "target_region", #"manual", "region", or "target_region"
     VIP_regions = ["SCdg", "SCdw", "SCig", "SCiw", "SCm", "SCop", "SCs", "SCsg", "SCzo"], # list of brain regions with VIP treatement (Default value = [])
     VIP_color = "darkseagreen", # color to use for VIP data (Default value = None)
     others_color = "ivory", # color for not VIP data (Default value = "white")
     others_alpha = 0.1, # Default is 1
     verbose = True, # Prints all areas projecting to target
     include_all_inj_regions = False,
     display_injection_volume = True) # add a spehere to display the injection coordinates and volume

# This renders tractography data and adds it to the scene. A subset of tractography data can receive special treatment using the  with VIP regions argument: if the injection site for the tractography data is in a VIP region, this is colored differently.
# Try "SC", "VMH", "SCm", "LHA":
    ##["SCdg", "SCdw", "SCig", "SCiw", "SCm", "SCop", "SCs", "SCsg", "SCzo"] -- Superior Colliculus
    ##(LHA) -- Lateral hypothalamic area
    ##(VMH) -- Ventromedial hypothalamic nucleus
    ##(ZI) -- Zona incerta


# // RENDER INTERACTIVELY //
# Render interactively. You can press "s" to take a screenshot
scene.render(interactive = True, camera = "sagittal", zoom = 1)