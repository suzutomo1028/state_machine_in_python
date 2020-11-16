# -*- coding: utf-8 -*-

from transitions import Machine

class Led:
  """ The LED control with state machine. """

  # The transition table of the state machine.
  #
  # +---------------+-----------------+-----------------+
  # |               | state='off'     | state='on'      |
  # +---------------+-----------------+-----------------+
  # | trigger='off' | (nop)           | -> state='off'  |
  # +---------------+-----------------+-----------------+
  # | trigger='on'  | -> state='on'   | (nop)           |
  # +---------------+-----------------+-----------------+

  def __init__(self) -> None:
    """ The constractor of the class. """

    self.__states = ['off', 'on']
    self.__machine = Machine(model=self, states=self.__states, initial=self.__states[0],
                             auto_transitions=False, ordered_transitions=False,
                             ignore_invalid_triggers=True)
    self.__machine.add_transition(trigger='off', source='on',  dest='off', before='_turn_off')
    self.__machine.add_transition(trigger='on',  source='off', dest='on',  before='_turn_on')
    self._turn_off()

  def _turn_off(self) -> None:
    """ Turn off the LED. """

    print('Turn off the LED.')

  def _turn_on(self) -> None:
    """ Turn on the LED. """

    print('Turn on the LED.')


""" Exsample code. """

led = Led()                   # Turn off the LED.
print('state =', led.state)   # state = off

led.on()                      # Turn on the LED.
print('state =', led.state)   # state = on

led.off()                     # Tuen off the LED.
print('state =', led.state)   # state = off

led.off()                     # Nothing is displayed.
print('state =', led.state)   # state = off
