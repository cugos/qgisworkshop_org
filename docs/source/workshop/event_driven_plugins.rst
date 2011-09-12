.. event driven plugins (3rd hour)

========================================================
Building Event-Driven Plugins
========================================================

Event Concepts in QGIS
-----------------------

Event-driven design with the Qt library uses the concepts of signals and slots. As mentioned in the second-hour materials, some good places to learn about the concepts of signals and slots are from\  `this PyQt tutorial <http://www.commandprompt.com/community/pyqt/c1267>`_ \and the\  `official Qt docs <http://doc.qt.nokia.com/4.7/signalsandslots.html>`_\. Here we'll flesh out the biggest take-home points.

SIGNALS
********

Qt objects (any descendent of QObject) has the ability to emit signals. The object emits signals whenever it feels like broadcasting an event of significance. For example, the designers of the\  ``QgsMapCanvas`` \class felt like it's important for a map canvas object to broadcast a QgsPoint when the mouse is hovering over it. The signal\  `xyCoordinates <http://doc.qgis.org/head/classQgsMapCanvas.html#bf90fbd211ea419ded7c934fd289f0ab>`_ \defines this signal. The signal function signature of\  ``xyCoordintes`` \looks like this::

    void QgsMapCanvas::xyCoordinates    (   const QgsPoint &    p    )

We use this signature to define how other objects will connect and interact with this object (as we'll see in the next section). 

In PyQt we can emit an existing signal using a reference to the object that normally emits that signal. For example, below I have a reference to the map canvas object. I can emit a\  ``xyCoordinates`` \signal::

    self.iface.mapCanvas().emit(SIGNAL("xyCoordinates(const QgsPoint &)"), QgsPoint(-122,45))

SLOTS
*******

Slots are the receivers of signal information. We connect slots to signals using the\  `QObject.connect() function <http://doc.qt.nokia.com/4.7/qobject.html#connect>`_ \. The function arguments are::

    - Sender -- the QObject object that is responsible for emitting the signal
    - Signal -- the signal function signature passed as a string to the SIGNAL() macro
    - Receiver -- the function that will catch the signal and do something coo
    - Type -- the connection type (this can be left out for our purposes here)

If I had a function called\  ``listen_xyCoordinates`` \that I wanted to recieve information from the\  ``xyCoordinates`` \signal when it fires then I can make a connection like this::

    # notice that we are only passing the first three arguments here (sender, signal receiver)
    QObject.connect(self.iface.mapCanvas(), SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xyCoordinates)

The slot function that connects to a signal has to accept the same arugments the signal signature passing. In the case of the signal\  ``xyCoordinates`` \that means our custom function should be able to accept a QgsPoint. Here is that function::

    def listen_xyCoordinates(self,point):
        self.dlg.outputTextEdit.append("xyCoordinates - %d,%d" % (point.x() if point else "",point.y() if point else ""))


Create Custom SIGNALS
************************

Though slightly more confusing, developers do have the ability to create custom signals. Below is an example of how to create a custom signal and connect a slot to it. The example below is taken from the workshop example\  ``foss4g2011_example3_solution`` \plugin:


\  **1.** \Make sure your plugin class subclasses QObject. It also should call the QObject constructor under\  ``__init__`` \as shown below:: 

    class foss4g2011_example3_solution(QObject):

        def __init__(self, iface):
            QObject.__init__(self)
            # Save reference to the QGIS interface
            self.iface = iface

\  **2.** \Create a custom function that will define your signal signature. It doesn't even have to do anything useful (though it would be nice if it did)::

        def feedbackStatus(self):
            # do some really cool analysis and feedback....or
            print "I don't do anything useful - Yah!"

\  **3.** \Create a slot that will recieve this signal. Notice that it is accepting a parameter\  ``message`` \that wasn't defined in the signal (interesting)::

     def listen_feedbackStatus(self, message):
            self.dlg.outputTextEdit.append("feedbackStatus - %s" % (message if message else ""))

\  **4.** \Now connect your slot to your signal somewhere in your code::

    QObject.connect(self, SIGNAL("feedbackStatus(PyQt_PyObject)"), self.listen_feedbackStatus) 

\  **5.** \Now anywhere in your plugin (because it subclasses QObject) you can emit this signal if you think it is important and pass a message to your slot. The\  ``foss4g2011_example3_solution`` \plugin is doing this on a button click::

     def btn_emitFeedbackStatus(self, checked):
           self.emit(SIGNAL("feedbackStatus(PyQt_PyObject)"), "Bruce Lee is my hero!")



