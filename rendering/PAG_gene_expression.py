"""
    Download and visualise volumetric gene expression data from the Allen Atlas dataset: https://mouse.brain-map.org/
"""
import brainrender
from brainrender.scene import Scene
from brainrender.colors import makePalette
from brainrender.ABA.gene_expression import GeneExpressionAPI
from brainrender.animation.video import BasicVideoMaker as VideoMaker


# // DEFAULT SETTINGS //
# Change some of the default settings
brainrender.SHADER_STYLE = "metallic" # affects the look of rendered brain regions, values can be: ["metallic", "plastic", "shiny", "glossy", "cartoon"] and can be changed in interactive mode
brainrender.BACKGROUND_COLOR = "white" # color of the background window (defaults to "white", try "blackboard")
brainrender.ROOT_COLOR = [0.4, 0.4, 0.4] # color of the overall brain model's actor (defaults to [0.4, 0.4, 0.4])
brainrender.ROOT_ALPHA = 0.2 # transparency of the overall brain model's actor (defaults to 0.2)
brainrender.DEFAULT_SCREENSHOT_NAME = "PAG_gene_expression" # screenshots will have this name and the time at which they were taken
brainrender.DEFAULT_SCREENSHOT_TYPE = ".png" # png, svg or jpg supported
brainrender.DEFAULT_SCREENSHOT_SCALE = 1 # values >1 yield higher resolution screenshots
brainrender.SCREENSHOT_TRANSPARENT_BACKGROUND = True # whether to save screenshots with transparent background


# // SET PARAMETERS //
# Save folder
save_folder = "D:/Dropbox (UCL - SWC)/Project_transcriptomics/analysis/PAG_scRNAseq_brainrender/output"

# Create screenshot parameters
screenshot_params = dict(folder = save_folder, name = "PAG_gene_expression")


# // DOWNLOAD GENE DATA //
# To download a gene's data you need two things: (1) the id of the gene in the allen database and (2) the id(s) of the ISH experiments for that gene. You can get both with GeneExpressionAPI
geapi = GeneExpressionAPI() # used to download the data from the allen API

# Choose a gene name to download
gene = "Cacna2d1"

# Get gene id
geneid = geapi.get_gene_id_by_name(gene)  # 12078

# Get experiment IDs
expids = geapi.get_gene_experiments(geneid)  # [75042246, 72119649, 74000600, 69236915]

# Download the data for one of the experiments above
data = geapi.get_gene_data(geneid, expids[0])


# // CREATE GENE ACTOR //
# Now you can take the volumetric data and turn it into an actor that can be added to your brainrender scene. When creating the mesh it's useful to set a threshold to eliminate voxels with low gene expression energy. This can be done in two ways: (1) use [min_value] to define a threshold value, or (2) use [min_quantile] to define a percentile (range 0-100) so that only voxels with value above the percentile are rendered. It is also possible to pass any matplotlib (or custom) colormap to cmap to specify how the voxels will be colored
gene_actor = geapi.griddata_to_volume(data, min_quantile = 85, min_value = None, cmap = "inferno")


# // CREATE SCENE //
# Create a scene with no title. You can also use scene.add_text to add other text elsewhere in the scene
scene = Scene(display_inset = True, title = None, camera = "sagittal", screenshot_kwargs = screenshot_params)


# // ADD GENE EXPRESSION AND BRAIN REGIONS//
pag = scene.add_brain_regions(["PAG"],
    alpha = 0.2, color = "darkgoldenrod", add_labels = False, use_original_color = False, wireframe = False)

scene.add_vtkactor(gene_actor)


# // CUT SCENE IN HALF AT DESIRED PLANE //
# Cut scene in half (set showplane = True if you want to see the plane location)
scene.cut_actors_with_plane("sagittal", showplane = False) 


# # // EXPORT AS HTML //
# # Export to a .html file that can be opened in a browser to render an interactive brainrender scene
# scene.export_for_web("output/PAG_gene_expression.html") # you can pass a filepath where to save the scene


# # // MAKE VIDEO //
# # Create an instance of VideoMaker with our scene
# vm = VideoMaker(scene,
#     save_fld = save_folder, # folder where to save video
#     save_name = "PAG_video_gene_expression", # video name
#     #video_format = "mp4", # defaults to mp4
#     #duration = 3, # video duration in seconds (defaults to 3)
#     #niters = 60, # number of iterations (frames) when creating the video (defaults to 60)
#     #fps = 30 # framerate of video (defaults to 30)
#     ) 

# # Make a video and specify how the scene rotates at each frame. You can also change several parameters (destination folder, video name, fps, duration, etc.) specified above
# vm.make_video(azimuth = 1, elevation = 1, roll = 0, # rotation in degrees per frame on the relative axis    
#     save_fld = save_folder, save_name = "PAG_video_gene_expression",
#     video_format = "avi", duration = 5, niters = 50, fps = 30)


# // RENDER INTERACTIVELY //
# Render interactively. You can press "s" to take a screenshot
scene.render(interactive = True, video = False, camera = "sagittal", zoom = 1)