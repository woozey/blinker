# MIT License

# Copyright (c) 2022 blinker developers

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import itertools

class Blinker:
    
    def __init__(self, period, number, duration):
        self._period = period
        self._number = number
        self._duration = duration
    

    def start(self):
        self.setup()
    
    @property
    def period(self):
        return self._period
    
    @period.setter
    def period(self, new_period):
        self._period = new_period
        self.setup()

    @property
    def number(self):
        return self._number
    
    @number.setter
    def period(self, new_number):
        self._number = new_number
        self.setup()
        
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, new_duration):
        self._duration = new_duration
        self.setup()


    def connect_toggle(self, f):
        self.toggle = f
        

    def connect_reset(self, f):
        self._reset = f
        

    def connect_diff(self, f):
        self.diff = f
    
    
    def next_cycle(self):
        self.toggle()
        self.cur_state = next(self.cycle)
        self.start_time = self.now()
        
        
    def reset(self):
        self._reset()
        self.cycle = itertools.cycle(self.sequence)
        
        
    def connect_now(self, f):
        self.now = f
        

    def setup(self):
#         self.sequence = [T_BLINK for i in range(self.number*2 - 1)] + [T_WAIT]
        self.sequence = [self._duration for i in range(self._number*2 - 1)] + [self._period]
        self.reset()
        self.next_cycle()
        
    
    def run(self):
        if self.diff(self.now(), self.start_time) > self.cur_state:
            self.next_cycle()
    