const fs = require('fs')
const input = fs.readFileSync('input.txt', 'utf-8')
                .trim()
                .split('\n');
let totalPart1 = 0;
let totalPart2 = 0;
//Regex would look nicer than this mess
for (let i = 0; i < input.length;i++){
	var temp = input[i].split(':');
	var toMatch = temp[0].split(' ');
	var ntoMatch = toMatch[0].split('-');
	var lower = parseInt(ntoMatch[0]);
	var higher = parseInt(ntoMatch[1]);
	var password = temp[1].trim();
	var chr = toMatch[1];
	var sum = 0;
	for (let i = 0; i < password.length; i++) {
		if(password.charAt(i) == chr){
			sum++;
		}	
	}
	if((password.charAt(lower-1) === chr) ^ (password.charAt(higher-1) === chr)){
		totalPart2++;
		}
	if (sum >= lower && sum <= higher){
		totalPart1++;
	}
}
console.log("Part 1: " + totalPart1);
console.log("Part 2: " + totalPart2);