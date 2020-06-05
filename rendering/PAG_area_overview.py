"""
    Render a PAG scene following the basic examples in the Brainrender repository
"""

import time
import brainrender
from brainrender.scene import Scene
from brainrender.animation.video import BasicVideoMaker as VideoMaker

# // DEFAULT SETTINGS //
# Change some of the default settings
brainrender.SHADER_STYLE = "metallic" # affects the look of rendered brain regions, values can be: ["metallic", "plastic", "shiny", "glossy", "cartoon"] and can be changed in interactive mode
brainrender.BACKGROUND_COLOR = "white" # color of the background window (defaults to "white", try "blackboard")
brainrender.ROOT_COLOR = [.4, .4, .4] # color of the overall brain model's actor (defaults to [.4, .4, .4])
brainrender.ROOT_ALPHA = .2 # transparency of the overall brain model's actor (defaults to .2)
brainrender.DEFAULT_SCREENSHOT_NAME = "PAG_overview" # screenshots will have this name and the time at which they were taken
brainrender.DEFAULT_SCREENSHOT_TYPE = ".png" # png, svg or jpg supported
brainrender.DEFAULT_SCREENSHOT_SCALE = 1 # values >1 yield higher resolution screenshots
brainrender.SCREENSHOT_TRANSPARENT_BACKGROUND = True # whether to save screenshots with transparent background


# // SET PARAMETERS //
# Save folder
save_folder = "D:/Dropbox (UCL - SWC)/Project_transcriptomics/analysis/PAG_scRNAseq_brainrender/output"

# Create screenshot parameters
screenshot_params = dict(
    folder = save_folder,
    name = "PAG_overview")


# // CREATE SCENE //
# Create a scene with no title. You can also use scene.add_text to add other text elsewhere in the scene
scene = Scene(display_inset = True, title = None, camera = "sagittal", screenshot_kwargs = screenshot_params) 


# // ADD BRAIN REGIONS //
# Add brain regions with scene.add_brain_regions
pag = scene.add_brain_regions(["PAG"], 
    alpha = .4, color = "darkgoldenrod", add_labels = False, use_original_color = False, wireframe = False)
dorsal_raphe = scene.add_brain_regions(["DR"], 
    alpha = .4, color = "olivedrab", add_labels = False, use_original_color = False, wireframe = True)
superior_colliculus = scene.add_brain_regions(["SCdg", "SCdw", "SCig", "SCiw", "SCm", "SCop", "SCs", "SCsg", "SCzo"],
    alpha = .4, color = "olivedrab", add_labels = False, use_original_color = False, wireframe = True)


# # // ADD LABELS //
# # Add labels with scene.add_actor_label
# scene.add_actor_label(pag, "PAG", size = 400, color = "blackboard", xoffset = 0, yoffset = 0, radius = None)
# scene.add_actor_label(superior_colliculus, "SC", size = 400, color = "blackboard", xoffset = 0, yoffset = 0, radius = None)
# scene.add_actor_label(dorsal_raphe, "DRN", size = 400, color = "blackboard", xoffset = 0, yoffset = 0, radius = None)


# # // CUT SCENE IN HALF AT DESIRED PLANE //
# # Cut scene in half (set showplane = True if you want to see the plane location)
# scene.cut_actors_with_plane("sagittal", showplane = False) 


# # // TAKE SPECIFIC SCREENSHOTS //
# # Render and take screenshot
# scene.render(camera = "top", interactive = False, zoom = 1) 
# ## if interactive = false the program won't stop when the scene is rendered, which means that the next line will be executed
# scene.take_screenshot()
# time.sleep(1)

# # Take another screenshot from a different angle
# scene.render(camera = "coronal", interactive = False, zoom = 0.5)
# scene.take_screenshot() # screenshots are saved with a timestamp in the name so you won't be overwriting the previous one.


# # // EXPORT AS HTML //
# # Export to a .html file that can be opened in a browser to render an interactive brainrender scene
# scene.export_for_web(save_folder) # <- you can pass a  filepath to specify where to save the scene


# // MAKE VIDEO //
# Create an instance of VideoMaker with our scene
vm = VideoMaker(scene,
    save_fld = save_folder, # folder where to save video
    save_name = "PAG_video", # video name
    #video_format = "mp4", # defaults to mp4
    #duration = 3, # video duration in seconds (defaults to 3)
    #niters = 60, # number of iterations (frames) when creating the video (defaults to 60)
    #fps = 30 # framerate of video (defaults to 30)
    ) 

# Make a video and specify how the scene rotates at each frame. You can also change several parameters (destination folder, video name, fps, duration, etc.) specified above
vm.make_video(azimuth = 1, elevation = 1, roll = 0, # rotation in degrees per frame on the relative axis    
    save_fld = save_folder, save_name = "PAG_video",
    video_format = "avi", duration = 5, niters = 50, fps = 30)


# // RENDER INTERACTIVELY //
# Render interactively. You can press "s" to take a screenshot
scene.render(interactive = True, video = False, camera = "sagittal", zoom = 1)