#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gobject
import dbus
from dbus import glib

gobject.threads_init()

glib.init_threads()

# Create a session bus.
bus = dbus.SessionBus()

remote_object = bus.get_object("org.kde.kstars", "/KStars/Ekos/DustCap")

# first lets get the status if we are unparked no need to do anything
iface = dbus.Interface(remote_object, 'org.freedesktop.DBus.Properties')
properties = iface.GetAll('org.kde.kstars.Ekos.DustCap')
iface = dbus.Interface(remote_object, 'org.kde.kstars.Ekos.DustCap')
if properties['status'] != 0:
    # we are not unparked
    # make sure the light is off
    res = iface.setLightEnabled(False)
    # print("light off {}".format(res))
    # unpark the cap
    res = iface.unpark()
    # print("unparked {}".format(res))
#else:
    # we are parked lets make sure the light is off, This is illegal
    # res = iface.setLightEnabled(False)
    # print("light off {}".format(res))
