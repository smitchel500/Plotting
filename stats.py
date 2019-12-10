def stats():
    import subprocess

    gnuplotCmds = '''
    # set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 
    # set output 'stats.1.png'
    set key fixed left top vertical Left noreverse enhanced autotitle nobox
    set label 1 "min" at 7.00000, graph 0.1, 0 center norotate back nopoint offset character 0, -1, 0
    set label 2 "max" at 9.00000, graph 0.9, 0 center norotate back nopoint offset character 0, 1, 0
    set arrow 1 from 7.00000, graph 0.1, 0 to 7.00000, 2.20087, 0.00000 head back filled linewidth 1.000 dashtype solid
    set arrow 2 from 9.00000, graph 0.9, 0 to 9.00000, 3.13972, 0.00000 head back filled linewidth 1.000 dashtype solid
    set style increment default
    set offsets 0, 0, 0.5, 0.5
    set style data lines
    set title "Use of stats command to find min/max/mean before plotting\nOne data column" 
    set autoscale tfixmin
    set autoscale tfixmax
    set autoscale ufixmin
    set autoscale ufixmax
    set autoscale vfixmin
    set autoscale vfixmax
    set xrange [ * : * ] noreverse writeback
    set autoscale xfixmin
    set autoscale xfixmax
    set x2range [ * : * ] noreverse writeback
    set autoscale x2fixmin
    set autoscale x2fixmax
    set yrange [ * : * ] noreverse writeback
    set autoscale yfixmin
    set autoscale yfixmax
    set y2range [ * : * ] noreverse writeback
    set autoscale y2fixmin
    set autoscale y2fixmax
    set zrange [ * : * ] noreverse writeback
    set autoscale zfixmin
    set autoscale zfixmax
    set cbrange [ * : * ] noreverse writeback
    set autoscale cbfixmin
    set autoscale cbfixmax
    set rrange [ * : * ] noreverse writeback
    set autoscale rfixmin
    set autoscale rfixmax
    A_records = 20
    A_invalid = 0
    A_headers = 0
    A_blank = 1
    A_blocks = 1
    A_outofrange = 0
    A_columns = 11
    A_mean = 2.54077965
    A_stddev = 0.222745079388137
    A_ssd = 0.228531629485718
    A_skewness = 0.978323019217487
    A_kurtosis = 3.60561959806089
    A_adev = 0.178523515
    A_mean_err = 0.0498073139165462
    A_stddev_err = 0.0352190894230769
    A_skewness_err = 0.547722557505166
    A_kurtosis_err = 1.09544511501033
    A_sum = 50.815593
    A_sumsq = 130.103532004915
    A_min = 2.20087
    A_max = 3.139718
    A_median = 2.4609945
    A_lo_quartile = 2.3865975
    A_up_quartile = 2.6562155
    A_index_min = 7
    A_index_max = 9
    ## Last datafile plotted: "orbital_elements.dat"
    plot 'orbital_elements.dat' index 1 using 0:2 title "  Data" lw 2,      A_mean title "  Mean"
    '''
    cmdList = ['gnuplot', '-p']

    subprocess.run(cmdList, input=gnuplotCmds, encoding='utf-8')

    print("gauss end")

stats()
