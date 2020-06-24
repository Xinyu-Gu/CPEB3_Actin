hide all
unset dynamic_measures
show cartoon, all
run draw_links.py
distance min_frst_wm= (/16//H/25/CA),(/16//H/27/CA)
draw_links 16 and resi 25 and name CA and Chain H, 16 and resi 52 and name CA and Chain H, color=green, color2=green, radius=0.2, object_name=25:52_green
zoom all
hide labels
color green, min_frst_wm
