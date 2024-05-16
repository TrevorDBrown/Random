import argparse
import json
import typing

class ZDDKVListEntry:
    delay: int
    mediaKeyIndex: int
    mouseKeyIndex: int
    normalKeyIndex: int
    spKeyList: typing.List[int]

    def __init__ (self, delay: int, mediaKeyIndex: int, mouseKeyIndex: int, normalKeyIndex: int, spKeyList: typing.List[int]):
        self.delay = delay
        self.mediaKeyIndex = mediaKeyIndex
        self.mouseKeyIndex = mouseKeyIndex
        self.normalKeyIndex = normalKeyIndex
        self.spKeyList = spKeyList
    
    def __str__ (self):
        formattedString: str = ""

        formattedString = "{\"delay\": %i, \"media_key_index\": %i, \"mouse_key_index\": %i, \"normal_key_index\": %i, \"sp_key_list\": [" % (self.delay, self.mediaKeyIndex, self.mouseKeyIndex, self.normalKeyIndex)

        for i, spKey in enumerate(self.spKeyList): 
            formattedString += "%i" % (spKey)

            if (i + 1 < len(self.spKeyList)):
                formattedString += ","
        
        formattedString += "]}"

        return formattedString

class ZDDKeyEntryKVList:
    zddkvListEntries: typing.List[ZDDKVListEntry]

    def __init__ (self, sourceString: str):
        if (len(sourceString) <= 0):
            self.zddkvListEntries = []
            self.zddkvListEntries.append(ZDDKVListEntry(0, 0, 0, 0, [0]))
            return

        self.zddkvListEntries = []
        
        for i, character in enumerate(sourceString):
            normalKeyIndex: int
            spKeyList: typing.List[int]

            normalKeyIndex, spKeyList = keymapLookup(character)

            if (normalKeyIndex < 0):
                print("Error - key \"%s\" not found. Skipping..." % (character))
                continue

            self.zddkvListEntries.append(ZDDKVListEntry(0, 0, 0, normalKeyIndex, spKeyList))
        
        return

    def __str__ (self):
        formattedString: str = ""

        formattedString = "["

        for i, kddkvListEntry in enumerate(self.zddkvListEntries):
            formattedString += "%s" % (str(kddkvListEntry))

            if (i + 1 < len(self.zddkvListEntries)):
                formattedString += ","
        
        formattedString += "]"

        return formattedString

class ZDDKeyEntry:
    isMacro: bool
    isMedia: bool
    isMouse: bool
    zddkvList: ZDDKeyEntryKVList
    name: str

    def __init__ (self, name: str, macro: bool, media: bool, mouse: bool, sourceString: str):
        self.name = name
        self.isMacro = macro
        self.isMedia = media
        self.isMouse = mouse
        self.zddkvList = ZDDKeyEntryKVList(sourceString)

        return
    
    def __str__ (self):
        formattedString: str = ""

        formattedString = "{\"is_macro\": %s, \"is_media\": %s, \"is_mouse\": %s, \"kv_list\": %s, \"name\": \"%s\"}" % (str(self.isMacro).lower(), str(self.isMedia).lower(), str(self.isMouse).lower(), str(self.zddkvList), self.name)

        return formattedString

class ZDDCKList:
    keyEntries: typing.List[ZDDKeyEntry]

    def __init__ (self):
        self.keyEntries = []
        return
    
    def __str__ (self):
        formattedString: str = ""

        formattedString = "["

        for i, keyEntry in enumerate(self.keyEntries):
            formattedString += str(keyEntry)

            if (i + 1 < len(self.keyEntries)):
                formattedString += ","
            
        formattedString += "]"

        return formattedString

    def add_kddcklist_entry(self, keyName: str, sourceString: str):
        # If keyData is empty, then create a default key.
        if (len(sourceString) <= 0):
            self.keyEntries.append(ZDDKeyEntry(keyName, False, False, False, sourceString))
            return

        self.keyEntries.append(ZDDKeyEntry(keyName, True, False, False, sourceString))
        return

