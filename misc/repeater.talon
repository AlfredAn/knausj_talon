mode: command
mode: user.opus
-
<number_small> times: core.repeat_command(number_small-1)
^<number_small> more: core.repeat_command(number_small)
dupe: core.repeat_command(1)
trip: core.repeat_command(2)
quad: core.repeat_command(3)
quint: core.repeat_command(4)

all <number_small> times: core.repeat_partial_phrase(number_small-1)
^all <number_small> more: core.repeat_partial_phrase(number_small)
all dupe: core.repeat_partial_phrase(1)
all trip: core.repeat_partial_phrase(2)
all quad: core.repeat_partial_phrase(3)
all quint: core.repeat_partial_phrase(4)
