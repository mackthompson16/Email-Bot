**This Script should manage by business email**

It runs on a VM instance in a google cloud project. 
This executes whenever Brooksportscamp@gmail.com recieves an email
because of the pub/sub functionality.

After execution:

1. Read inbox
2. Generate message based on context,content, and openai.chatcomplete
3. Determine whether the response is valid via classification and confidence
4. Send response as reply

_Disclaimer: this repo was made in August 2024, but refactored in September 2025 because of some deprication issues._
_Also, the email and google cloud project have been deactivated since I no longer run the camp._
