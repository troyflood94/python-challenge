import os
import csv 
reader_csv = csv.reader(open(r"pypoll\resources\election_data.csv", 'r', encoding='UTF-8'))
read_list=list(reader_csv)

#store headers to enable adding logic later that allows us to skip them
headerlines=["Ballot ID","County","Candidate"]
vote_list=[]  #create empty list to append to
for vote,county,candidate in read_list:    #create loop and define the variables even though we dont need them all
    if vote not in headerlines:             #block headers from being iterated over
        vote_list.append(county)            #chose county because it is all same characters with no spaces as my item to count. Seemed to be simplest item.
   #count the number of entries appended to the list
votecount=len(vote_list)

#create empty lists to append votes to after running logic
ccs=[]
dg= []
rad=[]


for voter, county, candidate in read_list:
    if candidate=="Charles Casper Stockham":
        ccs.append(county)
    elif candidate=="Diana DeGette":
        dg.append(county)
    elif candidate=="Raymon Anthony Doane":
        rad.append(county)
#create some calculated variables to make print statements easier by making the types consistent
ccsvotes=len(ccs)
dgvotes=len(dg)
radvotes=len(rad)
ccsperc=round((ccsvotes/votecount)*100,2)
dgperc=round((dgvotes/votecount)*100,2)
radperc=round((radvotes/votecount)*100,2)

#print Statements for summary
print("Election Results")
print("-------------------------")
print("Total Votes:" + " " + str(len(vote_list)))
print(f"Charles Casper Stockham:" +" "+ str(ccsperc)+"%" + " " + str(ccsvotes))
print(f"Diana DeGette:" +" "+ str(dgperc)+"%" + " " + str(dgvotes))
print(f"Raymon Anthony Doane:" +" "+ str(radperc)+"%" + " " + str(radvotes))
print("-------------------------")
#final print statement with logic before choosing
if ccsvotes>dgvotes and ccsvotes>radvotes:
    print("Winner: Charles Casper Stockham")
elif dgvotes>ccsvotes and dgvotes> radvotes:
    print("Winner: Diana Degette")
elif radvotes>ccsvotes and radvotes>dgvotes:
    print("Winner: Raymon Anthony Doane")

with open("Text Analysis", "w") as readme_file:
    readme_file.write("Election Results\n")
    readme_file.write("-------------------------\n")
    readme_file.write(f"Total Votes: {len(vote_list)}\n")
    readme_file.write(f"Charles Casper Stockham: {ccsperc:.2f}% ({ccsvotes})\n")
    readme_file.write(f"Diana DeGette: {dgperc:.2f}% ({dgvotes})\n")
    readme_file.write(f"Raymon Anthony Doane: {radperc:.2f}% ({radvotes})\n")
    readme_file.write("-------------------------\n")
    
    # Final print statement with logic before choosing the winner
    if ccsvotes > dgvotes and ccsvotes > radvotes:
        readme_file.write("Winner: Charles Casper Stockham\n")
    elif dgvotes > ccsvotes and dgvotes > radvotes:
        readme_file.write("Winner: Diana Degette\n")
    elif radvotes > ccsvotes and radvotes > dgvotes:
        readme_file.write("Winner: Raymon Anthony Doane\n")