class ZDDConfig:
    zddckList: ZDDCKList
    keynum: int
    name: str
    pid: int
    vid: int

    def __init__ (self):
        self.zddckList: ZDDCKList = ZDDCKList()
        self.keynum = 10
        self.name = "Test"
        self.pid = 8217
        self.vid = 20785

        return

    def __str__ (self):
        formattedString: str = ""

        formattedString = "{\"ck_list\": %s, \"keynum\": %i, \"name\": \"%s\", \"pid\": %i, \"vid\": %i}" % (str(self.zddckList), self.keynum, self.name, self.pid, self.vid)

        return formattedString
        
    def add_kddcklist(self, keyName: str, sourceString: str):
        self.zddckList.add_kddcklist_entry(keyName, sourceString)
        return

def populateKeymap() -> None:
    keymapFile: str = "Keymap.json"

    global keymapData
    keymapData = {}

    with open(keymapFile) as f:
        keymapData = json.load(f)

def keymapLookup(keyToFind: str) -> tuple[int, typing.List[int]]:
    normalKeyIndex: int = -1
    spKeyList: typing.List[int] = []

    for i, keymapEntry in enumerate(keymapData["keys"]):
        if (keymapEntry["key"] == keyToFind):
            normalKeyIndex = keymapEntry["index"]

            if (len(keymapEntry["modifiers"]) > 0):
                for j, modifierKeyMapEntry in enumerate(keymapEntry["modifiers"]):
                    spKeyIndex: int
                    spKeyListList: typing.List[int]
                    
                    spKeyIndex, spKeyListList = keymapLookup(modifierKeyMapEntry)

                    spKeyList.append(spKeyIndex)
            
            return normalKeyIndex, spKeyList

    return normalKeyIndex, spKeyList

def convertStringsToConfigFile(sourceStrings: typing.List[str]) -> ZDDConfig:
    
    # Create the new instance of ZDDConfig
    configContent: ZDDConfig = ZDDConfig()
    
    for i, sourceString in enumerate(sourceStrings):
        currentKeyName: str = "KEY%i" % (i + 1)
        configContent.add_kddcklist(currentKeyName, sourceString)

    return configContent

def main() -> None:
    # Parse command line arguments
    parser = argparse.ArgumentParser("strings-to-zdd.py",
                                     "Generates a ZDD file from a collection of strings for use with CustomKeyboard.")
    
    # Prepare the arguments for parsing
    parser.add_argument("-o", "--output-file")
    parser.add_argument("-k1", "--key1")
    parser.add_argument("-k2", "--key2")
    parser.add_argument("-k3", "--key3")
    parser.add_argument("-k4", "--key4")
    parser.add_argument("-k5", "--key5")
    parser.add_argument("-k6", "--key6")
    parser.add_argument("-k7", "--key7")
    parser.add_argument("-k8", "--key8")
    parser.add_argument("-k9", "--key9")
    parser.add_argument("-k10", "--key10")

    # Parse the arguments
    args = parser.parse_args()

    # Populate the keymap
    populateKeymap()

    # Specified output filename, or default to "Output.zdd"
    outputFilename = args.output_file or "Output.zdd"

    # Define the list of source strings (if null, store a blank string)
    sourceStrings = [
        args.key1 or "",
        args.key2 or "",
        args.key3 or "",
        args.key4 or "",
        args.key5 or "",
        args.key6 or "",
        args.key7 or "",
        args.key8 or "",
        args.key9 or "",
        args.key10 or ""
    ]

    # Generate the config file.
    configContent: ZDDConfig = convertStringsToConfigFile(sourceStrings)

    # Store the generated config file.
    configContentJson = json.loads(str(configContent))

    with open(outputFilename, "w") as f:
        json.dump(configContentJson, f, indent=4, ensure_ascii=False)

main()