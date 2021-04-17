Convert plots from png to gif using something like this:

    rm -f vol_cost*w.png
    for file in vol_cost_pt_y20*png; do convert $file -background white -flatten $file.w.png; done
    convert -delay 50 vol_cost_pt_y20*w.png vol_cost_pt_anim.gif
