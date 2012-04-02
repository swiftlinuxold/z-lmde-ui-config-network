#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os

class NetworkWizard:

    def __init__(self):
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) # Create a new window
        self.window.set_title("Network Wizard") # Set the window title
        self.window.set_border_width(20)# Sets the border width of the window.
        self.window.connect("delete_event", self.delete_event) # Click on the X -> close window
        
        # Create vertical box
        self.vbox = gtk.VBox ()
        
        # EACH OPTION GETS ITS OWN HORIZONTAL BOX (wizard_option)
        
        # OPTION 1: ceni
        self.box_image = '/usr/share/icons/hicolor/32x32/apps/ceni.png'
        self.box_label = 'ceni (WiFi and Ethernet)'
        self.box = self.wizard_option (self.box_image, self.box_label, self.ceni)
        self.vbox.add (self.box)
        
        # Option 2: GNOME PPP
        self.box_image = '/usr/share/icons/hicolor/48x48/apps/gnome-ppp.png'
        self.box_label = 'GNOME-PPP (dial-up)'
        self.box = self.wizard_option (self.box_image, self.box_label, self.gnomeppp)
        self.vbox.add (self.box)
        
        # Option 3: Firewall
        self.box_image = '/usr/share/icons/hicolor/48x48/apps/gufw.png'
        self.box_label = 'Firewall'
        self.box = self.wizard_option (self.box_image, self.box_label, self.firewall)
        self.vbox.add (self.box)
        
        # Option 4: Ad Blocker
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/emblems/emblem-noread.png'
        self.box_label = 'Ad Blocker'
        self.box = self.wizard_option (self.box_image, self.box_label, self.adblock)
        self.vbox.add (self.box)
        
        # Show everything
        #self.table.show()
        self.window.add (self.vbox)
        self.window.show ()
        self.window.show_all ()
        
        
        
    # This callback quits the program
    def delete_event (self, widget, event, data=None):
        gtk.main_quit()
        return False
        
    def ceni (self, widget, callback_data=None):
        os.system ('roxterm -e ceniwrapper &')
        
    def gnomeppp (self, widget, callback_data=None):
        os.system ('gnome-ppp &')
        
    def firewall (self, widget, callback_data=None):
        os.system ('gksu gufw &')
    
    def adblock (self, widget, callback_data=None):
        os.system ('gksu /usr/local/bin/block-advert.sh &')
    
    def wizard_option (self, filename_image, string_label, fctn_action):
        # Horizontal box
        self.hbox = gtk.HBox ()
        
        # Button icon
        self.image = gtk.Image ()
        self.image.set_from_file (filename_image)
        self.image.show ()
        
        # Button
        self.button = gtk.Button()
        self.button.set_size_request(64, 64)
        self.button.connect('clicked', fctn_action)
        self.button.add(self.image) # Add image to button
        self.button.show()
        self.hbox.pack_start(self.button, False, False, 0)
        
        # Label
        self.label = gtk.Label (' ' + string_label)
        self.label.set_alignment (0, .5)
        self.label.show ()
        
        self.hbox.pack_start(self.label, False, False, 0)
        self.hbox.show ()
        
        return self.hbox
    
def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    NetworkWizard()
    main()
