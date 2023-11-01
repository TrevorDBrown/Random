const vscode = require('vscode');

/**
 * Macro configuration settings
 * { [name: string]: {              ... Name of the macro
 *    no: number,                   ... Order of the macro
 *    func: ()=> string | undefined ... Name of the body of the macro function
 *  }
 * }
 */
module.exports.macroCommands = {
  PrettifyASN: {
    no: 1,
    func: prettifyASN,
  },
};

async function prettifyASN() {
  const editor = vscode.window.activeTextEditor;

  if (!editor) {
    // Return an error message if necessary.
    return 'Active text editor not found.';
  }
  const document = editor.document;
  document.replace("~", "\n");
}