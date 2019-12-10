def gauss():
    import subprocess

    # set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 512, 280 
    # set output 'transparent.2.png'
    gnuplotCmds = '''
    set clip two
    set style fill transparent solid 0.50 noborder
    set key title "Gaussian Distribution"
    set key inside left top vertical Left reverse enhanced autotitles nobox
    set key noinvert samplen 1 spacing 1 width 0 height 0
    set style function filledcurves y1=0
    set title "Transparent filled curves" 
    set xrange [ -5.00000 : 5.00000 ] noreverse nowriteback
    set yrange [ 0.00000 : 1.00000 ] noreverse nowriteback
    unset colorbox
    Gauss(x,mu,sigma) = 1./(sigma*sqrt(2*pi)) * exp( -(x-mu)**2 / (2*sigma**2) )
    d1(x) = Gauss(x, 0.5, 0.5)
    d2(x) = Gauss(x,  2.,  1.)
    d3(x) = Gauss(x, -1.,  2.)
    GPFUN_Gauss =\"Gauss(x,mu,sigma) = 1./(sigma*sqrt(2*pi)) * exp( -(x-mu)**2 / (2*sigma**2) \"
    GPFUN_d1 = "d1(x) = Gauss(x, 0.5, 0.5)"
    GPFUN_d2 = "d2(x) = Gauss(x,  2.,  1.)"
    GPFUN_d3 = "d3(x) = Gauss(x, -1.,  2.)"
    plot d1(x) fs solid 1.0 lc rgb "forest-green" title "μ =  0.5 σ = 0.5",
        d2(x) lc rgb "gold" title "μ =  2.0 σ = 1.0", d3(x) lc rgb "red"
        "title "μ = -1.0 σ = 2.0"
    quit
    '''
    cmdList = ['gnuplot', '-p']

    subprocess.run(cmdList, input=gnuplotCmds, encoding='utf-8')

    print("gauss end")

gauss()