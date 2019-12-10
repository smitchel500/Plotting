# Single line plot using hard-coded data
import subprocess

gnuplotCmdsTmp = '\n'.join([
    "set terminal windows",
    #"set terminal aqua", # For Mac OS, uncomment this line of code
    #"set terminal dumb", # For Linux or Command Prompt, uncomment this line
    "set xlabel '%s'",
    "set ylabel '%s'",
    "plot '%s' with linespoints title '%s'",
    "quit"
])

gnuplotCmds = gnuplotCmdsTmp % ("Year", "Deaths", "allDrugs.dat", "Deaths Due to All Drugs")

cmdList = ['gnuplot', '-p']
subproc = subprocess.run(cmdList, input=gnuplotCmds, encoding='ascii')