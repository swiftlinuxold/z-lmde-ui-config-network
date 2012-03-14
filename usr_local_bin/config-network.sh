#!/bin/bash 
# This is the script for the Network Wizard
# Command for executing this script: config-network.sh (NOT "sh config-network.sh")

export ConfigNetwork=$(cat <<End_of_Text

<window title="`gettext $"Network Wizard"`" window-position="1">

<vbox>
  <frame>
  <hbox>
	<vbox>
	  <frame>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/gTangish-2.0a1/32x32/status/connect_creating.png"</input>
		<action>roxterm -e ceniwrapper &</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"`gettext $"ceni"`"</label></text>
      </hbox>
      </frame>
      <frame>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/gTangish-2.0a1/32x32/devices/network-wired.png"</input>
		<action>gnome-ppp &</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"`gettext $"GNOME-PPP"`"</label></text>
	  </hbox>
	  </frame>
	</vbox>

	<vbox>
	  <frame>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/gTangish-2.0a1/32x32/apps/firewall.png"</input>
		<action>gksu gufw &</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"`gettext $"Firewall"`"</label></text>
      </hbox>
      </frame>
      <frame>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/gTangish-2.0a1/32x32/emblems/emblem-noread.png"</input>
		<action>block-advert.sh</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"`gettext $"Update Ad Blocker"`"</label></text>
	  </hbox>
	  </frame>
	</vbox>
  </hbox>
  </frame>
		
  <hbox>
	<button>
	  <label>"`gettext $"Close"`"</label>
	  <input file>"/usr/share/icons/gTangish-2.0a1/16x16/actions/dialog-cancel.png"</input>
	  <action>EXIT:close</action>
	</button>
  </hbox>
</vbox>
  
</window>
End_of_Text
)

gtkdialog -c --program=ConfigNetwork
unset ConfigNetwork
