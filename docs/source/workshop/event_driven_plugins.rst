.. event driven plugins (3rd hour)

========================================================
Building Event-Driven Plugins
========================================================

Event Concepts in QGIS
-----------------------

Event-driven design with the Qt library uses the concepts of signals and slots. As mentioned in the second-hour materials, some good places to learn about the concepts of signals and slots are from\  `this PyQt tutorial <http://www.commandprompt.com/community/pyqt/c1267>`_ \and the\  `official Qt docs <http://doc.qt.nokia.com/4.7/signalsandslots.html>`_\. Here we'll flesh out the biggest take-home points.

SIGNALS
********

Qt objects (really any descendent of QObject) has the ability to emit signals. The object emits signals whenever it feels like broadcasting an event of significance. For example, the designers of the\  ``QgsMapCanvas`` \class felt like it's important for a map canvas object to broadcast a QgsPoint when the mouse is hovering over it. The signal\  `xyCoordinates <http://doc.qgis.org/head/classQgsMapCanvas.html#bf90fbd211ea419ded7c934fd289f0ab>`_ \defines this signal. The signal function signature of\  ``xyCoordintes`` \looks like this::

    void QgsMapCanvas::xyCoordinates    (   const QgsPoint &    p    )

We use this signature to define how other objects will connect and interact with this object (as we'll see in the next section). 

In PyQt we can emit an existing signal using a reference to the object that would normally emit that signal. For example, below I have a reference to the map canvas object. I can emit a\  ``xyCoordinates`` \signal::

    self.iface.mapCanvas().emit(SIGNAL("xyCoordinates(const QgsPoint &)"), QgsPoint(-122,45))

SLOTS
*******

Slots are the receivers of signal information. We connect slots to signals using the\  `QObject.connect() function <http://doc.qt.nokia.com/4.7/qobject.html#connect>`_ \. The function arguments are::

    - Sender -- the QObject  object that is responsible for emitting the signal
    - Signal -- the signal function signature passed as a string to the SIGNAL() macro
    - Receiver -- the function that will catch the signal and do something coo
    - Type -- the connection type (this can be left out for our purposes here)

Below is an example of how 


------------------------------------

Examples
----------------

stub



