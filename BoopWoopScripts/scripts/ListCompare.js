/**
	{
		"api":1,
		"name":"Compare Lists",
		"description":"Determines the XOR of two lists.",
		"author":"TrevorDBrown",
		"icon":"quote",
		"tags":"oracle,database,sql,plsql,select,where,in"
	}
**/

function main(state) {
	try {
        // Use regex and replace function to wrap each entry with single quotes, and a comma is needed, as well as parentheses.
        var lists = `${state.fullText}`.split("[List]");

        // state.fullText = String(lists.length);

        console.log(String(lists.length));

        // lists.forEach(function(list){
        //     state.fullText = state.fullText + list;
        // });
	}
	catch(error) {
        // Post error to Boop/Woop, if something fails.
		state.postError("Failed to format list.");
        state.fullText = `${state.fullText}\n${error.message}`;
	}
}