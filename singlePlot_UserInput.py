# Single line plot with data input by user
import subprocess

def singleLinePlot(filename, xlabel, ylabel, legend):
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
    subprocess.run(cmdList, input=gnuplotCmds, encoding='ascii')

if __name__ == '__main__':
    filename = input("Enter file name: ")
    xlabel = input("Enter X-axis label: ")
    ylabel = input("Enter Y-axis label: ")
    legend = input("Enter legend: ")

    singleLinePlot(filename, xlabel, ylabel, legend)