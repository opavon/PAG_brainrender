"""
    Render efferent mesoscale connectivity data from the Allen mouse connectome project as streamlines
    From brainrender example: https://github.com/brainglobe/brainrender/blob/19c63b97a34336898871d66fb24484e8a55d4fa7/examples/streamlines.py
"""

import brainrender
from brainrender import Scene, Animation
from vedo import settings as vsettings
from brainrender.video import VideoMaker
from brainrender.atlas_specific import get_streamlines_for_region
from brainrender.actors.streamlines import make_streamlines
from brainrender.colors import makePalette

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
scene = Scene(root = True, atlas_name = 'allen_mouse_10um', inset = False, title = None, screenshots_folder = save_folder, plotter = None)


# // DOWNLOAD STREAMLINES //
# Download streamlines data for injections in the Periaqueductal Gray
streams = get_streamlines_for_region("PAG")[:2]
scene.add(*make_streamlines(*streams, color="salmon", alpha=0.5))

# // ADD BRAIN REGIONS //
pag = scene.add_brain_region("PAG", alpha = 0.4, color = "darkgoldenrod", silhouette = None, hemisphere = "both")


# # // OPTION A // Color each streamline with a different color //
# # Create palette to color each streamline with a different color
# color_palette = makePalette(len(data), "salmon", "darkseagreen")
# color_palette = makePalette(len(data), "darkblue", "powderblue")
# color_palette = makePalette(len(data), "deeppink", "lightpink")


# # Add the efferents by passing either the filepaths or the data
# ## one actor is 1 streamline (i.e. the traces for 1 injection)
# scene.add_streamlines(data, color = color_palette, show_injection_site = False, alpha = 0.6)


# // OPTION B // Color streamlines with a color gradient along x position //
# Add the efferents by passing either the filepaths or the data
## one actor is 1 streamline (i.e. the traces for 1 injection)
actors = scene.add_streamlines(data, color = None, show_injection_site = False, alpha = 0.6)
#if not isinstance(actors, list): actors = [actors] # make sure it's a list or zip will fail

# Now modify the color of each actor to color each actor's vertices based on the X position
## len(color_combos) needs to be the same as len(actors)
color_combos = [["darkblue", "powderblue"],
                ["deeppink", "lightpink"],
                ["darkblue", "powderblue"],
                ["deeppink", "lightpink"],
                ["darkblue", "powderblue"],
                ["deeppink", "lightpink"],
                ["darkblue", "powderblue"],
                ["deeppink", "lightpink"],
                ["darkblue", "powderblue"]] 

for actor, colors in zip(actors, color_combos): # this will take a while
    scals = actor.points()[:, 0]   # pick x coordinates of vertices
    cmap = makePalette(len(scals), colors[0], colors[1]) # make colors
    actor.pointColors(scals, cmap = cmap)


# // RENDER INTERACTIVELY //
# Render interactively. You can press "s" to take a screenshot
scene.render(interactive = True, camera = "sagittal", zoom = 1)