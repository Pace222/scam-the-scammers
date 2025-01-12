# Paid phone number verification
A scammer approached me on Telegram and asked me to register on their phishing website. The process asks for a phone number.  
I realised that when entering an incorrect phone number, the site performs a request to the server, the latter takes 1-2 seconds to process it and responds that the number is invalid.  
Doing my research on Internet, I learnt that it costs a little fee (about 5 cents) to check for a phone number's validity, just like a credit card.

`scam.py` is thus a little script that generates lots of requests to the site, costing the scammer a fee for each of them.
