"""
    Download and visualise volumetric gene expression data from the Allen Atlas dataset: https://mouse.brain-map.org/
    From brainrender example: https://github.com/brainglobe/brainrender/blob/19c63b97a34336898871d66fb24484e8a55d4fa7/examples/gene_expression.py
"""
import brainrender
from brainrender import Scene, Animation
from vedo import settings as vsettings
from brainrender.video import VideoMaker
from brainrender.atlas_specific import GeneExpressionAPI


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
brainrender.settings.WHOLE_SCREEN = True  # If true render window is full screen
brainrender.settings.OFFSCREEN = False

# ------------------------------- vedo settings ------------------------------ #
# For transparent background with screenshots
vsettings.screenshotTransparentBackground = True  # vedo for transparent bg
vsettings.useFXAA = False  # This needs to be false for transparent bg


# // SET PARAMETERS //
# Save folder
save_folder = r"D:\Dropbox (UCL)\Project_transcriptomics\analysis\PAG_scRNAseq_brainrender\output"


# // DOWNLOAD GENE DATA //
# To download a gene's data you need two things: (1) the id of the gene in the allen database and (2) the id(s) of the ISH experiments for that gene. You can get both with GeneExpressionAPI
geapi = GeneExpressionAPI() # used to download the data from the allen API

# Choose a gene name to download
gene = "Cacna2d1"

# Get experiment IDs
expids = geapi.get_gene_experiments(gene)  # [75042246, 72119649, 74000600, 69236915]

# Download the data for one of the experiments above
data = geapi.get_gene_data(gene, expids[0])


# // CREATE GENE ACTOR //
# Now you can take the volumetric data and turn it into an actor that can be added to your brainrender scene. When creating the mesh it's useful to set a threshold to eliminate voxels with low gene expression energy. This can be done in two ways: (1) use [min_value] to define a threshold value, or (2) use [min_quantile] to define a percentile (range 0-100) so that only voxels with value above the percentile are rendered. It is also possible to pass any matplotlib (or custom) colormap to cmap to specify how the voxels will be colored
gene_actor = geapi.griddata_to_volume(data, min_quantile = 85, min_value = None, cmap = "inferno")


# // CREATE SCENE //
# Create a scene with no title. You can also use scene.add_text to add other text elsewhere in the scene
scene = Scene(root = True, atlas_name = 'allen_mouse_10um', inset = False, title = None, screenshots_folder = save_folder, plotter = None)

# // ADD GENE EXPRESSION AND BRAIN REGIONS//
pag = scene.add_brain_region("PAG", alpha = 0.2, color = "darkgoldenrod", silhouette = None, hemisphere = "both")
act = scene.add(gene_actor)


# // RENDER INTERACTIVELY //
# Render interactively. You can press "s" to take a screenshot
scene.render(interactive = True, camera = "sagittal", zoom = 1)