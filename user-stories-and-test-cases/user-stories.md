# User Stories — Hotel Information Agent

Ten short, real-world scenarios showing how the agent helps different guests, used as the portfolio's "user stories" documentation (Step 4) and as the basis for the paired test cases in `user-story-test-cases.md`.

## 1. Sara — quick amenity questions
Sara is checking into the hotel with her dog and wants to know if pets are allowed and when the restaurant opens for dinner. Instead of waiting on hold for the front desk, she opens the chat widget and gets both answers in one exchange, sourced from the hotel's policy and restaurant documents.

## 2. Marcus — fast booking before a conference
Marcus needs a standard room for two nights before an early-morning conference and doesn't have time for a phone call. He asks the agent directly for availability on his dates, gets a same-message confirmation with room type and price, and completes the booking without ever speaking to a human.

## 3. Elena — multilingual support
Elena, a Spanish-speaking guest, asks about spa hours in Spanish. The agent detects the language, answers in Spanish, and offers to continue the conversation in either language — so she never has to switch to a translation app or wait for a bilingual staff member.

## 4. James — family logistics
James is traveling with two young kids and asks about late checkout and extra towels for the room. The agent confirms the checkout policy, offers to request a late checkout, and notifies housekeeping about the towels — handling two unrelated requests in a single conversation.

## 5. Aisha — a complaint that needs a human
Aisha messages the agent that her room is right next to a construction site and she hasn't slept in two nights. The agent detects the negative sentiment, apologizes, and immediately escalates the conversation to hotel management rather than trying to resolve it itself — getting a frustrated guest to a real person fast instead of leaving her stuck in a chatbot loop.

## 6. Tom — a genuine emergency
Tom realizes he's lost his passport the morning of an international flight and messages the agent in a panic. Rather than giving a vague, unhelpful answer, the agent recognizes this as an urgent, out-of-scope situation and immediately directs him to the front desk and provides the emergency contact number — matching the escalation fix identified in the earlier testing and evaluation activity.

## 7. Priya — the same question, asked differently
Priya asks for the WiFi password on check-in day, then asks again the next morning using different wording ("how do I connect to the internet?"). Both times she gets the exact same network name and password, because the knowledge base entry was consolidated to a single source of truth rather than letting the agent improvise an answer each time.

## 8. David — recognizing a room from a photo
David saw a photo of a room type on the hotel's website and wants to know if that exact room is available for his dates. He uploads the photo, and the agent identifies the room type from the image and checks availability, saving him from having to describe what he's looking for in words.

## 9. Chen — coordinating a group booking
Chen is organizing a 15-person offsite and asks the agent about booking multiple standard rooms for the same dates and whether a group rate applies. The agent handles the multi-room request and, for the group-discount question outside its knowledge base, clearly says so and refers Chen to the sales team rather than guessing at a number.

## 10. Robert — a returning loyalty guest
Robert, a returning loyalty-program member, asks about early check-in on his arrival day. The agent recognizes the loyalty-related nature of the question, confirms what the program guarantees (subject to availability), and — where it doesn't have guaranteed information — tells Robert to confirm at the front desk rather than promising something it can't verify.

