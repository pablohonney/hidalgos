from abc import ABC, abstractmethod


class ZigzagHandler(ABC):
    @abstractmethod
    def __call__(self, start, end):
        raise NotImplementedError

    @abstractmethod
    def get_results(self):
        raise NotImplementedError


class LongestRunHandler(ZigzagHandler):
    """
    Keep the longest run
    """

    def __init__(self):
        self.max_start = 0
        self.max_length = 0

    def __call__(self, start, end):
        length = (end + 1) - start
        if length > self.max_length:
            self.max_length = length
            self.max_start = start

    def get_results(self):
        return self.max_start, self.max_start + self.max_length


class AllRunsHandler(ZigzagHandler):
    """
    Keep all runs
    """

    def __init__(self):
        self.runs = []

    def __call__(self, start, end):
        length = (end + 1) - start
        self.runs.append((start, start + length))

    def get_results(self):
        return self.runs


def zigzags(sequence, handler):
    """
    Feed handler with zigzag runs

    :param sequence:
    :param handler:
    :return: handler.get_results()

    ------------------------------------

    FSM notes.

    2x2 states:
        in zigzag run:
            true
            false
        growing:
            true
            false

    state transitions:

                                direction
                    change                   same
                --------------------------------------------
        z       |
        i in    |   keep running            end the run,
        g       |                           call the handler
        z       |
        a out   |   start a new run         keep running
        g       |

    ------------------------------------

    performance.

    time  O(n)
    space O(1) + space(handler)
    """

    # guard.
    if len(sequence) < 3:
        return handler.get_results()

    cur_start = 0
    in_a_zigzag = False

    # suppose no equals in a row. only ups and downs.
    state = sequence[0] < sequence[1]

    for index in range(1, len(sequence) - 1):
        new_state = sequence[index] < sequence[index + 1]
        if state == new_state:
            if in_a_zigzag:
                in_a_zigzag = False
                handler(cur_start, index)
            else:
                # continue the slope
                pass
        else:
            if in_a_zigzag:
                # continue the run
                pass
            else:
                # start a new run
                in_a_zigzag = True
                cur_start = index - 1
            state = new_state

    if in_a_zigzag:
        handler(cur_start, len(sequence) - 1)

    return handler.get_results()
