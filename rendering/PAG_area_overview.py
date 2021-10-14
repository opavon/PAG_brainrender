"""
    Render a PAG scene following the basic examples in the Brainrender repository
"""

import brainrender
from brainrender import Scene, Animation
from vedo import settings as vsettings
from brainrender.video import VideoMaker


# // ATLASES //
# You can choose one of several available atlases from the brainglobe atlas api (https://github.com/brainglobe/bg-atlasapi)

# # To check the available atlases in brainglobe:
# from bg_atlasapi import show_atlases
# show_atlases()
# allen_mouse_10um
# allen_mouse_25um
# allen_mouse_50um
# kim_mouse_10um
# kim_mouse_25um
# kim_mouse_50um
# osten_mouse_10um 
# osten_mouse_25um 
# osten_mouse_50um 


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


# // ADD BRAIN REGIONS //
# https://github.com/brainglobe/brainrender/blob/19c63b97a34336898871d66fb24484e8a55d4fa7/examples/brain_regions.py

# Add brain regions with scene.add_brain_regions
pag = scene.add_brain_region("PAG", alpha = 0.4, color = "darkgoldenrod", silhouette = None, hemisphere = "both")
dorsal_raphe = scene.add_brain_region("DR", alpha = 0.4, color = "olivedrab", silhouette = None, hemisphere = "both")
superior_colliculus = scene.add_brain_region("SCdg", "SCdw", "SCig", "SCiw", "SCm", "SCop", "SCs", "SCsg", "SCzo", alpha = 0.4, color = "olivedrab", silhouette = None, hemisphere = "both")


# # // ADD LABELS //
# # Add labels with scene.add_label
# # :param kwargs: key word arguments can be passed to determine text appearance and location:
#         # - size: int, text size. Default 300
#         # - color: str, text color. A list of colors can be passed. If None, the actor's color is used. Default None.
#         # - xoffset, yoffset, zoffset: integers that shift the label position
#         # - radius: radius of sphere used to denote label anchor. Set to 0 or None to hide.

# scene.add_label(pag, "PAG", size = 400, color = "blackboard", radius = None, xoffset = 0, yoffset = -500, zoffset = 0)
# scene.add_label(dorsal_raphe, "DRN", size = 400, color = "blackboard", radius = None, xoffset = 0, yoffset = -500, zoffset = 0)


# // SLICE SCENE //
# https://github.com/brainglobe/brainrender/blob/19c63b97a34336898871d66fb24484e8a55d4fa7/examples/slice.py

# # Slice actors with a specified plane
# scene.slice("frontal", actors = [pag])
# # Slice with a custom plane
# plane = scene.atlas.get_plane(pos = pag.centerOfMass(), norm=(1, 1, 0))
# scene.slice(plane, actors = [pag, dorsal_raphe])


# # // EXPORT AS HTML //
# # Export to a .html file that can be opened in a browser to render an interactive brainrender scene
# scene.export("output/PAG_area_overview.html") # you can pass a filepath where to save the scene


# # // MAKE VIDEO //
# # https://github.com/brainglobe/brainrender/blob/19c63b97a34336898871d66fb24484e8a55d4fa7/examples/video.py

# # Create an instance of VideoMaker with our scene
# vm = VideoMaker(scene,
#     save_fld = save_folder, # folder where to save video
#     name = "PAG_video_areas_overview", # name of the video
#     fmt = "mp4", # video format. Defaults to mp4
#     size = "1620x1050", # size of video's frames in pixels. Defaults to 1620x1050
#     make_frame_func = None # function to animate as desired
#     ) 

# # Parameters of `make_frame_func` include:
# #     :param scene: scene to be animated.
# #     :param frame_number: int, not used
# #     :param tot_frames: int, total numner of frames
# #     :param azimuth: integer, specify the rotation in degrees per frame on the relative axis. (Default value = 0)
# #     :param elevation: integer, specify the rotation in degrees per frame on the relative axis. (Default value = 0)
# #     :param roll: integer, specify the rotation in degrees per frame on the relative axis. (Default value = 0)

# # Make a video and specify how the scene rotates at each frame. You can also change several parameters (destination folder, video name, fps, duration, etc.) specified above
# vm.make_video(
#     duration = 3, # video duration in seconds (defaults to 3)
#     fps = 30, # frame rate of video (defaults to 30)
#     azimuth = 1, elevation = 1, roll = 0, # rotation in degrees per frame on the relative axis
#     )


# # // MAKE ANIMATION //
# # https://github.com/brainglobe/brainrender/blob/19c63b97a34336898871d66fb24484e8a55d4fa7/examples/animation.py

# # Create an animated video by specifying the cameraa parameters at a number of key frames
# anim = Animation(scene,
#     save_fld = save_folder, # folder where to save video
#     name = "PAG_video_areas_overview", # name of the video
#     fmt = "mp4", # video format. Defaults to mp4
#     size = "1620x1050" # size of video's frames in pixels. Defaults to 1620x1050
#     ) 

# # Specify camera position and zoom at some key frames. Each key frame defines the scene's state after n seconds have passed
# anim.add_keyframe(0, camera = "top", zoom = 1.3)
# anim.add_keyframe(1, camera = "sagittal", zoom = 3)
# anim.add_keyframe(2, camera = "frontal", zoom = 0.8)
# anim.add_keyframe(3, camera = "frontal", zoom = 1)

# # Make videos
# anim.make_video(
#     duration = 3, # video duration in seconds (defaults to 3)
#     fps = 30, # frame rate of video (defaults to 30)
#     azimuth = 1, elevation = 1, roll = 0, # rotation in degrees per frame on the relative axis
#     )

# // RENDER INTERACTIVELY //
# Render interactively. You can press "s" to take a screenshot
scene.render(interactive = True, camera = "sagittal", zoom = 1)


# # // RENDER WITH CUSTOM CAMERA //
# # https://github.com/brainglobe/brainrender/blob/19c63b97a34336898871d66fb24484e8a55d4fa7/examples/custom_camera.py

# # To render a scene with a custom camera you can specify a dictionary of camera parameters.
# # To get the parameters for a custom camera camera:
# #   - render an interactive scene with any camera
# #   - move the camera to where you need it to be
# #   - press 'c'
# #   - this will print the current camera parameters to your console. Copy paste the parameters in your script as follows

# custom_camera = {
#     "pos": (41381, -16104, 27222),
#     "viewup": (0, -1, 0),
#     "clippingRange": (31983, 76783),
# }
# scene.render(interactive = True, camera = custom_camera, zoom = 1)
