""" 
    Download and render afferent mesoscale projection data
    using the AllenBrainAtlas (ABA) and Scene classes
"""

import brainrender
brainrender.SHADER_STYLE = 'cartoon'
from brainrender.scene import Scene
from brainrender.atlases.aba import ABA

# Create a scene
scene = Scene()

# Get the center of mass of the region of interest
p0 = scene.atlas.get_region_CenterOfMass("PAG")

# Get projections to that point
analyzer = ABA()
tract = analyzer.get_projection_tracts_to_target(p0=p0)

# Add the brain regions
scene.add_brain_regions(['PAG'], alpha=.4, color='darkgoldenrod', add_labels=False, use_original_color=False, wireframe=False)
#scene.add_brain_regions(['HY'], alpha=.2, color='lightsalmon', add_labels=False, use_original_color=False, wireframe=True)

# Add the projections to the chosen brain region
scene.add_tractography(tract,
     color=None, #"darkseagreen" # color of rendered tractography data
     color_by="target_region", #"manual", "region", or "target_region"
     VIP_regions=["SCdg", "SCdw", "SCig", "SCiw", "SCm", "SCop", "SCs", "SCsg", "SCzo"], # list of brain regions with VIP treatement (Default value = [])
     VIP_color="darkseagreen", # color to use for VIP data (Default value = None)
     others_color="ivory", # color for not VIP data (Default value = "white")
     others_alpha=.1, # Default is 1
     verbose=True, # Prints all areas projecting to target
     include_all_inj_regions=False, 
     extract_region_from_inj_coords=False, 
     display_injection_volume=True) # add a spehere to display the injection coordinates and volume

# This renders tractography data and adds it to the scene. A subset of tractography data can receive special treatment using the  with VIP regions argument: if the injection site for the tractography data is in a VIP region, this is colored differently.
# Try "SC", "VMH", "SCm", "LHA":
    ##["SCdg", "SCdw", "SCig", "SCiw", "SCm", "SCop", "SCs", "SCsg", "SCzo"] -- Superior Colliculus
    ##(LHA) -- Lateral hypothalamic area
    ##(VMH) -- Ventromedial hypothalamic nucleus
    ##(ZI) -- Zona incerta

# Render scene
scene.render(interactive=True, camera='sagittal')