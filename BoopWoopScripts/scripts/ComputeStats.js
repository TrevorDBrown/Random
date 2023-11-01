/**
	{
		"api":1,
		"name":"Compute Stats",
		"description":"Calculates statistics from a list of numbers (split by new line).",
		"author":"TrevorDBrown",
		"icon":"abacus",
		"tags":"calculate,stats,calculator,list"
	}
**/

function parseInput(input){
    var rawArray = input.split("\n")
    
    rawArray.forEach(function(number, index, newRawArray){
        newRawArray[index] = parseFloat(number);
    });

    return rawArray.sort((a,b) => a - b);
}

function computeSum(input){
    var listSum = 0.0;
    input.forEach(number => listSum += number);
    return listSum;
}

function computeMean(input){
    listMean = computeSum(input) / input.length;
    return listMean;
}

function computeMedian(input){
    return input[Math.floor(input.length / 2)];
}

function computeMode(input){
    var counts = {};
    var listModes = [];

    input.forEach((number) => {
        counts[number] = counts[number] ? counts[number] + 1 : 1;
    });

    var values = Object.values(counts);
    var maxValue = Math.max(values);

    return listModes;
}

function computeRange(input){
    var listRange = [];
    listRange.push(input[0]);
    listRange.push(input[input.length - 1]);
    return listRange;
}

function main(state) {
	try {
        // Parse the list into a computable set of values.
        var listOfNumbers = parseInput(state.fullText);

        // Compute the stats...
        var listSum = computeSum(listOfNumbers);
        var listMean = computeMean(listOfNumbers);
        var listMedian = computeMedian(listOfNumbers);
        var listMode = computeMode(listOfNumbers);
        var listRange = computeRange(listOfNumbers);

        state.fullText = `${state.fullText}\n-----\nSum: ${listSum}\nMean: ${listMean}\nMedian: ${listMedian}\nMode: ${listMode}\nRange: [${listRange[0]},${listRange[1]}]\n`;
	}
	catch(error) {
        // Post error to Boop/Woop, if something fails.
		state.postError("Failed to compute average.");
        state.fullText = `${state.fullText}\n-----\n${error.message}`;
	}
}