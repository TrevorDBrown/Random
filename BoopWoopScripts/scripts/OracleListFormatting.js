/**
	{
		"api":1,
		"name":"Format for Oracle IN Clause",
		"description":"Wraps list items in single quotes for use in Oracle SQL queries.",
		"author":"TrevorDBrown",
		"icon":"quote",
		"tags":"oracle,database,sql,plsql,select,where,in"
	}
**/

function main(state) {
	try {
        // Use regex and replace function to wrap each entry with single quotes, and a comma is needed, as well as parentheses.
        state.fullText = `(${state.fullText.replace(/([a-z0-9]+)$[\n|\r]+(?=[a-z0-9]+)/gim, "'$1',\n").replace(/([a-z0-9]+)$[\n|\r]*(?![a-z0-9]+)/gim, "'$1'")})`;
	}
	catch(error) {
        // Post error to Boop/Woop, if something fails.
		state.postError("Failed to format list.");
        state.fullText = `${state.fullText}\n${error.message}`;
	}
}