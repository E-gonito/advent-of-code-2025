line[0] = right or left, followed by a number between 1-999.

Dial starts at 50, possible numbers is 0-99, 0 - 1 = 99. 

Password = number of times dial ends up at 0. 

Psuedocode : 
dial = 50
for each line in puzzleinput:
    direction = R | L
    magnitude = X
    counterFor0 = 0
    if Direction = R {
        operator = +
    } else {
        operator = -
    }
    dial + operator + magnitude
    if dial < 0 {
        dial + 100
    } 
    if dial > 99 {
        dial - 100
    }
    if dial === 0 {
        counterFor0 ++
    }
return counterFor0 ++



