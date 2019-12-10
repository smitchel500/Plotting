def binning():
    import subprocess

    gnuplotCmds = '''
    # set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 
    # set output 'smooth.1.png'
    set boxwidth 0.05 absolute
    set key fixed left top vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid
    set style increment default
    set xzeroaxis
    set yzeroaxis
    set zzeroaxis
    set title "Uniform Distribution" 
    set xrange [ -0.100000 : 1.10000 ] noreverse writeback
    set autoscale xfixmin
    set autoscale xfixmax
    set x2range [ * : * ] noreverse writeback
    set yrange [ -0.400000 : 1.60000 ] noreverse nowriteback
    set y2range [ * : * ] noreverse writeback
    set zrange [ * : * ] noreverse writeback
    set cbrange [ * : * ] noreverse writeback
    set rrange [ * : * ] noreverse writeback
    bin(x, s) = s*int(x/s)
    STATS_records = 300
    STATS_invalid = 0
    STATS_headers = 0
    STATS_blank = 0
    STATS_blocks = 1
    STATS_outofrange = 0
    STATS_columns = 4
    STATS_mean_x = 0.489028602629325
    STATS_stddev_x = 0.284214790260807
    STATS_ssd_x = 0.284689669105347
    STATS_skewness_x = 0.00845756567925355
    STATS_kurtosis_x = 1.80797909532985
    STATS_adev_x = 0.24724449127266
    STATS_mean_err_x = 0.016409148566475
    STATS_stddev_err_x = 0.011603020224852
    STATS_skewness_err_x = 0.14142135623731
    STATS_kurtosis_err_x = 0.282842712474619
    STATS_sum_x = 146.708580788797
    STATS_sumsq_x = 95.9781063577753
    STATS_min_x = 0.00268886761206842
    STATS_max_x = 0.994440660126254
    STATS_median_x = 0.501553979298141
    STATS_lo_quartile_x = 0.239498522764712
    STATS_up_quartile_x = 0.719533872399656
    STATS_index_min_x = 158
    STATS_index_max_x = 169
    STATS_mean_y = 0.101174059040574
    STATS_stddev_y = 0.979756162161808
    STATS_ssd_y = 0.981393182789031
    STATS_skewness_y = -0.145054812500423
    STATS_kurtosis_y = 2.771044161482
    STATS_adev_y = 0.782186633380536
    STATS_mean_err_y = 0.0565662483964314
    STATS_stddev_err_y = 0.0399983778273993
    STATS_skewness_err_y = 0.14142135623731
    STATS_kurtosis_err_y = 0.282842712474619
    STATS_sum_y = 30.3522177121723
    STATS_sumsq_y = 291.047498255034
    STATS_min_y = -2.58506671902739
    STATS_max_y = 2.62217903865129
    STATS_median_y = 0.148518719067474
    STATS_lo_quartile_y = -0.497150169223868
    STATS_up_quartile_y = 0.801146309145715
    STATS_index_min_y = 245
    STATS_index_max_y = 264
    STATS_slope = -0.31953511556509
    STATS_intercept = 0.25743587009637
    STATS_slope_err = 0.198833430525872
    STATS_intercept_err = 0.11246434720669
    STATS_correlation = -0.0926930693152367
    STATS_sumxy = 7.09967583921745
    STATS_pos_min_y = 0.0594512499186007
    STATS_pos_max_y = 0.192141155866905
    N = 300
    ## Last datafile plotted: "random-points"
    plot "random-points" u 1:(0.25*rand(0)-.35) t '',      "" u (bin($1,0.05)):(20./N) smooth freq t 'smooth frequency' w boxes,      "" u 1:(1.) smooth cnorm t 'smooth cnorm'
    '''
    cmdList = ['gnuplot', '-p']

    subprocess.run(cmdList, input=gnuplotCmds, encoding='utf-8')

    print("gauss end")

binning()
