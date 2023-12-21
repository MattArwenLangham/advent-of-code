#flip flop modules, start off. When a low pulse is recieved it flips between on/off, which flips the pulse type. High pulses pass through
#conjunction is multi-input. Remembers input from connected modules. If all are high, sends low. Otherwise sends high.
#broadcaster just passes through pulse.
#Pulses must finish passing before running again.
#Pulses are processed in the order they are sent. If a pulse is sent to a, b and c. a is processed, then b (regardless of where a is sent after)
#Figure out where it loops and then find the remainder from 1000

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().split("\n")

class FlipFlop:
    flip_pulse = False

    def __init__(self, input, outputs):
        self.input = input
        self.outputs = outputs
    
    def process_pulse(self, pulse):
        if pulse == 'low':
            if flip_pulse: flip_pulse = False
            else: flip_pulse = True
        
        if flip_pulse:
            if pulse == 'low': return 'high'
            else: return 'low'
        else: return pulse

class Conjuction:
    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output
        self.input_memory = {}
        for input in inputs:
            self.input_memory[input] = 'low'
    
    def process_pulse(self, input, pulse):
        self.input_memory[input] = pulse
    
        if all(self.input_memory.values() == 'high'):
            return 'low'
        else:
            return 'high'

class Broadcast:

    def __init__(self, name, output):
        self.name = name
        self.output = output
    
    def process_pulse(self):
        return 'low'

component_dict = {

}

def connect_components(raw_instructions):

    print(raw_instructions)
    if 'broadcaster':
        broadcaster = Broadcast('broadcaster', ['a'])
        component_dict[broadcaster.name] = broadcaster

raw_instructions = read_input("test_input.txt")
connect_components(raw_instructions)
print(component_dict)
#print(result)