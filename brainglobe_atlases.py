"""
    Install different atlases from the brainglob atas api
"""

import brainrender
from brainrender import Scene

# // INSTALL ATLASES //
# You can choose one of several available atlases from the brainglobe atlas api (https://github.com/brainglobe/bg-atlasapi)


# To check the available atlases in brainglobe:
from bg_atlasapi import show_atlases
show_atlases()
# allen_mouse_10um
# allen_mouse_25um
# allen_mouse_50um
# kim_mouse_10um
# kim_mouse_25um
# kim_mouse_50um
# osten_mouse_10um 
# osten_mouse_25um 
# osten_mouse_50um 


# To install an atlas, run one of the following with the atlas name. If it has never been used, it will download it.
scene = Scene(atlas_name = "allen_mouse_10um")
# scene = Scene(atlas_name = "allen_mouse_25um")
# scene = Scene(atlas_name = "allen_mouse_50um")
scene = Scene(atlas_name = "kim_mouse_10um")
# scene = Scene(atlas_name = "kim_mouse_25um")
# scene = Scene(atlas_name = "kim_mouse_50um")
scene = Scene(atlas_name = "osten_mouse_10um")
# scene = Scene(atlas_name = "osten_mouse_25um")
# scene = Scene(atlas_name = "osten_mouse_50um")