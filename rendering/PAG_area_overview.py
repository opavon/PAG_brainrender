"""
    Render a PAG scene following the basic examples in the Brainrender repository
"""

import brainrender
brainrender.SHADER_STYLE = 'cartoon' # gives actors a flat shading (good for schematics and illustrations)
from brainrender.scene import Scene

# Create a scene with a title
scene = Scene(title=None) # You can use scene.add_text to add other text elsewhere in the scene

# Create brain regions with scene.add_brain_regions
pag = scene.add_brain_regions(['PAG'], 
    alpha=.4, color='darkgoldenrod', add_labels=False, use_original_color=False, wireframe=False)
dorsal_raphe = scene.add_brain_regions(['DR'], 
    alpha=.4, color='olivedrab', add_labels=False, use_original_color=False, wireframe=True)
superior_colliculus = scene.add_brain_regions(['SCdg', 'SCdw', 'SCig', 'SCiw', 'SCm', 'SCop', 'SCs', 'SCsg', 'SCzo'],
    alpha=.4, color='olivedrab', add_labels=False, use_original_color=False, wireframe=True)

# Add labels with scene.add_actor_label
# scene.add_actor_label(pag, 'PAG', size=400, color='blackboard', xoffset=0, yoffset=0, radius=None)
# scene.add_actor_label(superior_colliculus, 'SC', size=400, color='blackboard', xoffset=0, yoffset=0, radius=None)
# scene.add_actor_label(dorsal_raphe, 'DRN', size=400, color='blackboard', xoffset=0, yoffset=0, radius=None)

# Render scene
scene.render(interactive=True, camera='sagittal')