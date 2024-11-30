import random

chat={
"hello": ["Hi there!🙏 How can I assist you with your job application?",
              "Hello!🙏 Ready to help you with your application process!",
              "Hey🙏! Let me know what you need help with regarding your job application."],

    "how are you": ["I'm just a bot, but I'm here to help you succeed in your job search!👍",
                    "I'm ready to assist you!👍 What do you need help with?",
                    "I'm functioning well and excited to support your career journey!👍"],

    "what is your name": ["I'm your job application assistant!😍",
                          "You can call me CareerBot!🤩",
                          "I'm your virtual assistant for job applications!🤩"],

    "bye": ["Good luck with your application! Goodbye!",
            "See you later! Don't forget to follow up on your applications!",
            "Take care and best wishes for your career journey!"],

    "how do I apply for a job": [
        "You can apply for a job by visiting the company's website and following their application instructions.",
        "Prepare your resume and cover letter, then submit them through the application portal.",
        "Research the job posting and tailor your application to the role before submitting."],

    "how to write a good resume": [
        "Start with a professional summary, highlight your achievements, and tailor it to the job description.",
        "Keep it concise, use bullet points, and focus on measurable accomplishments.",
        "Use action verbs and quantify your experience wherever possible."],

    "what is a cover letter": ["A cover letter is a personalized letter explaining why you're a great fit for the job.",
                               "It accompanies your resume and provides more detail about your skills and experience.",
                               "Your cover letter should highlight how your background matches the job's requirements."],

    "how to prepare for an interview": [
        "Research the company and role, practice common interview questions, and prepare questions to ask the interviewer.",
        "Dress professionally, arrive on time, and bring copies of your resume.",
        "Practice your responses to behavioral questions using the STAR method."],

    "how to follow up after an interview": [
        "Send a thank-you email within 24 hours, expressing gratitude for the opportunity.",
        "Mention something specific you discussed during the interview to personalize the message.",
        "Reiterate your interest in the role and ask about the next steps."],

    "how do I check my application status": [
        "You can email the hiring manager or HR to politely inquire about the status of your application.",
        "Log into the job application portal to see if there are any updates.",
        "Wait for about a week after applying before following up."],

    "what is STAR method": [
        "The STAR method stands for Situation, Task, Action, and Result, used to answer behavioral questions.",
        "Describe the Situation, the Task you needed to accomplish, the Action you took, and the Result of your efforts.",
        "It's a great way to structure answers during interviews."],

    "how to negotiate salary": ["Research the market rate for the role and have a specific range in mind.",
                                "Wait for the employer to bring up salary, and express enthusiasm for the role before discussing numbers.",
                                "Be prepared to explain why you're worth the number you're asking for, based on your skills and experience."],

    "what documents do I need for a job application": [
        "You'll typically need a resume, cover letter, and any certifications relevant to the role.",
        "Some applications may also require references or a portfolio of your work.",
        "Check the job posting for specific document requirements."],
}
def chatbot_prosser(text):
    word=text.lower()
    for key in  chat:
        if key in word:
            return random.choice(chat[key])
        return "hello i am chat bro"
while True:
    word2=input("user:")

    if word2.lower()=="bye champ":
        print("chat:goobye champ")
        break

    value= chatbot_prosser(word2)
    print("chat",value)

