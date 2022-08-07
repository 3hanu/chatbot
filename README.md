# chatbot
remember this project has to be made on jupyter notebook where we have .ipynb files not .py

to add more questions we can make changes in ans.json

{
    "response_type": "question",
    "user_input": ["can", "you", "recommend", "me","a","good","book"],
    "bot_response": "What kind?",
    "required_words": ["can", "recommend", "book"]
  },
  {
    "response_type": "question",
    "user_input": ["manga"],
    "bot_response": "20th century boys",
    "required_words": []
  }
  
  since there is only one kind of book we have to add more categories
    {
    "response_type": "question",
    "user_input": ["horror"],
    "bot_response": "frankenstein",
    "required_words": []
  }
    {
    "response_type": "question",
    "user_input": ["sci-fi"],
    "bot_response": "time machine",
    "required_words": []
  }
  
 When you make random_responses.ipynb it has to be imported in chatbot.ipynb that's why we used import random_responses
 
 These are the names you gave to your python file. For convenience save using the names written here

