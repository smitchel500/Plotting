# Double line plot with data input by user
def doubleLinePlot(filename1, filename2, xlabel, ylabel, legend1, legend2):
    import subprocess

    gnuplotCmdsTmp = '\n'.join([
        "set terminal windows",
        #"set terminal aqua", # For Mac OS, uncomment this line
        #"set terminal dumb", # For Linux or Command Prompt, uncomment this line
        "set xlabel '%s'",
        "set ylabel '%s'",
        "plot '%s' with linespoints title '%s', '%s' with linespoints title '%s'",
        "quit"
    ])
    gnuplotCmds = gnuplotCmdsTmp % (xlabel, ylabel, filename1, legend1, filename2, legend2)
    cmdList = ['gnuplot', '-p']

    subprocess.run(cmdList, input=gnuplotCmds, encoding='ascii')

if __name__ == '__main__':
    filename1 = input("Enter 1st file name: ")
    filename2 = input("Enter 2nd file name: ")
    xlabel = input("Enter X-axis label: ")
    ylabel = input("Enter Y-axis label: ")
    legend1 = input("Enter 1st legend: ")
    legend2 = input("Enter 2nd legend: ")

    doubleLinePlot(filename1, filename2, xlabel, ylabel, legend1, legend2)