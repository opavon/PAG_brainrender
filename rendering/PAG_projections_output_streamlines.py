"""
    Render efferent mesoscale connectivity data from the Allen mouse connectome project as streamlines
"""

import brainrender
from brainrender.scene import Scene
from brainrender.colors import makePalette
from brainrender.animation.video import BasicVideoMaker as VideoMaker

# // DEFAULT SETTINGS //
# Change some of the default settings
brainrender.SHADER_STYLE = "cartoon" # affects the look of rendered brain regions, values can be: ["metallic", "plastic", "shiny", "glossy", "cartoon"] and can be changed in interactive mode
brainrender.BACKGROUND_COLOR = "blackboard" # color of the background window (defaults to "white", try "blackboard")
brainrender.ROOT_COLOR = [0.4, 0.4, 0.4] # color of the overall brain model's actor (defaults to [0.4, 0.4, 0.4])
brainrender.ROOT_ALPHA = 0.2 # transparency of the overall brain model's actor (defaults to 0.2)
brainrender.DEFAULT_SCREENSHOT_NAME = "PAG_streamlines" # screenshots will have this name and the time at which they were taken
brainrender.DEFAULT_SCREENSHOT_TYPE = ".png" # png, svg or jpg supported
brainrender.DEFAULT_SCREENSHOT_SCALE = 1 # values >1 yield higher resolution screenshots
brainrender.SCREENSHOT_TRANSPARENT_BACKGROUND = True # whether to save screenshots with transparent background


# // SET PARAMETERS //
# Save folder
save_folder = "D:/Dropbox (UCL - SWC)/Project_transcriptomics/analysis/PAG_scRNAseq_brainrender/output"

# Create screenshot parameters
screenshot_params = dict(folder = save_folder, name = "PAG_overview")


# // CREATE SCENE //
# Create a scene with no title. You can also use scene.add_text to add other text elsewhere in the scene
scene = Scene(display_inset = True, title = None, camera = "sagittal", screenshot_kwargs = screenshot_params) 


# // DOWNLOAD STREAMLINES //
# Download streamlines data for injections in the Periaqueductal Gray
filepaths, data = scene.atlas.download_streamlines_for_region("PAG")
#data = data[:2] # do this to select a subset of injections. Change color_combos if you uncomment this.


# // ADD BRAIN REGIONS //
scene.add_brain_regions(["PAG"], alpha = 0.4, color = "darkgoldenrod", add_labels = False, use_original_color = False, wireframe = False)


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


# # // CUT SCENE IN HALF AT DESIRED PLANE //
# # Cut scene in half (set showplane = True if you want to see the plane location)
# scene.cut_actors_with_plane("sagittal", showplane = False) 


# # // EXPORT AS HTML //
# # Export to a .html file that can be opened in a browser to render an interactive brainrender scene
# scene.export_for_web("output/PAG_streamlines.html") # you can pass a filepath where to save the scene


# # // MAKE VIDEO //
# # Create an instance of VideoMaker with our scene
# vm = VideoMaker(scene,
#     save_fld = save_folder, # folder where to save video
#     save_name = "PAG_video_streamlines", # video name
#     #video_format = "mp4", # defaults to mp4
#     #duration = 3, # video duration in seconds (defaults to 3)
#     #niters = 60, # number of iterations (frames) when creating the video (defaults to 60)
#     #fps = 30 # framerate of video (defaults to 30)
#     ) 

# # Make a video and specify how the scene rotates at each frame. You can also change several parameters (destination folder, video name, fps, duration, etc.) specified above
# vm.make_video(azimuth = 1, elevation = 1, roll = 0, # rotation in degrees per frame on the relative axis    
#     save_fld = save_folder, save_name = "PAG_video_streamlines",
#     video_format = "avi", duration = 5, niters = 50, fps = 30)


# // RENDER INTERACTIVELY //
# Render interactively. You can press "s" to take a screenshot
scene.render(interactive = True, video = False, camera = "sagittal", zoom = 1)