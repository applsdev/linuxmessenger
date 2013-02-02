from PyQt4 import QtCore

import network
import settings
import browser

class External(QtCore.QObject):

  def __init__(self, browserWindow):
    QtCore.QObject.__init__(self)
    self._browserWindow = browserWindow

  @QtCore.pyqtSlot(str, str)
  def arbiterInformSerialized(self, name, payload):
    print("arbiterInformSerialized({0}, ...)".format(name))

  @QtCore.pyqtSlot()
  def captureMouseWheel(self):
    print("captureMouseWheel")

  @QtCore.pyqtSlot()
  def clearHeartBeat(self):
    print("clearHeartBeat")

  @QtCore.pyqtSlot(str, str, result=int)
  def asyncConfirm(self, message, caption):
    print("asyncConfirm({0}, {1})".format(message, caption))
    print("returning 0")
    return 0

  @QtCore.pyqtSlot(str)
  def debugLog(self, text):
    print("debugLog({0})".format(text))

  @QtCore.pyqtSlot(result=str)
  def getAccessToken(self):
    print("getAccessToken()")
    token = settings.get_setting("AccessToken")
    print("returning '{0}'".format(token))
    return token

  @QtCore.pyqtSlot(str, result=bool)
  def getCapability(self, capabilityName):
    print("getCapability({0})".format(capabilityName))
    print("returning False")
    return False

  @QtCore.pyqtSlot(str, result=str)
  def getSetting(self, key):
    print("getSetting({0})".format(key))
    val = settings.get_setting(key)
    print("returning '{0}'".format(val))
    return val

  @QtCore.pyqtSlot(result=str)
  def getStateBlob(self):
    print("getStateBlob()")
    print("returning ''")
    return ''

  @QtCore.pyqtSlot(str, result=str)
  def getValue(self, key):
    print("getValue({0})".format(key))
    val = settings.get_value(key)
    print("returning '{0}'".format(val))
    return val

  @QtCore.pyqtSlot(result=str)
  def getVersion(self):
    print("getVersion")
    print("returning ''")
    return ''

  @QtCore.pyqtSlot(result=bool)
  def hasAccessToken(self):
    print("hasAccessToken()")
    ret = settings.get_setting("AccessToken") != ""
    print("returning " + str(ret))
    return ret

  @QtCore.pyqtSlot()
  def heartBeat(self):
    print("heartBeat()")

  @QtCore.pyqtSlot()
  def invalidateAccessToken(self):
    print("invalidateAccessToken()")
    settings.set_setting("AccessToken", "")
    settings.set_setting("UserId", "")
    browser.BrowserWindow.refresh_all()

  @QtCore.pyqtSlot(result=bool)
  def isIdle(self):
    print("isIdle()")
    print("returning False")
    return False

  @QtCore.pyqtSlot(result=bool)
  def isMqttConnected(self):
    print("isMqttConnected()")
    print("returning False")
    return False

  @QtCore.pyqtSlot(result=bool)
  def isToastVisible(self):
    print("isToastVisible()")
    print("returning False")
    return False

  @QtCore.pyqtSlot(str, str)
  def logEvent(self, name, payload):
    print("logEvent({0}, {1})".format(name, payload))

  @QtCore.pyqtSlot(str, str, str)
  def logEvent2(self, category, name, payload):
    print("logEvent2({0}, {1}, {2})".format(category, name, payload))

  @QtCore.pyqtSlot(str)
  def mqttSubscribe(self, topic):
    print("mqttSubscribe({0})".format(topic))

  @QtCore.pyqtSlot(str)
  def navigateBrowserToUrl(self, url):
    print("navigateBrowserToUrl({0})".format(url))

  @QtCore.pyqtSlot(str)
  def navigateWindowToUrl(self, url):
    print("navigateWindowToUrl({0})".format(url))
    self._browserWindow.navigate(url)

  @QtCore.pyqtSlot(str, str, str, str)
  def postWebRequest(self, url, callback, method, postData):
    print("postWebRequest({0}, {1}, {2}, {3})".format(
        url, callback, method, postData))
    def _callback(reply):
      self._browserWindow.callJSFunction(callback, reply)
    network.async_request(url, _callback, method, postData)

  @QtCore.pyqtSlot()
  def recycle(self):
    print("recycle()")

  @QtCore.pyqtSlot()
  def releaseMouseWheel(self):
    print("releaseMouseWheel()")

  @QtCore.pyqtSlot(str, str)
  def setAccessToken(self, uid, token):
    print("setAccessToken({0}, {1})".format(uid, token))
    if token != settings.get_setting("AccessToken"):
      settings.set_setting("AccessToken", token)
      settings.set_setting("UserId", uid)
      browser.BrowserWindow.refresh_all()

  @QtCore.pyqtSlot(str)
  def setArbiterInformCallback(self, callback):
    print("setArbiterInformCallback({0})".format(callback))
    settings.set_setting("ArbiterInformCallback", callback)

  @QtCore.pyqtSlot(int)
  def setIcon(self, icon_id):
    print("setIcon({0})".format(icon_id))

  @QtCore.pyqtSlot(str, str)
  def setSetting(self, key, value):
    print("setSetting({0}, {1})".format(key, value))
    settings.set_setting(key, value)

  @QtCore.pyqtSlot(str, str)
  def setValue(self, key, value):
    print("setValue({0}, {1})".format(key, value))
    settings.set_value(key, value)

  @QtCore.pyqtSlot()
  def showChatDevTools(self):
    print("showChatDevTools()")

  @QtCore.pyqtSlot()
  def showDevTools(self):
    print("showDevTools()")

  @QtCore.pyqtSlot()
  def showSidebarDevTools(self):
    print("showSidebarDevTools()")

  @QtCore.pyqtSlot()
  def showToastDevTools(self):
    print("showToastDevTools()")

  @QtCore.pyqtSlot()
  def showFlyoutDevTools(self):
    print("showFlyoutDevTools()")

  @QtCore.pyqtSlot()
  def showDialogDevTools(self):
    print("showDialogDevTools()")

  @QtCore.pyqtSlot(str, str)
  def showTickerFlyout(self, url, storyYPos):
    print("showTickerFlyout({0}, {1})".format(url, storyYPos))

  @QtCore.pyqtSlot()
  def hideTickerFlyout(self):
    print("hideTickerFlyout()")

  @QtCore.pyqtSlot()
  def showDialog(self):
    print("showDialog()")

  @QtCore.pyqtSlot()
  def hideDialog(self):
    print("hideDialog()")