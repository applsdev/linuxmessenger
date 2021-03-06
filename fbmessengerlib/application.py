# Python2 defaults to PyQt4's API level 1, but Python3
# defaults to level 2, which is what we want. For
# compatibility, we have to explicitly ask for level 2.
import sip
for module in ("QString", "QUrl"):
  sip.setapi(module, 2)

import sys
import signal
import os.path
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.phonon import Phonon

def init():
  global _app
  _app = QtGui.QApplication(sys.argv)
  # Needs to be set for media below
  _app.setApplicationName("fbmessenger")

  # These can't be local variables during play or they'll get GC'd.
  global _pling_media, _pling_audio, _pling_source
  _pling_media = Phonon.MediaObject()
  _pling_audio = Phonon.AudioOutput(Phonon.MusicCategory)
  Phonon.createPath(_pling_media, _pling_audio)
  _pling_source = Phonon.MediaSource(resource_path("pling.wav"))
  _pling_media.setCurrentSource(_pling_source)

  # Handle Qt's debug output
  QtCore.qInstallMsgHandler(handle_qt_debug_message)

  # Enable quitting with ctrl-c
  signal.signal(signal.SIGINT, signal.SIG_DFL)

def get_desktop_rectangle():
  g = _app.desktop().availableGeometry()
  return (g.x(), g.y(), g.width(), g.height())

def handle_qt_debug_message(level, message):
  print("Qt debug:", message.decode('utf-8'))

def main_loop():
  sys.exit(_app.exec_())

def resource_path(resource_name):
  this_module = sys.modules[__name__]
  module_dir = os.path.dirname(this_module.__file__)
  return os.path.join(module_dir, "resources", resource_name)

def play_message_sound():
  _pling_media.stop()
  _pling_media.play()

def quit():
  _app.quit()
