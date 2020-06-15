"""
    Download neurons from the MouseLight datase with morphapi and render them with a custom color palette
    We can also manually download data from the neuronbrowser website and render by passing the downloaded files to "scene.add_neurons"
"""

import brainrender
from brainrender.scene import Scene
from brainrender.colors import makePalette
from morphapi.api.mouselight import MouseLightAPI
from brainrender.animation.video import BasicVideoMaker as VideoMaker


# // DEFAULT SETTINGS //
# Change some of the default settings
brainrender.SHADER_STYLE = "cartoon" # affects the look of rendered brain regions, values can be: ["metallic", "plastic", "shiny", "glossy", "cartoon"] and can be changed in interactive mode
brainrender.BACKGROUND_COLOR = "blackboard" # color of the background window (defaults to "white", try "blackboard")
brainrender.ROOT_COLOR = [0.4, 0.4, 0.4] # color of the overall brain model's actor (defaults to [0.4, 0.4, 0.4])
brainrender.ROOT_ALPHA = 0.3 # transparency of the overall brain model's actor (defaults to 0.2)
brainrender.DEFAULT_SCREENSHOT_NAME = "PAG_mouselight" # screenshots will have this name and the time at which they were taken
brainrender.DEFAULT_SCREENSHOT_TYPE = ".png" # png, svg or jpg supported
brainrender.DEFAULT_SCREENSHOT_SCALE = 1 # values >1 yield higher resolution screenshots
brainrender.SCREENSHOT_TRANSPARENT_BACKGROUND = True # whether to save screenshots with transparent background
brainrender.SOMA_RADIUS = 2000  # radius of the soma sphere, in microns
brainrender.DEFAULT_NEURITE_RADIUS = 8  # rneurites (axon/dendrites) radius as a fraction of soma radius
brainrender.NEURON_RESOLUTION = 16  # resolution of actors used to render the neuron
brainrender.NEURON_ALPHA = 0.8  # transparency of the neurons actors


# // SET PARAMETERS //
# Save folder
save_folder = "D:/Dropbox (UCL - SWC)/Project_transcriptomics/analysis/PAG_scRNAseq_brainrender/output"

# Create screenshot parameters
screenshot_params = dict(folder = save_folder, name = "PAG_mouselight")


# // DOWNLOAD NEURONS //
mlapi = MouseLightAPI()

# Fetch metadata for neurons with some in the secondary motor cortex
neurons_metadata = mlapi.fetch_neurons_metadata(filterby = "soma", filter_regions = ["PAG"]) # There is only 1 neuron so far

# Then we can download the files and save them as a .json file
neurons =  mlapi.download_neurons(neurons_metadata[:50]) # restrict to 50 neurons max, may take a while the first time


# // CREATE SCENE //
# Create a scene with no title. You can also use scene.add_text to add other text elsewhere in the scene
scene = Scene(display_inset = False, title = None, camera = "sagittal", add_root = True, screenshot_kwargs = screenshot_params)


# // ADD BRAIN REGIONS //
pag = scene.add_brain_regions(["PAG"],
    alpha = 0.2, color = "darkgoldenrod", add_labels = False, use_original_color = False, wireframe = False)


# // ADD AND COLOR DOWNLOADED NEURONS //
# # OPTION A // color all neurons of the same color
# scene.add_neurons(neurons, color = "olivedrab", alpha = 0.8,
#     display_axon = True, display_dendrites = True, neurite_radius = 8, use_cache = False)

# OPTION B // specify a color for each neuronal component
scene.add_neurons(neurons,
    color = dict(soma = "blackboard", dendrites = "olivedrab", axon = "lightgreen"),
    alpha = 0.8, display_axon = True, display_dendrites = True, neurite_radius = 8, soma_radius = 2000, use_cache = False)

# # OPTION C // color each neuron of a different color using a colormap - if you have more than one neuron
# scene.add_neurons(neurons, color = "Reds", alpha = 0.8,
#     display_axon = True, display_dendrites = True, neurite_radius = 8, use_cache = False)

# # OPTION D // specify a color for each neuron - if you have more than one neuron
# scene.add_neurons(neurons,
#     color = ["salmon", "darkseagreeb", "skyblue", "chocolate", "darkgoldenrod"],
#     alpha = 0.8, display_axon = True, display_dendrites = True, neurite_radius = 8, use_cache = False)

# # OPTION E // Create a custom colormap between 2 colors - if you have more than one neuron
# color_palette = makePalette(len(neurons), "salmon", "lightgreen")
# scene.add_neurons(neurons, color = color_palette, alpha = 0.8, 
#     display_axon = True, display_dendrites = True, neurite_radius = 8, use_cache = False)


# # // CUT SCENE IN HALF AT DESIRED PLANE //
# # Cut scene in half (set showplane = True if you want to see the plane location)
# scene.cut_actors_with_plane("sagittal", showplane = False) 


# # // EXPORT AS HTML //
# # Export to a .html file that can be opened in a browser to render an interactive brainrender scene
# scene.export_for_web("output/PAG_mouselight.html") # <- you can pass a  filepath to specify where to save the scene


# # // MAKE VIDEO //
# # Create an instance of VideoMaker with our scene
# vm = VideoMaker(scene,
#     save_fld = save_folder, # folder where to save video
#     save_name = "PAG_video_mouselight", # video name
#     #video_format = "mp4", # defaults to mp4
#     #duration = 3, # video duration in seconds (defaults to 3)
#     #niters = 60, # number of iterations (frames) when creating the video (defaults to 60)
#     #fps = 30 # framerate of video (defaults to 30)
#     ) 

# # Make a video and specify how the scene rotates at each frame. You can also change several parameters (destination folder, video name, fps, duration, etc.) specified above
# vm.make_video(azimuth = 1, elevation = 1, roll = 0, # rotation in degrees per frame on the relative axis    
#     save_fld = save_folder, save_name = "PAG_video_mouselight",
#     video_format = "avi", duration = 5, niters = 50, fps = 30)


# // RENDER INTERACTIVELY //
# Render interactively. You can press "s" to take a screenshot
scene.render(interactive = True, video = False, camera = "sagittal", zoom = 1)