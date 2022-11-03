#declares variable 'log_file' and passes the contents of 'um-server-01.txt' as value
log_file = open("um-server-01.txt")

#defines function that prints sales report 
def generate_sales_reports(log_file):
    for line in log_file: #for loop to iterate through line in file
        line = line.rstrip() #formats line to strip away blank space on the right
        day = line[0:3] #declares variable with slice from 0 to 3 from line string
        if day == "Mon": #if statement to check if slice matches desired value, if so then prints line
            print(line)

#calls function
generate_sales_reports(log_file)

#made inconsequential change to test git command
