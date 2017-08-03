# UppercaseClipboard.ps1
# ©2017 Trevor D. Brown.
# Use: retrieves text from clipboard, converts it to all uppercase, and stores the changed value back into the clipboard.

#Clears all current content on screen.
clear 

# Title Text
echo "UppercaseClipboard"
echo "By Trevor D. Brown `n"

# Gets the clipboard content.
$in = Get-Clipboard

# Display provided text.
echo "Current Text: $in"

#Display convert text, and convert to uppercase.
echo "Converting text to all uppercase..."
$in = $in.ToUpper()
echo "Done! `n"

echo "Uppercased Text: $in"

echo "Copying to clipboard... `n"
Set-Clipboard -Value $in

echo "Done! `n"

echo "Process complete!"