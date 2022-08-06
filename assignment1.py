line = input("Please enter the input : ")
time = int(input("Please enter days: "))
fishTrack = [0,0,0,0,0,0,0,0,0]


fishTimer = line.split(',')
fishTimer = [int(item) for item in fishTimer]

for i in fishTimer:
    fishTrack[i] += 1
    
for i in range(time):
    fishTrack[7] += fishTrack[0]
    fishTrack = fishTrack[1:] + fishTrack[:1]    
    
print("The total fishes after " + str(time) + " will be " + str(sum(fishTrack)))

