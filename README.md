# discord-ai-bot
A Discord bot using discord.py and textgenrnn to respond to queries.

## Requirements

 Python<3.8, textgenrnn, and discord.py>1.3
 
 A file containing training data separated by newlines (optionally, include queries/responses in a `query : response` format on each line)
 
 ## Usage

To train the AI, first open a Python shell

```py
> from textgenrnn import textgenrnn
# a bunch of output will be sent here
> textgen = textgenrnn()
# a bunch more output will be seen
> textgen.train_from_file("filename.txt", num_epochs=7)
# This will train and send sample output as it trains
```
The `num_epochs` can be configured as needed to refine the model. I used a value of 15.

When training is complete, a file `textgenrnn_weights.hdf5` will be created. Set the bot token properly and you're good to go!

You can also adjust the `temperature` kwarg within the generate function between 0 and 1.0; values near 0 will stick closer to the original source, whereas values closer to 1.0 will be more creative.
