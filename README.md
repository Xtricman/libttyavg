libttyavg
=========

A python module used to create AVG.

User-defined class  should have its own display method implementation(which must be a generator) to render node content,handle user input and yield Event object(only four types of Event object are suported now).