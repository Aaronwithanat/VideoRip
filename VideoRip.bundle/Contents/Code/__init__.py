# Vidrip

from PMS import *



####################################################################################################
def Start():
	MediaContainer.thumb = R("icon-default.png")
	MediaContainer.art = R("art-default.png")
	DirectoryItem.thumb = R("icon-default.png")
	DirectoryItem.art = R("art-default.png")
	
	
####################################################################################################
@handler("/applications/videorip", "VideoRip")
def MainMenu():
	dir = MediaContainer(title1="VideoRip")
	dir.Append(Function(InputDirectoryItem(RunRip, title="Rip Movie", prompt="Name of movie")))
	dir.Append(Function(InputDirectoryItem(RunEp, title="Rip TV Episodes", prompt="Name of TV Series with s0Xe0X format for first episode on disc")))
	dir.Append(Function(InputDirectoryItem(BluRayRip, title="Rip Blu-ray", prompt="Name of movie")))
	dir.Append(Function(DirectoryItem(EjectDisc, title="Eject Disc")))
	dir.Append(PrefsItem(title="Settings"))
	return dir

####################################################################################################
def RunRip(sender, query):

	NOHANDBRAKE="10"
	NOVLC="11"
	NOOUTPUTDIR="12"
	NODVD="13"
	
	hbpreset = Prefs.Get('preset')
	outputpath = Prefs.Get('moviepath')
	natlanguage = Prefs.Get('nativelanguage')
	
	if not outputpath.endswith("/"):
		outputpath = outputpath + "/"
	
	if hbpreset == "Universal":
		ext = ".mp4"
	elif hbpreset == "AppleTV":
		ext = ".mp4"
	elif hbpreset == "Normal":
		ext = ".mp4"
	elif hbpreset == "Classic":
		ext = ".mp4"
	elif hbpreset == "Animation":
		ext = ".mkv"
	elif hbpreset == "Film":
		ext = ".mkv"
	elif hbpreset == "Television":
		ext = ".mkv"
	
	filename = query + ext
	
	hdr = "Error:"
	command = "ripscript.sh"
	returncode = Helper.Run(command, outputpath, filename, Prefs.Get('eject'), Prefs.Get('log'), Prefs.Get('preset'), natlanguage, Prefs.Get('folder'), Prefs.Get('size'), Prefs.Get('twopass'))
	
	if returncode == NOHANDBRAKE:
		returnmsg = "You don't appear to have HandBrakeCLI installed in your Applications folder"
	elif returncode == NOVLC:
		returnmsg = "You don't appear to have VLC installed in your Applications folder"
	elif returncode == NOOUTPUTDIR:
		returnmsg = "Output directory not found - check settings"
	elif returncode == NODVD:
		returnmsg = "No DVD found"
	else: returnmsg = "Something unknown happened"
	
	msgcon = MessageContainer(hdr, returnmsg)	
	return msgcon

####################################################################################################
def RunEp(sender, query):

	NOHANDBRAKE="10"
	NOVLC="11"
	NOOUTPUTDIR="12"
	NODVD="13"
	
	hbpreset = Prefs.Get('preset')
	outputpath = Prefs.Get('tvpath')
	natlanguage = Prefs.Get('nativelanguage')
	
	if not outputpath.endswith("/"):
		outputpath = outputpath + "/"

	if hbpreset == "Universal":
		ext = ".mp4"
	elif hbpreset == "AppleTV":
		ext = ".mp4"
	elif hbpreset == "Normal":
		ext = ".mp4"
	elif hbpreset == "Classic":
		ext = ".mp4"
	elif hbpreset == "Animation":
		ext = ".mkv"
	elif hbpreset == "Film":
		ext = ".mkv"
	elif hbpreset == "Television":
		ext = ".mkv"
	
	filename = query + ext
	
	hdr = "Error:"
	command = "blurayrip.sh"
	returncode = Helper.Run(command, outputpath, filename, Prefs.Get('eject'), Prefs.Get('log'), Prefs.Get('preset'), natlanguage, Prefs.Get('folder'), Prefs.Get('size'), Prefs.Get('twopass'))
	
	if returncode == NOHANDBRAKE:
		returnmsg = "You don't appear to have HandBrakeCLI installed in your Applications folder"
	elif returncode == NOVLC:
		returnmsg = "You don't appear to have VLC installed in your Applications folder"
	elif returncode == NOOUTPUTDIR:
		returnmsg = "Output directory not found - check settings"
	elif returncode == NODVD:
		returnmsg = "No DVD found"
	else: returnmsg = "Something unknown happened"
	
	msgcon = MessageContainer(hdr, returnmsg)	
	return msgcon

####################################################################################################

def BluRayRip(sender, query):

	NOHANDBRAKE="10"
	NOVLC="11"
	NOOUTPUTDIR="12"
	NODVD="13"
	
	outputpath = Prefs.Get('moviepath')
	
	if not outputpath.endswith("/"):
		outputpath = outputpath + "/"	

	hdr = "Error:"
	command = "blurayrip.sh"
	returncode = Helper.Run(command, outputpath, query, Prefs.Get('log'))
	
	if returncode == NOHANDBRAKE:
		returnmsg = "You don't appear to have MakeMKV installed in your Applications folder"
	elif returncode == NOVLC:
		returnmsg = "You don't appear to have VLC installed in your Applications folder"
	elif returncode == NOOUTPUTDIR:
		returnmsg = "Output directory not found - check settings"
	elif returncode == NODVD:
		returnmsg = "No DVD found"
	else: returnmsg = "Something unknown happened"
	
	msgcon = MessageContainer(hdr, returnmsg)	
	return msgcon

####################################################################################################
	
def EjectDisc(sender):

	command = "ejectscript.sh"
	Helper.Run(command)
	return
			
