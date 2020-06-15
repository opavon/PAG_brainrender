""" 
    Download and render afferent mesoscale projection data using the AllenBrainAtlas (ABA) and Scene classes
"""

import brainrender
from brainrender.scene import Scene
from brainrender.atlases.mouse import ABA
from brainrender.animation.video import BasicVideoMaker as VideoMaker

# // DEFAULT SETTINGS //
# Change some of the default settings
brainrender.SHADER_STYLE = "cartoon" # affects the look of rendered brain regions, values can be: ["metallic", "plastic", "shiny", "glossy", "cartoon"] and can be changed in interactive mode
brainrender.BACKGROUND_COLOR = "white" # color of the background window (defaults to "white", try "blackboard")
brainrender.ROOT_COLOR = [0.4, 0.4, 0.4] # color of the overall brain model's actor (defaults to [0.4, 0.4, 0.4])
brainrender.ROOT_ALPHA = 0.2 # transparency of the overall brain model's actor (defaults to 0.2)
brainrender.DEFAULT_SCREENSHOT_NAME = "PAG_tractography" # screenshots will have this name and the time at which they were taken
brainrender.DEFAULT_SCREENSHOT_TYPE = ".png" # png, svg or jpg supported
brainrender.DEFAULT_SCREENSHOT_SCALE = 1 # values >1 yield higher resolution screenshots
brainrender.SCREENSHOT_TRANSPARENT_BACKGROUND = True # whether to save screenshots with transparent background


# // SET PARAMETERS //
# Save folder
save_folder = "D:/Dropbox (UCL - SWC)/Project_transcriptomics/analysis/PAG_scRNAseq_brainrender/output"

# Create screenshot parameters
screenshot_params = dict(folder = save_folder, name = "PAG_tractography")


# // CREATE SCENE //
# Create a scene with no title. You can also use scene.add_text to add other text elsewhere in the scene
scene = Scene(display_inset = True, title = None, camera = "sagittal", screenshot_kwargs = screenshot_params) 


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


# # // CUT SCENE IN HALF AT DESIRED PLANE //
# # Cut scene in half (set showplane = True if you want to see the plane location)
# scene.cut_actors_with_plane("sagittal", showplane = False) 


# # // EXPORT AS HTML //
# # Export to a .html file that can be opened in a browser to render an interactive brainrender scene
# scene.export_for_web("output/PAG_tractography.html") # you can pass a filepath where to save the scene


# # // MAKE VIDEO //
# # Create an instance of VideoMaker with our scene
# vm = VideoMaker(scene,
#     save_fld = save_folder, # folder where to save video
#     save_name = "PAG_video_tractography", # video name
#     #video_format = "mp4", # defaults to mp4
#     #duration = 3, # video duration in seconds (defaults to 3)
#     #niters = 60, # number of iterations (frames) when creating the video (defaults to 60)
#     #fps = 30 # framerate of video (defaults to 30)
#     ) 

# # Make a video and specify how the scene rotates at each frame. You can also change several parameters (destination folder, video name, fps, duration, etc.) specified above
# vm.make_video(azimuth = 1, elevation = 1, roll = 0, # rotation in degrees per frame on the relative axis    
#     save_fld = save_folder, save_name = "PAG_video_tractography",
#     video_format = "avi", duration = 5, niters = 50, fps = 30)


# // RENDER INTERACTIVELY //
# Render interactively. You can press "s" to take a screenshot
scene.render(interactive = True, video = False, camera = "sagittal", zoom = 1)