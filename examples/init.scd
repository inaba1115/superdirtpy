SuperDirt.start;

MIDIClient.init;
~midiOut = MIDIOut.newByName("IAC Driver", "Bus 1");
~dirt.soundLibrary.addMIDI(\mydevice, ~midiOut);

OSCFunc.trace(true);
OSCFunc.trace(false);
