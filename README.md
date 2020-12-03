# Advent of Code 2020
**Solutions by Vincent van Setten(Vvamp)**
- https://adventofcode.com/2020/
- https://adventofcode.com/2020/leaderboard/private (code=`1016489-968fe61d`)

# WARNING: Spoilers ahead!
Only read this if you do not mind seeing answers for the 2020 advent of code!
## Day 1
### Part 1
The very first assignment was relatively simple. 
The input was a list of integers. The goal was to find which two numbers added up to 2020 and then take the product of those two numbers.

I wrote a simple nested for loop(not the best way, but it was the first thing that came to mind) that checked each number against its counterpart. As soon as the first pair was found, I showed the two numbers and multiplied them together.

### Part 2
The second part was only a small change compared to part 1. This time, there were three numbers, instead of two, that had to add up to 2020. I simply created a 3-deep nested for loop(one for each number) and checked the numbers against themselves.

## Day 2
### Part 1
The second day, the goal was to find which data was valid after a data corruption issue. 
The input was a list of passwords, along with the requirements of that specific time. For instance, there would be a line with the following: '1-3 a: fiajia'. This meant that the 'a' had to be included at least once and at most thrice. The second part 'fiajia' was the password. The result was the amount of passwords that matched their requirements.

My solution was to loop through the passwords, split the requirements and password based on specific characteristics and simply checked the password character by character. Each time the characters matched, I added it up to a counter and checked if it matched the requirement. If it did, I added that to another counter.

### Part 2 
Part two was another small spinoff from part 1. This time, the requirement meant something else. Namely, the 1-3 meant that the character had to be in either position 1 or position 3(not both). I simply changed a small thing in my code to match this requirement.

## Day 3
### Part 1
At day three, the fun really started. The input was a matrix of characters. These characters were either a dot('.') or a hashtag('#'). A dot meant free space, while a hashtag meant there was a tree. The goal was to know how many trees were in the way.

Starting from position 0, the goal was to move down and right a certain amount of steps each time and then check whether or not there was a tree there. Each time there was a tree, I added it to a counter.

I took quite a while with this. This was due to a mistake I made with the rounding after the spaceship hit the right side of the matrix and had to go back to the left. 
### Part 2 
Part two was the same as part 1, but this time the input was 5 different amounts to move down and right. Those answers had to be multiplied together to form the actual answer. 
I simply made a function that returned the amount of trees and called that function 5 times. 
