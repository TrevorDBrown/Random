/**
	{
		"api":1,
		"name":"Longest Line",
		"description":"Finds the longest line in the list and its length.",
		"author":"TrevorDBrown",
		"icon":"abacus",
		"tags":"length,count,line"
	}
**/

function main(state) {
	try {
        // Use regex and replace function to wrap each entry with single quotes, and a comma is needed, as well as parentheses.
        var lines = state.fullText.split("\n")
        var longestLine = ""
        var longestLength = 0

        lines.forEach(line => {
            if (line.length > longestLength){
                longestLine = line
                longestLength = line.length
            }
        });

        state.fullText = `${state.fullText}\n-----\nLongest Line: ${longestLine}\nLength: ${longestLength}`

	}
	catch(error) {
        // Post error to Boop/Woop, if something fails.
		state.postError("Failed to determine longest line.");
        state.fullText = `${state.fullText}\n-----\n${error.message}`;
	}
}