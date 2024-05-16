/**
	{
		"api":1,
		"name":"Unix to Windows Path Conversion",
		"description":"Formats the provided path as a Windows path.",
		"author":"TrevorDBrown",
		"icon":"quote",
		"tags":"paths,filesystem,windows,unix"
	}
**/

function main(state) {
	try {
        // Use regex and replace function to wrap each entry with single quotes, and a comma is needed, as well as parentheses.
        state.fullText = `${state.fullText.replace(/(\/)/gim, "\\")}`;
	}
	catch(error) {
        // Post error to Boop/Woop, if something fails.
		state.postError("Failed to format path.");
        state.fullText = `${state.fullText}\n${error.message}`;
	}
}