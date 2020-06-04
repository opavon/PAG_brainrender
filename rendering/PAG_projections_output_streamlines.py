"""
    Render efferent mesoscale connectivity data from the Allen mouse connectome project as streamlines
"""
import brainrender
brainrender.SHADER_STYLE = 'cartoon'
from brainrender.scene import Scene

# Create a scene with the allen brain atlas atlas
scene = Scene()

# Download streamlines data for injections in the Periaqueductal Gray
filepaths, data = scene.atlas.download_streamlines_for_region("PAG")

# Add the brain regions
scene.add_brain_regions(['PAG'], alpha=.4, color='darkgoldenrod', add_labels=False, use_original_color=False, wireframe=False)

# Add the efferents by passing either the filepaths or the data
scene.add_streamlines(data,
    colorby=None, # how to color the streamline data (Default value = None)
    color_each=False, # if False all streamlines (one streamline object per injection) will have the same color, else you can color each individually
    show_injection_site=False, 
    color='darkseagreen', 
    alpha=.6)
# This should color each streamline with a different color
#brainrender.colors.makePalette(len(data),'blue', 'red') will give you a list of colors

# Render scene
scene.render(interactive=True, camera='sagittal', zoom=1)