def financial():
    import subprocess

    gnuplotCmds = '''
    # set terminal pngcairo  transparent enhanced font "arial,8" fontscale 1.0 size 660, 320 
    # set output 'finance.1.png'
    set style increment default
    set ytics  norangelimit 
    set ytics   (80.0000, 85.0000, 90.0000, 95.0000, 100.000, 105.000)
    set title "Demo of plotting financial data" 
    set xrange [ 50.0000 : 253.000 ] noreverse nowriteback
    set x2range [ * : * ] noreverse writeback
    set yrange [ 75.0000 : 105.000 ] noreverse nowriteback
    set y2range [ * : * ] noreverse writeback
    set zrange [ * : * ] noreverse writeback
    set cbrange [ * : * ] noreverse writeback
    set rrange [ * : * ] noreverse writeback
    set lmargin  9
    set rmargin  2
    ## Last datafile plotted: "finance.dat"
    plot 'finance.dat' using 0:4 notitle with lines
    '''
    cmdList = ['gnuplot', '-p']

    subprocess.run(cmdList, input=gnuplotCmds, encoding='utf-8')

    print("financial end")

financial()
