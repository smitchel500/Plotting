# linePlot.py
# Susan M. Mitchell
# CMSC 201, Fall 2019
# Plotting library for Project 3 - Data Visualization: Opioid Deaths
# This version works with UMBC's GL system

###################################################################
# singleLinePlot() displays a single x-y line plot
# Input:           filename; string, file containing the data to be plotted
#                  xlabel; string, the x-axis label
#                  ylabel; string, the y-axis label
#                  legend; string, the plot legend
# Output:          none
# Preconditions:
# - the file contains two columns, separated by whitespace; the first column
#   is the x-axis data, the second is the y-axis data

def singleLinePlot(filename, xlabel, ylabel, legend):
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
    gnuplotCmds = gnuplotCmdsTmp % (xlabel, ylabel, filename, legend)
    cmdList = ['gnuplot', '-p']

    subproc = subprocess.run(cmdList, input=gnuplotCmds, encoding='ascii')

###################################################################
# doubleLinePlot() displays two x-y line plots simultaneously
# Input:           filename1; string, file containing 1st dataset to be plotted
#                  filename2; string, file containing 2nd dataset to be plotted
#                  xlabel; string, x-axis label
#                  ylabel; string, y-axis label
#                  legend1; string; legend for 1st plot
#                  legend2; string; legend for 2nd plot
# Output:          none
# Preconditions:
# - files contains two columns, separated by whitespace; the first column
#   is the x-axis data, the second is the y-axis data

def doubleLinePlot(filename1, filename2, xlabel, ylabel, legend1, legend2):
    import subprocess

    gnuplotCmdsTmp = '\n'.join([
        "set terminal windows",
        #"set terminal aqua", # For Mac OS, uncomment this line of code
        #"set terminal dumb", # For Linux or Command Prompt, uncomment this line
        "set xlabel '%s'",
        "set ylabel '%s'",
        "plot '%s' with linespoints title '%s', '%s' with linespoints title '%s'",
        "quit"
    ])
    gnuplotCmds = gnuplotCmdsTmp % (xlabel, ylabel, filename1, legend1, filename2, legend2)
    cmdList = ['gnuplot', '-p']

    subprocess.run(cmdList, input=gnuplotCmds, encoding='ascii')
