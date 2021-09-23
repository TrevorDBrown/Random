/**
	{
		"api":1,
		"name":"Generate GUID",
		"description":"Generates and returns a valid GUID.",
		"author":"TrevorDBrown",
		"icon":"dice",
		"tags":"guid,uuid,id"
	}
**/

// updatePositionFromAlphabet - replaces specific character within specified GUID string from a character in the provided alphabet.
function updatePositionFromAlphabet(guid, position, alphabet){
    // If the position specified is out of bounds, return the GUID as is.
    if (position >= guid.length || position < 0) {
        return guid;
    }

    // TODO: replace Math.random with better RNG in the future.
    replacement = alphabet.substr(Math.floor(Math.random() * alphabet.length), 1);
 
    // Return the GUID string with the replaced character.
    return guid.substring(0, position) + replacement + guid.substring(position + 1);
    
}

// generateGUID - returns a valid RFC4122 version 4-compliant GUID.
// Based on: https://stackoverflow.com/a/105074/5931861
function generateGUID(){
    /*
    *   Return format: xxxxxxxx-xxxx-mxxx-nxxx-xxxxxxxxxxxx
    *      x: 0-9,A-F
    *      M: 1-5
    *      N: 8,9,A,B
    */

    var xAlphabet = "0123456789abcdef";                     // Valid characters for "x" positions.
    var mAlphabet = "12345";                                // Valid characters for "m" positions.
    var nAlphabet = "89ab"                                  // Valid characters for "n" positions.
    var guid = "xxxxxxxx-xxxx-mxxx-nxxx-xxxxxxxxxxxx";      // GUID structured with x, m, and n positions.

    // Loop through GUID positions. Use alphabet respective to the current character.
    // Replace the current character with a random character from the respective alphabet.
    for (var position = 0; position < guid.length; position++){
        switch (guid.charAt(position)){
            case 'x':
                guid = updatePositionFromAlphabet(guid, position, xAlphabet);
                break;
            case 'm':
                guid = updatePositionFromAlphabet(guid, position, mAlphabet);
                break;
            case 'n':
                guid = updatePositionFromAlphabet(guid, position, nAlphabet);
                break;
        }
    }

    // Return the generated GUID with a trailing new line (mostly for multiple generations of GUIDs)
    return guid + "\n";
}

function main(state) {
	try {
        var numberOfGUIDs = state.fullText || 1;    // Always generate at least one GUID.
        var output = "";                            // Store output, regardless of number of GUIDs generated.

        // Generate the specified number of GUIDs
        for (var i = 0; i < numberOfGUIDs; i++){
            output += generateGUID();
        }

        // Store the generated GUIDs back to the state for Boop/Woop.
        state.fullText = output;
	}
	catch(error) {
        // Post error to Boop/Woop, if something fails.
		state.postError("Failed to generate GUID(s).")
	}
}